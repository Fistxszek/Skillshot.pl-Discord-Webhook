import requests
import feedparser
from config import URL
from cache import load_cache, save_cache


def get_new_entries():
    cache = load_cache()
    headers = {}
    last_id = None

    if cache['etag']:
        headers['If-None-Match'] = cache['etag']
    if cache['modified']:
        headers['If-Modified-Since'] = cache['modified']

    if cache.get('last_id'):
        last_id = cache['last_id']

    try:
        response = requests.get(URL, headers=headers, timeout=10)

        if response.status_code == 304:
            print("No new content.")
            return []

        response.raise_for_status()

        feed = feedparser.parse(response.content)
        new_entries = []

        if not last_id:
            last_found = True
        else:
            last_found = False

        for entry in reversed(feed.entries):
            if last_id == entry.id:
                last_found = True
                continue
            if last_found:
                new_entries.append(entry)
                last_id = entry.id

        new_etag = response.headers.get('etag')
        new_modified = response.headers.get('last-modified')
        save_cache(new_etag, new_modified, last_id)

        return new_entries

    except requests.exceptions.RequestException as e:
        print(f"Network Error: {e}")
        return []
