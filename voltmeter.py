import time
import board
import adafruit_ads1x15.ads1115 as  ADS
from adafruit_ads1x15.analog_in import AnalogIn
import busio

# I2C initialization
i2c = busio.I2C(board.SCL, board.SDA)

# Initialize ADS1115
ads = ADS.ADS1115(i2c)

# Set up channel (A0)
chan = AnalogIn(ads, ADS.P0)

# Voltage divider factor
divider_factor = 6.1

# Continuous reading
while True:
    raw_voltage = chan.voltage  # Voltage at ADC pin
    actual_voltage = raw_voltage * divider_factor  # Scale to original voltage
    print(f"Raw Voltage: {raw_voltage:.2f} V, Actual Voltage: {actual_voltage:.>
    time.sleep(1)
