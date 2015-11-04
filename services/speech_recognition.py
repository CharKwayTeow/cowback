from services.service import Service

class SpeechRecognition(Service):
    """docstring for SpeechRecognition"""
    def __init__(self, handler):
        super(SpeechRecognition, self).__init__()
        self.handler = handler

    def run(self):
        pass

    def send(self, message):
        self.handler.receive(message)
