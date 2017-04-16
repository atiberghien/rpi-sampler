#!/usr/bin/env python
import termios, os, time, pygame
pygame.mixer.init()

def getkey():
    term = open("/dev/tty", "r")
    fd = term.fileno()
    old = termios.tcgetattr(fd)
    new = termios.tcgetattr(fd)
    new[3] &= ~termios.ICANON & ~termios.ECHO
    termios.tcsetattr(fd, termios.TCSANOW, new)
    c = None
    try:
        c = os.read(fd, 1)
    finally:
        termios.tcsetattr(fd, termios.TCSAFLUSH, old)
        term.close()
    return c


class Sample(object):
    def __init__(self, name, file_name):
        self.name = name
        self.chan = pygame.mixer.find_channel()
        snd = pygame.mixer.Sound(file_name)
        self.chan.play(snd, loops=-1)
        self.chan.pause()
        self.is_playing = False

    def pause_unpause(self):
        if self.is_playing:
            self.chan.pause()
        else:
            self.chan.unpause()
        self.is_playing = not self.is_playing
        time.sleep(.5)

    def __str__(self):
        return self.name + " : " + ("play" if self.is_playing else "pause")
