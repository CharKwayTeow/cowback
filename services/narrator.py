import os
import re
from tempfile import TemporaryFile
from services.service import Service

class Narrator(Service):
    """docstring for Narrator"""
    def __init__(self):
        super(Narrator, self).__init__()

    def process(self, feed):
        try:
            content = re.compile("[\r?\n|\r']+").sub(',', feed[2])
            self.logger.debug(content)
            path = "audio/" + feed[0] + "/" + feed[1]
            command = "espeak -s 120 -v en-us '" + content + "' -w " + path
            os.system(command)
            self.logger.debug("Wav file has been saved in path " + path + ".")
        except Exception as e:
            self.logger.warn(e)
