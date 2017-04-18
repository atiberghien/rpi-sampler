#!/usr/bin/env python
from sequence import Sequence
from settings import sequences
import time, pygame

pygame.display.set_mode([200, 100])

current_sequence = None

for seq in sequences.itervalues():
    seq.start()

while True:
    for event in pygame.event.get(pygame.KEYDOWN):
        if event.key == pygame.K_ESCAPE:
            for seq in sequences.itervalues():
                try:
                    seq.stop()
                except:
                    pass
            exit()

        if event.key in sequences:
            current_sequence = sequences[event.key]
            current_sequence.play()

    for event in pygame.event.get(pygame.KEYUP):
        if event.key in sequences:
            current_sequence.pause()
            current_sequence = None

    time.sleep(0.5)
