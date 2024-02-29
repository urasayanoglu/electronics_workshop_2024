/*
File      :   main.cpp
Time      :   25.02.2024 17:10:04
Compile   :   g++ -ansi -pedantic -Wall -Wextra -Weffc++ main.cpp -o main
Version   :   1.0
Author(s) :   Uras Ayanoglu
Contact   :   uras.ayanoglu@edu.turkuamk.fi
Desc      :   A simple Morse code generator with a tactile push switch, and a led  using NodeMCU ESP32-S2.

*/

#include <Arduino.h>

#define LED_BUILTIN 2
#define BUTTON_PIN 3

unsigned long buttonPressTime = 0;
unsigned long buttonReleaseTime = 0;
unsigned long pressDuration = 0;

const unsigned long dotDuration = 200; // Duration in milliseconds for a dot
const unsigned long dashDuration = 600; // Duration in milliseconds for a dash

void setup() {
    pinMode(LED_BUILTIN, OUTPUT);
    digitalWrite(LED_BUILTIN, LOW);

    pinMode(BUTTON_PIN, INPUT); // Set the button pin as input
}

void loop() {
    int buttonState = digitalRead(BUTTON_PIN);

    // Check if the button is pressed
    if (buttonState == LOW) {
        if (buttonPressTime == 0) {
            // Record the time when the button is first pressed
            buttonPressTime = millis();
        }
        digitalWrite(LED_BUILTIN, HIGH);
    } else if (buttonPressTime != 0) {
        // Record the time when the button is released
        buttonReleaseTime = millis();

        // Calculate the duration of the press
        pressDuration = buttonReleaseTime - buttonPressTime;

        // Reset the press time
        buttonPressTime = 0;

        // Determine if it was a dot or a dash
        if (pressDuration < dotDuration) {
            // Short press: dot
            Serial.println(".");
        } else if (pressDuration >= dotDuration && pressDuration <= dashDuration) {
            // Long press: dash
            Serial.println("-");
        }

        digitalWrite(LED_BUILTIN, LOW);

        // Add a small delay to debounce the switch
        delay(50);
    }
}
