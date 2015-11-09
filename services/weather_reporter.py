from services.service import Service

class WeatherReporter(Service):
    """docstring for WeatherReporter"""
    def __init__(self):
        super(WeatherReporter, self).__init__()

    def run(self):
        self.logger.info("WeatherReporter is running.")
