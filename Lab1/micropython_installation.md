Installing MicroPython on AI-Thinker NodeMCU ESP32-S2
=====================================================

## 1. Erasing and Flashing the firmware of NodeMCU ESP32-S2

1. Install **esptool.py:** 
    - `python3 -m pip install esptool`
    - If you have more than one python installation on your computer, you may need to specify to which python you'd like to install the esptool, e.g: `python3.12 -m pip install esptool`
2. Connect the board to your computer and check which port it is connected to.
    - For linux : `ls /dev/tty*` would show which port.
3. On your terminal run: 
    - `esptool.py --chip esp32s2 --port /dev/ttyUSB0 erase_flash` - port ttyUSB0 port might be different in yours.
4. Go to [Micropython's website](https://micropython.org/download/ESP32_GENERIC_S2/) and and download the [latest firmware (.bin)](https://micropython.org/resources/firmware/ESP32_GENERIC_S2-20240222-v1.22.2.bin) for your board
5. On your terminal change directory to the directory where you have the downloaded .bin file. and run:
    - `esptool.py --chip esp32s2 --port /dev/ttyUSB0 write_flash -z 0x1000 ESP32_GENERIC_S2-20240222-v1.22.2.bin`
    - Change the command above the parts /dev/ttyUSB0 with the port your device is connected, and ESP32_GENERIC_S2-20240222-v1.22.2.bin accordingly with what you downloaded.

## 2. Installing Pymakr extension

1. On VSCode extensions tab, search for [Pymakr](https://marketplace.visualstudio.com/items?itemName=pycom.Pymakr) and install it.
2. On the activity bar, click on the pymakr.
3. In the devices section, you should see the port name and icons of terminal, open device, connect and ... By pressing the connect button, you should establish a connection betwen your board and your computer via VSCode.

## 3. Using Micropython and Pymakr

1. Write the python code that you want to test on the board and save it.
    - Here is a [quick reference](https://docs.micropython.org/en/latest/esp32/quickref.html) for ESP32
2. On the far right end side of the tab bar, there is `...`more actions button, you will see the `pymakr` and after clicking it,  `upload to device` option.
3. After uploading the code to the board, start micropython terminal. `activity bar --> pymakr --> create terminal`
4. To see what files are there in the board you should:
    - `import os`
    - `os.listdir()`
5. To run the code you uploaded to the board:
    - `import your_fancy_script.py`
6. To delete the script from the board:
    - `os.remove("file_name")`
