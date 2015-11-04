from services.service import Service

class Handler(Service):
    """docstring for Handler"""
    def __init__(self):
        super(Handler, self).__init__()

    def process(self, message):
        self.logger.debug(message)
