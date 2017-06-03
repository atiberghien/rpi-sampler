#!/usr/bin/env python
from threading import Thread, Event
from pydub import AudioSegment
from slugify import slugify

import pygame
import time
import os

pygame.init()


class Sequence(Thread):
    def __init__(self, name="", playlist=[], next_sequence=None):
        Thread.__init__(self, name=name)
        self._channel = pygame.mixer.find_channel()
        self._wav_path = "%s.wav" % slugify(name, separator="_")
        track = sum([AudioSegment.from_wav(wav_file) for wav_file in playlist])
        track.export(self._wav_path, format="wav")

        self.next_sequence = next_sequence

        self._play = Event()
        self._stop = Event()

        self._stop.clear()
        self._play.clear()

        self._reset_channel()

    def _reset_channel(self):
        self._channel.play(pygame.mixer.Sound(self._wav_path))
        self.pause()

    def wait(self):
        while self._channel.get_busy() and not self._stop.is_set():
            # if self.name == "Sequence 1":
            #     print self.name, "waits stopping"
            time.sleep(0.2)

    def run(self):
        while not self._stop.is_set():
            self.wait()
            # 
            # if not self._stop.is_set() and self.next_sequence:
            #     self.next_sequence.play()
            #     self.next_sequence.wait()

            self._channel.play(pygame.mixer.Sound(self._wav_path))

    def is_playing(self):
        return self._channel.get_busy() and self._play.is_set()

    def pause(self):
        # print self.name, "PAUSE"
        # if self.next_sequence and self.next_sequence.is_playing():
        #     self.next_sequence.pause()

        self._channel.pause()
        self._play.clear()

    def play(self):
        self._channel.unpause()
        self._play.set()

    def stop(self):
        # if self.next_sequence:
        #     self.next_sequence.stop()
        self._channel.stop()
        self._stop.set()
        self._play.clear()
        os.remove(self._wav_path)
