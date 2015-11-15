import logging
import feedparser
from time import sleep
from utils.db_handler import get_news
from utils.db_handler import insert_news
from services.service import Service
from services.subscriptor import Subscriptor

class NewsSubscriptor(Subscriptor):
    """docstring for NewsSubscriptor"""
    def __init__(self):
        super(NewsSubscriptor, self).__init__()

    def process(self, message):
        logging.debug(message)

    def run(self):
        while True:
            self.crawl_news()
            # print(get_news())
            sleep(10) # in seconds

    # Crawl News website and store into DB
    def crawl_news(self):
        rss = 'http://www.voanews.com/api/epiqq'
        feed = feedparser.parse(rss)
        for key in feed["entries"]: 
            insert_news(key["published"],key["title"],key["description"])
        print("crawl_news done.")
