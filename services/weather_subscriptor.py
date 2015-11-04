import logging
from services.service import Service
from services.subscriptor import Subscriptor

class WeatherSubscriptor(Subscriptor):
    """docstring for WeatherSubscriptor"""
    def __init__(self):
        super(WeatherSubscriptor, self).__init__()

    def process(self, message):
        logging.debug(message)
