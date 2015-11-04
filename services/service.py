from multiprocessing import Process, Queue

class Service(Process):
    """docstring for Service"""
    def __init__(self):
        super(Service, self).__init__()
        self.queue = Queue()
        self.daemon = True

    def run(self):
        while True:
            message = self.queue.get()
            self.process(message)

    def process(self, message):
        pass

    def receive(self, message):
        self.queue.put(message)
