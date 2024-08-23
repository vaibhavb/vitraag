from dotenv import load_dotenv
import os
from notion_client import Client
from datetime import datetime, timedelta
import sqlite3
import json
import argparse

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

            # Extract the creation date from the 'Created' property
            created_property = page["properties"]["Created"]["created_time"]
            if created_property.endswith('Z'):
                created_property = created_property.replace('Z', '+00:00')
            created_date = datetime.fromisoformat(created_property).strftime("%Y-%m-%d")

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

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch Notion links")
    parser.add_argument('--numdays', type=int, default=7, help='Number of days to look back')
    parser.add_argument('--datesince', type=str, help='YYYY-MM-DD')
    parser.add_argument('--db', type=str, help="filename.db")
    parser.add_argument('--json_file', type=str, default="../assets/data/bookmarks.json", help="bookmarks.json")
    args = parser.parse_args()

    get_notion_links(args.numdays, args.datesince, args.db, args.json_file)
