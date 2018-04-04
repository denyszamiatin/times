import datetime

import scrapy
from times.tools.config import Config


__all__ = ['CensorNet', 'News24TVSpider']


class BaseSpider(scrapy.Spider):

    config = None

    def parse(self, response):
        articles = response.xpath(self.config.newssite['Articles'])
        for article in articles:
            title = article.xpath(self.config.newssite['Title']).extract_first()
            url = article.xpath(self.config.newssite['URL']).extract_first()
            yield response.follow(url, callback=self.parse_article, meta={'Title': title.rstrip()})
        if not self.settings["DEBUG"]:
            next_url = response.xpath(self.config.newssite['NextURL']).extract_first()
            yield response.follow(next_url, callback=self.parse)

    def parse_article(self, response):
        url = response.url
        title = response.meta.get('Title')
        text = self.get_text(response)
        author = self.get_author(response)
        date = self.get_date(response)
        if title and text:
            yield {'Title': title.strip(), 'Date': date, 'Author': author, 'URL': url, 'Text': text.strip()}

    def get_text(self, response):
        return "".join(response.xpath(self.config.newssite['Text']).extract())

    def get_author(self, response):
        author = response.xpath(self.config.newssite['Author']).extract_first()
        return author or 'Unknown author'

    def get_date(self, response):
        date_ = response.xpath(self.config.newssite['Date']).extract_first()
        return self._ensure_date_exist(date_)

    @staticmethod
    def _ensure_date_exist(date_):
        return date_ or datetime.datetime.isoformat(datetime.datetime.now())


class CensorNet(BaseSpider):
    name = 'CensorNet'
    config = Config(name)
    allowed_domains = [config.newssite['Domain']]
    start_urls = [config.newssite['StartURL']]


class News24TVSpider(BaseSpider):
    name = 'News24TV'
    config = Config(name)
    allowed_domains = [config.newssite['Domain']]
    start_urls = [config.newssite['StartURL']]

    def get_date(self, response):
        date_ = response.xpath(self.config.newssite['Date']).re_first(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}')
        return self._ensure_date_exist(date_)


