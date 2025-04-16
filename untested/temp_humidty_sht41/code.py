import time
import board
import adafruit_sht4x

i2c = board.STEMMA_I2C()  # or board.I2C() on Pico W

sensor = adafruit_sht4x.SHT4x(i2c)
print("Found SHT4x sensor")

# You can set precision if you want (default is HIGH)
# sensor.mode = adafruit_sht4x.Mode.NOHEAT_HIGHPRECISION

while True:
    temperature, relative_humidity = sensor.measurements
    print("Temperature: {:.2f} °C".format(temperature))
    print("Humidity: {:.2f}%".format(relative_humidity))
    time.sleep(1)
