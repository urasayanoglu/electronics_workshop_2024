#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   twillight_switch_PartA.py
@Time    :   2024/03/25 22:31:33
@Author  :   Uras Ayanoglu
@Version :   1.0
@Contact :   uras.ayanoglu@edu.turkuamk.fi
@License :   (C)Copyright 2024, Uras Ayanoglu
@Desc    :   A twilight switch that turns on an LED when the light intensity is below a certain threshold
@Platform:   AI-Thinker NodeMCU ESP12k ESP32-S2 on MicroPython v1.22.2
'''

from machine import ADC, Pin
import time

# Initialize ADC for sensors
adc_lux = ADC(Pin(6)) # photoresistor that will be used to measure the light intensity
adc_lux.atten(ADC.ATTN_11DB)

# Initialize the led
led = Pin(3, Pin.OUT) # led that will be used to indicate the light intensity

def update_led(light_intensity):
    # Define the threshold for light intensity
    threshold = 80  # Example threshold, this means low light

    # Inverted the logic due to KY-018: Turn on the LED if the light intensity is high, which indicates low light
    if light_intensity > threshold:
        led.value(1)  # Turn on the LED
    else:
        led.value(0)  # Turn off the LED

def read_light_intensity():
    # Read ADC value
    raw_value = adc_lux.read()
    #print("Raw value: {}".format(raw_value))
    
    # maximum ADC value observed
    actual_max_adc_value = 8191

    # Normalize the reading to a percentage (0-100%)
    percentage = (raw_value / actual_max_adc_value) * 100

    # Ensure the percentage is within 0-100%
    percentage = max(0, min(percentage, 100))
    return percentage

while True:
    # Continuously read the light intensity and update LED state
    light_intensity = read_light_intensity()
    update_led(light_intensity)

    # Delay to prevent rapid polling (adjust as needed)
    time.sleep(0.1)