from time import sleep
import logging
from multiprocessing import Process
from services.handler import Handler
from services.speech_recognition import SpeechRecognition
from services.news_subscriptor import NewsSubscriptor
from services.weather_subscriptor import WeatherSubscriptor
from entities.message import Message

class CowBack(object):
    """docstring for CowBack"""
    def __init__(self):
        super(CowBack, self).__init__()
        self.services = {}
        self.load_services()

    def load_services(self):
        self.services["handler"] = Handler()
        self.services["speech_recognition"] = SpeechRecognition(self.services["handler"])
        self.services["news_subscriptor"] = NewsSubscriptor()
        self.services["weather_subscriptor"] = WeatherSubscriptor()

    def start_services(self):
        for (name, service) in self.services.items():
            service.start()
            logging.info(name + " service started.")

        [service.join() for service in self.services.values()]

    def terminate_services(self):
        for (name, service) in self.services.items():
            service.terminate()

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)
    c = CowBack()
    # c.services['speech_recognition'].send(Message('Hello', 'World', '!'))
    c.start_services()
    sleep(1)
    # c.terminate_services()
