import json


def get_sites():
    with open('sites.json', 'rt') as jfile:
        sites = json.load(jfile)['Sites']
        return sites
