import re
import configparser



def extract_urls(fname):
    with open(fname) as f:
        return re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', f.read())



start_urls = extract_urls("links.txt")




config = configparser.ConfigParser()
config.read('xpath_query.ini')
xpath = config.get('xpath_query', 'title')
