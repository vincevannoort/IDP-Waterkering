from django.http import HttpResponse
from channels.handler import AsgiHandler
from channels import Group
import waterkering.functions.sensors as sensors

# Connected to websocket.connect
def connect(message):
    message.reply_channel.send({"accept": True})
    Group("waterstand").add(message.reply_channel)

# Connected to websocket.receive
def update(message):
    # get data | from sensors.py
    waterstand = sensors.get_sensor_waterstand(message)
    # save data | from sensors.py
    sensors.save_sensor_waterstand(waterstand)
    # send data to websocket
    Group("waterstand").send({"text": "{}".format(waterstand)})

# Connected to websocket.disconnect
def disconnect(message):
    Group("waterstand").discard(message.reply_channel)