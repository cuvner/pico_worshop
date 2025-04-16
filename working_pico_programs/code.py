import board
import time
import busio
import pwmio
import sys
from digitalio import DigitalInOut, Direction

#from circuitPyHuskyLib import HuskyLensLibrary
from adafruit_motor import servo
# Temp sensor
import adafruit_sht4x

# Onboard LED (works on Pico and Pico W)
led = DigitalInOut(board.LED)
led.direction = Direction.OUTPUT
print("Hello World")

while True:
    led.value = True   # LED on
    time.sleep(0.5)
    led.value = False  # LED off
    time.sleep(0.5)

