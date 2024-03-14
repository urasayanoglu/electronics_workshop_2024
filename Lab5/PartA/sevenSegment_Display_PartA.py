#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   sevenSegment_Display.py
@Time    :   2024/03/07 14:47:29
@Author  :   Uras Ayanoglu
@Version :   1.0
@Contact :   uras.ayanoglu@edu.turkuamk.fi
@License :   (C)Copyright 2023, Uras Ayanoglu
@Desc    :   A small program that blinks LED G and lights on LEDs in series from A to F in a continuous loop on a 4-digit 7-segment display.
@Platform:   AI-Thinker NodeMCU ESP12k ESP32-S2 on MicroPython v1.22.2
'''

'''
Pin connections between 4-digit 7-segment display and NodeMCU ESP32-S2:

Segment A (Display Pin 11) to NodeMCU GPIO21
Segment B (Display Pin 7) to NodeMCU GPIO19
Segment C (Display Pin 4) to NodeMCU GPIO18
Segment D (Display Pin 2) to NodeMCU GPIO5
Segment E (Display Pin 1) to NodeMCU GPIO17
Segment F (Display Pin 10) to NodeMCU GPIO16
Segment G (Display Pin 5) to NodeMCU GPIO4
Decimal Point (DP) (Display Pin 3) to NodeMCU GPIO1 

Display Digits to NodeMCU Pins
Digit 1 (D1) (Display Pin 12) to NodeMCU GPIO15
Digit 2 (D2) (Display Pin 9) to NodeMCU GPIO2
Digit 3 (D3) (Display Pin 8) to NodeMCU GPIO14
Digit 4 (D4) (Display Pin 6) to NodeMCU GPIO13

'''

from machine import Pin
from time import sleep

# Define the GPIO pins (replace x with actual pin numbers)
segments = {'A': Pin(21, Pin.OUT), 
            'B': Pin(19, Pin.OUT), 
            'C': Pin(18, Pin.OUT),
            'D': Pin(5, Pin.OUT),
            'E': Pin(17, Pin.OUT),
            'F': Pin(16, Pin.OUT), 
            'G': Pin(4, Pin.OUT),
            'DP': Pin(1, Pin.OUT)
            }

common_cathodes = {'D1': Pin(15, Pin.OUT), 
                   'D2': Pin(2, Pin.OUT), 
                   'D3': Pin(14, Pin.OUT), 
                   'D4': Pin(13, Pin.OUT)
                   }

def clear_segments(exclude='G'):
    for segment in segments.keys():
        if segment != exclude:
            segments[segment].value(1)

def display_digit(digit):
    for cathode in common_cathodes.values():
        cathode.value(1)  # Turn off all digits
    common_cathodes[digit].value(0)  # Turn on selected digit
    segments['G'].value(g_state)  # Maintain current state of G

def blink_G():
    global g_state
    g_state = 0
    for digit in common_cathodes:
        display_digit(digit)
    sleep(0.1)
    g_state = 1
    for digit in common_cathodes:
        display_digit(digit)
    sleep(0.1)

# Initial state of G segment
g_state = 1

while True:
    # Continuously blink LED G on all digits
    blink_G()

    # Sequentially blink LEDs A to F on all digits
    for seg in ['A', 'B', 'C', 'D', 'E', 'F']:
        for digit in common_cathodes:
            display_digit(digit)
            clear_segments()
            segments[seg].value(0)  # Turn on segment
            sleep(0.1)
