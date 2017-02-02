# credits to https://github.com/recantha/stepper-pi
import applicatie.settings as settings
from waterkering.models import Melding
import time

# GPIO variables
if settings.RASPBERRY == True: 
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BOARD)

    for pins in settings.MOTOR_PINS:
        for pin in pins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, 0)

    # motor 1
    P1 = settings.MOTOR_PINS[0][0]
    P2 = settings.MOTOR_PINS[0][1]
    P3 = settings.MOTOR_PINS[0][2]
    P4 = settings.MOTOR_PINS[0][3]

    # motor 2
    P5 = settings.MOTOR_PINS[1][0]
    P6 = settings.MOTOR_PINS[1][1]
    P7 = settings.MOTOR_PINS[1][2]
    P8 = settings.MOTOR_PINS[1][3]

    # variables for calculations
    deg_per_step = 5.625 / 64 
    steps_per_rev = int(360 / deg_per_step)
    step_angle = 0
    revs_per_minute = 15
    _rpm = revs_per_minute

    # T is the amount of time to stop between signals
    _T = (60.0 / _rpm) / steps_per_rev


class Motor:

    def close_gate(angle=settings.TURN_ANGLE):

        # Only allow to close doors when current status is opened
        if settings.status == 'opened':

            # Set status to closing
            print('Closing gate.')
            settings.status = 'closing'
            Melding(melding = 'Closing').save()

            # Raspberry Pi connected
            if settings.RASPBERRY == True:
                target_step_angle = (int(angle / deg_per_step) / 8)
                steps = target_step_angle
                steps = int(steps % steps_per_rev)
                GPIO.output(P1, 0)
                GPIO.output(P5, 0)
                GPIO.output(P2, 0)
                GPIO.output(P6, 0)
                GPIO.output(P3, 0)
                GPIO.output(P7, 0)
                GPIO.output(P4, 0)
                GPIO.output(P8, 0)

                for i in range(steps):
                    GPIO.output(P3, 0)
                    GPIO.output(P7, 0)
                    time.sleep(_T)
                    GPIO.output(P1, 1)
                    GPIO.output(P5, 1)
                    time.sleep(_T)
                    GPIO.output(P4, 0)
                    GPIO.output(P8, 0)
                    time.sleep(_T)
                    GPIO.output(P2, 1)
                    GPIO.output(P6, 1)
                    time.sleep(_T)
                    GPIO.output(P1, 0)
                    GPIO.output(P5, 0)
                    time.sleep(_T)
                    GPIO.output(P3, 1)
                    GPIO.output(P7, 1)
                    time.sleep(_T)
                    GPIO.output(P2, 0)
                    GPIO.output(P6, 0)
                    time.sleep(_T)
                    GPIO.output(P4, 1)
                    GPIO.output(P8, 1)
                    time.sleep(_T)

            # Change status to closed regardless whether the RPi is connected and logs the action
            settings.status = 'closed'
            Melding(melding = 'Closed').save()

        # Fires when the close_gate function in called but the current status is not opened
        else:
            print('The gates cannot be closed when the gates are not open.')
            Melding(melding = 'Tried closing but failed because doors where not open').save()


    def open_gate(angle=settings.TURN_ANGLE):

        # Only allow to open doors when current status is closed
        if settings.status == 'closed':

            # Set status to opening
            print('Opening gate.')
            settings.status = 'opening'
            Melding(melding = 'Opening').save()

            # Raspberry Pi connected
            if settings.RASPBERRY == True:
                target_step_angle = (int(angle / deg_per_step) / 8)
                steps = target_step_angle
                steps = int(steps % steps_per_rev)
                GPIO.output(P1, 0)
                GPIO.output(P5, 0)
                GPIO.output(P2, 0)
                GPIO.output(P6, 0)
                GPIO.output(P3, 0)
                GPIO.output(P7, 0)
                GPIO.output(P4, 0)
                GPIO.output(P8, 0)

                for i in range(steps):
                    GPIO.output(P4, 1)
                    GPIO.output(P8, 1)
                    time.sleep(_T)
                    GPIO.output(P2, 0)
                    GPIO.output(P6, 0)
                    time.sleep(_T)
                    GPIO.output(P3, 1)
                    GPIO.output(P7, 1)
                    time.sleep(_T)
                    GPIO.output(P1, 0)
                    GPIO.output(P5, 0)
                    time.sleep(_T)
                    GPIO.output(P2, 1)
                    GPIO.output(P6, 1)
                    time.sleep(_T)
                    GPIO.output(P4, 0)
                    GPIO.output(P8, 0)
                    time.sleep(_T)
                    GPIO.output(P1, 1)
                    GPIO.output(P5, 1)
                    time.sleep(_T)
                    GPIO.output(P3, 0)
                    GPIO.output(P7, 0)
                    time.sleep(_T)

            # Change status to opened regardless whether the RPi is connected and logs the action
            settings.status = 'opened'
            Melding(melding = 'Opened').save()

        # Fires when the open_gate function in called but the current status is not closed
        else:
            print('The gates cannot be opened when the gates are not closed.')
            Melding(melding = 'Tried opening but failed because doors where not closed').save()