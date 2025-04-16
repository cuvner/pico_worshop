import board
from circuitPyHuskyLib import HuskyLensLibrary
import time

# Initialize UART HuskyLens on custom pins
hl = HuskyLensLibrary('UART', TX=board.GP8, RX=board.GP9)

# Set the algorithm to Face Recognition
hl.algorithm("ALGORITHM_FACE_RECOGNITION")

while True:
    blocks = hl.blocks()
    if blocks:
        for block in blocks:
            print("Face ID:", block.ID)
            print("Position:", block.x, block.y)
    else:
        print("No face detected.")
    time.sleep(0.2)
