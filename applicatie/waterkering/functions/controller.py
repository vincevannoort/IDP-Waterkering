import waterkering.functions.sensors as sensors
import waterkering.functions.motors as motors
from waterkering.models import Waterstand
import applicatie.settings as settings
import time

#TODO:
	# check waterlevel from database (last 5 values)
    # activate motors / open | from motors.py
    # deactivate motors / close  | from motors.py

def run():
	while(True):
		time.sleep(5)
		waterstanden = Waterstand.objects.all().order_by('-id')[:5]
		sum = 0
		for waterstand in waterstanden:
			sum += waterstand.waterstand
		average = sum / len(waterstanden)
		if(average > settings.MAX_WATER_HEIGHT):
			print("Gate closing")
			#motors.close_gate()

			#for waterstand in waterstanden:
		#	print(waterstand.waterstand)
