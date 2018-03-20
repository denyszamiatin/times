import re


def scrap_words(text: str) -> list:
    return re.findall(r"[\w]+(?:['’ʼ][\w]+)?", text)
