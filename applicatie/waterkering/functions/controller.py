from waterkering.functions.sensors import Sensor
from waterkering.functions.motors import Motor
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
		median = statistics.median(waterstanden)[0]
		average = sum(waterstand[0] for waterstand in waterstanden) / 5

		print(waterstanden)
		print('mediaan: {}, average: {}'.format(median, average))
		print('mediaan: {}, average: {}'.format(type(median), type(average)))

		if settings.status == 'opened' and int(median) > settings.MAX_WATER_HEIGHT and int(average) > settings.MAX_WATER_HEIGHT:
			settings.status = 'closing'
			Motor.close_gate()
			settings.status = 'closed'
		elif settings.status == 'closed' and int(median) < settings.MAX_WATER_HEIGHT and int(average) < settings.MAX_WATER_HEIGHT:
			settings.status = 'opening'
			Motor.open_gate()
			settings.status = 'opened'
		elif settings.status == 'closing' or settings.status == 'opening':
			pass

def updater():
	while(True):
		time.sleep(0.8)
		waterstand = Sensor.get_sensor_waterstand(Waterstand.objects.latest('id').waterstand)
		Sensor.save_sensor_waterstand(waterstand)
		Group("waterstand").send({"text": "{}".format(waterstand)})