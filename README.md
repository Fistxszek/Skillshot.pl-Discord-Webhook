# [Skillshot.pl](https://www.skillshot.pl/) Discord webhook

## Description

This is very simple `python` project that reads Atom feed from [Skillshot.pl](https://www.skillshot.pl/) and posts Discord message with Discord Webhook.

> [!INFO]
> Disclaimer: This bot is an unofficial community project made by me. It is not affiliated with, maintained by, or endorsed by Skillshot.pl."

## Features

- Monitors Atom feed from Skillshot.pl for new job postings
- Sends formatted Discord embeds with job details (title, author, experience level, location, additional info)
- Caches feed data to prevent duplicate notifications
- Supports role mentions based on job categories
- Extracts images from job descriptions for embed thumbnails

## Prerequisites

- Python 3.x
- A Discord webhook URL (obtain from your Discord server settings)

## Installation

1. Clone the repository:
   ```
   git clone git@github.com:Fistxszek/Skillshot.pl-Discord-Webhook.git
   ```

2. Install the required Python packages:
   ```
   pip install discord-webhook feedparser requests
   ```

## Setup

1. Set up your environment variables:

   Set the environment variable:

   ```
   export DISCORD_WEBHOOK_URL='your_discord_webhook_url_here'
   ```
> [!IMPORTANT]  
> The `ROLES` dictionary in `config.py` maps Skillshot categories to Discord role mentions.
> - Replace the IDs with your own Discord role IDs if you want role ping support to work correctly.

## Usage

Run the script to check for new job postings and send notifications:

```
python3 src/main.py
```

The bot will:
- Fetch the latest Atom feed
- Compare with cached data
- Send Discord notifications for new entries
- Update the cache

For continuous monitoring, you can run this script periodically (e.g., via cron job or a scheduler).

## Configuration

- **URL**: The Atom feed URL (currently set to http://www.skillshot.pl/jobs/feed/all)
- **CACHE_FILES**: Path to the cache file (default: 'feed_cache.json')
- **ROLES**: Discord role mentions for different job categories (customize as needed)
- **ADDITIONAL_INFO**: Keywords to extract additional job information
- **EXPERIENCE**: Experience levels to detect in job titles/descriptions

## Legal Disclaimer & Ethics

### 1. Ownership of Content

This bot is a technical tool designed for personal or community informational purposes only. All job offers, descriptions, company names, and brand logos are the sole property of their respective owners and the **Skillshot.pl** service. This project does not claim any ownership over the data fetched via the Atom/RSS feed.

### 2. Use of Trademarks and Logos

Any logos or images displayed within Discord Embeds are fetched directly from public URLs provided in the automated feed. These assets are used under the principle of "Fair Use" for identification and context, intended to assist the user in identifying the employer associated with a specific listing.

### 3. Service Respect & Infrastructure

This bot is built to be a "good citizen" of the web. It respects **Skillshot.pl**'s infrastructure by:

- Using **ETag** and **Last-Modified** HTTP headers to minimize unnecessary data transfer and server load.
- Implementing a responsible polling interval to ensure compliance with standard web crawler ethics.

## Third-Party Libraries
This project is build based on other libraries. It uses the following open-source libraries:
* **discord-webhook** (MIT) - Used for sending formatted messages to Discord.
* **feedparser** (BSD-2-Clause) - Used for parsing the Skillshot.pl Atom feed.
* **requests** (Apache-2.0) - Used for making HTTP requests with ETag support.

# License

See the [LICENSE](LICENSE.md) file for license rights and limitations (MIT).
