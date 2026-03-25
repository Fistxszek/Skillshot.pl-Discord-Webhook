from discord_webhook import DiscordWebhook, DiscordEmbed
import feedparser
import requests
import time
import json
import os
import re

URL = 'http://www.skillshot.pl/jobs/feed/all'
CACHE_FILES = 'feed_cache.json'

WEBHOOK_URL = os.environ.get('DISCORD_WEBHOOK_URL')

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


def get_first_image_from_html(html_content):
    match = re.search(r'<img [^>]*src="([^"]+)"', html_content)
    return match.group(1) if match else None


def send_to_discord(entry):
    embed = DiscordEmbed(
        title=entry.title,
        color="fa9405",
        url=entry.link
    )

    image = get_first_image_from_html(entry.summary)
    if image:
        embed.set_image(image)

    embed.set_author(entry.author)
    embed.set_thumbnail(
        url='https://www.skillshot.pl/gfx/skillshot-logo-square-256.jpg'
    )
    embed.add_embed_field(
        name="Rola", value=ROLES[entry.category], inline=True
    )

    embed.add_embed_field(name="", value="", inline=False)
    experienceKeyword = [
        word for word in EXPERIENCE if word.lower() in entry.title.lower()
    ]

    if experienceKeyword == "":
        experienceKeyword = [
            word for word in EXPERIENCE if word.lower()
            in entry.summary.lower()
        ]
    if experienceKeyword:
        embed.add_embed_field(
            name="Wymagane doświadczenie", value=experienceKeyword[0], inline=True
        )
    else:
        embed.add_embed_field(
            name="Wymagane doświadczenie", value="Nieznane", inline=True
        )

    embed.add_embed_field(
        name="Lokalizacja", value=entry.get('location', 'Zdalna'), inline=True
    )
    additional_info = [
        word for word in ADDITIONAL_INFO if word.lower() in entry.summary.lower()
    ]

    final_info = ""
    for info in additional_info:
        info = f"{info}"
        final_info = f"{final_info + info} "
    if final_info:
        embed.add_embed_field(
            name="Dodatkowe informacje", value=final_info, inline=True
        )

    embed.add_embed_field(name="", value="", inline=False)

    embed.set_timestamp()
    if hasattr(entry, 'published_parsed'):
        data_str = time.strftime('%d.%m.%Y %H:%M', entry.published_parsed)
        embed.set_footer(
            text=f"Opublikowano na Skillshot.pl: {data_str}.\nGodzina powiadomienia"
        )

    webhook = DiscordWebhook(url=WEBHOOK_URL)
    webhook.add_embed(embed)
    webhook.execute()


def load_cache():
    if os.path.exists(CACHE_FILES):
        with open(CACHE_FILES, 'r') as f:
            return json.load(f)
    return {'etag': None, 'modified': None, 'last_id': None}


def save_cache(etag, modified, id):
    with open(CACHE_FILES, 'w') as f:
        json.dump({'etag': etag, 'modified': modified, 'last_id': id}, f)


def getNewEntries():
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
            return

        response.raise_for_status()

        feed = feedparser.parse(response.content)

        if not last_id:
            last_found = True
        else:
            last_found = False

        for entry in reversed(feed.entries):
            if last_id == entry.id:
                last_found = True
                continue
            if last_found:
                send_to_discord(entry)
                last_id = entry.id

        new_etag = response.headers.get('etag')
        new_modified = response.headers.get('last-modified')
        save_cache(new_etag, new_modified, last_id)

    except requests.exceptions.RequestException as e:
        print(f"Network Error: {e}")


getNewEntries()
