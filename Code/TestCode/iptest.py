# This example requires the requests library be installed.  You can learn more
# about the Requests library here: http://docs.python-requests.org/en/latest/
from requests import get
import time
from chump import Application

AppKey = "attevjd8kcgd6eam6issgahy9923sn"
UserKey = "upjprra9byi342g5qj81uxphhdc1cg"

app = Application(AppKey) 
AppKeyStatus = "%s - APP is authenticated" % app.is_authenticated

user = app.get_user(UserKey)
UserKeyStatus =  "User is authenticated - %s the device is a %s" %  (user.is_authenticated, user.devices)

ip = get('https://api.ipify.org').text
print('My public IP address is: {}'.format(ip))
LinkToServer = "http:911//{}/main" .format(ip)
print LinkToServer

message = user.send_message(
    title = "PIR 1 triggered", 
    message = "ActionSensed",
    url = LinkToServer,
    url_title = "Click here to go to webpage",
    priority= 1)