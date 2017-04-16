#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

PINS = [17, 18, 27, 22]

def buttonPress(channel):  
    print "Button", channel, "pressed!"

for pin in PINS:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(pin, GPIO.FALLING, callback=buttonPress, bouncetime=300)

raw_input("Listening...")
GPIO.cleanup()           # clean up GPIO on normal exit  
