import re

def clean_text(text):
    text = re.sub(r'\[.*?\]', '', text)
    text = re.sub(r'\s+', ' ', text)

    # remove emojis / unsupported chars
    text = text.encode("latin-1", "ignore").decode("latin-1")

    return text.strip()