import applicatie.settings as settings
import time
from random import randrange
from waterkering.models import Waterstand

# GPIO variables
if settings.RASPBERRY == True: 
    print('initialize sensor')
    import RPi.GPIO as GPIO

    # sensor 1
    GPIO.setmode(GPIO.BOARD)
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
                
            return measure_waterstand()

        # Raspberry Pi not connected, returning random value for testing purposes
        else:
            distance = int(previousWaterstand) + randrange(-3, 3 + 1)
            if distance >= 100: distance = 99
            elif distance <= 0: distance = 1
            return distance

    def save_sensor_waterstand(value):
        Waterstand(waterstand = value).save()