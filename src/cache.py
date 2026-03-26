import json
import os
from config import CACHE_FILES


def load_cache():
    if os.path.exists(CACHE_FILES):
        with open(CACHE_FILES, 'r') as f:
            return json.load(f)
    return {'etag': None, 'modified': None, 'last_id': None}


def save_cache(etag, modified, last_id):
    with open(CACHE_FILES, 'w') as f:
        json.dump({'etag': etag, 'modified': modified, 'last_id': last_id}, f)
