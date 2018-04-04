import re
import os


def lower_text(text):
    return text.lower()


def clear_text(text):
    return ' '.join(re.findall(r"[\w]+(?:['’ʼ][\w]+)?", text))


def to_base_form(text):
    #  TODO translate words to base form
    return text


def remove_stop_words(text):
    stop_words = load_stop_words(text)
    words = text.split()
    for stop_word in stop_words:
        while stop_word in words:
            words.remove(stop_word)
    return ' '.join(words)


def load_stop_words(text):
    # lang = _detect_language(text)
    return _load_stop_words()


def _load_stop_words(lang='ua'):
    #  TODO
    dir_ = 'stop_words'
    filename = 'stop_words_%s.txt' % lang
    path = os.path.join(dir_, filename)
    try:
        with open(path, 'rt') as f:
            return f.read().split(', ')
    except FileNotFoundError:
        return ''


def _detect_language(text):
    #  TODO
    lang = None
    return lang


PIPES = [lower_text, clear_text, to_base_form, remove_stop_words]
