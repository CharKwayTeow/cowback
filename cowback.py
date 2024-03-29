from time import sleep
import logging
import os
from multiprocessing import Process
from services.handler import Handler
from services.speech_recognition import SpeechRecognition
from services.narrator import Narrator
from services.news_subscriptor import NewsSubscriptor
from services.weather_subscriptor import WeatherSubscriptor
from services.mediaplayer import MediaPlayer
from entities.message import Message
from utils.logging import get_logger, logging

class CowBack(object):
    """docstring for CowBack"""
    def __init__(self):
        super(CowBack, self).__init__()
        self.logger = get_logger(type(self).__name__)
        self.init_dirs()
        self.services = {}
        self.load_services()

    def init_dirs(self):
        self.init_dir('audio')
        self.init_dir('audio/music')
        self.init_dir('audio/news')
        self.init_dir('audio/weather')
        self.init_dir('audio/stop')

    def init_dir(self, directory):
        if not os.path.exists(directory):
            os.makedirs(directory)

    def load_services(self):
        self.services["mediaplayer"] = MediaPlayer()
        self.services["handler"] = Handler(self.services["mediaplayer"])
        self.services["speech_recognition"] = SpeechRecognition(self.services["handler"])
        self.services["narrator"] = Narrator()
        self.services["news_subscriptor"] = NewsSubscriptor(self.services["narrator"])
        self.services["weather_subscriptor"] = WeatherSubscriptor(self.services["narrator"])

    def start_services(self):
        for (name, service) in self.services.items():
            service.start()
            self.logger.info(name + " service started.")

        [service.join() for service in self.services.values()]

    def terminate_services(self):
        for (name, service) in self.services.items():
            service.terminate()
            self.logger.info(name + " service terminated.")

if __name__ == '__main__':
    c = CowBack()
    try:
        c.start_services()
    except KeyboardInterrupt:
        pass
    finally:
        c.terminate_services()
