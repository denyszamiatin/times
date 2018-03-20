import scrapy
from scrapy import Request

from times.tools.config import Config


class BaseSpider(scrapy.Spider):

    def parse(self, response):
        articles = response.xpath(self.config.newssite['Articles'])
        for article in articles:
            title = article.xpath(self.config.newssite['Title']).extract_first()
            relative_url = article.xpath(self.config.newssite['URL']).extract_first()
            absolute_url = response.urljoin(relative_url)
            yield Request(absolute_url,
                          callback=self.parse_article,
                          meta={'URL': absolute_url, 'Title': title.rstrip()})

        relative_next_url = response.xpath(self.config.newssite['NextURL']).extract_first()
        absolute_next_url = response.urljoin(relative_next_url)
        yield Request(absolute_next_url,
                      callback=self.parse)

    def parse_article(self, response):
        url = response.meta.get('URL')
        title = response.meta.get('Title')
        text = "".join(response.xpath(self.config.newssite['Text']).extract())
        author = response.xpath(self.config.newssite['Author']).extract_first()
        date = self.get_date(response)
        yield {'Title': title.strip(), 'Date': date, 'Author': author, 'URL': url, 'Text': text.strip()}

    def get_date(self, response):
        return response.xpath(self.config.newssite['Date']).extract_first()


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
        return response.xpath(self.config.newssite['Date']).re_first(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}')


