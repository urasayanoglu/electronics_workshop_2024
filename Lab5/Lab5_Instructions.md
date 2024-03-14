AB 5 – Seven Segment Display 
============================

## Description:

Read https://www.hacktronics.com/Tutorials/arduino-and-7-segment-led.html 


The used seven segment display is not the same as in the previous link, but the working idea is the same. Read about the used seven segment display from the data sheet, MAN3920A.pdf. 

**TODO:**  
All the segments are LEDs and so you should use same resistance value (about 200 Ω) with all of the cathode pins (A, B, C, D, E, F and G). Anode is connected to +5 V at Arduino. Think over how you should drive the cathode pins so that LEDs shine at the seven segment display.  

### Part A: 

- Make circuit with seven segment display and resistors to the breadboard and connect it to the Arduino. 

- Make a program that blinks LED G and lights on LEDs in series from A to F in a continuous loop.  

### Part B (For basics of programming microcontrollers): 

- Make a program that shows numbers from 0 to 9 continuously in a loop (0, 1, …,, 9, 0, 1, …).  

### Part C (For programming microcontrollers) 

- Add tactile push switch to the circuit and make a program that works as described below: 
    - shows 0 until the tactile push switch is pressed. 

    - shows numbers from 0 to 9 continuously in a loop until the tactile push switch is pressed and shows 0 until the tactile push switch is pressed again (what???) 

### Extra mile:  

- Use a 4-digit 7-segment module for the above 

- https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/880/Grove_4_Digit_Display_Web.pdf 

- https://lastminuteengineers.com/tm1637-arduino-tutorial/ 