from services.service import Service

class NewsReporter(Service):
    """docstring for NewsReporter"""
    def __init__(self):
        super(NewsReporter, self).__init__()

    def run(self):
        self.logger.info("NewsReporter is running.")
