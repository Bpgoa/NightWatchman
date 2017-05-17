# coding: utf-8

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
PIR_PIN_1 = 23  # Right hand PIR
PIR_PIN_2 = 24  # Left hand PIR

GPIO.setup(PIR_PIN_1, GPIO.IN)
GPIO.setup(PIR_PIN_2, GPIO.IN)

def OMOTION(PIR_PIN_1):
    print "Motion Detected! - Outside Garage - right"

def IMOTION(PIR_PIN_1):
    print "Motion Detected! - inside Garage - left"

print "PIR Module Test (CTRL+C to exit)"
time.sleep(2)
print "Ready"

try:
    GPIO.add_event_detect(PIR_PIN_1, GPIO.RISING, callback=OMOTION)
    GPIO.add_event_detect(PIR_PIN_2, GPIO.RISING, callback=IMOTION)
    while 1:
        time.sleep(100)

except KeyboardInterrupt:
    print " Quit"
    GPIO.cleanup()




