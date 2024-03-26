#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   sevenSegment_Display_ExtraMile.py
@Time    :   2024/03/26 22:06:43
@Author  :   Uras Ayanoglu
@Version :   1.0
@Contact :   uras.ayanoglu@edu.turkuamk.fi
@License :   (C)Copyright 2024, Uras Ayanoglu
@Desc    :   A simple micropython program to display numbers on a Catalex 3642BH 4-digit display module 
@Platform:   AI-Thinker NodeMCU ESP12k ESP32-S2 on MicroPython v1.22.2
'''

'''
Pin connections between Catalex 3642BH 4-digit display module and AI-Thinker NodeMCU ESP12k ESP32-S2:

CLK (Display Pin 1) to NodeMCU GPIO9
DIO (Display Pin 2) to NodeMCU GPIO08
VCC (Display Pin 3) to NodeMCU 5V
GND (Display Pin 4) to NodeMCU GND

Button Connection:
Button 1 to NodeMCU GPIO6

'''

from machine import Pin
from time import sleep
import tm1637  # Importing the TM1637 library for Catalex 3642BH 4-digit display module

# Set up the display
CLK = Pin(9, Pin.OUT)   # CLK pin
DIO = Pin(8, Pin.OUT)   # DIO pin
display = tm1637.TM1637(clk=CLK, dio=DIO)

# Define the GPIO pin for the button
button = Pin(6, Pin.IN)

def debounce_button():
    if button.value() == 0:
        sleep(0.2)  # Debounce delay
        return True
    return False

state = 0  # Start with displaying 0

while True:
    if debounce_button():
        state = 1 - state
        sleep(0.2)  # Delay to prevent immediate re-toggle

    if state == 0:
        # State 0: Display 0 0 0 0
        display.show('0000')
    else:
        # State 1: Counting loop
        for number in range(10):
            if debounce_button():
                state = 0
                break
            display.number(number)  # Using the number() method for displaying numbers
            sleep(0.5)  # Adjust the delay as needed