from services.service import Service
import speech_recognition as sr
from entities.message import Message


class SpeechRecognition(Service):
    """docstring for SpeechRecognition"""

    def __init__(self, handler):

        super(SpeechRecognition, self).__init__()
        self.handler = handler
        self.stopDict = ["stop", "cancel", "thank you", "enough"]
        self.ask_dict = ["What's", "How", "what", "tell me"]

    def _configure(self, r):
        r.pause_threshold = 0.5
        r.energy_threshold = 400

    def run(self):
        r = sr.Recognizer()
        self._configure(r)
        while True:
            with sr.Microphone() as source:
                self.logger.info("Say something!")
                # print("Say something!")
                r.record(source, duration=2, offset=0)
                #        print(r.

                audio = r.listen(source)
                self.logger.info("Start Processing!")
                # print("Start Processing!")
                import time
                start_time = time.time()

                # recognize speech using Google Speech Recognition
            try:
                # for testing purposes, we're just using the default API key
                # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
                # instead of `r.recognize_google(audio)`
                self.logger.info("service started.")
                voice_command = r.recognize_google(audio)
                self.parse_command(voice_command)


            except sr.UnknownValueError:
                self.logger.warn("Google Speech Recognition could not understand audio")
                # print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                self.logger.warn("Could not request results from Google Speech Recognition service; {0}".format(e))
            end_time = time.time()
            # self.logger.info("This Processing totally uses " + (end_time-start_time))

    def parse_command(self, voice_command):
        self.logger.info("Google Speech Recognition thinks you said " + voice_command)

        if any(stop in voice_command for stop in self.stopDict):
            self.send(Message('All', 'stop', None))
            # self.send(Message('mediaplayer', 'start', None))
            self.logger.info("stop reading or playing")
        elif "play" and "music" in voice_command:
            # self.send(Message('All', 'stop', None))
            self.send(Message('music_player', 'start', None))
            self.logger.info("start playing music")
        elif "weather" in voice_command:
            # and any(ask in voice_command for ask in self.ask_dict):
            # self.send(Message('All', 'stop', None))
            self.send(Message('weather_reporter', 'start', None))
            self.logger.info("today's weather")
        elif "news" in voice_command:
            # self.send(Message('All', 'stop', None))
            self.send(Message('news_reporter', 'start', None))
            self.logger.info("start reading news")
            # if any(ask in voice_command for ask in self.ask_dict):
            #     print "read news"
            # else:
            #     print "Do u wanna today's news?"

        else:
            self.logger.info("Sorry I don't understand")

    def send(self, message):
        self.handler.receive(message)
