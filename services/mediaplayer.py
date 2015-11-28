from services.service import Service
import pygame
import os
import re
import random
from time import sleep


class MediaPlayer(Service):
    """docstring for MediaPlayer"""

    def __init__(self):
        super(MediaPlayer, self).__init__()
        self.option = "stop"
        # self.song_number = 0

    def run(self):
        self.logger.info("MediaPlayer is running.")
        while True:
            file_list = self.build_file_list()
            print (file_list)
            if (len(file_list) == 0):
                self.logger.info("No music in local.")
                # self.option = "empty"
                while not self.check_queue():
                    continue
            else:
                self.play_songs(file_list)

    def build_file_list(self):
        folder_path = "/Users/dy/Git/cs244/cowback/audio/" + self.option
        print(folder_path)
        file_list = []
        for root, folders, files in os.walk(folder_path):
            folders.sort()
            files.sort()
            for filename in files:
                print(filename)
                if re.search(".(wav|flac|m4a|pls|m3u)$", filename):
                    file_list.append(os.path.join(root, filename))

        return file_list

    def play_songs(self, file_list):
        pygame.mixer.init()
        random.shuffle(file_list)
        while True:
            self.play_next_song(file_list)
            while pygame.mixer.music.get_busy():
                if self.check_queue():
                    pygame.mixer.music.stop()
                    return
                continue

    def play_next_song(self, file_list):
        file_list.insert(0, file_list.pop())  # move current song to the back of the list
        pygame.mixer.music.load(file_list[0])
        pygame.mixer.music.play()
        # print(len(file_list[0]))
        # print(file_list)

    def check_queue(self):
        sleep(1)
        if not self.queue.empty():
            self.option = self.queue.get()
            return True
        return False;
