import waterkering.functions.sensors as sensors
import waterkering.functions.motors as motors
from waterkering.models import Waterstand
import applicatie.settings as settings
import time

def monitor():
	while(True):
		time.sleep(5)

		sum = 0
		waterstanden = Waterstand.objects.all().order_by('-id')[:5]
		for waterstand in waterstanden:
			sum += waterstand.waterstand
		average = sum / len(waterstanden)

		if(average > settings.MAX_WATER_HEIGHT):
			print("Average value of", average, "is above maximum; gate closing.")