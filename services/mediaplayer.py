from services.service import Service
import pygame
import os
import re
import random


class MediaPlayer(Service):
    """docstring for MediaPlayer"""

    def __init__(self):
        super(MediaPlayer, self).__init__()
        self.folder_path = "/Users/dy/Downloads/GEM"
        # self.song_number = 0

    def run(self):
        self.logger.info("MediaPlayer is running.")
        file_list = self.build_file_list()
        self.play_songs(file_list)

    def build_file_list(self):
        file_list = []
        for root, folders, files in os.walk(self.folder_path):
            folders.sort()
            files.sort()
            for filename in files:
                if re.search(".(wav|flac|m4a|pls|m3u)$", filename) != None:
                    file_list.append(os.path.join(root, filename))
        return file_list

    def play_songs(self, file_list):
        pygame.mixer.init()
        random.shuffle(file_list)
        while True:
            self.play_next_song(file_list)
            while pygame.mixer.music.get_busy() == True:
                continue

    def play_next_song(self,file_list):
        file_list.insert(0, file_list.pop()) # move current song to the back of the list
        pygame.mixer.music.load(file_list[0])
        pygame.mixer.music.play()
        print(len(file_list[0]))
        print(file_list)
