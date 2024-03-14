#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   sevenSegment_Display_PartB.py
@Time    :   2024/03/12 10:45:44
@Author  :   Uras Ayanoglu
@Version :   1.0
@Contact :   uras.ayanoglu@edu.turkuamk.fi
@License :   (C)Copyright 2024, Uras Ayanoglu
@Desc    :   None
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

def clear_segments():
    for segment in segments.values():
        segment.value(1)

def activate_segments(number):
    clear_segments()
    for segment in number_mapping[number]:
        segments[segment].value(0)

def display_number(number):
    activate_segments(number)
    for _ in range(100):  # Loop to create persistence of vision
        for cathode in common_cathodes.values():
            cathode.value(0)
            sleep(0.001)  # Short delay for each digit
            cathode.value(1)

number_mapping = {
    0: ['A', 'B', 'C', 'D', 'E', 'F'],
    1: ['B', 'C'],
    2: ['A', 'B', 'G', 'E', 'D'],
    3: ['A', 'B', 'G', 'C', 'D'],
    4: ['F', 'G', 'B', 'C'],
    5: ['A', 'F', 'G', 'C', 'D'],
    6: ['A', 'F', 'G', 'C', 'D', 'E'],
    7: ['A', 'B', 'C'],
    8: ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    9: ['A', 'B', 'C', 'D', 'F', 'G']
}

while True:
    for number in range(10):
        display_number(number)
        sleep(1)  # Adjust the delay as needed