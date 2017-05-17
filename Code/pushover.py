#!/usr/bin/python
##coding:utf-8
import RPi.GPIO as GPIO
import time
from chump import Application
from setmeup import *


# this is a function to write out to the log file
def SENDTOLOG(PassedText):
    print PassedText
    #open the file - defined in setmeup.py
    f = open(MyLogFile,"a")
    #create the string with the date and time at the start
    # ******* note time is one hour out *********
    WrittenText = time.strftime("%d/%m/%Y") + " " +  time.strftime("%H:%M:%S")  + " " + PassedText + "\n"
    # write the entry into the file
    f.write(WrittenText)
    # close the file
    f.close()
    return

# these functions are called by interupts generated on the GPIO lines
# variables are set up in setmeup.py to control actions
def MOTION_1():
    ActionSensed = "Motion Detected " + PIR_PIN_1_LOCATION
    SENDTOLOG(ActionSensed)
    message = user.send_message(ActionSensed,priority=PIR_PIN_1_PRIORITY)

def MOTION_2():
    ActionSensed = "Motion Detected " + PIR_PIN_2_LOCATION
    SENDTOLOG(ActionSensed)
    message = user.send_message(ActionSensed,priority=PIR_PIN_2_PRIORITY)

def MOTION_3():
    ActionSensed = "Motion Detected " + PIR_PIN_3_LOCATION
    SENDTOLOG(ActionSensed)
    message = user.send_message(ActionSensed,priority=PIR_PIN_3_PRIORITY)

def MOTION_4():
    ActionSensed = "Motion Detected " + PIR_PIN_4_LOCATION
    SENDTOLOG(ActionSensed)
    message = user.send_message(ActionSensed,priority=PIR_PIN_4_PRIORITY)


# log the startup 
SENDTOLOG("Watchman is starting up")

# setup GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN_1, GPIO.IN)
GPIO.setup(PIR_PIN_2, GPIO.IN)
GPIO.setup(PIR_PIN_3, GPIO.IN)
GPIO.setup(PIR_PIN_4, GPIO.IN)

# log GPIO pins set up
SENDTOLOG("GPIO pins set up")


# log starting to setup Pushover
SENDTOLOG("Setting up Pushover")

# Setup Pushover connection
# install APP API Key
app = Application(AppKey) 
AppKeyStatus = "%s - APP is authenticated" % app.is_authenticated
SENDTOLOG(AppKeyStatus)

# connect APP to user Key
user = app.get_user(UserKey)
UserKeyStatus =  "User is authenticated - %s the device is a %s" %  (user.is_authenticated, user.devices)
SENDTOLOG(UserKeyStatus)

#let everything (electronics) stabalise
time.sleep(2)

SENDTOLOG("Night Watchman is On Duty (CTRL+C to exit)"")


#main loop

try:
    GPIO.add_event_detect(PIR_PIN_1, GPIO.RISING, callback=MOTION_1)
    GPIO.add_event_detect(PIR_PIN_2, GPIO.RISING, callback=MOTION_2)
    while 1:
        time.sleep(100)
except KeyboardInterrupt:
    print " Quit"
    GPIO.cleanup()