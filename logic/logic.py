# import re

# from data.template_messages import ask_messages

# def clean_text(text: str) -> str:
#     return re.sub(r"[^\w\s]", "", text.lower())


# def find_matching_phrase(text: str) -> bool:
#     text_clean = clean_text(text)
#     for phrase in ask_messages:
#         if clean_text(phrase) in text_clean:
#             return True
#     return False
