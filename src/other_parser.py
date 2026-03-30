from config import ADDITIONAL_INFO, EXPERIENCE, ROLES

def other_parse_entry_data(entry):
    title = entry.get('title', '')
    summary = entry.get('description', '')
    
    experience_keywords = [
        word for word in EXPERIENCE if word.lower() in title.lower()
    ]
    
    if not experience_keywords:
        experience_keywords = [
            word for word in EXPERIENCE if word.lower() in summary.lower()
        ]

    experience_level = experience_keywords[0] if experience_keywords else "Nieznane"
    
    additional_info = [
        word for word in ADDITIONAL_INFO if word.lower() in summary.lower()
    ]
    
    return {
        'title': title,
        'link': entry.get('link', ''),
        'author': entry.get('author', ''),
        'summary': summary,
        'experience_level': experience_level,
        'additional_info': additional_info,
        'date' : entry.get('published_parsed', '')
    }

