#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   rear_lights_fading_both_directions.py
@Time    :   2024/03/05 15:05:24
@Author  :   Uras Ayanoglu
@Version :   1.0
@Contact :   uras.ayanoglu@edu.turkuamk.fi
@License :   (C)Copyright 2023, Uras Ayanoglu
@Desc    :   None
@Platform:   AI-Thinker NodeMCU ESP12k ESP32-S2 on MicroPython v1.22.2
'''
import machine
import time

# Initialize the LED (with PWM for fading) and button
led = machine.PWM(machine.Pin(2), freq=1000)
button = machine.Pin(3, machine.Pin.IN, machine.Pin.PULL_UP)

# Set the fade period (in seconds)
fade_period = 2  # Adjust this value between 1 and 3

# Variable to keep track of fading direction
fading_up = True

# Function to fade the LED
def fade_led(period, fade_up):
    fade_time = period / 1024  # Divide period by number of steps
    if fade_up:
        for duty_cycle in range(0, 1024):
            led.duty(duty_cycle)
            time.sleep(fade_time)
    else:
        for duty_cycle in range(1023, -1, -1):
            led.duty(duty_cycle)
            time.sleep(fade_time)

# Debouncing function for the button
def button_pressed(last_press_time):
    if time.ticks_diff(time.ticks_ms(), last_press_time) > 200:
        return True
    return False

last_press_time = 0

while True:
    if button.value() == 0 and button_pressed(last_press_time):
        last_press_time = time.ticks_ms()
        fading_up = not fading_up  # Reverse the fading direction
    else:
        fade_led(fade_period, fading_up)
