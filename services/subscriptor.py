import hashlib
from time import sleep
import feedparser # pip3 install feedparser
from services.service import Service
from services.narrator import Narrator

class Subscriptor(Service):
    """docstring for Subscriptor"""
    def __init__(self, narrator):
        super(Subscriptor, self).__init__()
        self.narrator = narrator

    def run(self):
        while True:
            self.crawl()
            sleep(600) # in seconds

    def crawl(self):
        feed = feedparser.parse(self.rss)
        self.process(feed)

    def process(self, feed):
        pass

    def send(self, type, filename, content):
        self.narrator.receive((type, filename, content))

    def _get_md5(self, content):
        return hashlib.sha224(content.encode()).hexdigest()
