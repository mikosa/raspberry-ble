# to install voltmeter

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
