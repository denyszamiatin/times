import logging

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from times.spiders import News24TVSpider, CensorNet

SPIDERS = (
    CensorNet,
    News24TVSpider,
)

logging.getLogger('scrapy').propagate = False

process = CrawlerProcess(get_project_settings())
for spider in SPIDERS:
    process.crawl(spider)
process.start()
