import time
import board
from circuitPyHuskyLib import HuskyLensLibrary

# Setup UART
huskylens = HuskyLensLibrary("I2C", SCL=board.GP5, SDA=board.GP4)


while True:
    objects = huskylens.requestAll()
    if objects:
        for obj in objects:
            print(f"Detected ID: {obj.ID}")
    else:
        print("No objects detected.")
    time.sleep(1)
