#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   twillight_switch_PartC.py
@Time    :   2024/03/26 10:44:37
@Author  :   Uras Ayanoglu
@Version :   1.0
@Contact :   uras.ayanoglu@edu.turkuamk.fi
@License :   (C)Copyright 2024, Uras Ayanoglu
@Desc    :   A simple twilight switch that dims an LED based on the photoresistor values.
@Platform:   AI-Thinker NodeMCU ESP12k ESP32-S2 on MicroPython v1.22.2
'''

from machine import ADC, Pin, PWM
import time

# Initialize ADC for the photoresistor
adc_lux = ADC(Pin(6))
adc_lux.atten(ADC.ATTN_11DB)

# Initialize the LED with PWM
led = PWM(Pin(3), freq=1000)

# Define the threshold for light intensity
threshold = 30  

def update_led_brightness(light_intensity):
    # Calculate duty cycle for the PWM based on light intensity
    # Higher light intensity values mean darker conditions for Keyes KY-018 Photoresistor
    min_brightness_threshold = 30  # Light intensity threshold for starting to light up the LED

    if light_intensity < min_brightness_threshold:
        # If light intensity is below the threshold, turn off the LED
        led.duty(0)
    else:
        # Adjust the light intensity range from 30-100% to 0-100% for brightness scaling
        adjusted_intensity = (light_intensity - min_brightness_threshold) / (100 - min_brightness_threshold)

        # Scale the adjusted intensity to the PWM duty cycle
        duty_cycle = adjusted_intensity * 1023
        led.duty(int(duty_cycle))

def read_light_intensity():
    # Read and normalize light intensity
    raw_value = adc_lux.read()
    actual_max_adc_value = 8191
    percentage = (raw_value / actual_max_adc_value) * 100
    return max(0, min(percentage, 100))

while True:
    # Continuously read the light intensity
    light_intensity = read_light_intensity()

    # Update LED brightness based on the light intensity
    update_led_brightness(light_intensity)

    time.sleep(0.1)
