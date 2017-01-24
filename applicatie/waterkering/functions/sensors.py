import applicatie.settings as settings
import time
from random import randrange
from waterkering.models import Waterstand

# GPIO variables
if settings.RASPBERRY == True: 
    import RPi.GPIO as GPIO 
    GPIO.setmode(GPIO.BCM)
    GPIO_TRIGGER = 23;
    GPIO_ECHO = 24;
    GPIO.setup(GPIO_TRIGGER,GPIO.OUT)
    GPIO.setup(GPIO_ECHO,GPIO.IN)
    GPIO.output(GPIO_TRIGGER, False)

# get sensor data, for now random data
def get_sensor_waterstand():
    
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
            distance1 = measure_waterstand() time.sleep(0.1)
            distance2 = measure_waterstand() time.sleep(0.1)
            distance3 = measure_waterstand()
            return ((distance1 + distance2 + distance3) / 3)

    # Raspberry Pi not connected
    else:
        return int(randrange(100, 900 + 1))

# save waterstand to database with variable waterstand
def save_sensor_waterstand(value):
    Waterstand(waterstand=value).save()