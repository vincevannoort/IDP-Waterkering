from random import randrange
from waterkering.models import Waterstand

class Sensor():
    pass

# get sensor data, for now random data
def get_sensor_waterstand():
    return int(randrange(100, 900 + 1))

# save waterstand to database with variable waterstand
def save_sensor_waterstand(value):
    Waterstand(waterstand=value).save()