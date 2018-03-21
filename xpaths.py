import re
import json


URL_PATTERN = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'


def read_file(filename):
    with open(filename) as f:
        return f.read()


def extract_urls(text):
    return re.findall(URL_PATTERN, text)


start_urls = extract_urls(read_file("links.txt"))


class XPaths:
    def get_xpaths(self):
        with open('sites.json', 'rt') as jfile:
            xpaths = json.load(jfile)['Sites']
            return xpaths
