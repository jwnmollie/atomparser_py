import requests
import feedparser
from datetime import datetime, timedelta

def fetch_atom_feed(url):
    response = requests.get(url)
    return response.content

def parse_atom_feed(feed_content):
    feed = feedparser.parse(feed_content)
    return feed.entries

def get_last_entries(entries, count):
    return entries[-count:]

def main():
    url = "https://www.paypal-status.com/feed/atom"

    atom_feed_content = fetch_atom_feed(url)
    entries = parse_atom_feed(atom_feed_content)
    last_entries = get_last_entries(entries, 3)

    for entry in last_entries:
        print(f"Title: {entry.title}")
        print(f"Description: {entry.summary}")
        print("\n---\n")

if __name__ == "__main__":
    main()
