#!/usr/bin/env python3
"""
Auto-sync news from Obsidian daily notes into _data/*.yml.

Steps:
1. Read last date from each _data/*.yml to determine per-category start dates
2. Scan Personal-Archive (2025) and Personal-Data (2026) daily notes' "### notes"
   sections for linked items, one pass covering the full date range
3. Classify each item into a category — by explicit hashtag if present
   (backward compatible with the old tagging convention), otherwise by
   keyword-based content classification against the title/description.
   Items that don't score for any category (personal links, hobby stuff,
   generic tweets with no context, etc.) are dropped.
4. Write _data/handoff_data.json
5. Run news_updater.py to prepend/merge into YAML files (deduplicates by link)

Obsidian tag → YAML file mapping (still honored when present):
  #security-news     → security-news.yml
  #ai-news           → ai-news.yml
  #digitalhealth-news → digitalhealth-news.yml
  #finance-news      → finance-news.yml
  #product-news | #product → pm-news.yml

Content classification (used when no tag matches) scores each item against
per-category keyword lists and assigns the highest-scoring category, with
ties broken by specificity order: security > digitalhealth > finance > pm > ai.
AI is the catch-all/broadest category so it only wins outright matches, never
ties.

Usage:
  python obsidian_news_auto.py [--target-date YYYY-MM-DD] [--dry-run] [--verbose]
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime, timedelta
from pathlib import Path

import yaml

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = REPO_ROOT / "_data"
OBS_ROOT = Path("/Users/vaibhavb/Library/Mobile Documents/iCloud~md~obsidian/Documents")
ARCHIVE_DAILY = OBS_ROOT / "Personal-Archive/2025/daily"
CURRENT_DAILY = OBS_ROOT / "Personal-Data/2026/daily"

CATEGORIES = [
    {"tags": ["#security-news"],            "out": "security-news"},
    {"tags": ["#ai-news"],                  "out": "ai-news"},
    {"tags": ["#digitalhealth-news"],       "out": "digitalhealth-news"},
    {"tags": ["#finance-news"],             "out": "finance-news"},
    {"tags": ["#product-news", "#product"], "out": "pm-news"},
]
TAG_TO_CATEGORY = {tag: cat["out"] for cat in CATEGORIES for tag in cat["tags"]}

# Specificity order used both for tie-breaking and for output iteration.
CATEGORY_ORDER = ["security-news", "digitalhealth-news", "finance-news", "pm-news", "ai-news"]

# Content classification keyword lists, weighted by specificity.
# Strong/unambiguous signal words (weight 2) decisively indicate a category
# even when generic AI vocabulary ("ai", "agent", "model", ...) is also
# present in the same item — e.g. "Adversarial AI Source Code Review" should
# win security-news off "adversarial"/"source code review", not ai-news off
# "ai". Generic AI terms (weight 1) are the catch-all and only win when
# nothing more specific matches.
CATEGORY_KEYWORDS: dict[str, dict[str, int]] = {
    "security-news": {
        "security": 1, "cyber": 1, "cve": 2, "vulnerab": 2, "exploit": 2,
        "breach": 2, "pentest": 2, "penetration test": 2, "malware": 2,
        "ransomware": 2, "phishing": 2, "threat actor": 2, "threat hunt": 2,
        "threat model": 2, "infosec": 2, "attack surface": 2, "ciso": 2,
        "soc": 1, "encrypt": 1, "cryptograph": 2, "zero-day": 2, "0-day": 2,
        "red team": 2, "blue team": 2, "incident response": 2, "data leak": 2,
        "data breach": 2, "hacker": 2, "hacking": 2, "hijack": 2,
        "exfiltrat": 2, "prompt injection": 2, "supply chain attack": 2,
        "bug bounty": 2, "reverse engineer": 2, "sast": 2, "guardrail": 1,
        "attack vector": 2, "adversarial": 2, "otp": 1, "root account": 2,
        "password spray": 2, "risk management platform": 2,
        "cyber insurance": 2, "cyber apprenticeship": 2, "surveillance": 1,
        "darknet": 2, "dark web": 2, "sentenced": 1, "extort": 2,
        "source code review": 1, "cloud security": 2,
    },
    "digitalhealth-news": {
        "health": 1, "medical": 2, "patient": 2, "clinical": 2,
        "healthcare": 2, "hospital": 2, "fda": 2, "biotech": 2, "pharma": 2,
        "diagnos": 2, "drug": 1, "therap": 1, "cancer": 2, "disease": 2,
        "doctor": 1, "clinician": 2, "mychart": 2, "ehr": 2, "epic": 1,
        "genome": 2, "dermatology": 2, "medicare": 2, "mental health": 2,
        "cbt": 1, "nhs": 1, "tumor": 2, "physician": 2, "nursing": 2,
    },
    "finance-news": {
        "venture capital": 2, " vc ": 1, "funding round": 2, "series a": 2,
        "series b": 2, "series c": 2, "ipo": 2, "valuation": 2,
        "private equity": 2, "investment firm": 1, "investor": 1,
        "unicorn": 1, "nvca": 2, "hedge fund": 2, "market cap": 2,
        "economics of": 1, "dram": 2, "semiconductor market": 2,
        "capital deployed": 2, "gp outlook": 2, "acquisition": 1, "m&a": 2,
        "revenue growth": 1,
    },
    "pm-news": {
        "product management": 2, "roadmap": 1, "go-to-market": 2, "gtm": 2,
        "customer discovery": 2, "user research": 2, "product launch": 1,
        "product-market fit": 2, "marketing": 1, "positioning": 1,
        "onboarding flow": 2, "growth strategy": 1, "customer finder": 1,
        "design system": 1, "product design": 1,
    },
    "ai-news": {
        "ai": 1, "llm": 1, "gpt": 1, "language model": 1,
        "machine learning": 1, "ml": 1, "neural network": 1, "openai": 1,
        "anthropic": 1, "claude": 1, "kimi": 1, "transformer": 1,
        "inference": 1, "chatbot": 1, "generative": 1, "agent": 1,
        "agentic": 1, "fine-tune": 1, "foundation model": 1,
        "open-weights": 1, "mixture-of-experts": 1, "moe": 1,
        "diffusion model": 1, "text-to-speech": 1, "reasoning model": 1,
    },
}

MD_LINK_RE  = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
BARE_URL_RE = re.compile(r"(https?://[^\s)\]]+)")
TAG_RE      = re.compile(r"#[A-Za-z0-9][\w\-/]*")
OBS_LINK_RE = re.compile(r"\[\[[^\]]*\]\]")
NOTES_HEADING_RE = re.compile(r"^###\s+notes\s*$", re.IGNORECASE)
HEADING_RE = re.compile(r"^###\s+")

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def last_yaml_date(category: str) -> str | None:
    """Return the most recent date string in _data/<category>.yml, or None."""
    path = DATA_DIR / f"{category}.yml"
    if not path.exists():
        return None
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or []
        if data:
            return str(data[0].get("date", ""))
    except Exception:
        pass
    return None


def filename_date(p: Path) -> str | None:
    m = re.match(r"^(\d{4}-\d{2}-\d{2})\.md$", p.name)
    return m.group(1) if m else None


def build_desc(line: str) -> tuple[str, str]:
    """Build a clean description from a daily note line.

    Returns (title, desc_text) where desc_text is the full "Title — body"
    string used both for the YAML entry and for content classification.
    """
    s = line.strip().lstrip("- *").strip()
    s = OBS_LINK_RE.sub("", s)
    titles = [m.group(1) for m in MD_LINK_RE.finditer(s)]
    s = MD_LINK_RE.sub("", s)
    s = BARE_URL_RE.sub("", s)
    s = TAG_RE.sub("", s)
    s = re.sub(r"[-–—:]+", " ", s)
    s = re.sub(r"\s+", " ", s).strip()

    title = titles[0] if titles else ""
    if title and s:
        return title, f"{title} — {s}"
    elif title:
        return title, title
    return "", (s or "Link")


# Precompiled matchers: multi-word/spaced keywords match as plain substrings
# (spaces are natural boundaries); single-word keywords match with a left
# word-boundary (allows plural/suffix forms like "agents", "hackers") to
# avoid false hits inside unrelated words (e.g. "ai" inside "email").
def _matcher(keyword: str):
    if " " in keyword or "-" in keyword:
        return lambda s: keyword in s
    pat = re.compile(r"\b" + re.escape(keyword))
    return lambda s: pat.search(s) is not None

_CATEGORY_MATCHERS: dict[str, list[tuple]] = {
    cat: [(_matcher(kw), weight) for kw, weight in kws.items()]
    for cat, kws in CATEGORY_KEYWORDS.items()
}


def classify_content(text: str) -> str | None:
    """Score `text` against each category's weighted keywords, return best match or None."""
    lowered = text.lower()
    scores: dict[str, int] = {}
    for cat, matchers in _CATEGORY_MATCHERS.items():
        score = sum(weight for match, weight in matchers if match(lowered))
        if score:
            scores[cat] = score
    if not scores:
        return None
    best_score = max(scores.values())
    # Tie-break by specificity order; ai-news never wins a tie.
    for cat in CATEGORY_ORDER:
        if scores.get(cat) == best_score:
            return cat
    return None


def extract_notes_lines(text: str) -> list[str]:
    """Return bullet-link lines found within the '### notes' section only."""
    lines = []
    in_notes = False
    for line in text.splitlines():
        if NOTES_HEADING_RE.match(line):
            in_notes = True
            continue
        if HEADING_RE.match(line):
            in_notes = False
            continue
        if in_notes and line.strip().startswith("- ["):
            lines.append(line)
    return lines


def scan_dir(
    daily_dir: Path,
    start: str,
    end: str,
    verbose: bool = False,
) -> list[dict]:
    """Scan a daily notes dir and return classified items with their date."""
    items: list[dict] = []
    if not daily_dir.exists():
        print(f"  WARNING: dir not found: {daily_dir}", file=sys.stderr)
        return items

    for p in sorted(daily_dir.iterdir()):
        d = filename_date(p)
        if not d or d < start or d > end:
            continue
        text = p.read_text(encoding="utf-8", errors="ignore")
        for line in extract_notes_lines(text):
            # Explicit tag wins over content classification (back-compat).
            category = None
            for tag, cat in TAG_TO_CATEGORY.items():
                if tag in line:
                    category = cat
                    break

            urls = [m.group(2) for m in MD_LINK_RE.finditer(line)]
            if not urls:
                urls = [m.group(1) for m in BARE_URL_RE.finditer(line)]
            if not urls:
                continue

            title, desc = build_desc(line)
            if category is None:
                category = classify_content(f"{title} {desc}")
            if category is None:
                if verbose:
                    print(f"    [{d}] SKIP (unclassified): {desc[:70]}")
                continue

            for url in urls:
                url = url.rstrip(".,;)")
                items.append({"date": d, "category": category, "desc": desc, "link": url})
                if verbose:
                    print(f"    [{d}] -> {category}: {desc[:70]}")
    return items


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    ap = argparse.ArgumentParser(description="Auto-sync Obsidian news → _data/*.yml")
    ap.add_argument("--target-date", default=datetime.today().strftime("%Y-%m-%d"),
                    help="Date to file items under (default: today)")
    ap.add_argument("--start", help="Override start date for all categories (YYYY-MM-DD)")
    ap.add_argument("--dry-run", action="store_true", help="Build handoff_data.json but skip news_updater")
    ap.add_argument("--verbose", action="store_true")
    args = ap.parse_args()

    target_date = args.target_date

    print(f"📰 Obsidian News Auto-Sync (content-based classification)")
    print(f"   Target date : {target_date}")
    print(f"   Dry run     : {args.dry_run}")
    print()

    # Per-category start dates (day after last YAML entry, or 14 days ago fallback).
    start_dates: dict[str, str] = {}
    for cat in CATEGORIES:
        out = cat["out"]
        if args.start:
            start_dates[out] = args.start
        else:
            last = last_yaml_date(out)
            if last:
                start_dates[out] = (datetime.strptime(last, "%Y-%m-%d") + timedelta(days=1)).strftime("%Y-%m-%d")
            else:
                start_dates[out] = (datetime.today() - timedelta(days=14)).strftime("%Y-%m-%d")

    overall_start = min(start_dates.values())
    print(f"🔍 Scanning notes sections from {overall_start} → {target_date}")
    for out in CATEGORY_ORDER:
        print(f"   {out}: since {start_dates[out]}")
    print()

    # Single pass over daily notes covering the full range; classify once per item.
    all_items = scan_dir(ARCHIVE_DAILY, overall_start, "2025-12-31", args.verbose)
    all_items += scan_dir(CURRENT_DAILY, max(overall_start, "2026-01-01"), target_date, args.verbose)

    categories_out: dict[str, dict] = {out: {"items": []} for out in CATEGORY_ORDER}
    seen_per_cat: dict[str, set[str]] = {out: set() for out in CATEGORY_ORDER}
    total_items = 0

    for item in all_items:
        cat = item["category"]
        if item["date"] < start_dates[cat]:
            continue
        if item["link"] in seen_per_cat[cat]:
            continue
        seen_per_cat[cat].add(item["link"])
        categories_out[cat]["items"].append({"desc": item["desc"], "link": item["link"]})
        total_items += 1

    for out in CATEGORY_ORDER:
        print(f"   {out}: {len(categories_out[out]['items'])} item(s)")

    handoff = {
        "target_date": target_date,
        "categories": categories_out,
        "summary": {
            "total_items": total_items,
            "categories_updated": [c for c, v in categories_out.items() if v["items"]],
        },
    }

    handoff_path = DATA_DIR / "handoff_data.json"
    handoff_path.write_text(json.dumps(handoff, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\n✅ Wrote handoff_data.json ({total_items} total items)")

    if args.dry_run:
        print("🔍 Dry run — skipping news_updater.py")
        return

    if total_items == 0:
        print("ℹ️  No new items — skipping news_updater.py")
        return

    print("\n🔄 Running news_updater.py...")
    result = subprocess.run(
        [sys.executable, str(Path(__file__).parent / "news_updater.py"),
         "--input", str(handoff_path)],
        capture_output=False,
    )
    sys.exit(result.returncode)


if __name__ == "__main__":
    main()
