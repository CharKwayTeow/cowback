from services.service import Service

class Handler(Service):
    """docstring for Handler"""
    def __init__(self, player):
        super(Handler, self).__init__()
        self.daemon = False
        self.player = player

    def process(self, message):
        self.logger.debug(message)
        if message.action == 'start':
            self._start_service(message)
        elif message.action == 'stop':
            self._stop_service()

    def _start_service(self, message):
        if message.service == 'music_player':
            self.player.receive('music')
        elif message.service == 'news_reporter':
            self.player.receive('news')
        elif message.service == 'weather_reporter':
            self.player.receive('weather')
        else:
            return

    def _stop_service(self):
        self.player.receive('stop')
