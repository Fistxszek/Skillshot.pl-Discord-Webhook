from config import ADDITIONAL_INFO, EXPERIENCE
import re

def get_first_image_from_html(html_content):
    match = re.search(r'<img [^>]*src="([^"]+)"', html_content)
    return match.group(1) if match else None


def parse_entry_data(entry):
    title = entry.get('title', '')
    summary = entry.get('summary', '')
    
    experience_keywords = [
        word for word in EXPERIENCE if word.lower() in title.lower()
    ]
    
    if not experience_keywords:
        experience_keywords = [
            word for word in EXPERIENCE if word.lower() in summary.lower()
        ]
    
    experience_level = experience_keywords[0] if experience_keywords else "Nieznane"
    
    location = entry.get('location', 'Zdalna')
    
    additional_info = [
        word for word in ADDITIONAL_INFO if word.lower() in summary.lower()
    ]
    
    image_url = get_first_image_from_html(summary)
    
    return {
        'title': title,
        'link': entry.get('link', ''),
        'author': entry.get('author', ''),
        'category': entry.get('category', ''),
        'summary': summary,
        'experience_level': experience_level,
        'location': location,
        'additional_info': additional_info,
        'image_url': image_url,
        'published_parsed': entry.get('published_parsed')
    }

