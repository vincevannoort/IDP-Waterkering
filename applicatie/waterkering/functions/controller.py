import waterkering.functions.sensors as sensors
import waterkering.functions.motors as motors
from waterkering.models import Waterstand
import applicatie.settings as settings
import time

def monitor():
	while(True):
		time.sleep(5)

		waterstanden = Waterstand.objects.all().order_by('-id')[:5]
		average = sum(waterstand.waterstand for waterstand in waterstanden)
		if(average > settings.MAX_WATER_HEIGHT):
			print("Average value of", average, "is above maximum; gate closing.")