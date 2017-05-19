#!/usr/bin/python
#coding:utf-8

import RPi.GPIO as GPIO
import time
from chump import Application
from setmeup import *
from requests import get


# this is a function to write out to the log file and console
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
    # write a trigger action to the log
    ActionSensed = "Motion Detected " + PIR_PIN_1_LOCATION
    SENDTOLOG(ActionSensed)
    # get my external IP address to use in the message
    ip = get('https://api.ipify.org').text
    #write the discovered IP address to the logfile
    SENDTOLOG("external IP address recorded as {}" .format(ip))
    # build a link to find the Night Watchman
    LinkToServer = "http:911//{}/main" .format(ip)
    message = user.send_message(
        title = "PIR 1 triggered", 
        message = ActionSensed,
        url = LinkToServer,
        url_title = "Click here to go to the Night Watchman",
        priority=PIR_PIN_1_PRIORITY)

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
if PIR_PIN_1_PRIORITY != 9:
   GPIO.setup(PIR_PIN_1, GPIO.IN)
if PIR_PIN_2_PRIORITY != 9:
    GPIO.setup(PIR_PIN_2, GPIO.IN)
if PIR_PIN_3_PRIORITY != 9:
    GPIO.setup(PIR_PIN_3, GPIO.IN)
if PIR_PIN_4_PRIORITY != 9:
    GPIO.setup(PIR_PIN_4, GPIO.IN)

# log GPIO pins set up
TText = "PIR GPIO pins set up: 1 = " + str(PIR_PIN_1_PRIORITY) + " 2 = " + str(PIR_PIN_2_PRIORITY) + " 3 = " + str(PIR_PIN_3_PRIORITY) + " 4 = " + str(PIR_PIN_4_PRIORITY)
SENDTOLOG(TText)


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

SENDTOLOG("Night Watchman is On Duty (CTRL+C to exit)")


#main loop

try:
    GPIO.setmode(GPIO.BCM)
    # setup call backs for interupts on PIR pins
    # the value 9 is a rogue value to stop the callbacks from being setup
    if PIR_PIN_1_PRIORITY != 9:
        GPIO.add_event_detect(PIR_PIN_1, GPIO.RISING, callback=MOTION_1)
    if PIR_PIN_2_PRIORITY != 9:
        GPIO.add_event_detect(PIR_PIN_2, GPIO.RISING, callback=MOTION_2)
    if PIR_PIN_3_PRIORITY != 9:
        GPIO.add_event_detect(PIR_PIN_2, GPIO.RISING, callback=MOTION_3)
    if PIR_PIN_4_PRIORITY != 9:
        GPIO.add_event_detect(PIR_PIN_2, GPIO.RISING, callback=MOTION_4)
    while 1:
        time.sleep(100)
except KeyboardInterrupt:
    SENDTOLOG("Night Watchman is closing down")
    GPIO.cleanup()