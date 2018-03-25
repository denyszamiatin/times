import pymorphy2


TABLE = str.maketrans('', '', '!"#$%&\()*+,./:;<=>?@[\\]^_`{|}~–')
MORPH = pymorphy2.MorphAnalyzer(lang='uk')


def remove_punctuation(words):
    words[:] = [word.replace(".", " ") if "." in word else word for word in words]
    return ' '.join(words).translate(TABLE).split()


def set_lower(words):
    return [word.lower() for word in words]


def set_to_root(words):
    return [MORPH.parse(word)[0].normal_form for word in words]
