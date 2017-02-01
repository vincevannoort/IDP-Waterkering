from waterkering.functions.sensors import Sensor
from waterkering.functions.motors import Motor

class Testing:

    def test(function):
        # determine which function should run
        if function == 'close_gate':
            Motor.close_gate()
        elif function == 'open_gate':
            Motor.open_gate()