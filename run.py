from times.spiders.news import TimesSpider
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
import json
import os
from pipeline import pipeline


ARTICLES_DIR = "data/news"


def main():
    # configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
    # runner = CrawlerRunner(get_project_settings())
    #
    # d = runner.crawl(TimesSpider)
    # d.addBoth(lambda _: reactor.stop())
    # reactor.run()

    for file in os.listdir(ARTICLES_DIR):
        with open(os.path.join(ARTICLES_DIR, file), "rt") as jfile:
            articles = json.load(jfile)
            for article in articles:
                print(pipeline.preprocess_article(article['Text']))


if __name__ == '__main__':
    main()
