import requests
import feedparser
from cache import load_other_cache, save_other_cache
from config import FB_URL, WP_URL, FB, WP, WP_CACHE_FILES, FB_CACHE_FILES, MAX_ENTRIES


def other_get_new_entries(noti_type):
    cache = None
    if noti_type is FB:
        cache = load_other_cache(FB_CACHE_FILES)
    elif noti_type is WP:
        cache = load_other_cache(WP_CACHE_FILES)
    last_link = None
    if cache.get('last_link'):
        last_link = cache['last_link']

    try:
        if noti_type is FB:
            url = FB_URL
        elif noti_type is WP:
            url = WP_URL
        response = requests.get(url, timeout=10)

        response.raise_for_status()

        feed = feedparser.parse(response.content)

        entries_to_check = feed.entries[:MAX_ENTRIES]
        new_entries = []

        if not last_link:
            last_found = True
        else:
            last_found = False

        for entry in reversed(entries_to_check):
            if last_link == entry.link:
                last_found = True
                continue
            if last_found:
                new_entries.append(entry)
                last_link = entry.link

        if noti_type is FB:
            save_other_cache(last_link, FB_CACHE_FILES)
        elif noti_type is WP:
            save_other_cache(last_link, WP_CACHE_FILES)


        return new_entries

    except requests.exceptions.RequestException as e:
        print(f"Network Error: {e}")
        return []
