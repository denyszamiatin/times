import os
import glob
import json
import datetime
import logging


class NewsPreProcessor:

    def __init__(self, pipeline, articles_glob_pattern):
        self.pipeline = pipeline
        self.articles_glob_pattern = articles_glob_pattern
        self.articles = []

    def start(self):
        paths = self._get_news_paths()
        if paths:
            for path in paths:
                articles = self._load_articles(path)
                if articles:
                    self.process_articles(articles, path)

    def _get_news_paths(self):
        return glob.glob(self.articles_glob_pattern)

    @staticmethod
    def _load_articles(filename):
        try:
            with open(filename) as f:
                return json.load(f)
        except json.JSONDecodeError:
            logging.warning('can not decode file {}'.format(filename))
            return None

    def process_articles(self, articles, path):
        try:
            [self._process_article(article) for article in articles]
        except Exception as e:
            logging.error(e)
        else:
            self._save_articles()
            self._remove_old_articles(path)

    def _process_article(self, article):
        title = article.get('Title', '')
        text = article.get('Text', '')

        title, text = self.pipeline.proceed_item(title), self.pipeline.proceed_item(text)

        article['Title'] = title
        article['Text'] = text
        if self.is_article_valid(article):
            self._collect_article(article)

    @staticmethod
    def is_article_valid(article):
        return all(article.values())

    def _collect_article(self, article):
        self.articles.append(article)

    def _save_articles(self, dir_='data_processed'):
        filename = datetime.datetime.now().strftime('%Y-%d-%m_%H:%M:%S:%f')
        path = os.path.join(dir_, filename + '.json')
        try:
            with open(path, 'wt') as file:
                json.dump(self.articles, file, ensure_ascii=False)
        except FileNotFoundError:
            logging.warning('Directory does not exist. Creating data_processed directory')
            os.mkdir('data_processed')
            self._save_articles()
        else:
            self.articles.clear()

    def _remove_old_articles(self, path):
        try:
            os.remove(path)
        except FileNotFoundError as e:
            logging.warning(e)


