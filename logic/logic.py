import re
from data.templateMessages import askMessages


def clean_text(text: str) -> str:
    return re.sub(r"[^\w\s]", "", text.lower())


def find_matching_phrase(text: str) -> bool:
    text_clean = clean_text(text)
    for phrase in askMessages:
        if clean_text(phrase) in text_clean:
            return True
    return False
