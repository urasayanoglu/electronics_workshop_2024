#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   rgbLed_Controller_ExtraMile.py
@Time    :   2024/03/22 11:41:37
@Author  :   Uras Ayanoglu
@Version :   1.0
@Contact :   uras.ayanoglu@edu.turkuamk.fi
@License :   (C)Copyright 2024, Uras Ayanoglu
@Desc    :   An RGB LED (WS2812D-F5_STRAW HAT-15MA) controller with a potentiometer and a button that displays the selected color and voltage on an LCD.
@Platform:   AI-Thinker NodeMCU ESP12k ESP32-S2 on MicroPython v1.22.2
'''

from machine import ADC, Pin, PWM, SoftI2C
from lib_lcd1602_2004_with_i2c import LCD
from neopixel import NeoPixel
import time

# Initialize ADC for potentiometer
adc = ADC(Pin(7))  
adc.atten(ADC.ATTN_11DB)  # For full range of 3.3V or 5V

# Initialize NeoPixel for WS2812 LED
neo_pin = Pin(4, Pin.OUT)  # Use the GPIO pin connected to Din of WS2812
num_leds = 1  # Number of LEDs in the strip
np = NeoPixel(neo_pin, num_leds)

# Initialize the button
button = Pin(3, Pin.IN)  

# Initialize I2C for LCD (modify the pins as per your ESP32-S2 board)

scl_pin = 9 # pin number for SCL
sda_pin = 8 # pin number for SDA

# Create LCD object
lcd = LCD(SoftI2C(scl=Pin(scl_pin), sda=Pin(sda_pin), freq=100000)) 

color_names = ["Red", "Green", "Blue"]

def update_lcd(color, voltage):
    lcd.clear()
    # Display color information on the first row (y=0)
    lcd.puts("Color: {}".format(color_names[color]), y=0, x=0)
    # Display voltage information on the second row (y=1)
    lcd.puts("Voltage: {:.2f}V".format(voltage), y=1, x=0)

# Variables to track button state and color selection
last_button_state = 1
current_color = 0
debounce_time = 50

def update_led_brightness(color, value):
    # Convert potentiometer value to RGB value (0-255)
    rgb_value = int(value * 255 / 1023)
    
    # Create a color tuple (R, G, B)
    if color == 0:  # green
        color_tuple = (0, rgb_value, 0)
    elif color == 1:  # red
        color_tuple = (rgb_value, 0, 0)
    else:  # blue
        color_tuple = (0, 0, rgb_value)

    # Set the color of the first LED
    np[0] = color_tuple
    np.write()

while True:
    button_state = button.value()
    if button_state != last_button_state:
        if button_state == 0:  # Button is pressed
            time.sleep_ms(debounce_time)  # Debouncing
            current_color = (current_color + 1) % 3  # Cycle through colors

    last_button_state = button_state

    # Read potentiometer value and map to PWM range
    pot_value = adc.read() * 1023 // 8191

    # Update the brightness of the selected LED
    update_led_brightness(current_color, pot_value)

    # Calculate the voltage (assuming 3.3V max for ADC)
    print(adc.read())
    voltage = adc.read() * 3.3 / 8191

    # Update the LCD display
    update_lcd(current_color, voltage)

    time.sleep(0.1)  # Small delay to reduce flickering

