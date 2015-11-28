import logging
import feedparser # pip3 install feedparser
from time import sleep
from utils.db_handler import get_news
from utils.db_handler import insert_news
from services.service import Service
from services.subscriptor import Subscriptor

class NewsSubscriptor(Subscriptor):
    """docstring for NewsSubscriptor"""
    def __init__(self):
        super(NewsSubscriptor, self).__init__()
        self.rss = 'http://www.voanews.com/api/epiqq'

    # Crawl News website and store into DB
    def process(self, feed):
        for key in feed["entries"]: 
            # insert_news(key["published"],key["title"],key["description"])
            content = key["published"],key["title"],key["description"]
            send("news", randint(1000000,9999999)+".wav", content)
        self.logger.info(("crawl_news done.")
