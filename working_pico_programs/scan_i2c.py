import time
import board
import busio

# Set up hardware I2C on the Pico
i2c = busio.I2C(board.GP5, board.GP4)  # SCL, SDA

# Wait for I2C to be ready
while not i2c.try_lock():
    pass

try:
    devices = i2c.scan()
    if devices:
        print("I2C devices found:", [hex(address) for address in devices])
    else:
        print("No I2C devices found.")
finally:
    i2c.unlock()
