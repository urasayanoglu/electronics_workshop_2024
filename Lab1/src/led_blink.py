#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   led_blink.py
@Time    :   2024/02/22 21:49:17
@Author  :   Uras Ayanoglu
@Version :   1.0
@Contact :   uras.ayanoglu@edu.turkuamk.fi
@License :   (C)Copyright 2023, Uras Ayanoglu
@Desc    :   A simple LED blink example for AI-Thinker NodeMCU ESP32-S2 on MicroPython v1.22.2
'''


import machine
import time

led = machine.Pin(2, machine.Pin.OUT)

while True:
    led.value(1)
    time.sleep(1)
    led.value(0)
    time.sleep(1)

