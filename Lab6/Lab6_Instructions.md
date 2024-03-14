LAB 6 – LCD Display 
===================

## Description:

First read about [lcd displays](https://learn.adafruit.com/adafruit-arduino-lesson-11-lcd-displays-1/overview)

Look also from YouTube with search: [How to Connect an I2C Lcd Display to an Arduino Uno Tutorial](https://www.youtube.com/results?search_query=How+to+Connect+an+I2C+Lcd+Display+to+an+Arduino+Uno+Tutorial) 

- [How to Connect I2C LCD Display to Arduino UNO](https://www.instructables.com/How-to-Connect-I2C-Lcd-Display-to-Arduino-Uno/)

- [I2C LCD Arduino Tutorial](https://www.makerguides.com/character-i2c-lcd-arduino-tutorial/)

Header pins should be already attached to the display, so you can skip the “soldering pins to the display” –part. 

**NOTE:** You only need to do either Part A or Part B, depending on which course you are attending! 

### Part A (For basics of programming microcontrollers) 

Using an LCD display, an NTC thermistor and a light-dependent resistor (LDR), build a device that shows the temperature and the light intensity reading on the display. The device should have either continuous update for values or a switch so that the readings are updated when the switch is pushed. There should also be a switch to change the temperature reading between Celsius and Fahrenheit. 

  

### Part B (For programming microcontrollers) 

Using an LCD display, an NTC thermistor and a light-dependent resistor (LDR), build a device that shows the temperature and the light intensity reading on the display. The device should have either continuous update for values or a switch so that the readings are updated when the switch is pushed. There should also be a switch to change the temperature reading between Celsius and Fahrenheit. 

The device should also have LEDs to indicate different temperature areas (e.g. blue for cold, yellow for medium, red for warm). You can determine the limits by yourself, but you should be able to test at least two areas. 

### Extra Mile

Use some external bus-connected (I2C) sensor to measure pressure / humidity / moisture etc. 

For example, you can use the following sensors:  

**BME280**  

- https://www.adafruit.com/product/2652 

- https://www.mouser.fi/datasheet/2/783/bst_bme280_ds002-2238172.pdf 

**BME688**  

- https://www.bosch-sensortec.com/products/environmental-sensors/gas-sensors/bme688/ 