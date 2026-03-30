from feed_parser import get_new_entries
from other_feed_parser import other_get_new_entries
from discord_notifier import send_to_discord
from other_discord_notifier import other_send_to_discord
from parser import parse_entry_data
from other_parser import other_parse_entry_data
import time
from config import FB_URL, WP_URL, WP, FB


def main():
    skillshot_new_entries = get_new_entries()
    fb_new_entries = other_get_new_entries(FB)
    wp_new_entries = other_get_new_entries(WP)
    
    print(f"Found {len(skillshot_new_entries)} new enrties.")
    for entry in skillshot_new_entries:
        parsed_entry = parse_entry_data(entry)
        print(f"Sending discord notification about {parsed_entry['title']} for {parsed_entry['category']} role.")
        send_to_discord(parsed_entry)
        time.sleep(1)

    print(f"FB: Found {len(fb_new_entries)} new enrties.")
    for entry in fb_new_entries:
        fb_parsed_entry = other_parse_entry_data(entry)
        print(f"Sending discord notification about FB offer {fb_parsed_entry['title']}.")
        other_send_to_discord(fb_parsed_entry, FB)
        time.sleep(1)

    print(f"WorkPlays: Found {len(wp_new_entries)} new enrties.")
    for entry in wp_new_entries:
        fb_parsed_entry = other_parse_entry_data(entry)
        print(f"Sending discord notification about WorkPlays offer {fb_parsed_entry['title']}.")
        other_send_to_discord(fb_parsed_entry, WP)
        time.sleep(1)


if __name__ == "__main__":
    main()
