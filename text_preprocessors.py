import string
import pymorphy2

PUNCTUATION = string.punctuation.replace("'", '').replace('-', '') + '–—'

TABLE = str.maketrans(PUNCTUATION, ' '*len(PUNCTUATION))
MORPH = pymorphy2.MorphAnalyzer(lang='uk')


def remove_punctuation(text: str):
    return text.translate(TABLE)


def set_lower(text: str):
    return text.lower()


def set_to_root(words):
    return [MORPH.parse(word)[0].normal_form for word in words]
