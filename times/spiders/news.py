import scrapy
from scrapy import Request
import configparser


class Config:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('xpath_query.ini')
        self.newssite = self.config['NewsSite']
        self.xpath = self.config['XPaths']


config = Config()


class TimesSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = [config.newssite['Domain']]
    start_urls = [config.newssite['StartURL']]

    def parse(self, response):
        articles = response.xpath(config.xpath['Articles'])

        for article in articles:
            title = article.xpath(config.xpath['Title']).extract_first("")
            relative_url = article.xpath(config.xpath['URL']).extract_first()
            absolute_url = response.urljoin(relative_url)
            yield Request(absolute_url,
                          callback=self.parse_article,
                          meta={'URL': absolute_url, 'Title': title.rstrip()})

        relative_next_url = response.xpath(config.xpath['NextURL']).extract_first()
        absolute_next_url = response.urljoin(relative_next_url)
        yield Request(absolute_next_url,
                      callback=self.parse)

    def parse_article(self, response):
        url = response.meta.get('URL')
        title = response.meta.get('Title')
        text = "".join(line for line in response.xpath(config.xpath['Text']).extract())
        author = response.xpath(config.xpath['Author']).extract()
        date = response.xpath(config.xpath['Date']).extract()
        yield {'Title': title.strip(), 'Date': date, 'Author': author, 'URL': url, 'Text': text.strip()}

