import scrapy
import config


sites = config.get_sites()


class TimesSpider(scrapy.Spider):
    name = 'news'
    start_urls = [[site['startURL'] for site in sites][0]]

    def parse(self, response):
        for index, site in enumerate(sites):
            if site['domain'] == response.meta['download_slot']:
                articles = response.xpath(site['articles'])

                for article in articles:
                    title = article.xpath(site['title']).extract_first("")
                    relative_url = article.xpath(site['URL']).extract_first()
                    absolute_url = response.urljoin(relative_url)
                    yield scrapy.Request(absolute_url,
                                  callback=self.parse_article,
                                  meta={'URL': absolute_url, 'Title': title.rstrip(), 'Site': site})

                relative_next_url = response.xpath(site['nextURL']).extract_first()

                if relative_next_url:
                    absolute_next_url = response.urljoin(relative_next_url)
                    yield scrapy.Request(absolute_next_url, callback=self.parse)
                else:
                    yield scrapy.Request(site[index + 1]['domain'], callback=self.parse)

    def parse_article(self, response):
        url = response.meta.get('URL')
        title = response.meta.get('Title')
        site = response.meta.get('Site')
        text = "".join(line for line in response.xpath(site['text']).extract())
        author = response.xpath(site['author']).extract()
        date = response.xpath(site['date']).extract()
        yield {'Title': title.strip(), 'Date': date, 'Author': author, 'URL': url, 'Text': text.strip()}
