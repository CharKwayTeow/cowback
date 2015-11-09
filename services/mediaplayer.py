from services.service import Service

class MediaPlayer(Service):
    """docstring for MediaPlayer"""
    def __init__(self):
        super(MediaPlayer, self).__init__()

    def run(self):
        self.logger.info("MediaPlayer is running.")
