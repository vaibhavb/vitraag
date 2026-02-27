#!/usr/bin/env python3
"""
Auto-sync news from Obsidian daily notes into _data/*.yml.

Steps:
1. Read last date from each _data/*.yml to determine per-category start dates
2. Scan Personal-Archive (2025) and Personal-Data (2026) daily notes for tagged items
3. Write _data/handoff_data.json
4. Run news_updater.py to prepend/merge into YAML files (deduplicates by link)

Obsidian tag → YAML file mapping:
  #security-news     → security-news.yml
  #ai-news           → ai-news.yml
  #digitalhealth-news → digitalhealth-news.yml
  #finance-news      → finance-news.yml
  #product-news | #product → pm-news.yml

Usage:
  python obsidian_news_auto.py [--target-date YYYY-MM-DD] [--dry-run] [--verbose]
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from collections import defaultdict
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
    {"tags": ["#security-news"],                          "out": "security-news"},
    {"tags": ["#ai-news"],                                "out": "ai-news"},
    {"tags": ["#digitalhealth-news"],                     "out": "digitalhealth-news"},
    {"tags": ["#finance-news"],                           "out": "finance-news"},
    {"tags": ["#product-news", "#product"],               "out": "pm-news"},
]

MD_LINK_RE  = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
BARE_URL_RE = re.compile(r"(https?://[^\s)\]]+)")
TAG_RE      = re.compile(r"#[A-Za-z0-9][\w\-/]*")
OBS_LINK_RE = re.compile(r"\[\[[^\]]*\]\]")

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


def build_desc(line: str) -> str:
    """Build a clean description from a daily note line."""
    s = line.strip().lstrip("- *").strip()
    # Remove Obsidian internal links
    s = OBS_LINK_RE.sub("", s)
    # Extract markdown link title(s) and surrounding context
    titles = [m.group(1) for m in MD_LINK_RE.finditer(s)]
    # Strip all markdown links, bare URLs, tags, obsidian links
    s = MD_LINK_RE.sub("", s)
    s = BARE_URL_RE.sub("", s)
    s = TAG_RE.sub("", s)
    # Clean up punctuation noise
    s = re.sub(r"[-–—:]+", " ", s)
    s = re.sub(r"\s+", " ", s).strip()

    if titles and s:
        return f"{titles[0]} — {s}"
    elif titles:
        return titles[0]
    return s or "Link"


def scan_dir(
    daily_dir: Path,
    start: str,
    end: str,
    cat_tags: list[str],
    seen_links: set[str],
    verbose: bool = False,
) -> list[dict]:
    """Scan a daily notes dir and return items matching any of cat_tags."""
    items = []
    if not daily_dir.exists():
        print(f"  WARNING: dir not found: {daily_dir}", file=sys.stderr)
        return items

    for p in sorted(daily_dir.iterdir()):
        d = filename_date(p)
        if not d or d < start or d > end:
            continue
        text = p.read_text(encoding="utf-8", errors="ignore")
        for line in text.splitlines():
            if not any(tag in line for tag in cat_tags):
                continue
            urls = [m.group(2) for m in MD_LINK_RE.finditer(line)]
            if not urls:
                # Fall back to bare URLs if no markdown link
                urls = [m.group(1) for m in BARE_URL_RE.finditer(line)]
            for url in urls:
                url = url.rstrip(".,;)")
                if url in seen_links:
                    continue
                seen_links.add(url)
                desc = build_desc(line)
                items.append({"desc": desc, "link": url})
                if verbose:
                    print(f"    [{d}] {desc[:70]}")
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

    print(f"📰 Obsidian News Auto-Sync")
    print(f"   Target date : {target_date}")
    print(f"   Dry run     : {args.dry_run}")
    print()

    categories_out: dict[str, dict] = {}
    total_items = 0

    for cat in CATEGORIES:
        out = cat["out"]
        tags = cat["tags"]

        # Determine start date: day after last YAML entry (or 14 days ago as fallback)
        if args.start:
            start_date = args.start
        else:
            last = last_yaml_date(out)
            if last:
                start_date = (datetime.strptime(last, "%Y-%m-%d") + timedelta(days=1)).strftime("%Y-%m-%d")
            else:
                start_date = (datetime.today() - timedelta(days=14)).strftime("%Y-%m-%d")

        print(f"🔍 {out} (tags: {', '.join(tags)}, from {start_date} → {target_date})")

        seen: set[str] = set()
        items: list[dict] = []

        # 2025 archive
        archive_items = scan_dir(ARCHIVE_DAILY, start_date, "2025-12-31", tags, seen, args.verbose)
        items.extend(archive_items)

        # 2026 current
        current_items = scan_dir(CURRENT_DAILY, max(start_date, "2026-01-01"), target_date, tags, seen, args.verbose)
        items.extend(current_items)

        print(f"   {len(items)} item(s) found")
        categories_out[out] = {"items": items}
        total_items += len(items)

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

    # Run news_updater.py
    print("\n🔄 Running news_updater.py...")
    result = subprocess.run(
        [sys.executable, str(Path(__file__).parent / "news_updater.py"),
         "--input", str(handoff_path)],
        capture_output=False,
    )
    sys.exit(result.returncode)


if __name__ == "__main__":
    main()
