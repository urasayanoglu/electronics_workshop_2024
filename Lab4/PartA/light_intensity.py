#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   light_intensity.py
@Time    :   2024/03/26 10:26:29
@Author  :   Uras Ayanoglu
@Version :   1.0
@Contact :   uras.ayanoglu@edu.turkuamk.fi
@License :   (C)Copyright 2024, Uras Ayanoglu
@Desc    :   A small script to read the raw adc value, and light intensity from a photoresistor and print the percentage of light intensity
'''

from machine import Pin, ADC
import time

# Initialize ADC for sensors
adc_lux = ADC(Pin(6)) # photoresistor that will be used to measure the light intensity
adc_lux.atten(ADC.ATTN_11DB)

def read_light_intensity():
    # Read ADC value
    raw_value = adc_lux.read()
    print("Raw value: {}".format(raw_value))
    
    # Adjust for the actual maximum ADC value observed
    actual_max_adc_value = 8191

    # Normalize the reading to a percentage (0-100%)
    percentage = (raw_value / actual_max_adc_value) * 100

    # Ensure the percentage is within 0-100%
    percentage = max(0, min(percentage, 100))
    return percentage


while True:
    # Continuously read the light intensity and update LED state
    light_intensity = read_light_intensity()
    print("Light intensity: {:.2f}%".format(light_intensity))
    
    # Delay to prevent rapid polling (adjust as needed)
    time.sleep(1)