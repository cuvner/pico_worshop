import time
import board
import digitalio

# Set up the LED on GP15
led = digitalio.DigitalInOut(board.GP15)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True   # Turn on
    time.sleep(0.5)

    led.value = False  # Turn off
    time.sleep(0.5)