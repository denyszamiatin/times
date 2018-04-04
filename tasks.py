from celery import Celery
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from times.spiders import News24TVSpider, CensorNet
from news_preprocessor.pipeline import NewsPipeLine
from news_preprocessor.preprocessors import NewsPreProcessor
from news_preprocessor.pipes import PIPES


SPIDERS = (
    CensorNet,
    News24TVSpider,
)

ARTICLES_GLOB_PATTERN = 'data/**/*.json'

app = Celery('tasks', broker='pyamqp://guest@localhost//')


@app.task
def run_spiders():
    process = CrawlerProcess(get_project_settings())
    for spider in SPIDERS:
        process.crawl(spider)
    process.start()


@app.task
def process_articles():
    pipeline = NewsPipeLine(PIPES)
    preprocessor = NewsPreProcessor(pipeline, ARTICLES_GLOB_PATTERN)
    preprocessor.start()

run_spiders()
process_articles()
