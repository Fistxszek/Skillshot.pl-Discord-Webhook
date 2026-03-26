import time
from discord_webhook import DiscordWebhook, DiscordEmbed
from config import WEBHOOK_URL, ROLES


def send_to_discord(parsed_entry):
    embed = DiscordEmbed(
        title=parsed_entry['title'],
        color="fa9405",
        url=parsed_entry['link']
    )

    if parsed_entry['image_url']:
        embed.set_image(parsed_entry['image_url'])

    embed.set_author(parsed_entry['author'])
    embed.set_thumbnail(
        url='https://www.skillshot.pl/gfx/skillshot-logo-square-256.jpg'
    )

    embed.add_embed_field(
        name="Rola", 
        value=ROLES.get(parsed_entry['category'], parsed_entry['category']),
        inline=True
    )

    embed.add_embed_field(name="", value="", inline=False)

    embed.add_embed_field(
        name="Wymagane doświadczenie", 
        value=parsed_entry['experience_level'], 
        inline=True
    )

    embed.add_embed_field(
        name="Lokalizacja", 
        value=parsed_entry['location'], 
        inline=True
    )

    if parsed_entry['additional_info']:
        additional_info_str = ", ".join(parsed_entry['additional_info'])
        embed.add_embed_field(
            name="Dodatkowe informacje", 
            value=additional_info_str, 
            inline=True
        )

    embed.add_embed_field(name="", value="", inline=False)

    embed.set_timestamp()
    if parsed_entry['published_parsed']:
        data_str = time.strftime('%d.%m.%Y %H:%M', parsed_entry['published_parsed'])
        embed.set_footer(
            text=f"Opublikowano na Skillshot.pl: {data_str}.\nGodzina powiadomienia"
        )

    webhook = DiscordWebhook(url=WEBHOOK_URL)
    webhook.add_embed(embed)
    webhook.execute()
