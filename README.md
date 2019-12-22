# MicroPythonHolidayLights

MicroPython Lights

For this workshop, we'll be using:

An ESP8266, a mini breadboard, a 10 neopixel strip, wires, and a normally disconnected button

Using the button connected from pin D5 to ground, we can turn on the NeoPixel strip animation
The NeoPixel strip can be plugged into VCC or 5v for power, ground for ground, and D3 for signal (the middle pin)

Flash the boot.py to your board using Ampy with the command:

ampy --port SERIAL_PORT_OF_ESP8266 put PATH_TO/boot.py

Make sure to replace with the serial port of the ESP and the path to the boot.py file.
