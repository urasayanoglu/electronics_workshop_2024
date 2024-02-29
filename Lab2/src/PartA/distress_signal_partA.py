#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   distress_signal_partA.py
@Time    :   2024/02/23 23:01:39
@Author  :   Uras Ayanoglu
@Version :   1.0
@Contact :   uras.ayanoglu@edu.turkuamk.fi
@License :   (C)Copyright 2023, Uras Ayanoglu
@Desc    :   A simple continious distress signal example for AI-Thinker NodeMCU ESP32-S2 on MicroPython v1.22.2
'''

import machine
import time

led = machine.Pin(2, machine.Pin.OUT)

# Morse code timings in seconds
dot_length = 0.2
dash_length = dot_length * 3
inter_element_gap = dot_length
inter_letter_gap = dot_length * 3
inter_word_gap = dot_length * 7

# Function to represent a dot
def dot():
    led.value(1)
    time.sleep(dot_length)
    led.value(0)
    time.sleep(inter_element_gap)

# Function to represent a dash
def dash():
    led.value(1)
    time.sleep(dash_length)
    led.value(0)
    time.sleep(inter_element_gap)

def distress_signal():
    """A simple continuous distress signal function"""
    for _ in range(3):
        dot()
    for _ in range(3):
        dash()
    for _ in range(3):
        dot()
    time.sleep(inter_word_gap)

while True:
    distress_signal()