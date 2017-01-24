import waterkering.functions.sensors as sensors
import waterkering.functions.motors as motors
import applicatie.settings as settings
import time

#TODO:
	# check waterlevel from database (last 5 values)
    # activate motors / open | from motors.py
    # deactivate motors / close  | from motors.py

def run():
	while(True):
		waterHeight = sensors.get_sensor_waterstand()
		if(waterHeight > settings.MAX_WATER_HEIGHT):
			motors.close_gate()
		time.sleep(1);
