# credits to https://github.com/recantha/stepper-pi
import applicatie.settings as settings
import time

# GPIO variables
if settings.RASPBERRY == True: 
    print('initialize sensor')
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BOARD)

    # motor 1
    P1 = settings.MOTOR_PINS[0]
    P2 = settings.MOTOR_PINS[1]
    P3 = settings.MOTOR_PINS[2]
    P4 = settings.MOTOR_PINS[3]

    # motor 2
    P5 = settings.MOTOR_PINS[4]
    P6 = settings.MOTOR_PINS[5]
    P7 = settings.MOTOR_PINS[6]
    P8 = settings.MOTOR_PINS[7]

    # variables for calculations
    deg_per_step = 5.625 / 64 
    steps_per_rev = int(360 / deg_per_step)
    step_angle = 0
    revs_per_minute = 15
    _rpm = revs_per_minute

    # T is the amount of time to stop between signals
    _T = (60.0 / _rpm) / steps_per_rev


class Motor:

    def close_gate(angle=90):
        print("Closing gate.")
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
                sleep(_T)
                GPIO.output(P2, 0)
                GPIO.output(P6, 0)
                sleep(_T)
                GPIO.output(P3, 1)
                GPIO.output(P7, 1)
                sleep(_T)
                GPIO.output(P1, 0)
                GPIO.output(P5, 0)
                sleep(_T)
                GPIO.output(P2, 1)
                GPIO.output(P6, 1)
                sleep(_T)
                GPIO.output(P4, 0)
                GPIO.output(P8, 0)
                sleep(_T)
                GPIO.output(P1, 1)
                GPIO.output(P5, 1)
                sleep(_T)
                GPIO.output(P3, 0)
                GPIO.output(P7, 0)
                sleep(_T)

    def open_gate(angle=90):
        print("Opening gate.")
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
                sleep(_T)
                GPIO.output(P1, 1)
                GPIO.output(P5, 1)
                sleep(_T)
                GPIO.output(P4, 0)
                GPIO.output(P8, 0)
                sleep(_T)
                GPIO.output(P2, 1)
                GPIO.output(P6, 1)
                sleep(_T)
                GPIO.output(P1, 0)
                GPIO.output(P5, 0)
                sleep(_T)
                GPIO.output(P3, 1)
                GPIO.output(P7, 1)
                sleep(_T)
                GPIO.output(P2, 0)
                GPIO.output(P6, 0)
                sleep(_T)
                GPIO.output(P4, 1)
                GPIO.output(P8, 1)
                sleep(_T)