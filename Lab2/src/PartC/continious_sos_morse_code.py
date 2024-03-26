#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   continious_sos_morse_code.py
@Time    :   2024/02/25 17:19:06
@Author  :   Uras Ayanoglu
@Version :   1.0
@Contact :   uras.ayanoglu@edu.turkuamk.fi
@License :   (C)Copyright 2023, Uras Ayanoglu
@Desc    :   A simple morse code generator example with continious distress signal sending for AI-Thinker NodeMCU ESP32-S2 on MicroPython v1.22.2
'''
import machine
import time

# LED and Button Pin Configuration
led = machine.Pin(2, machine.Pin.OUT)
button = machine.Pin(3, machine.Pin.IN)

# Morse Code and SOS Pattern
SOS_PATTERN = "...---..."
MORSE_CODE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', ' ': '/'
}

# Timing Constants
DOT_LENGTH = 0.2
DASH_LENGTH = 0.6
LETTER_PAUSE = 0.3
DEBOUNCE_TIME = 0.2


# Function Definitions
def play_dot():
    led.value(1)
    time.sleep(0.2)
    led.value(0)
    time.sleep(0.2)

def play_dash():
    led.value(1)
    time.sleep(0.6)
    led.value(0)
    time.sleep(0.2)

def check_interrupt():
    if button_pressed():
        wait_for_button_release()
        return True
    return False

def send_sos():
    for symbol in SOS_PATTERN:
        if check_interrupt():
            return

        if symbol == '.':
            play_dot()
        elif symbol == '-':
            play_dash()

def send_morse_code(symbol):
    if symbol in MORSE_CODE:
        for char in MORSE_CODE[symbol]:
            if char == '.':
                play_dot()
            elif char == '-':
                play_dash()
        time.sleep(0.3)  # Inter-letter silence

def button_pressed():
    return button.value() == 0

def wait_for_button_release():
    while button_pressed():
        time.sleep(0.01)

def get_button_press_duration():
    duration = 0
    while button_pressed():
        time.sleep(0.01)
        duration += 0.01
    return duration

# Main Function
def main():
    last_button_press_time = time.time()

    while True:
        if button_pressed():
            last_button_press_time = time.time()
            press_duration = get_button_press_duration()
            wait_for_button_release()

            # Send Morse Code
            if press_duration >= DASH_LENGTH:
                send_morse_code('-')
            else:
                send_morse_code('.')

        elif time.time() - last_button_press_time > LETTER_PAUSE:
            # Send SOS if no button press for a certain duration
            send_sos()

        time.sleep(0.01)

main()