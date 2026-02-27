#!/usr/bin/env python3
"""
Sync bookmarks from Obsidian daily notes into assets/data/bookmarks.json.

Extracts markdown links [Title](URL) from daily notes.
Optionally fetches page titles for bare URLs (--fetch-bare-urls flag).

Sources (configured by CLI args):
  --archive-daily  Path to Personal-Archive/YYYY/daily  (2025 notes)
  --current-daily  Path to Personal-Data/YYYY/daily     (2026 notes)

Usage:
  python obsidian_bookmarks_sync.py \\
      --archive-daily "/path/to/Personal-Archive/2025/daily" \\
      --current-daily "/path/to/Personal-Data/2026/daily" \\
      --start 2025-11-10
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.request
import urllib.error
from datetime import datetime
from html.parser import HTMLParser
from pathlib import Path


MD_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
BARE_URL_RE = re.compile(r"(?<!\()(https?://[^\s)\]\"'<>]+)")
OBSIDIAN_LINK_RE = re.compile(r"\[\[([^\]]*)\]\]")


# ---------------------------------------------------------------------------
# HTML title fetcher
# ---------------------------------------------------------------------------

class _TitleParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self._in_title = False
        self.title: str | None = None

    def handle_starttag(self, tag, attrs):
        if tag == "title":
            self._in_title = True

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False

    def handle_data(self, data):
        if self._in_title and self.title is None:
            self.title = data.strip()


def fetch_title(url: str, timeout: int = 5) -> str | None:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            content_type = resp.headers.get("Content-Type", "")
            if "text/html" not in content_type:
                return None
            html = resp.read(8192).decode("utf-8", errors="ignore")
        parser = _TitleParser()
        parser.feed(html)
        return parser.title
    except Exception:
        return None


# ---------------------------------------------------------------------------
# Core extraction
# ---------------------------------------------------------------------------

def filename_date(p: Path) -> str | None:
    m = re.match(r"^(\d{4}-\d{2}-\d{2})\.md$", p.name)
    return m.group(1) if m else None


def extract_links(
    path: Path,
    date: str,
    fetch_bare: bool = False,
    verbose: bool = False,
) -> list[dict]:
    """Return list of {date, title, url} dicts extracted from a daily note."""
    text = path.read_text(encoding="utf-8", errors="ignore")
    # Remove Obsidian internal links so their text doesn't confuse the regex
    text = OBSIDIAN_LINK_RE.sub("", text)

    results: list[dict] = []
    seen_urls: set[str] = set()

    for line in text.splitlines():
        # Skip routine/plan/task lines
        stripped = line.strip()
        if not stripped or stripped.startswith("##"):
            continue

        # Extract [Title](URL) markdown links
        for m in MD_LINK_RE.finditer(line):
            title_raw = m.group(1).strip()
            url = m.group(2).strip()
            if not url.startswith("http"):
                continue
            if url in seen_urls:
                continue
            seen_urls.add(url)
            # Keep any inline tags in the title (matches Notion format)
            results.append({"date": date, "title": title_raw, "url": url})
            if verbose:
                print(f"  [{date}] MD  {title_raw[:60]}")

        # Optionally extract bare URLs
        if fetch_bare:
            for bm in BARE_URL_RE.finditer(line):
                url = bm.group(0).rstrip(".,;)")
                # Skip if already captured as part of a markdown link
                if url in seen_urls:
                    continue
                seen_urls.add(url)
                # Use surrounding context as title fallback
                context = line.strip().lstrip("- *").strip()
                # Remove the URL itself from context
                context = context.replace(url, "").strip().lstrip("—–-").strip()
                title = context if context else None
                if not title:
                    if verbose:
                        print(f"  [{date}] BARE fetch {url[:60]}")
                    title = fetch_title(url) or url
                results.append({"date": date, "title": title, "url": url})
                if verbose:
                    print(f"  [{date}] BARE {title[:60]}")

    return results


def collect_from_dir(
    daily_dir: Path,
    start: str,
    end: str,
    fetch_bare: bool = False,
    verbose: bool = False,
) -> list[dict]:
    items: list[dict] = []
    if not daily_dir.exists():
        print(f"  WARNING: directory not found: {daily_dir}", file=sys.stderr)
        return items
    for p in sorted(daily_dir.iterdir()):
        d = filename_date(p)
        if not d:
            continue
        if d < start or d > end:
            continue
        day_items = extract_links(p, d, fetch_bare=fetch_bare, verbose=verbose)
        items.extend(day_items)
    return items


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    ap = argparse.ArgumentParser(description="Sync Obsidian bookmarks into bookmarks.json")
    ap.add_argument("--archive-daily", help="Path to 2025 Personal-Archive daily notes dir")
    ap.add_argument("--current-daily", help="Path to 2026 Personal-Data daily notes dir")
    ap.add_argument("--start", default="2025-11-10", help="Start date YYYY-MM-DD (default: 2025-11-10 = Week 46)")
    ap.add_argument("--end", default=datetime.today().strftime("%Y-%m-%d"), help="End date YYYY-MM-DD (default: today)")
    ap.add_argument("--output", help="Path to bookmarks.json (default: auto-detect from repo root)")
    ap.add_argument("--fetch-bare-urls", action="store_true", help="Also extract bare URLs and fetch their page titles")
    ap.add_argument("--dry-run", action="store_true", help="Print what would be added without writing")
    ap.add_argument("--verbose", action="store_true", help="Show each extracted link")
    args = ap.parse_args()

    repo_root = Path(__file__).resolve().parents[1]
    obs_root = Path("/Users/vaibhavb/Library/Mobile Documents/iCloud~md~obsidian/Documents")

    # Resolve daily directories
    archive_dir = Path(args.archive_daily) if args.archive_daily else obs_root / "Personal-Archive/2025/daily"
    current_dir = Path(args.current_daily) if args.current_daily else obs_root / "Personal-Data/2026/daily"

    output_path = Path(args.output) if args.output else repo_root / "assets/data/bookmarks.json"

    start_date = args.start
    end_date = args.end
    fetch_bare = args.fetch_bare_urls

    print(f"📚 Obsidian Bookmarks Sync")
    print(f"   Archive dir : {archive_dir}")
    print(f"   Current dir : {current_dir}")
    print(f"   Date range  : {start_date} → {end_date}")
    print(f"   Output      : {output_path}")
    print(f"   Bare URLs   : {'yes (fetching titles)' if fetch_bare else 'no'}")
    print()

    # Load existing bookmarks
    existing: list[dict] = []
    if output_path.exists():
        existing = json.loads(output_path.read_text(encoding="utf-8"))
    existing_urls: set[str] = {b["url"] for b in existing}
    print(f"📂 Existing bookmarks: {len(existing)}")

    # --- 2025 archive (up to Dec 31 2025) ---
    print(f"\n🔍 Scanning archive (2025 notes from {start_date} to 2025-12-31)...")
    archive_items = collect_from_dir(
        archive_dir,
        start=start_date,
        end="2025-12-31",
        fetch_bare=fetch_bare,
        verbose=args.verbose,
    )
    print(f"   Found {len(archive_items)} links")

    # --- 2026 current ---
    print(f"\n🔍 Scanning current (2026 notes from 2026-01-01 to {end_date})...")
    current_items = collect_from_dir(
        current_dir,
        start="2026-01-01",
        end=end_date,
        fetch_bare=fetch_bare,
        verbose=args.verbose,
    )
    print(f"   Found {len(current_items)} links")

    all_new = archive_items + current_items

    # Deduplicate new items against each other and against existing
    deduped: list[dict] = []
    seen_new: set[str] = set()
    skipped_existing = 0
    skipped_dupes = 0

    for item in all_new:
        url = item["url"]
        if url in existing_urls:
            skipped_existing += 1
            continue
        if url in seen_new:
            skipped_dupes += 1
            continue
        seen_new.add(url)
        deduped.append(item)

    print(f"\n📊 Summary:")
    print(f"   Total raw links found : {len(all_new)}")
    print(f"   Already in bookmarks  : {skipped_existing}")
    print(f"   Duplicates within new : {skipped_dupes}")
    print(f"   Net new bookmarks     : {len(deduped)}")

    if not deduped:
        print("\n✅ No new bookmarks to add.")
        return

    print(f"\n📝 New bookmarks preview (first 10):")
    for item in deduped[:10]:
        print(f"   [{item['date']}] {item['title'][:65]}")
    if len(deduped) > 10:
        print(f"   ... and {len(deduped) - 10} more")

    if args.dry_run:
        print("\n🔍 Dry run — no changes written.")
        return

    # Merge and sort descending by date
    merged = existing + deduped
    merged.sort(key=lambda x: x["date"], reverse=True)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(merged, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\n✅ Written {len(merged)} total bookmarks to {output_path}")
    print(f"   ({len(existing)} existing + {len(deduped)} new)")


if __name__ == "__main__":
    main()
