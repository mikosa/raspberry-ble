# to install voltmeter with R bridge calculated for 20v

activate I2C with 
```
sudo raspi-config
```

Then install the following

```
pip install adafruit-circuitpython-ads1x15 adafruit-blinka
```

to  test i2c
```
sudo apt install i2c-tools
i2cdetect -y 1
```


ADS1115 


    +------------------+
    | Input Voltage    |
    | (Battery)        |
    |   +              |
    |   |              |
    +---+              |
        |              |
      R1 (51kΩ)        |
        |              |
        +--- A0        |
        |              |
      R2 (10kΩ)        |
        |              |
       GND             |
        |              |
    +---+              |
    | ADS1115          |
    |                  |
    |   A0             |
    |   SDA -----------+------------------- GPIO 2 (SDA)
    |   SCL -----------+------------------- GPIO 3 (SCL)
    |   VDD -----------+------------------- 3.3V (or 5V)
    |   GND -----------+------------------- GND
    +------------------+

