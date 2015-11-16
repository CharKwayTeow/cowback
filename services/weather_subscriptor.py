import logging
import feedparser # pip3 install feedparser
from time import sleep
from utils.db_handler import get_weather
from utils.db_handler import insert_weather
from services.service import Service
from services.subscriptor import Subscriptor

class WeatherSubscriptor(Subscriptor):
    """docstring for WeatherSubscriptor"""
    def __init__(self):
        super(WeatherSubscriptor, self).__init__()

    def process(self, message):
        logging.debug(message)

    def run(self):
        while True:
            self.crawl_weather()
            # print(get_weather())
            sleep(600) # in seconds

    # RSS: http://weather.yahooapis.com/forecastrss?w=26815018  # °F
    # RSS: http://weather.yahooapis.com/forecastrss?w=26815018&u=c  # °C
    # Crawl weather website and store into DB
    def crawl_weather(self):
        rss = 'http://weather.yahooapis.com/forecastrss?w=26815018'
        feed = feedparser.parse(rss)
        for key in feed["entries"]: 
            content = " The temperature is " + key["yweather_condition"]["temp"] + " degrees F. This is weather " + key["title"] + "."
            # print(content)
            insert_weather(content)
        print("crawl_weather done.")

