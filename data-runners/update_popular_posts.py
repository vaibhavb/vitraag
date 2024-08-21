from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import DateRange, Metric, Dimension, OrderBy, RunReportRequest
from google.oauth2 import service_account
import yaml
import os
import argparse
from datetime import datetime, timezone

def get_analytics_client(key_file_path):
    credentials = service_account.Credentials.from_service_account_file(
        key_file_path,
        scopes=["https://www.googleapis.com/auth/analytics.readonly"]
    )
    return BetaAnalyticsDataClient(credentials=credentials)

def get_top_links_from_google_analytics(property_id, client, num_links=10, date_range_days=365):
    date_range = DateRange(start_date=f"{date_range_days}daysAgo", end_date="today")
    metrics = [Metric(name="screenPageViews")]
    dimensions = [Dimension(name="pagePath"), Dimension(name="pageTitle")]
    
    request = RunReportRequest(
        property=f"properties/{property_id}",
        date_ranges=[date_range],
        metrics=metrics,
        dimensions=dimensions,
        limit=num_links,
        order_bys=[OrderBy(metric=OrderBy.MetricOrderBy(metric_name="screenPageViews"), desc=True)]
    )
    
    response = client.run_report(request)
    
    top_links = []
    for row in response.rows:
        page_path = row.dimension_values[0].value
        page_title = row.dimension_values[1].value
        pageviews = int(row.metric_values[0].value)
        top_links.append({
            "path": page_path,
            "title": page_title,
            "pageviews": pageviews
        })
    
    return top_links

def save_to_yaml(data, filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w') as file:
        yaml.dump(data, file)

def main():
    parser = argparse.ArgumentParser(description='Fetch top links from Google Analytics and save to YAML for Jekyll.')
    parser.add_argument('--property-id', default='347063338', help='Google Analytics property ID (default: 347063338)')
    parser.add_argument('--key-file', default='/Users/vaibhavb/.google/google_cloud_ganalytics.json', help='Path to the JSON key file (default: /Users/vaibhavb/.google/google_cloud_ganalytics.json)')
    parser.add_argument('--output', default='content/data/popular_posts.yml', help='Output YAML file location (default: content/data/popular_posts.yml)')
    parser.add_argument('--num-links', type=int, default=10, help='Number of top links to fetch (default: 10)')
    parser.add_argument('--days', type=int, default=365, help='Number of days to look back for data (default: 365)')
    
    args = parser.parse_args()
    
    client = get_analytics_client(args.key_file)
    top_links = get_top_links_from_google_analytics(args.property_id, client, args.num_links, args.days)
    
    # Add last_updated timestamp
    now = datetime.now(timezone.utc)
    data = {
        "last_updated": now.isoformat(),
        "posts": top_links
    }
    
    save_to_yaml(data, args.output)
    
    print(f"Top {args.num_links} links saved to {args.output}")
    print(f"Data last updated: {now.strftime('%Y-%m-%d %H:%M:%S %Z')}")
    for link in top_links:
        print(f"Title: {link['title']}")
        print(f"Link: {link['path']}")
        print(f"Pageviews: {link['pageviews']}")
        print("---")

if __name__ == '__main__':
    main()

