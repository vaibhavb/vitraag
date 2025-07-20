from dotenv import load_dotenv
import os
from notion_client import Client
from datetime import datetime, timedelta
import sqlite3
import json
import argparse
import sys

def get_notion_links(numdays=7, datesince=None, db=None, json_file="../assets/data/bookmarks.json"):
    "Fetch all the links either from numdays or datesince (YYYY-MM-DD)"
    # Load environment variables from .env file
    load_dotenv()

    # Read the Notion token from the environment variable
    notion_token = os.getenv("NOTION_TOKEN")

    if notion_token is None:
        raise ValueError("No Notion token found in environment variables")

    # Initialize the Notion client with your integration token
    notion = Client(auth=notion_token)

    # The ID of the database you want to access
    database_id = os.getenv("DATABASE_ID")

    if database_id is None:
        raise ValueError("No database ID found in environment variables")

    save_as_sqlite = bool(db)
    save_as_json = bool(json_file)

    # Calculate the date to look back from
    if datesince:
        num_days_ago = datetime.strptime(datesince, "%Y-%m-%d")
    elif save_as_sqlite or save_as_json:
        num_days_ago = datetime.strptime("2024-01-01", "%Y-%m-%d")
    else:
        num_days_ago = datetime.now() - timedelta(days=numdays)
    
    num_days_ago_iso = num_days_ago.isoformat()

    print(f"Fetching results since: {num_days_ago_iso}")

    # Create a list to hold the data
    links_data = []

    # Implement pagination
    has_more = True
    next_cursor = None

    while has_more:
        # Query the database with a filter for the specified date range
        results = notion.databases.query(
            database_id=database_id,
            filter={
                "property": "Created",  # or "Updated" based on your requirement
                "date": {
                    "after": num_days_ago_iso
                }
            },
            start_cursor=next_cursor
        )

        # Iterate over the results and extract the link name, URL, and date
        for page in results["results"]:
            # Extract the link name from the 'Name' property
            name_property = page["properties"]["Name"]["title"]
            link_name = name_property[0]["text"]["content"] if name_property else "No Name"

            # Extract the URL from the 'URL' property
            url_property = page["properties"]["URL"]["url"]
            link_url = url_property if url_property else "No URL"

            # Extract the date from the 'Created' formula property or fallback to 'System Created'
            try:
                if "Created" in page["properties"] and page["properties"]["Created"]["formula"]:
                    # Use the formula result (which shows the effective date)
                    formula_result = page["properties"]["Created"]["formula"]
                    if formula_result and "date" in formula_result and formula_result["date"]:
                        created_date = formula_result["date"]["start"]
                    else:
                        # Formula exists but no date, fallback to System Created
                        created_property = page["properties"]["System Created"]["created_time"]
                        if created_property.endswith('Z'):
                            created_property = created_property.replace('Z', '+00:00')
                        created_date = datetime.fromisoformat(created_property).strftime("%Y-%m-%d")
                else:
                    # No formula property, use System Created
                    created_property = page["properties"]["System Created"]["created_time"]
                    if created_property.endswith('Z'):
                        created_property = created_property.replace('Z', '+00:00')
                    created_date = datetime.fromisoformat(created_property).strftime("%Y-%m-%d")
            except KeyError:
                # Fallback if properties don't exist as expected
                created_date = "Unknown"

            # Append the data to the list
            links_data.append((created_date, link_name, link_url))

        # Update pagination info
        has_more = results["has_more"]
        next_cursor = results["next_cursor"]

        print(f"Fetched {len(results['results'])} results. More results: {has_more}")

    # Sort the list by date
    links_data.sort()

    print(f"Total results fetched: {len(links_data)}")

    if save_as_sqlite:
        with sqlite3.connect(db) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                           CREATE TABLE IF NOT EXISTS links (
                             date TEXT,
                             title TEXT,
                             link TEXT
            )
            ''')
            for date, name, url in links_data:
                cursor.execute('INSERT INTO links (date, title, link) VALUES(?,?,?)',
                               (date, name, url))
            conn.commit()
        print(f"Data saved to SQLite database: {db}")
    elif save_as_json: 
        bookmarks = []
        # Sort bookmarks by date (most recent first)
        for date, name, url in links_data:
            bookmarks.append({
                "date": date,
                "title": name,
                "url": url
            })
        bookmarks.sort(key=lambda x: x['date'], reverse=True)
        os.makedirs(os.path.dirname(json_file), exist_ok=True)
        # Write data to JSON file
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(bookmarks, f, ensure_ascii=False, indent=2)
        print(f"Data saved to JSON file: {json_file}")
    else:
        # Print the sorted results
        for date, name, url in links_data:
            print(f"-[{date}]-[{name}]({url})")

def add_bookmark(title, url, tags=None, date=None):
    """Add a new bookmark to Notion database with URL as primary key"""
    load_dotenv()
    
    notion_token = os.getenv("NOTION_TOKEN")
    if notion_token is None:
        raise ValueError("No Notion token found in environment variables")
    
    database_id = os.getenv("DATABASE_ID")
    if database_id is None:
        raise ValueError("No database ID found in environment variables")
    
    notion = Client(auth=notion_token)
    
    # Check if URL already exists
    existing = notion.databases.query(
        database_id=database_id,
        filter={
            "property": "URL",
            "url": {
                "equals": url
            }
        }
    )
    
    if existing["results"]:
        print(f"⚠️  URL already exists: {url}")
        print(f"   Existing title: {existing['results'][0]['properties']['Name']['title'][0]['text']['content']}")
        return existing["results"][0]["id"]
    
    # Create properties for the new page
    properties = {
        "Name": {
            "title": [
                {
                    "text": {
                        "content": title
                    }
                }
            ]
        },
        "URL": {
            "url": url
        }
    }
    
    # Add custom date if provided (using a Date property)
    if date:
        try:
            # Parse date string to ensure it's valid
            from datetime import datetime
            if isinstance(date, str):
                parsed_date = datetime.strptime(date, "%Y-%m-%d")
                properties["Created date"] = {
                    "date": {
                        "start": date
                    }
                }
                print(f"📅 Setting bookmark for date: {date}")
        except ValueError:
            print(f"⚠️  Invalid date format: {date}. Using current date instead.")
            date = None
    
    # Add tags if provided
    if tags:
        tag_list = [tag.strip() for tag in tags.split(',') if tag.strip()]
        if tag_list:
            properties["Tags"] = {
                "multi_select": [{"name": tag} for tag in tag_list]
            }
    
    try:
        # Create the page in the database
        response = notion.pages.create(
            parent={"database_id": database_id},
            properties=properties
        )
        print(f"✅ Successfully added bookmark: {title}")
        print(f"   URL: {url}")
        if tags:
            print(f"   Tags: {tags}")
        return response['id']
    except Exception as e:
        print(f"❌ Error adding bookmark: {e}")
        return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch or add Notion links")
    parser.add_argument('--numdays', type=int, default=7, help='Number of days to look back')
    parser.add_argument('--datesince', type=str, help='YYYY-MM-DD')
    parser.add_argument('--db', type=str, help="filename.db")
    parser.add_argument('--json_file', help="bookmarks.json")
    parser.add_argument('--add', action='store_true', help='Add a new bookmark')
    parser.add_argument('--title', type=str, help='Title of the bookmark')
    parser.add_argument('--url', type=str, help='URL of the bookmark')
    parser.add_argument('--tags', type=str, help='Comma-separated tags')
    parser.add_argument('--date', type=str, help='Date for the bookmark (YYYY-MM-DD format)')
    args = parser.parse_args()

    if args.add:
        if not args.title or not args.url:
            print("❌ Error: --title and --url are required when using --add")
            sys.exit(1)
        add_bookmark(args.title, args.url, args.tags, args.date)
    else:
        get_notion_links(args.numdays, args.datesince, args.db, args.json_file)
