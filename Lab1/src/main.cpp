/*
File      :   main.cpp
Time      :   22.02.2024 23:55:59
Compile   :   g++ -ansi -pedantic -Wall -Wextra -Weffc++ main.cpp -o main
Version   :   1.0
Author(s) :   Uras Ayanoglu
Contact   :   uras.ayanoglu@edu.turkuamk.fi
Desc      :   A basic example of how to use the Arduino framework to blink the built-in LED on the NodeMCU ESP32-S2. 
              Another led is attached to the same pin as the built-in LED, so it will also blink.
*/

#include <Arduino.h>

#define LED_BUILTIN 2 

void setup() {
  // Initialize the LED pin as an output
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, LOW);
}

void loop() {
  // Turn the LED on
  digitalWrite(LED_BUILTIN, HIGH);

  // Wait for a second
  delay(1000);

  // Turn the LED off
  digitalWrite(LED_BUILTIN, LOW);

  // Wait for a second
  delay(1000);
}