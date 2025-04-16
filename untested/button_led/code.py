import board
import digitalio
import time

# Set up the button on GP13 with Pull-UP
button = digitalio.DigitalInOut(board.GP13)
button.switch_to_input(pull=digitalio.Pull.UP)

# Set up the LED on GP15 as output
led = digitalio.DigitalInOut(board.GP15)
led.direction = digitalio.Direction.OUTPUT

while True:
    if not button.value:  # Button is pressed (LOW)
        led.value = True  # Turn on LED
        print("Button pressed - LED ON")
    else:
        led.value = False  # Turn off LED
        print("Button released - LED OFF")
    
    time.sleep(0.1)

