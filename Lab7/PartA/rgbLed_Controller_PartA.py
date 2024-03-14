#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   rgbLed_Controller_PartA.py
@Time    :   2024/03/13 12:56:54
@Author  :   Uras Ayanoglu
@Version :   1.0
@Contact :   uras.ayanoglu@edu.turkuamk.fi
@License :   (C)Copyright 2024, Uras Ayanoglu
@Desc    :   A simple RGB LED controller using potentiometer
@Platform:   AI-Thinker NodeMCU ESP12k ESP32-S2 on MicroPython v1.22.2
'''

from machine import ADC, Pin, PWM
import time

# Initialize ADC for potentiometer
adc = ADC(Pin(7)) 
adc.atten(ADC.ATTN_11DB)  # For full range of 3.3V or 5V

# Initialize PWM for RGB LED
red = PWM(Pin(4), freq=5000)  
green = PWM(Pin(5), freq=5000)  
blue = PWM(Pin(6), freq=5000)  

while True:
    voltage = adc.read()  # Read potentiometer value
    if voltage < 1365:
        # Turn on red
        red.duty(1023)
        green.duty(0)
        blue.duty(0)
    elif voltage < 2730:
        # Turn on green
        red.duty(0)
        green.duty(1023)
        blue.duty(0)
    else:
        # Turn on blue
        red.duty(0)
        green.duty(0)
        blue.duty(1023)

    time.sleep(0.1)  # Small delay to reduce flickering
