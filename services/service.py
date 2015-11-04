from multiprocessing import Process, Queue
from utils.logging import get_logger

class Service(Process):
    """docstring for Service"""
    def __init__(self):
        super(Service, self).__init__()
        self.queue = Queue()
        self.daemon = True
        self.logger = get_logger(type(self).__name__)

    def run(self):
        while True:
            message = self.queue.get()
            self.process(message)

    def process(self, message):
        pass

    def receive(self, message):
        self.queue.put(message)
