from tasks import run_spiders, process_articles

run_spiders.delay()
process_articles.delay()
