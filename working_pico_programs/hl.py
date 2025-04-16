import board
from circuitPyHuskyLib import HuskyLensLibrary
huskylens = HuskyLensLibrary("I2C", SCL=board.GP5, SDA=board.GP4)

print(huskylens.knock())