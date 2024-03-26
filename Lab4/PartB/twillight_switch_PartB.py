#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   twillight_switch_PartB.py
@Time    :   2024/03/25 23:43:18
@Author  :   Uras Ayanoglu
@Version :   1.0
@Contact :   uras.ayanoglu@edu.turkuamk.fi
@License :   (C)Copyright 2024, Uras Ayanoglu
@Desc    :   A simple twilight switch using a photoresistor and a potentiometer to control the brightness of an LED.
@Platform:   AI-Thinker NodeMCU ESP12k ESP32-S2 on MicroPython v1.22.2
'''

from machine import ADC, Pin, PWM
import time

# Initialize ADC for sensors
adc_lux = ADC(Pin(6))  # photoresistor for measuring light intensity
adc_lux.atten(ADC.ATTN_11DB)
adc_pot = ADC(Pin(7))  # ADC pin for variable resistor
adc_pot.atten(ADC.ATTN_11DB)

# Initialize the LED with PWM
led = PWM(Pin(3), freq=1000)  # Use a PWM pin for the LED

def update_led_brightness():
    # Read the ADC value from the variable resistor
    pot_value = adc_pot.read()
    max_pot_value = 8191
    duty = (pot_value / max_pot_value) * 1023  # Scale to PWM duty range

    # Update the LED brightness
    led.duty(int(duty))

def update_led_state(light_intensity):
    # Define the threshold for light intensity
    threshold = 80

    # Adjust the LED state based on light intensity
    if light_intensity > threshold:
        update_led_brightness()  # Adjust LED brightness based on potentiometer
    else:
        led.duty(0)  # Turn off the LED


def read_light_intensity():
    # Read and normalize light intensity
    raw_value = adc_lux.read()
    actual_max_adc_value = 8191
    percentage = (raw_value / actual_max_adc_value) * 100
    percentage = max(0, min(percentage, 100))
    return percentage

while True:
    light_intensity = read_light_intensity()
    update_led_state(light_intensity)
    time.sleep(0.1)
