#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   rear_lights.py
@Time    :   2024/03/05 13:51:58
@Author  :   Uras Ayanoglu
@Version :   1.0
@Contact :   uras.ayanoglu@edu.turkuamk.fi
@License :   (C)Copyright 2023, Uras Ayanoglu
@Desc    :   A simple rear lights example.
@Platform:   AI-Thinker NodeMCU ESP12k ESP32-S2 on MicroPython v1.22.2
'''

import machine
import time

led = machine.Pin(2, machine.Pin.OUT)
button = machine.Pin(3, machine.Pin.IN)

# Function for blinking the LED
def blink_led(interval):
    led.value(1)  # Turn on the LED
    time.sleep(interval)
    led.value(0)  # Turn off the LED
    time.sleep(interval)

while True:
    if button.value() == 0:  # Check if the button is pressed
        led.value(1)  # Turn on the LED for continuous shining
    else:
        blink_led(0.3)  # Led is shining with 0.3 seconds interval