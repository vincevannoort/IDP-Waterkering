from django.http import HttpResponse
from channels.handler import AsgiHandler
from channels import Group
from random import randrange

# Waterkering stand
def waterkeringStand(message):
    return int(message.content['text']) + randrange(-30, 30 + 1)

# Connected to websocket.connect
def ws_add(message):
    message.reply_channel.send({"accept": True})
    Group("waterstand").add(message.reply_channel)

# Connected to websocket.receive
def ws_message(message):
    value = waterkeringStand(message)
    Group("waterstand").send({"text": "{}".format(value)})

# Connected to websocket.disconnect
def ws_disconnect(message):
    Group("waterstand").discard(message.reply_channel)