from django.http import HttpResponse
from channels.handler import AsgiHandler
from channels import Group
from random import randrange

# Connected to websocket.connect
def connect(message):
    message.reply_channel.send({"accept": True})
    Group("waterstand").add(message.reply_channel)

# Connected to websocket.receive
def update(message):
    # get data | from sensors.py
    # save data | from sensors.py
    Group("waterstand").send({"text": "{}".format(500)})

# Connected to websocket.disconnect
def disconnect(message):
    Group("waterstand").discard(message.reply_channel)