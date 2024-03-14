LAB 3 – PWM Controlled LED 
============================

## Description:

Read [Arduino Lesson 2 - LEDs](https://learn.adafruit.com/adafruit-arduino-lesson-2-leds) 

Read [Arduino Lesson 5 - Serial Monitor](https://learn.adafruit.com/adafruit-arduino-lesson-5-the-serial-monitor) 

Read [Arduino Lesson 6 - Push Switches](https://learn.adafruit.com/adafruit-arduino-lesson-6-digital-inputs/push-switches) 

Read [Arduino Lesson 6 - Digital Inputs](https://learn.adafruit.com/adafruit-arduino-lesson-6-digital-inputs) 

Read [Arduino Lesson 7 - Tactile Switch and LED](https://www.buildcircuit.com/arduino-project-7-button-tactile-switch-and-led/) 

Read [Arduino BuiltInExample Fade](https://www.arduino.cc/en/Tutorial/BuiltInExamples/Fade) 

  
## Part A: Rear lights of car 


- Many new cars have rear and brake light made with same LEDs. When the brake light is needed then LEDs are shining continuously. When the rear light is in use the LEDs are blinking with a frequency that make light seem continuous but with less intensity by the human eye.  

- Make circuit with LED and tactile push switch to the breadboard. **Remember** that LED always needs a series resistor (**resistance** about **300 Ω**). 

- It is recommendable to use about 10 kΩ resistor from the tactile push to the ground.  

- Use the tactile push as a brake pedal. 

- Connect the circuit to the Arduino and make a program that normally blinking the LED using delay() function with a suitable frequency and when the brake pedal (tactile push) is pressed the LED is shining continuously (with maximum intensity). 

- With Parts B and C pay attention to the reliability of the programming code and remember that intensity of the light can´t be negative or higher that at the situation where LED is shining continuously. 

## Part B (For basics of programming microcontrollers) 

- Make circuit with LED and series resistor on the  breadboard. Connect the circuit to the Arduino and make program that change linearly light intensity from the zero to the maximum and back continuously (you can use Fade). The program should ask first the length of one time period (limit the period between 1 s and 3 s) for time the light intensity change from the zero to the maximum.  

## Part C (For programming microcontrollers) 

- Make program that change linearly light intensity from the zero to the maximum and back continuously (you can use Fade). The program should ask first the length of one time period (limit the period between    1 s and 3 s) for time the light intensity change from the zero to the maximum. When the button is pressed  

- First time the intensity of light starts increasing from zero. 
- Next times the direction of the intensity change is opposite for the previous direction of change. 