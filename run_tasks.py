from tasks import run_spiders, process_articles


#  TODO create queue for tasks
run_spiders.delay()
process_articles.delay()
