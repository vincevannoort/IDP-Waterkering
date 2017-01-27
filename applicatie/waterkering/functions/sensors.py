import applicatie.settings as settings
import time
from random import randrange
from waterkering.models import Waterstand

# GPIO variables
if settings.RASPBERRY == True: 
    print('initialize sensor')
    import RPi.GPIO as GPIO

    # sensor 1
    GPIO.setmode(GPIO.BCM)
    GPIO_TRIGGER = settings.SENSOR_PINS[0];
    GPIO_ECHO = settings.SENSOR_PINS[1];
    GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
    GPIO.setup(GPIO_ECHO, GPIO.IN)
    GPIO.output(GPIO_TRIGGER, False)

class Sensor:

    def get_sensor_waterstand(previousWaterstand):
        
        # Raspberry Pi connected
        if settings.RASPBERRY == True:
            def measure_waterstand():
                # activate GPIO sensors
                GPIO.output(GPIO_TRIGGER, True)
                time.sleep(0.00001)
                GPIO.output(GPIO_TRIGGER, False)

                # check distance with ultrasonic waves
                start = time.time()
                while GPIO.input(GPIO_ECHO) == 0:
                    start = time.time()
                while GPIO.input(GPIO_ECHO) == 1:
                    stop = time.time()

                # compute elapsed time based on waves
                elapsed = stop-start
                distance = (elapsed * 34300) / 2
                return distance
            def measure_average_waterstand():
                # measure 3 times
                distance1 = measure_waterstand() 
                time.sleep(0.1)
                distance2 = measure_waterstand() 
                time.sleep(0.1)
                distance3 = measure_waterstand()

                # compute average of those 3 measures
                average = ((distance1 + distance2 + distance3) / 3)
                print('measured distance: {}'.format(average));
                return average

            # send average of 3 measures back
            return measure_average_waterstand()

        # Raspberry Pi not connected
        else:
            return int(previousWaterstand) + randrange(-30, 30 + 1)

    def save_sensor_waterstand(value):
        Waterstand(waterstand = value).save()