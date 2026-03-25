import feedparser
import requests
import time
import json
import os

URL = 'http://www.skillshot.pl/jobs/feed/all'
CACHE_FILES = 'feed_cache.json'

def load_cache():
    if os.path.exists(CACHE_FILES):
        with open(CACHE_FILES, 'r') as f:
            return json.load(f)
    return {'etag': None, 'modified': None}

def save_cache(etag, modified):
    with open(CACHE_FILES, 'w') as f:
        json.dump({'etag': etag, 'modified': modified}, f)

def getNewEntries():
    cache = load_cache()

    headers = {}
    if cache['etag']:
        headers['If-None-Match'] = cache['etag']
    if cache['modified']:
        headers['If-Modified-Since'] = cache['modified']

    try:
        response = requests.get(URL, headers=headers, timeout=10)

        if response.status_code == 304:
            print("No new content.")
            return 

        response.raise_for_status()

        feed = feedparser.parse(response.content)
        print(f"===New entires found: {len(feed.entries)}---")

        print(f"Feed Title: {feed.feed.get('title')}")
        print(f"Feed Description: {feed.feed.get('description')}")

        entry = feed.entries[0]
        keywords = ['junior', 'mid', 'senior', 'pracy']
        content = entry.summary.lower()

        found = [word for word in keywords if word in content]

        if found:
            print(f"Znalezino dopasowania: {found}")
        # for entry in feed.entries:
        #     print(f"\nTitle: {entry.title}")
        #     print(f"Link: {entry.URL}")
        #     print(f"Kategoria: {entry.category}")
        #     print(f"Lokalizacja: {entry.location}")
        #     print(f"ID: {entry.id}")
        #     if hasattr(entry, 'published_parsed'):
        #         readable_date = time.strftime('%d.%m.%Yr %H:%M', entry.published_parsed)
        #         print(f"Date: {readable_date}")
        
        new_etag = response.headers.get('etag')
        new_modified = response.headers.get('last-modified')
        save_cache(new_etag, new_modified)

    except requests.exceptions.RequestException as e:
        print(f"Network Error: {e}")

getNewEntries()