import time
import board
import pwmio
from adafruit_motor import servo

# Create a PWMOut object on a pin (e.g. GP15)
pwm = pwmio.PWMOut(board.GP16, duty_cycle=0, frequency=50)

# Create a servo object
my_servo = servo.Servo(pwm)

while True:
    print("Moving to 0°")
    my_servo.angle = 0
    time.sleep(1)

    print("Moving to 90°")
    my_servo.angle = 90
    time.sleep(1)

    print("Moving to 180°")
    my_servo.angle = 180
    time.sleep(1)
