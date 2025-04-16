import time
import board
import pwmio
import digitalio
from adafruit_motor import servo

# Set up PWM output for the servo on GP15
pwm = pwmio.PWMOut(board.GP15, duty_cycle=0, frequency=50)

# Create a servo object
my_servo = servo.Servo(pwm)

# Set up button on GP14
button = digitalio.DigitalInOut(board.GP14)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.DOWN  # Makes sure the button reads False when not pressed

while True:
    if button.value:  # Button is pressed
        print("Button pressed - moving servo")
        my_servo.angle = 0
        time.sleep(1)

        my_servo.angle = 90
        time.sleep(1)

        my_servo.angle = 180
        time.sleep(1)
    else:
        print("Waiting for button...")
        time.sleep(0.1)
