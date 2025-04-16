import time
import board
from circuitPyHuskyLib import HuskyLensLibrary

# Set up the HuskyLens
huskylens = HuskyLensLibrary("I2C", SCL=board.GP5, SDA=board.GP4)


# (Optional) Add your own ID-to-name mapping if names are not fetched from device
object_names = {
    1: "Dog",
    2: "Cat",
    3: "Car"
}

while True:
    results = huskylens.requestAll()  # Get all detected objects
    if results:
        for obj in results:
            obj_id = obj.ID
            name = object_names.get(obj_id, "Unknown")
            print(f"ID: {obj_id}, Name: {name}")
    else:
        print("No objects detected.")
    time.sleep(1)

