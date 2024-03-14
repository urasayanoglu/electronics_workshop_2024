#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   rgbLed_Controller_PartC.py
@Time    :   2024/03/13 13:44:39
@Author  :   Uras Ayanoglu
@Version :   1.0
@Contact :   uras.ayanoglu@edu.turkuamk.fi
@License :   (C)Copyright 2024, Uras Ayanoglu
@Desc    :   None
@Platform:   AI-Thinker NodeMCU ESP12k ESP32-S2 on MicroPython v1.22.2
'''

from machine import ADC, Pin, PWM, I2C
import time
# from pcf8574_i2c import PCF8574_I2C # Import necessary libraries for AI-Thinker NodeMCU ESP12k ESP32-S2
# from lcd_api import LcdApi # Import necessary libraries for AI-Thinker NodeMCU ESP12k ESP32-S2

# Initialize ADC for potentiometer
adc = ADC(Pin(7))  
adc.atten(ADC.ATTN_11DB)  # For full range of 3.3V or 5V

# Initialize PWM for RGB LED
red = PWM(Pin(4), freq=5000)  
green = PWM(Pin(5), freq=5000)  
blue = PWM(Pin(6), freq=5000)  

# Initialize the button
button = Pin(3, Pin.IN)  

# Initialize I2C for LCD (modify the pins as per your ESP32-S2 board)
# i2c = I2C(scl=Pin(22), sda=Pin(21), freq=400000)
# lcd = LcdApi(PCF8574_I2C(i2c, 0x27), 2, 16)  # Adjust the I2C address if needed

color_names = ["Red", "Green", "Blue"]

def update_lcd(color, voltage):
    lcd.clear()
    lcd.putstr("Color: {}\nVoltage: {:.2f}V".format(color_names[color], voltage))

# Variables to track button state and color selection
last_button_state = 1
current_color = 0
debounce_time = 50

def update_led_brightness(color, value):
    # Make sure value is within PWM range
    pwm_value = max(0, min(1023, value))
    
    # Adjust the brightness of the specified color
    if color == 0:
        red.duty(pwm_value)
    elif color == 1:
        green.duty(pwm_value)
    else:
        blue.duty(pwm_value)

while True:
    button_state = button.value()
    if button_state != last_button_state:
        if button_state == 0:  # Button is pressed
            time.sleep_ms(debounce_time)  # Debouncing
            current_color = (current_color + 1) % 3  # Cycle through colors

    last_button_state = button_state

    # Read potentiometer value and map to PWM range
    pot_value = adc.read() * 1023 // 4095

    # Update the brightness of the selected LED
    update_led_brightness(current_color, pot_value)

    # Calculate the voltage (assuming 3.3V max for ADC)
    # voltage = adc.read() * 3.3 / 4095

    # Update the LCD display
    # update_lcd(current_color, voltage)

    time.sleep(0.1)  # Small delay to reduce flickering

