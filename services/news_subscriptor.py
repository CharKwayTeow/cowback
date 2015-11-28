import hashlib
from utils.db_handler import get_news
from services.service import Service
from services.subscriptor import Subscriptor

class NewsSubscriptor(Subscriptor):
    """docstring for NewsSubscriptor"""
    def __init__(self, narrator):
        super(NewsSubscriptor, self).__init__(narrator)
        self.rss = 'http://www.voanews.com/api/epiqq'

    # Crawl News website and store into DB
    def process(self, feed):
        for key in feed["entries"]: 
            self.send("news", self._get_md5(key["description"]) + ".wav", key["description"])
        self.logger.info("crawl_news done.")

    def _get_md5(self, content):
        return hashlib.sha224(content.encode()).hexdigest()
