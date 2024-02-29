/*
File      :   main.cpp
Time      :   24.02.2024 21:01:05
Compile   :   g++ -ansi -pedantic -Wall -Wextra -Weffc++ main.cpp -o main
Version   :   1.0
Author(s) :   Uras Ayanoglu
Contact   :   uras.ayanoglu@edu.turkuamk.fi
Desc      :   A simple continious distress signal example for AI-Thinker NodeMCU ESP32-S2
*/

#include <Arduino.h>

#define LED_BUILTIN 2

// Morse code timings in milliseconds
const int dot_length = 200;
const int dash_length = dot_length * 3;
const int inter_element_gap = dot_length;
const int inter_letter_gap = dot_length * 3;
const int inter_word_gap = dot_length * 7;

// Function prototypes
void dot();
void dash();
void distress_signal();

void setup() {
    // Initialize the LED pin as an output
    pinMode(LED_BUILTIN, OUTPUT);
    digitalWrite(LED_BUILTIN, LOW);
}

void loop() {
    // put your main code here, to run repeatedly:
    distress_signal();
}

// Function definitions
void dot() {
    digitalWrite(LED_BUILTIN, HIGH);
    delay(dot_length);
    digitalWrite(LED_BUILTIN, LOW);
    delay(inter_element_gap);
}

void dash() {
    digitalWrite(LED_BUILTIN, HIGH);
    delay(dash_length);
    digitalWrite(LED_BUILTIN, LOW);
    delay(inter_element_gap);
}

void distress_signal() {
    for (int i = 0; i < 3; i++) dot();
    for (int i = 0; i < 3; i++) dash();
    for (int i = 0; i < 3; i++) dot();
    delay(inter_word_gap);
}
