#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   Untitled-1
@Time    :   2024/03/27 10:31:43
@Author  :   Uras Ayanoglu
@Version :   1.0
@Contact :   uras.ayanoglu@edu.turkuamk.fi
@License :   (C)Copyright 2024, Uras Ayanoglu
@Desc    :   A micropython program that reads temperature, humidity, pressure, and light intensity from BME280 and photoresistor sensors, and displays the readings on an LCD screen.
The program also uses a WS2812 LED to indicate the temperature level.
@Platform:   AI-Thinker NodeMCU ESP12k ESP32-S2 on MicroPython v1.22.2
'''

from machine import ADC, Pin, SoftI2C
from lib_lcd1602_2004_with_i2c import LCD
from neopixel import NeoPixel
from bme280_float import BME280 
import time

# Initialize NeoPixel for WS2812 LED
neo_pin = Pin(4, Pin.OUT)  # GPIO pin connected to Din of WS2812
num_leds = 1  # Number of LEDs in the strip
np = NeoPixel(neo_pin, num_leds)

# Initialize the button
value_button = Pin(3, Pin.IN) # button that will be used to update the readings on the LCD
temperature_button = Pin(5, Pin.IN)  # button that will be used to change reading from celcus to fahrenheit

# Initialize I2C for LCD 
scl_pin = 9 # pin number for SCL
sda_pin = 8 # pin number for SDA

# Create LCD object
lcd = LCD(SoftI2C(scl=Pin(scl_pin), sda=Pin(sda_pin), freq=100000)) 


# Initialize the I2C connection for BME280
scl_bme = 1  # pin number for SCL
sda_bme = 10 # pin number for SDA

i2c_bme = SoftI2C(scl=Pin(scl_bme), sda=Pin(sda_bme), freq=100000)

# Initialize the BME280 sensor
bme = BME280(i2c=i2c_bme)

# Initialize ADC for sensors
adc_lux = ADC(Pin(6)) # photoresistor that will be used to measure the light intensity
adc_lux.atten(ADC.ATTN_11DB)

cold = (0, 0, 255) # blue color 
medium = (255, 255, 0) # yellow color
warm = (0, 255, 0) # red color; color channels are ordered differently GRB instead of RGB on the WS2812 LED


def update_leds(temp_c):
    # Determine the color of LED based on temperature
    print("Current Temperature:", temp_c)  # Debugging output

    if temp_c < 20:  # Cold threshold
        color = cold
    elif 20 <= temp_c < 30:  # Medium threshold
        color = medium
    else:  # Warm threshold
        color = warm

    np[0] = color
    np.write()

def update_display(temp_c, light, humidity, pressure, use_fahrenheit):
    # Update LCD display with sensor readings
    lcd.clear()
    if use_fahrenheit:
        temp_f = celsius_to_fahrenheit(temp_c)
        # Dispplay temperature and light intensity information on the first row (y=0)
        lcd.puts("T:{:.1f}F L:{:.1f}".format(temp_f, light), y=0, x=0)
        # Display humidity and pressure information on the second row (y=1)
        lcd.puts("H:{:.1f}% P:{:.1f}hPa".format(humidity, pressure), y=1, x=0) 
    else:
        # Dispplay temperature and light intensity information on the first row (y=0)
        lcd.puts("T:{:.1f}C L:{:.1f}".format(temp_c, light), y=0, x=0)
        # Display humidity and pressure information on the second row (y=1)
        lcd.puts("H:{:.1f}% P:{:.1f}hPa".format(humidity, pressure), y=1, x=0) 


def celsius_to_fahrenheit(celsius):
    return (celsius * 9.0/5.0) + 32

def read_light_intensity():
    # Read and normalize light intensity
    raw_value = adc_lux.read()
    actual_max_adc_value = 8191
    percentage = (raw_value / actual_max_adc_value) * 100
    return max(0, min(percentage, 100))

# Main loop
use_fahrenheit = False
last_value_button_state = 1
last_temperature_button_state = 1
debounce_time_ms = 200

auto_update_interval = 5  # Auto-update every 5 seconds

last_auto_update_time = time.time()

while True:
    current_time = time.time()

    # Handle manual update with value button
    current_value_button_state = value_button.value()
    if current_value_button_state == 0 and last_value_button_state == 1:
        time.sleep_ms(debounce_time_ms)
        if value_button.value() == 0:  # Double check after debounce
            # Readings from BME280
            temp, pressure, humidity = bme.read_compensated_data()
            pressure = pressure / 100  # Convert to hPa
            if temp is not None:  # Check for valid temperature reading
                light = read_light_intensity()
                update_display(temp, light, humidity, pressure, use_fahrenheit)
                update_leds(temp)
            last_auto_update_time = current_time  # Reset auto-update timer

    # Handle temperature unit change
    current_temperature_button_state = temperature_button.value()
    if current_temperature_button_state != last_temperature_button_state:
        time.sleep_ms(debounce_time_ms)  # Debouncing
        # Check if button state is still the same after debounce
        if temperature_button.value() == 0:
            use_fahrenheit = not use_fahrenheit  # Toggle the temperature unit
            print("Toggled Fahrenheit:", use_fahrenheit)  # Debug output

            # Force an immediate update to display with new unit
            temp, pressure, humidity = bme.read_compensated_data()
            pressure = pressure / 100  # Convert to hPa
            light = read_light_intensity()
            update_display(temp, light, humidity, pressure, use_fahrenheit)
            update_leds(temp)
            last_auto_update_time = current_time  # Reset auto-update timer

    last_temperature_button_state = current_temperature_button_state

    # Auto-update the display at set intervals
    if current_time - last_auto_update_time > auto_update_interval:
        # Readings from BME280
        temp, pressure, humidity = bme.read_compensated_data()
        pressure = pressure / 100  # Convert to hPa
        if temp is not None:  # Check for valid temperature reading
            light = read_light_intensity()
            update_display(temp, light, humidity, pressure, use_fahrenheit)
            update_leds(temp)
        last_auto_update_time = current_time  # Reset auto-update timer

    last_value_button_state = current_value_button_state
    last_temperature_button_state = current_temperature_button_state

    time.sleep(0.1)
