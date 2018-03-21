from times.spiders.news import TimesSpider
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging


def main():
    configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
    runner = CrawlerRunner(get_project_settings())

    d = runner.crawl(TimesSpider)
    d.addBoth(lambda _: reactor.stop())
    reactor.run()


if __name__ == '__main__':
    main()
