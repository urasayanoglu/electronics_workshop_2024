#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   bme280_test.py
@Time    :   2024/03/27 11:40:28
@Author  :   Uras Ayanoglu
@Version :   1.0
@Contact :   uras.ayanoglu@edu.turkuamk.fi
@License :   (C)Copyright 2024, Uras Ayanoglu
@Desc    :   A small script to test the BME280 sensor
@Platform:   AI-Thinker NodeMCU ESP12k ESP32-S2 on MicroPython v1.22.2
'''

from machine import Pin, SoftI2C
from bme280_float import BME280
import time

# Initialize I2C and create BME280 object
scl_bme = 1 # pin number for SCL
sda_bme = 10 # pin number for SDA

bme = BME280(i2c=SoftI2C(scl=Pin(scl_bme), sda=Pin(sda_bme), freq=100000))

# Initialize the I2C connection for BME280
scl_bme = 1  # pin number for SCL
sda_bme = 10 # pin number for SDA

i2c_bme = SoftI2C(scl=Pin(scl_bme), sda=Pin(sda_bme), freq=100000)

# Initialize the BME280 sensor
bme = BME280(i2c=i2c_bme)

while True:
    # Read temperature, pressure, and humidity
    temp, pressure, humidity = bme.read_compensated_data()

    print("Temperature: {:.2f} C".format(temp))
    print("Pressure: {:.2f} hPa".format(pressure/100))
    print("Humidity: {:.2f} %".format(humidity))

    # Sleep for a bit before reading again
    time.sleep(2)
