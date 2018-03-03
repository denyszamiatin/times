# -*- coding: utf-8 -*-

import scrapy
from scrapy import Request


class TimesSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = ['www.thetimes.co.uk']
    start_urls = ['https://www.thetimes.co.uk/']

    def parse(self, response):
        articles = response.xpath('//h3[contains(@class, "Item-headline")]')

        for article in articles:
            title = article.xpath('a/text()').extract_first("")
            relative_url = article.xpath('a/@href').extract_first()
            absolute_url = response.urljoin(relative_url)
            yield Request(absolute_url, callback=self.parse_article, meta={'URL': absolute_url, 'Title': title})

    def parse_article(self, response):
        url = response.meta.get('URL')
        title = response.meta.get('Title')

        author = response.xpath('//meta[@name="author"]/@content').extract()

        yield{'URL': url, 'Title': title, 'Author': author}
