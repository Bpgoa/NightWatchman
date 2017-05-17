#coding:utf-8

#leave these alone unles you absolutely have to touch them
PIR_PIN_1 = 23  # Right hand PIR - outside
PIR_PIN_2 = 24  # Left hand PIR - inside - sends emergency message
PIR_PIN_3 = 25  # not used
PIR_PIN_4 = 8   # not used
# ----------------

# locations of PIR devices
# change the string values to match desired location
# put "Not Used " in any variable where no sensor is present
PIR_PIN_1_LOCATION = "Outside Garage"
PIR_PIN_2_LOCATION = "Inside Garage"
PIR_PIN_3_LOCATION = "Not Used"
PIR_PIN_4_LOCATION = "Not Used"

# set the priority of action for  each PIR
#
# set to 2 for emergency and log
#   Message priority: Sound, vibration, and banner regardless of user’s quiet hours, 
#   and re-alerts until acknowledged
# set to 1 for high message and log
#   Message priority: Sound, vibration, and banner regardless of user’s quiet hours.
# set to 0 for normal message and log
#   Message priority: Sound, vibration, and banner if outside of user’s quiet hours
# set to 9 if PIR not used
#
PIR_PIN_1_PRIORITY = 0
PIR_PIN_2_PRIORITY = 2
PIR_PIN_3_PRIORITY = 9
PIR_PIN_4_PRIORITY = 9

# the following two keys are for pushover
# you get them when you sign up and create an app
AppKey = "attevjd8kcgd6eam6issgahy9923sn"
UserKey = "upjprra9byi342g5qj81uxphhdc1cg"
# put the filename or fullpath and filename
# for the logfile into the next  variable
MyLogFile = "watchman_logfile.text"