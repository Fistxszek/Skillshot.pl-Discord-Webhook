from discord_webhook import DiscordWebhook, DiscordEmbed
from config import WEBHOOK_URL, FB, WP
import time


def other_send_to_discord(parsed_entry, type):
    embed = DiscordEmbed(
        title=parsed_entry['title'],
        color="4287f5",
        url=parsed_entry['link']
    )

    embed.set_author(parsed_entry['author'])

    image_url = None
    if type is FB:
        image_url='https://upload.wikimedia.org/wikipedia/commons/c/cd/Facebook_logo_%28square%29.png' 
    elif type is WP:
        image_url='https://workplays.it/workplays/favicon.png'

    embed.set_thumbnail(url=image_url)

    embed.add_embed_field(
        name="Wymagane doświadczenie", 
        value=parsed_entry['experience_level'], 
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
    if parsed_entry['date']:
        data_str = time.strftime('%d.%m.%Y %H:%M', parsed_entry['date'])
        embed.set_footer(
            text=f"Opublikowano ofertę o: {data_str}.\nGodzina powiadomienia"
        )

    webhook = DiscordWebhook(url=WEBHOOK_URL)
    webhook.add_embed(embed)
    webhook.execute()
