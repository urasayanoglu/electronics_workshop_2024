#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   rear_lights_fading.py
@Time    :   2024/03/05 14:58:29
@Author  :   Uras Ayanoglu
@Version :   1.0
@Contact :   uras.ayanoglu@edu.turkuamk.fi
@License :   (C)Copyright 2023, Uras Ayanoglu
@Desc    :   A simple rear lights with fading example using PWM and a button.
@Platform:   AI-Thinker NodeMCU ESP12k ESP32-S2 on MicroPython v1.22.2
'''
import machine
import time

# Initialize the LED (with PWM for fading) and button
led = machine.PWM(machine.Pin(2), freq=1000)
button = machine.Pin(3, machine.Pin.IN, machine.Pin.PULL_UP)

# Set the fade period (in seconds)
fade_period = 2  # Adjust this value between 1 and 3

# Function to fade the LED
def fade_led(period):
    fade_time = period / 1024  # Divide period by number of steps
    for duty_cycle in range(0, 1024):
        led.duty(duty_cycle)
        time.sleep(fade_time)
    for duty_cycle in range(1023, -1, -1):
        led.duty(duty_cycle)
        time.sleep(fade_time)

# Debouncing function for the button
def button_pressed(last_press_time):
    if time.ticks_diff(time.ticks_ms(), last_press_time) > 200:
        return True
    return False


while True:
    if button.value() == 0:  # Check if the button is pressed
        led.duty(1023)  # Set LED to maximum brightness
    else:
        fade_led(fade_period)  # Fade the LED
