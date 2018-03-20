import configparser


class Config:
    def __init__(self, name):
        self.config = configparser.ConfigParser()
        self.config.read('xpath_query.ini')
        self.newssite = self.config[name]

