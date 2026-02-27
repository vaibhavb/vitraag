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

### Command: `update-news`

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

### Command: `sync-bookmarks`

**Purpose**: Extract markdown links from Obsidian daily notes and merge them into `assets/data/bookmarks.json`, which powers the `/bookmarks` page.

**Obsidian Vault Locations:**
- **2025 notes**: `$OBS_DIR/../Personal-Archive/2025/daily/` (Personal-Archive vault)
- **2026+ notes**: `$OBS_DIR/2026/daily/` (Personal-Data vault, i.e. `$OBS_DIR`)

**What gets extracted**: Only `[Title](URL)` markdown links. Bare URLs are skipped by default (use `--fetch-bare-urls` to include them with fetched page titles).

**Script**: `data-runners/obsidian_bookmarks_sync.py`

**Weekly Usage:**
```bash
cd data-runners

# Standard run (incremental from last sync date)
python obsidian_bookmarks_sync.py --start YYYY-MM-DD

# Dry run to preview without writing
python obsidian_bookmarks_sync.py --start YYYY-MM-DD --dry-run --verbose

# Include bare URLs (fetches page titles via HTTP)
python obsidian_bookmarks_sync.py --start YYYY-MM-DD --fetch-bare-urls
```

**Initial / Full Backfill** (Week 46 2025 onwards):
```bash
python obsidian_bookmarks_sync.py --start 2025-11-10
```

**How it works:**
1. Scans Personal-Archive 2025 daily notes from `--start` to 2025-12-31
2. Scans Personal-Data 2026 daily notes from 2026-01-01 to today
3. Extracts `[Title](URL)` links from each note
4. Deduplicates against existing `bookmarks.json` by URL
5. Merges new entries and sorts descending by date
6. Writes updated `assets/data/bookmarks.json`

**Output format** (matches existing Notion-sourced entries):
```json
{"date": "2026-02-27", "title": "Article Title #tag", "url": "https://..."}
```

**Git Operations:**
```bash
git add assets/data/bookmarks.json
git commit -m "Sync Obsidian bookmarks YYYY-MM-DD: +N new bookmarks"
git pull && git push
```

**Success Metrics:**
- Net new bookmark count reported (deduplication working correctly)
- No duplicate URLs in output file
- Date range spans both vault directories seamlessly
- `bookmarks.json` total count increases by expected amount

## Newsletter Generation Workflow

### Command: `generate-newsletter`

**Purpose**: Generate newsletter using updated news data after completing news update workflow

**Prerequisites**: 
- Must have completed `update-news` workflow successfully
- All YAML files should be updated and committed to git
- Newsletter generator script available at `data-runners/newsletter_generator.py`

**Workflow Steps:**
1. **Auto-detect target date** from most recent YAML entries across all categories
2. **Calculate next issue number** by examining existing newsletters in `_newsletters/` directory
3. **Determine optimal date range** based on last newsletter's end date to avoid gaps/overlaps
4. **Validate data availability** and ensure minimum content thresholds
5. **Generate newsletter** with rich formatting, metadata, and category organization
6. **Validate output** for completeness and proper structure
7. **Stage and commit** newsletter file with descriptive git message

**Command Execution:**
```bash
# Navigate to data-runners directory
cd data-runners

# Execute newsletter generator with auto-detection
python newsletter_generator.py --date [AUTO_DETECTED_DATE] --days [CALCULATED_RANGE] --force
```

**Auto-Detection Logic:**
- **Target Date**: Read first date from each `_data/*.yml` file, use most recent date found
- **Issue Number**: Scan all existing `.md` files in `_newsletters/` directory, sort chronologically, increment by 1
- **Date Range**: Calculate days since last newsletter's end date to ensure complete coverage without gaps
- **Validation**: Verify minimum 20 total stories across all categories before generation

**Issue Number Calculation:**
- Dynamically counts all existing newsletter files in `_newsletters/` directory
- Sorts by date to ensure chronological ordering
- Returns `total_existing_newsletters + 1` for new newsletters
- Handles existing dates by returning their chronological position

**Validation Steps:**
1. **Data Validation**:
   - Minimum 20 total stories required across all categories
   - At least 3 categories must have content
   - All story links must be valid URLs
   - No duplicate stories within date range

2. **Output Validation**:
   - Newsletter file successfully created in `_newsletters/` directory
   - Proper Jekyll frontmatter with all required fields
   - Issue number increments correctly from last newsletter
   - Story counts match between YAML sources and newsletter output

3. **Content Quality**:
   - Featured stories selected for each category
   - Top news sources calculated and included
   - Category descriptions and metadata populated
   - Date ranges and issue numbering consistent

**Git Operations:**
After successful newsletter generation:
1. **Stage newsletter file**: `git add _newsletters/[DATE].md`
2. **Commit with metadata**: 
```bash
git commit -m "Generate Newsletter #[ISSUE] for [DATE]: [TOTAL] stories across [CATEGORIES] categories

Featured content:
- Security: [COUNT] stories 
- AI/ML: [COUNT] stories
- Digital Health: [COUNT] stories  
- Product Management: [COUNT] stories
- Finance: [COUNT] stories

🗞️ Generated with [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com>"
```
3. **Sync with remote**: `git pull && git push`

**Error Handling:**
- **Insufficient Stories**: Skip generation, request more content via `update-news`
- **Missing YAML Files**: Report which categories are missing, suggest running `update-news`
- **Newsletter Exists**: Use `--force` flag or increment date to avoid conflicts
- **Git Conflicts**: Manual resolution required, preserve newsletter file
- **Validation Failures**: Detailed error reporting with specific issues and suggestions

**Success Metrics:**
- Newsletter file created with proper naming convention (`YYYY-MM-DD.md`)
- Issue number increments sequentially from previous newsletter
- All categories with available content are represented
- Story counts and metadata are accurate
- Git commit includes newsletter with descriptive message
- Generated newsletter is accessible at `https://vitraag.com/newsletter/[DATE]`

**Output Example:**
```
📰 NEWSLETTER GENERATION COMPLETE
✅ Newsletter #5 created: _newsletters/2025-08-26.md
📊 Content: 67 stories across 5 categories
📅 Date Range: 2025-08-15 to 2025-08-26 (12 days)
🌐 Top Sources: github.com (8), youtube.com (6), techcrunch.com (4)
📁 Git: Committed and pushed to remote repository
🔗 View: https://vitraag.com/newsletter/2025-08-26
```

**Usage Examples:**
```bash
# Auto-detect everything (recommended)
generate-newsletter

# Override target date if needed
generate-newsletter --date 2025-08-26

# Custom lookback period  
generate-newsletter --days 14

# Force regeneration of existing newsletter
generate-newsletter --force

# Dry run to preview without creating files
generate-newsletter --preview
```
