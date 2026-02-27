- For news (security-news, pm-news, finance-news and digitalhealth-news) get the appropriate tagged news from obsidian server and update the news items in \_data directory in YAML format. Do this on a weekly basis.

## Seasonal Theme Switching

### Available Themes
The website supports four seasonal themes with dedicated color palettes:
- **Winter** (`theme-winter.scss`) - Cool, frost-inspired colors with Meadow Blue primary
- **Spring** (`theme-spring.scss`) - Fresh blooms palette
- **Summer** (`theme-summer.scss`) - Tropical vibes palette
- **Fall** (`theme-fall.scss`) - Harvest colors palette

### Manual Theme Switching

**Current theme**: Winter (as of 2025-12-22)

**To switch themes manually:**
1. Edit `assets/sass/mybulma.scss` at line 3
2. Change the import statement to desired theme:
   ```scss
   @use "./theme-winter.scss" as theme;  // Winter
   @use "./theme-spring.scss" as theme;  // Spring
   @use "./theme-summer.scss" as theme;  // Summer
   @use "./theme-fall.scss" as theme;    // Fall
   ```
3. Rebuild the site for changes to take effect

### Theme Files Location
All theme files are located in: `assets/sass/theme-*.scss`

Each theme defines:
- Primary color palette (primary, info, success, warning, danger, link)
- Background and text colors
- Component-specific overrides
- Border and shadow styles

### Future Enhancement
Consider implementing automatic seasonal theme switching based on current date or adding UI controls for manual theme selection.

## Weekly News Update Workflow

### Automated Sync (preferred)

**Script**: `data-runners/obsidian_news_auto.py`
**Cron**: Every Sunday at 10:00 AM (`0 10 * * 0 ~/.config/me/vitraag_news_sync.sh`)
**Log**: `~/vitraag_news_sync.log`

The automated sync reads Obsidian daily notes directly — no manual handoff needed.

**Tag → YAML mapping:**
| Obsidian tag | YAML file |
|---|---|
| `#security-news` | `security-news.yml` |
| `#ai-news` | `ai-news.yml` |
| `#digitalhealth-news` | `digitalhealth-news.yml` |
| `#finance-news` | `finance-news.yml` |
| `#product-news` or `#product` | `pm-news.yml` |

**Obsidian vault sources:**
- 2025 notes: `Personal-Archive/2025/daily/`
- 2026+ notes: `Personal-Data/2026/daily/`

**Manual run:**
```bash
cd data-runners

# Auto-detect start dates from YAML files (recommended)
.venv/bin/python3 obsidian_news_auto.py

# Override start date
.venv/bin/python3 obsidian_news_auto.py --start 2026-02-20

# Preview without writing
.venv/bin/python3 obsidian_news_auto.py --dry-run --verbose
```

**How it works:**
1. Reads last date from each `_data/*.yml` → computes per-category start date (day after)
2. Scans daily notes for lines containing the category tag
3. Extracts `[Title](URL)` links; builds desc from title + surrounding context
4. Writes `_data/handoff_data.json`
5. Runs `news_updater.py` which prepends/merges into YAML (deduplicates by link URL)
6. Cron wrapper commits and pushes only if YAML files changed

---

### Manual Workflow (Claude Code assisted)

Use when you want AI-polished descriptions or need to review before committing.

**Command: `update-news`**

**Three-Phase Workflow:**
1. **Phase 1 (Claude Code)**: MCP search + AI formatting
2. **Phase 2 (User Review)**: Approve/modify results
3. **Phase 3 (Python Script)**: File operations + YAML updates

### Phase 1: Claude Code Processing

**Step 1: Read Last Update Dates**
- Read first date from each _data/*.yml file:
  - security-news.yml → #security-news
  - digitalhealth-news.yml → #digitalhealth-news
  - finance-news.yml → #finance-news
  - pm-news.yml → #product
  - ai-news.yml → #ai-news

**Step 2: MCP Search by Tag**
For each category:
- Use `mcp__obsidian-server__obsidian_complex_search` to find items with tag since last date
- Search pattern: `{"and": [{"regexp": ["#TAG", {"var": "content"}]}, {"regexp": ["2025-0[6-9]-[0-9]{2}|2025-1[0-2]-[0-9]{2}", {"var": "path"}]}]}`
- Date range: From day after last YAML date to target date (e.g., 2025-06-13 to 2025-07-09)
- Extract: date, description, link from each match
- **IMPORTANT**: Only include items that have the EXACT tag (e.g., #security-news, #finance-news) in content

**Step 3: AI Formatting**
For each news item:
- Send to Claude API for description enhancement
- Prompt: "Make this news description professional, 1-2 sentences, remove personal notes/tags"
- Preserve original link

**Step 4: Generate Handoff Data**
Create JSON structure and **ALWAYS overwrite the handoff_data.json file completely**:
```json
{
  "target_date": "2025-07-09",
  "categories": {
    "security-news": {
      "items": [
        {"desc": "Enhanced description", "link": "https://..."},
        ...
      ]
    },
    "digitalhealth-news": {...},
    ...
  },
  "summary": {
    "total_items": 20,
    "categories_updated": ["security-news", "digitalhealth-news", "ai-news"]
  }
}
```

**Step 5: User Review Points**
- Show raw extraction results for approval
- Show AI-formatted descriptions for approval
- Present final JSON for handoff to Python script

### Phase 2: User Review & Approval

**Extraction Review:**
```
🔒 SECURITY NEWS (8 items found):
   📅 2025-07-07: Wiz Safer Vibe Coding Rules
   📅 2025-07-06: CVE-2025-53109 Anthropic
   ...
Approve extraction? [y/n/edit]
```

**AI Formatting Review:**
```
🤖 AI FORMATTING CHANGES:
BEFORE: "Rules file from Wiz. #security-news"
AFTER:  "Wiz releases comprehensive coding rules file..."
Approve formatting? [y/n/edit]
```

**Final Handoff Review:**
```
📊 READY FOR HANDOFF:
- 20 total items across 4 categories
- All items consolidated under 2025-07-09
- JSON ready for Python script
Proceed with file updates? [y/n]
```

### Phase 3: Python Script (data-runners/news_updater.py)

**Input:** JSON from Phase 1 (stored in _data/handoff_data.json)
**Process:**
1. Create backups of existing _data files
2. Generate YAML entries (all items under target_date)
3. Prepend new entries to existing files
4. **Validation**: Verify exact item count matches between JSON input and YAML output for each category
5. Clean up backup files after successful updates
6. Provide update summary with item count verification

**Example Usage:**
```bash
python data-runners/news_updater.py --input _data/handoff_data.json
```

### Phase 4: Post-Processing (Git Operations)

**After successful Python script execution:**
1. **Git add**: Stage all modified YAML files
2. **Git commit**: Create descriptive commit message
3. **Git pull**: Sync with remote repository
4. **Git push**: Push changes to remote

**Example Commands:**
```bash
# Stage modified files
git add _data/*.yml

# Commit with descriptive message
git commit -m "Weekly news update $(date +%Y-%m-%d): Add X items across Y categories

🤖 Generated with [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com>"

# Sync and push
git pull && git push
```

### Error Handling
- **MCP Connection Issues**: Retry with fallback search
- **AI API Errors**: Use original descriptions
- **File Operation Errors**: Restore from backups using `--restore` flag
- **Validation Errors**: Show detailed error messages
- **Git Operation Errors**: Manual resolution required, backups preserved if Python script failed
- **Cleanup Errors**: Backup files preserved, updates still successful

### File Structure After Update
```yaml
# security-news.yml
- date: 2025-07-09
  news-items:
    - desc: "Enhanced description 1"
      link: "https://..."
    - desc: "Enhanced description 2"
      link: "https://..."
- date: 2025-06-12  # Previous entries preserved
  news-items: [...]
```

### Success Metrics
- All categories have consistent weekly updates
- No duplicate news items
- All links are valid and accessible
- YAML structure matches existing format
- **Item count validation**: Exact number of items in each category matches between JSON input and YAML output
- Backup files automatically cleaned after successful updates
- Git operations complete successfully with proper commit messages

## Bookmarks Sync Workflow

**Script**: `data-runners/obsidian_bookmarks_sync.py`
**Cron**: Every Sunday at 9:00 AM (`0 9 * * 0 ~/.config/me/vitraag_bookmarks_sync.sh`)
**Log**: `~/vitraag_bookmarks_sync.log`
**Output**: `assets/data/bookmarks.json` → powers the `/bookmarks` page

**Obsidian vault sources:**
- 2025 notes: `Personal-Archive/2025/daily/`
- 2026+ notes: `Personal-Data/2026/daily/`

**What gets extracted**: `[Title](URL)` markdown links only. Bare URLs skipped by default.

**Manual run:**
```bash
cd data-runners

# Auto (scans last 14 days, deduplication handles overlaps)
.venv/bin/python3 obsidian_bookmarks_sync.py

# From a specific date
.venv/bin/python3 obsidian_bookmarks_sync.py --start YYYY-MM-DD

# Preview without writing
.venv/bin/python3 obsidian_bookmarks_sync.py --start YYYY-MM-DD --dry-run --verbose

# Include bare URLs (fetches page titles via HTTP)
.venv/bin/python3 obsidian_bookmarks_sync.py --start YYYY-MM-DD --fetch-bare-urls
```

**How it works:**
1. Scans Personal-Archive 2025 notes from `--start` to 2025-12-31
2. Scans Personal-Data 2026 notes from 2026-01-01 to today
3. Extracts `[Title](URL)` links from each daily note
4. Deduplicates against existing `bookmarks.json` by URL
5. Merges and sorts descending by date, writes `assets/data/bookmarks.json`
6. Cron wrapper commits and pushes only if the file changed

**Output format** (matches existing Notion-sourced entries):
```json
{"date": "2026-02-27", "title": "Article Title #tag", "url": "https://..."}
```

## Newsletter Generation Workflow

**Script**: `data-runners/newsletter_generator.py`
**Trigger**: Run manually after `update-news` completes (no dedicated cron — newsletter is a deliberate weekly act)
**Output**: `_newsletters/YYYY-MM-DD.md` → accessible at `https://vitraag.com/newsletter/YYYY-MM-DD`

**Prerequisite**: `_data/*.yml` files must be updated first (run news sync).

**Manual run:**
```bash
cd data-runners

# Auto-detect date, issue number, and date range (recommended)
.venv/bin/python3 newsletter_generator.py --date $(date +%Y-%m-%d) --days 7 --force

# Override lookback window
.venv/bin/python3 newsletter_generator.py --date 2026-02-27 --days 14 --force
```

**How it works:**
1. Auto-detects issue number by counting existing files in `_newsletters/`
2. Reads stories from all `_data/*.yml` files within the date window
3. Requires minimum 20 total stories across at least 3 categories
4. Generates `_newsletters/YYYY-MM-DD.md` with Jekyll frontmatter, featured stories per category, and top sources
5. Commit and push manually after review:

```bash
git add _newsletters/YYYY-MM-DD.md
git commit -m "Weekly news update and Newsletter #N (YYYY-MM-DD): X items across Y categories"
git pull && git push
```

**Error handling:**
- `--force` overwrites an existing newsletter file for the same date
- If fewer than 20 stories exist, generation is skipped — run news sync first
