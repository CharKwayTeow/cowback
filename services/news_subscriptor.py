from services.service import Service
from services.subscriptor import Subscriptor

class NewsSubscriptor(Subscriptor):
    """docstring for NewsSubscriptor"""
    def __init__(self):
        super(NewsSubscriptor, self).__init__()

    def process(self, message):
        logging.debug(message)
