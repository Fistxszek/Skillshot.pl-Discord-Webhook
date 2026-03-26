from feed_parser import get_new_entries
from discord_notifier import send_to_discord
from parser import parse_entry_data
import time


def main():
    new_entries = get_new_entries()
    
    print(f"Found {len(new_entries)} new enrties.")
    for entry in new_entries:
        parsed_entry = parse_entry_data(entry)
        print(f"Sending discord notification about {parsed_entry['title']} for {parsed_entry['category']} role.")
        send_to_discord(parsed_entry)
        time.sleep(1)


if __name__ == "__main__":
    main()
