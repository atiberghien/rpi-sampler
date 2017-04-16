#!/usr/bin/env python
from utils import *
from settings import *
import time

def samples_info():
    for v in samples.values():
        print v
    print "*"*30


current_playing = None

try :
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)

    def pushButton(channel):
        if current_playing:
            samples[current_playing].pause_unpause()
        samples[gpio_key_assoc[str(channel)]].pause_unpause()
        current_playing = str(channel)
        samples_info()

    for gpio, key in gpio_key_assoc.iteritems():
        GPIO.setup(int(gpio), GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(int(gpio), GPIO.FALLING, callback=pushButton, bouncetime=200)
except:
    print "Not executed on raspberry"

while True:
    key = getkey()
    if key in samples:
        if current_playing:
            samples[current_playing].pause_unpause()
        samples[key].pause_unpause()
        current_playing = key
        samples_info()
    time.sleep(0.5)
