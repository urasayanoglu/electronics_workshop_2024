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

def send_sos():
    for symbol in SOS_PATTERN:
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

def get_button_press_duration():
    start_time = time.time()
    while button.value() == 0:
        time.sleep(0.01)  # Small delay to avoid high CPU usage
    return time.time() - start_time

# Debouncing Function
def is_button_pressed():
    time.sleep(DEBOUNCE_TIME)
    return button.value() == 0

def get_button_state():
    return button.value() == 0  # Button is active low due to pull-up resistor

# Main Function
def main():
    sos_mode = True
    button_pressed = False
    last_press_time = 0

    while True:
        current_time = time.time()
        button_state = get_button_state()

        if button_state and not button_pressed:
            # Button press detected
            button_pressed = True
            press_start_time = current_time
            sos_mode = False

        elif not button_state and button_pressed:
            # Button release detected
            button_pressed = False
            press_duration = current_time - press_start_time
            last_press_time = current_time

            if press_duration >= DASH_LENGTH:
                send_morse_code('-')
            else:
                send_morse_code('.')

        # Return to SOS mode if no button activity for a certain period
        if not button_state and (current_time - last_press_time) > LETTER_PAUSE:
            sos_mode = True

        if sos_mode:
            send_sos()

        time.sleep(0.01)  # Small delay for loop

main()