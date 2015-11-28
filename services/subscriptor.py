from services.service import Service
from services.narrator import Narrator

class Subscriptor(Service):
    """docstring for Subscriptor"""
    def __init__(self):
        super(Subscriptor, self).__init__()
        self.narrator = Narrator()

    def run(self):
        while True:
            self.crawl()
            sleep(600) # in seconds

    def crawl(self):
        feed = feedparser.parse(self.rss)
        self.process(feed)

    def process(self):
        pass

    def send(self, type, filename, content):
        self.narrator.receive((type, filename, content))
