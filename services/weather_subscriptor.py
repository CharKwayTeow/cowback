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
        self.rss = 'http://weather.yahooapis.com/forecastrss?w=26815018'

    # RSS: http://weather.yahooapis.com/forecastrss?w=26815018  # °F
    # RSS: http://weather.yahooapis.com/forecastrss?w=26815018&u=c  # °C
    # Crawl weather website and store into DB
    def process(self, feed):
        for key in feed["entries"]: 
            content = " The temperature is " + key["yweather_condition"]["temp"] + " degrees F. This is weather " + key["title"] + "."
            # insert_weather(content)
            send("weather", randint(1000000,9999999)+".wav", content)
        self.logger.info(("crawl_weather done.")
