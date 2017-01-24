import waterkering.functions.sensors as sensors
import waterkering.functions.motors as motors
from channels import Group
from waterkering.models import Waterstand
import applicatie.settings as settings
import time
import random
import statistics

def monitor():
	while(True):
		time.sleep(5)
		waterstanden = list(Waterstand.objects.values_list('waterstand').order_by('-id')[:5])
		average = sum(waterstand[0] for waterstand in waterstanden) / 5
		median = statistics.median(waterstanden)

		print(waterstanden)
		print('mediaan: {}, average: {}'.format(median, average))

		if status == 'opened' and median > settings.MAX_WATER_HEIGHT and average > setting.MAX_WATER_HEIGHT:
			setting.status = 'inused'
			print('closing doors')
			setting.status = 'closed'
		elif status == 'closed' and median < settings.MAX_WATER_HEIGHT and average < setting.MAX_WATER_HEIGHT:
			setting.status = 'inused'
			print('opening doors')
			setting.status = 'opened'
		elif status == 'inuse':
			pass

def updater():
	while(True):
		time.sleep(1)
		# get data | from sensors.py
		waterstand = sensors.get_sensor_waterstand(Waterstand.objects.latest('id').waterstand)
		# save data | from sensors.py
		sensors.save_sensor_waterstand(waterstand)
		# send data to websocket
		Group("waterstand").send({"text": "{}".format(waterstand)})