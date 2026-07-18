import re 
def normalize_text(text: str):

    text = text.lower()
    text = text.strip()
    text = re.sub(r"[^\w\s]", "", text)

    return text
