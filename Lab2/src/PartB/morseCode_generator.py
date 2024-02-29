#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   morseCode_generator.py
@Time    :   2024/02/29 13:39:07
@Author  :   Uras Ayanoglu
@Version :   1.0
@Contact :   uras.ayanoglu@edu.turkuamk.fi
@License :   (C)Copyright 2023, Uras Ayanoglu
@Desc    :   A simple Morse code generator with a tactile push switch, and a led using NodeMCU ESP32-S2 on MicroPython v1.22.2
'''

# main.py for NodeMCU ESP32-S2 with MicroPython
# Morse code generator using a tactile push switch

from machine import Pin
import utime

LED_BUILTIN = 2
BUTTON_PIN = 3

buttonPressTime = 0
buttonReleaseTime = 0
pressDuration = 0

dotDuration = 200  # Duration in milliseconds for a dot
dashDuration = 600  # Duration in milliseconds for a dash

# Initialize pins
led = Pin(LED_BUILTIN, Pin.OUT)
button = Pin(BUTTON_PIN, Pin.IN)

morseCode = "" # Variable to store the morse code for printing the message or storing it in a file

while True:
    buttonState = button.value()

    # Check if the button is pressed
    if buttonState == 0:
        if buttonPressTime == 0:
            # Record the time when the button is first pressed
            buttonPressTime = utime.ticks_ms()
        led.value(1)
    elif buttonPressTime != 0:
        # Record the time when the button is released
        buttonReleaseTime = utime.ticks_ms()

        # Calculate the duration of the press
        pressDuration = utime.ticks_diff(buttonReleaseTime, buttonPressTime)

        # Reset the press time
        buttonPressTime = 0

        # Determine if it was a dot or a dash
        if pressDuration < dotDuration:
            # Short press: dot
            morseCode += "."
            print(".")
        elif pressDuration >= dotDuration and pressDuration <= dashDuration:
            # Long press: dash
            morseCode += "-"
            print("-")

        led.value(0)

        # Add a small delay to debounce the switch
        utime.sleep_ms(50)
    