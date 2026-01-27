#!/usr/bin/env python3
"""Sync news items from Obsidian daily notes into vitraag _data/*.yml.

This is a backfill-friendly generator.

It scans Obsidian daily notes in the personal-data vault, extracts URLs from lines
that contain EXACT category tags, and writes Jekyll-friendly YAML grouped by date.

Categories (tag -> yaml):
- #security-news       -> _data/security-news.yml
- #ai-news             -> _data/ai-news.yml
- #digitalhealth-news  -> _data/digitalhealth-news.yml
- #finance-news        -> _data/finance-news.yml
- #product             -> _data/pm-news.yml

Usage:
  cd ~/vaults/vitraag
  python3 data-runners/obsidian_news_sync.py \
    --obsidian-daily ~/vaults/personal-data/content/daily \
    --start 2025-01-01 --end 2026-01-27
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from datetime import datetime
from collections import defaultdict

import yaml

URL_RE = re.compile(r"(https?://[^\s)\]]+)")
MD_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]*)\)")
TAG_RE = re.compile(r"#[A-Za-z0-9][\w\-/]*")

CATEGORIES = [
    {"tag": "#security-news", "out": "security-news"},
    {"tag": "#ai-news", "out": "ai-news"},
    {"tag": "#digitalhealth-news", "out": "digitalhealth-news"},
    {"tag": "#finance-news", "out": "finance-news"},
    {"tag": "#product", "out": "pm-news"},
]


def parse_date(s: str) -> datetime:
    return datetime.strptime(s, "%Y-%m-%d")


def filename_date(p: Path) -> str | None:
    m = re.match(r"^(\d{4}-\d{2}-\d{2})\.md$", p.name)
    return m.group(1) if m else None


def clean_desc(line: str) -> str:
    s = line.strip()
    s = re.sub(r"^[-*]\s+", "", s)
    # convert markdown links [text](url) -> text
    s = MD_LINK_RE.sub(r"\1", s)
    # remove URLs
    s = URL_RE.sub("", s)
    # remove tags
    s = TAG_RE.sub("", s)
    # remove empty parens
    s = re.sub(r"\(\s*\)", "", s)
    # collapse whitespace
    s = re.sub(r"\s+", " ", s).strip()
    # remove leading punctuation noise
    s = re.sub(r"^[-–—:]+\s*", "", s).strip()
    return s or "Link"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--obsidian-daily", required=True, help="Path to Obsidian daily notes folder")
    ap.add_argument("--start", required=True, help="YYYY-MM-DD")
    ap.add_argument("--end", required=True, help="YYYY-MM-DD")
    args = ap.parse_args()

    daily_dir = Path(args.obsidian_daily).expanduser().resolve()
    start = args.start
    end = args.end

    if not daily_dir.exists():
        raise SystemExit(f"Missing daily dir: {daily_dir}")

    # category -> date -> list[items]
    items = {c["out"]: defaultdict(list) for c in CATEGORIES}
    seen = {c["out"]: defaultdict(set) for c in CATEGORIES}  # category -> date -> set(url)

    for p in sorted(daily_dir.iterdir()):
        d = filename_date(p)
        if not d:
            continue
        if d < start or d > end:
            continue

        txt = p.read_text(encoding="utf-8", errors="ignore")
        for line in txt.splitlines():
            urls = [m.group(1) for m in URL_RE.finditer(line)]
            if not urls:
                continue
            for cat in CATEGORIES:
                tag = cat["tag"]
                out = cat["out"]
                if tag not in line:
                    continue
                desc = clean_desc(line)
                for url in urls:
                    if url in seen[out][d]:
                        continue
                    seen[out][d].add(url)
                    items[out][d].append({"desc": desc, "link": url})

    vitraag_root = Path(__file__).resolve().parents[1]
    data_dir = vitraag_root / "_data"
    data_dir.mkdir(parents=True, exist_ok=True)

    for cat in CATEGORIES:
        out = cat["out"]
        out_path = data_dir / f"{out}.yml"

        # Build YAML list sorted reverse chronological
        dates = sorted(items[out].keys(), reverse=True)
        y = []
        for d in dates:
            y.append({"date": d, "news-items": items[out][d]})

        with out_path.open("w", encoding="utf-8") as f:
            yaml.dump(y, f, allow_unicode=True, sort_keys=False, default_flow_style=False, indent=2)

        print(f"wrote {out_path} ({len(dates)} date groups)")


if __name__ == "__main__":
    main()
