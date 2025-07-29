#!/usr/bin/env python3
"""
Newsletter Generator for Weekly Tech Digest

This script reads news data from YAML files and generates newsletter markdown files
for Jekyll with NYT-style formatting and rich content.
"""

import yaml
import os
import sys
from datetime import datetime, timedelta
from pathlib import Path
from urllib.parse import urlparse
from collections import defaultdict
import argparse


def load_yaml_data(file_path):
    """Load and parse YAML news data"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f) or []
    except FileNotFoundError:
        print(f"⚠️  Warning: File not found: {file_path}")
        return []
    except yaml.YAMLError as e:
        print(f"❌ Error parsing YAML file {file_path}: {e}")
        return []


def filter_stories_by_date_range(news_data, start_date, end_date):
    """Filter stories within date range"""
    filtered_stories = []
    
    for date_group in news_data:
        try:
            # Parse date from YAML (format: '2025-07-28')
            group_date = datetime.strptime(str(date_group['date']), '%Y-%m-%d')
            
            if start_date <= group_date <= end_date:
                for story in date_group.get('news-items', []):
                    story_copy = story.copy()
                    story_copy['publish_date'] = date_group['date']
                    story_copy['category_date'] = group_date
                    filtered_stories.append(story_copy)
        except (ValueError, KeyError) as e:
            print(f"⚠️  Warning: Error processing date group: {e}")
            continue
    
    # Sort by date (most recent first)
    filtered_stories.sort(key=lambda x: x['category_date'], reverse=True)
    return filtered_stories


def extract_domain(url):
    """Extract clean domain from URL"""
    try:
        domain = urlparse(url).netloc
        if domain.startswith('www.'):
            domain = domain[4:]
        return domain
    except:
        return "unknown"


def calculate_top_sources(all_stories):
    """Calculate top news sources from stories"""
    domain_counts = defaultdict(int)
    
    for story in all_stories:
        if 'link' in story:
            domain = extract_domain(story['link'])
            domain_counts[domain] += 1
    
    # Return sorted list of (domain, count) tuples
    return sorted(domain_counts.items(), key=lambda x: x[1], reverse=True)


def get_next_issue_number():
    """Calculate next issue number based on existing newsletters"""
    newsletters_dir = Path('../_newsletters')
    if not newsletters_dir.exists():
        return 1
    
    existing_files = list(newsletters_dir.glob('*.md'))
    return len(existing_files) + 1


def generate_newsletter(target_date=None, days_back=7, force=False):
    """Generate newsletter for specified date range"""
    
    if target_date:
        try:
            end_date = datetime.strptime(target_date, '%Y-%m-%d')
        except ValueError:
            print(f"❌ Error: Invalid date format. Use YYYY-MM-DD")
            return None
    else:
        end_date = datetime.now()
    
    start_date = end_date - timedelta(days=days_back)
    
    print(f"📅 Generating newsletter for {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}")
    
    # Check if newsletter already exists
    newsletter_file = Path(f"../_newsletters/{end_date.strftime('%Y-%m-%d')}.md")
    if newsletter_file.exists() and not force:
        print(f"⚠️  Newsletter for {end_date.strftime('%Y-%m-%d')} already exists. Use --force to regenerate.")
        return None
    
    # Load news from all YAML files
    categories = {
        'security': {
            'file': '../_data/security-news.yml',
            'emoji': '🔒',
            'title': 'Security News',
            'description': 'Critical security developments, breaches, and cybersecurity innovations'
        },
        'ai': {
            'file': '../_data/ai-news.yml',
            'emoji': '🤖',
            'title': 'AI & Machine Learning',
            'description': 'Artificial intelligence breakthroughs, research, and industry developments'
        },
        'digitalhealth': {
            'file': '../_data/digitalhealth-news.yml',
            'emoji': '🏥',
            'title': 'Digital Health',
            'description': 'Healthcare technology, medical innovations, and digital health trends'
        },
        'pm': {
            'file': '../_data/pm-news.yml',
            'emoji': '📊',
            'title': 'Product Management',
            'description': 'Product strategy, management insights, and industry best practices'
        },
        'finance': {
            'file': '../_data/finance-news.yml',
            'emoji': '💰',
            'title': 'Finance & Markets',
            'description': 'Financial technology, market trends, and investment insights'
        }
    }
    
    newsletter_data = {
        'date': end_date.strftime('%Y-%m-%d'),
        'start_date': start_date.strftime('%Y-%m-%d'),
        'end_date': end_date.strftime('%Y-%m-%d'),
        'issue_number': get_next_issue_number(),
        'categories': {}
    }
    
    total_stories = 0
    all_stories = []
    
    # Process each category
    for category_key, category_info in categories.items():
        if os.path.exists(category_info['file']):
            news_data = load_yaml_data(category_info['file'])
            stories = filter_stories_by_date_range(news_data, start_date, end_date)
            
            newsletter_data['categories'][category_key] = {
                'stories': stories,
                'count': len(stories),
                'info': category_info
            }
            total_stories += len(stories)
            all_stories.extend(stories)
            
            print(f"📊 {category_info['emoji']} {category_info['title'].upper()}: {len(stories)} stories")
        else:
            print(f"⚠️  File not found: {category_info['file']}")
            newsletter_data['categories'][category_key] = {
                'stories': [],
                'count': 0,
                'info': category_info
            }
    
    newsletter_data['total_stories'] = total_stories
    newsletter_data['top_sources'] = calculate_top_sources(all_stories)
    newsletter_data['source_count'] = len(set(extract_domain(story['link']) for story in all_stories if 'link' in story))
    
    if total_stories == 0:
        print(f"⚠️  No stories found in the specified date range. Newsletter not generated.")
        return None
    
    # Generate the newsletter file
    create_newsletter_file(newsletter_data)
    
    return newsletter_data


def create_newsletter_file(data):
    """Create newsletter markdown file with NYT-style content"""
    
    # Ensure newsletters directory exists
    os.makedirs('../_newsletters', exist_ok=True)
    
    # Generate frontmatter
    frontmatter = f"""---
layout: newsletter
title: "The Weekly Vitraag Digest #{data['issue_number']}"
date: {data['date']}
issue_number: {data['issue_number']}
total_stories: {data['total_stories']}
date_range: "{data['start_date']} to {data['end_date']}"
security_count: {data['categories'].get('security', {}).get('count', 0)}
ai_count: {data['categories'].get('ai', {}).get('count', 0)}
health_count: {data['categories'].get('digitalhealth', {}).get('count', 0)}
pm_count: {data['categories'].get('pm', {}).get('count', 0)}
finance_count: {data['categories'].get('finance', {}).get('count', 0)}
source_count: {data['source_count']}
top_sources:"""

    # Add top sources as proper YAML list
    for source, count in data['top_sources'][:5]:
        frontmatter += f"\n  - name: \"{source}\"\n    count: {count}"
    
    frontmatter += """
categories: 
  - Technology
  - Security
  - AI
  - Health Tech
  - Product Management
  - Finance
editors_note: "This week brought significant developments across the tech landscape. Here are the {data['total_stories']} stories I've curated that shaped the week from {data['start_date']} to {data['date']}."
---

"""
    
    # Generate content sections
    content = generate_content_sections(data)
    
    # Write file
    filename = f"../_newsletters/{data['date']}.md"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(frontmatter + content)
    
    print(f"✅ Newsletter created: {filename}")
    print(f"📊 Total stories: {data['total_stories']}")
    print(f"🔢 Issue number: #{data['issue_number']}")


def generate_content_sections(data):
    """Generate newsletter content sections with NYT-style formatting"""
    
    content = ""
    
    # Process each category that has stories
    for category_key, category_data in data['categories'].items():
        if category_data['count'] > 0:
            stories = category_data['stories']
            info = category_data['info']
            
            content += f"""
<section class="category-section" id="{category_key}">
    <div class="category-header">
        <h2>{info['emoji']} {info['title']}</h2>
        <div class="category-subtitle">{category_data['count']} stories • {info['description']}</div>
    </div>
"""
            
            # Featured story (first/most recent story)
            if stories:
                featured = stories[0]
                content += f"""
    <div class="featured-story">
        <h3>Featured Story</h3>
        <div class="story-title">
            <a href="{featured['link']}" target="_blank">{featured['desc']}</a>
        </div>
        <div class="story-meta">Published {featured['publish_date']} • {extract_domain(featured['link'])}</div>
        <div class="story-excerpt">{featured['desc']}</div>
        <a href="{featured['link']}" target="_blank" class="read-more">Read Full Story →</a>
    </div>
"""
            
            # Other stories in the category
            if len(stories) > 1:
                content += f"""
    <div class="story-list">
        <h4>More {info['title']} Headlines</h4>
"""
                
                for i, story in enumerate(stories[1:6], 1):  # Show up to 5 more stories
                    content += f"""
        <div class="story-item">
            <div class="story-headline">
                <a href="{story['link']}" target="_blank">{story['desc']}</a>
            </div>
            <div class="story-meta">{story['publish_date']} • {extract_domain(story['link'])}</div>
            <div class="story-summary">{story['desc']}</div>
        </div>
"""
                
                # Show more button if there are additional stories
                if len(stories) > 6:
                    remaining = len(stories) - 6
                    content += f"""
        <div class="show-more">
            <button class="show-more-btn">▼ Show {remaining} more {info['title'].lower()} stories</button>
        </div>
"""
                    
                    # Hidden stories
                    for story in stories[6:]:
                        content += f"""
        <div class="story-item hidden" style="display: none;">
            <div class="story-headline">
                <a href="{story['link']}" target="_blank">{story['desc']}</a>
            </div>
            <div class="story-meta">{story['publish_date']} • {extract_domain(story['link'])}</div>
            <div class="story-summary">{story['desc']}</div>
        </div>
"""
                
                content += """
    </div>
"""
            
            content += """
</section>
"""
    
    return content


def main():
    """Main function with command line interface"""
    parser = argparse.ArgumentParser(
        description='Generate Weekly Tech Digest newsletter from YAML news files',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python newsletter_generator.py                    # Generate for current week
  python newsletter_generator.py --date 2025-07-28 # Generate for specific date
  python newsletter_generator.py --days 14         # Look back 14 days
  python newsletter_generator.py --force           # Regenerate existing newsletter
        """
    )
    
    parser.add_argument(
        '--date', 
        help='Target date for newsletter (YYYY-MM-DD)', 
        default=None
    )
    parser.add_argument(
        '--days', 
        help='Number of days to look back', 
        type=int, 
        default=7
    )
    parser.add_argument(
        '--force', 
        action='store_true',
        help='Force regeneration if newsletter already exists'
    )
    
    args = parser.parse_args()
    
    try:
        print("🚀 Starting newsletter generation...")
        newsletter_data = generate_newsletter(args.date, args.days, args.force)
        
        if newsletter_data:
            print(f"\n✅ Newsletter #{newsletter_data['issue_number']} generated successfully!")
            print(f"📁 File: _newsletters/{newsletter_data['date']}.md")
            print(f"📊 Stories: {newsletter_data['total_stories']} across {len([c for c in newsletter_data['categories'].values() if c['count'] > 0])} categories")
            print(f"🌐 Sources: {newsletter_data['source_count']} unique domains")
            print(f"\n📖 View at: https://vitraag.com/newsletter/{newsletter_data['date']}")
            print(f"📡 RSS: https://vitraag.com/newsletter.xml")
            
            if newsletter_data['top_sources']:
                print(f"\n📈 Top sources:")
                for domain, count in newsletter_data['top_sources'][:3]:
                    print(f"   • {domain}: {count} stories")
                    
        else:
            print("\n❌ Newsletter generation failed or no stories found.")
            sys.exit(1)
            
    except KeyboardInterrupt:
        print("\n\n⏹️  Newsletter generation cancelled by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error generating newsletter: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()