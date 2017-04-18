#!/usr/bin/env python
from threading import Thread, Event
import pygame
import time
pygame.init()


class Sequence(Thread):
    def __init__(self, name="", playlist=[], next_sequence=None):
        Thread.__init__(self, name=name)
        self._sounds = []
        self._channel = pygame.mixer.find_channel()
        self._sound_counter = 0
        for path in playlist:
            self._sounds.append(pygame.mixer.Sound(path))

        self.next_sequence = next_sequence

        self._play = Event()
        self._stop = Event()

        self._stop.clear()
        self._play.clear()

    def _wait_channel(self):
        while self._channel.get_busy():
            time.sleep(0.2)

    def run(self):
        while not self._stop.is_set():
            while self._sound_counter < len(self._sounds) and self.is_playing():
                print self.name, "plays track #", self._sound_counter
                self._channel.play(self._sounds[self._sound_counter])
                self._sound_counter += 1
                self._wait_channel()

            self._sound_counter = 0

            if self.next_sequence and self.is_playing():
                self.pause()
                self.next_sequence.play()

            if self.is_playing():
                self.pause()

            time.sleep(0.5)

    def pause(self):
        print self.name, "pauses on track #", self._sound_counter
        if self.next_sequence:
            self.next_sequence.pause()
        self._channel.pause()
        self._play.clear()

    def is_playing(self):
        return self._play.is_set()

    def play(self):
        print self.name, "is playing"
        self._channel.unpause()
        self._wait_channel()
        self._play.set()

    def stop(self):
        if self.next_sequence:
            self.next_sequence.stop()
        self._channel.stop()
        self._stop.set()
        self._play.clear()
