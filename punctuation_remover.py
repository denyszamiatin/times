import string

TABLE = str.maketrans('', '', string.punctuation)


def remove_punctuation(words):
    return ' '.join(words).translate(TABLE).split()
