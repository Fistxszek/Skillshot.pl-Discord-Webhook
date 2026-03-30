import os

URL = 'http://www.skillshot.pl/jobs/feed/all'
FB_URL = 'https://rss.app/feeds/TRCEpTeNX2L4IteC.xml'
WP_URL = 'https://workplays.it/api/rss.xml'
CACHE_FILES = 'skillshot_feed_cache.json'
FB_CACHE_FILES = 'fb_feed_cache.json'
WP_CACHE_FILES = 'wp_feed_cache.json'

WEBHOOK_URL = os.environ.get('DISCORD_WEBHOOK_URL')

SKILLSHOT='skillshot'
FB='fb'
WP='workplays'

MAX_ENTRIES=10

ADDITIONAL_INFO = [
    "Umowa o pracę",
    "Umowa o dzieło",
    "Umowa zlecenie",
    "B2B",
    "Część etatu",
    "Pół etatu",
    "Elastyczne godziny pracy",
    "Staż",
    "Praktyki"
]

EXPERIENCE = ["Junior", "Mid", "Senior"]

ROLES = {
    'Programowanie': "<@&1442114495039410248>",
    'Grafika i animacja': "<@&1442116831539101737>",
    'Design': "<@&1442116910178238496>",
    'Audio': "<@&1442116955854078032>",
    'Testowanie': "<@&1442116983364522064>",
    'Zarządzanie': "<@&1442117004378116262>",
    'Inne': "<@&1442117029581553684>"
}
