import os
import time
import random
import statistics
import subprocess

from channels import Group
import applicatie.settings as settings

from waterkering.functions.sensors import Sensor
from waterkering.functions.motors import Motor
from waterkering.models import Waterstand
from waterkering.models import Melding

# Monitors water level and takes appropriate action
def monitor():
	while(True):
		# Sleep 1 second before reading out the next set of water levels, because that is often enough and a good balance between response time and CPU usage
		time.sleep(1)

		# Get the latest 5 updates from the database, filter out the water levels and put them in a list
		waterstanden = list(Waterstand.objects.values_list('waterstand').order_by('-id')[:5])

		# Calculate the median and average of the list created above
		median = statistics.median(waterstanden)[0]
		average = sum(waterstand[0] for waterstand in waterstanden) / 5

		# Decide if the gate should be opened, closed or remain the same based on the current state and our calculations above
		if settings.status == 'opened' and int(median) > settings.MAX_WATER_HEIGHT and int(average) > settings.MAX_WATER_HEIGHT:
			Motor.close_gate()
		elif settings.status == 'closed' and int(median) < settings.MAX_WATER_HEIGHT and int(average) < settings.MAX_WATER_HEIGHT:
			Motor.open_gate()
		elif settings.status == 'closing' or settings.status == 'opening':
			pass

# Responsible for getting and saving the waterlevel
def updater():
	while(True):
		# Sleep 1 second, again because of the balance between response time and CPU usage
		time.sleep(1)

		# Get the current water level from the sensor
		waterstand = Sensor.get_sensor_waterstand(Waterstand.objects.latest('id').waterstand)
		# Save the current water level to our database
		Sensor.save_sensor_waterstand(waterstand)
		# Send our current water level to the web application
		Group("waterstand").send({"text": "{}".format(waterstand)})

# Responsible for copying the database to the redundant RPi
def copier():
	while(True):
		# Sleep 20 seconds, in sync with the program running on the redundant RPi
		time.sleep(20)

		# Raspberry Pi connected
		if settings.RASPBERRY == True and settings.RASPBERRY_MAIN == True:
			try:
				os.system('scp ~/IDP-Waterkering/applicatie/db.sqlite3 pi@192.168.137.2:~/IDP-Waterkering/applicatie/db.sqlite3')
				print('db.sqlite3 has been copied to the other RPi')
			except:
				print('db.sqlite3 copying has failed')





