from scrapy.crawler import CrawlerProcess
from times.spiders.news import News24TVSpider, CensorNet

SPIDERS = (
    CensorNet,
    News24TVSpider,
)


process = CrawlerProcess({'USER_AGENT': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0'})
process.crawl(*SPIDERS)
process.start()
