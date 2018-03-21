import scrapy
from scrapy import Request
from xpaths import XPaths


xpaths_obj = XPaths()
xpaths_list = xpaths_obj.get_xpaths()


class TimesSpider(scrapy.Spider):
    name = 'news'
    start_urls = [[xpaths['startURL'] for xpaths in xpaths_list][0]]

    def parse(self, response):
        for index, xpaths in enumerate(xpaths_list):
            if xpaths['domain'] == response.meta['download_slot']:
                articles = response.xpath(xpaths['articles'])

                for article in articles:
                    title = article.xpath(xpaths['title']).extract_first("")
                    relative_url = article.xpath(xpaths['URL']).extract_first()
                    absolute_url = response.urljoin(relative_url)
                    yield Request(absolute_url,
                                  callback=self.parse_article,
                                  meta={'URL': absolute_url, 'Title': title.rstrip(), 'Xpaths': xpaths})

                relative_next_url = response.xpath(xpaths['nextURL']).extract_first()

                if relative_next_url:
                    absolute_next_url = response.urljoin(relative_next_url)
                    yield Request(absolute_next_url, callback=self.parse)
                else:
                    yield Request(xpaths_list[index+1]['domain'], callback=self.parse)

    def parse_article(self, response):
        url = response.meta.get('URL')
        title = response.meta.get('Title')
        xpaths = response.meta.get('Xpaths')
        text = "".join(line for line in response.xpath(xpaths['text']).extract())
        author = response.xpath(xpaths['author']).extract()
        date = response.xpath(xpaths['date']).extract()
        yield {'Title': title.strip(), 'Date': date, 'Author': author, 'URL': url, 'Text': text.strip()}

