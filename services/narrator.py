from gtts import gTTS
from tempfile import TemporaryFile
from services.service import Service

class Narrator(Service):
    """docstring for Narrator"""
    def __init__(self):
        super(Narrator, self).__init__()

    def process(self, feed):
        try:
            tts = gTTS(text = feed[2], lang = 'en')
            tts.save('audio/' + feed[0] + '/' + feed[1])
        except Exception as e:
            self.logger.warn(e)
