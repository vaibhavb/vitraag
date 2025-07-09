- For news (security-news, pm-news, finance-news and digitalhealth-news) get the appropriate tagged news from obsidian server and update the news items in \_data directory in YAML format. Do this on a weekly basis.

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
  - pm-news.yml → #pm-news
  - ai-news.yml → #ai-news

**Step 2: MCP Search by Tag**
For each category:
- Use `mcp__obsidian-server__obsidian_complex_search` to find items with tag since last date
- Search pattern: `{"and": [{"regexp": ["#TAG", {"var": "content"}]}, {"regexp": ["2025-0[6-9]|2025-1[0-2]", {"var": "path"}]}]}`
- Extract: date, description, link from each match

**Step 3: AI Formatting**
For each news item:
- Send to Claude API for description enhancement
- Prompt: "Make this news description professional, 1-2 sentences, remove personal notes/tags"
- Preserve original link

**Step 4: Generate Handoff Data**
Create JSON structure:
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

### Phase 3: Python Script (news_updater.py)

**Input:** JSON from Phase 1
**Process:**
1. Create backups of existing _data files
2. Generate YAML entries (all items under target_date)
3. Prepend new entries to existing files
4. Provide update summary

**Example Usage:**
```bash
python news_updater.py --input handoff_data.json
```

### Error Handling
- **MCP Connection Issues**: Retry with fallback search
- **AI API Errors**: Use original descriptions
- **File Operation Errors**: Restore from backups
- **Validation Errors**: Show detailed error messages

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
- Backups created before any changes

- 
