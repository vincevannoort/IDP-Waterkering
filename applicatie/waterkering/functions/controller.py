import waterkering.functions.sensors as sensors
import waterkering.functions.motors as motors
from channels import Group
from waterkering.models import Waterstand
import applicatie.settings as settings
import time

def monitor():
	while(True):
		time.sleep(5)

		waterstanden = Waterstand.objects.all().order_by('-id')[:5]
		average = sum(waterstand.waterstand for waterstand in waterstanden) / 5
		if(average > settings.MAX_WATER_HEIGHT):
			print("Average value of", average, "is above maximum; gate closing.")

def updater():
	while(True):
		time.sleep(1)
		# get data | from sensors.py
		waterstand = sensors.get_sensor_waterstand(Waterstand.objects.latest('id').waterstand)
		# save data | from sensors.py
		sensors.save_sensor_waterstand(waterstand)
		# send data to websocket
		Group("waterstand").send({"text": "{}".format(waterstand)})