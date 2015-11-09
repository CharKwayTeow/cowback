from services.service import Service
from services.mediaplayer import MediaPlayer
from services.news_reporter import NewsReporter
from services.weather_reporter import WeatherReporter

class Handler(Service):
    """docstring for Handler"""
    def __init__(self):
        super(Handler, self).__init__()
        self.daemon = False
        self.services = {}

    def process(self, message):
        self.logger.debug(message)
        if message.action == 'start':
            self._start_service(message)
        elif message.action == 'stop':
            self._stop_service(message.service)

    def _start_service(self, message):
        if message.service == 'mediaplayer':
            self.services[message.service] = MediaPlayer()
        elif message.service == 'news_reporter':
            self.services[message.service] = NewsReporter()
        elif message.service == 'weather_reporter':
            self.services[message.service] = WeatherReporter()
        else:
            return

        self.services[message.service].start()

    def _stop_service(self, name):
        self.services[name].terminate()
        del self.services[name]

    def _stop_services(self):
        for name in self.services:
            self._stop_service(name)
