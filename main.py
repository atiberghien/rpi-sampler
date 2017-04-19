#!/usr/bin/env python
from settings import sequences
from events import EventManager
import time
import pygame
import signal
import sys
import serial

# pygame.display.set_mode([200, 100])

def stop_threads(*args):
    print "STOP ALL THREADS AND FORCE EXIT"
    for seq in sequences.itervalues():
        try:
            seq.stop()
        except:
            pass
    sys.exit(0)

signal.signal(signal.SIGINT, stop_threads)


for seq in sequences.itervalues():
    seq.start()

current_sequence = None

usb = serial.Serial('/dev/ttyACM0', 9600)
event_manager = EventManager()
while True:
    try:
        evt = int(usb.readline())
        event_type = "CTRL_DOWN" if evt / 100 == 0 else "CTRL_UP"
        evt = evt % 100
        event_manager.set_event(event_type, evt)
    except:
        pass

    # for event in pygame.event.get(pygame.KEYDOWN):
    #     event_manager.set_event("CTRL_DOWN", event.key)
    # for event in pygame.event.get(pygame.KEYUP):
    #     event_manager.set_event("CTRL_UP", event.key)
    #

    evt_down = event_manager.get_event("CTRL_DOWN")
    evt_up = event_manager.get_event("CTRL_UP")

    if evt_down and evt_down in sequences:
        print "RAISE CTRL_DOWN", evt_down
        current_sequence = sequences[evt_down]
        current_sequence.play()

    if evt_up and evt_up in sequences:
        print "RAISE CTRL_UP", evt_up
        current_sequence.pause()
        current_sequence = None
    time.sleep(0.2)
