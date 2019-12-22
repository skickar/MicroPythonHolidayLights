## TIM CODE
## Rainbow Racers, new colors every single pixel
## Add a button to make it go each time you press it

import machine
from machine import Pin 
import neopixel, random, math, time, utime
np = neopixel.NeoPixel(machine.Pin(2), 10)

## Set up a button on pin 14, or D5 on the D1 Mini board.

button = Pin(14, Pin.IN, Pin.PULL_UP)

## Set the delay between animations (lower value increases speed)

delayTime = 100

## Create a random function to make pretty random colors
def randint(lower, upper):
    gap = upper - lower
    if gap == 0:
        return lower
    return (random.getrandbits(int(math.log(gap, 2)))% gap) + lower


## Create a function to get BRIGHT random colors instead of pastels 
def BrightColors():
    x = randint(0, 100)
    colors = [0, int(255*math.cos(x)), int(255*math.sin(x))]
    r = colors.pop(randint(0, len(colors)))
    g = colors.pop(randint(0, len(colors)))
    b = colors.pop()
    return (r, g, b)

## A function to wipe/erase the pixels in the strip

def ErasePixels():
    for i in range(0,10):
        np[i] = (0,0,0)
        np.write()
        
## Make an animation that sweeps to the left
        
def LeftSweep(startAnimation):
    if startAnimation == True:
        for i in range(10):
            ErasePixels()
            racerColor = BrightColors()
            np[(9 - i)] = racerColor
            np.write()
            utime.sleep_ms(delayTime)
            
## Make an animation that sweeps to the right
        
def RightSweep(startAnimation):
    if startAnimation == True:
        for i in range(10):
            ErasePixels()
            racerColor = BrightColors()
            np[i] = racerColor
            np.write()
            utime.sleep_ms(delayTime)
            
## Make an animation that sweeps both from left to right at the same time

def CrossSweep(startAnimation):
    if startAnimation == True:
        for i in range(10):
            ErasePixels()
            racerColor = BrightColors()
            np[(9 - i)] = racerColor
            np[(8 - i)] = racerColor
            np[i] = racerColor
            if i < 9:
                np[i + 1] = racerColor
            np.write()
            utime.sleep_ms(delayTime)
            
## A function to check the value of our push button
            
def CheckButton():
    if button.value() == 0:
        if not startAnimation:
            startAnimation = True
            time.sleep(.5)
        else: 
            startAnimation = False
            time.sleep(.5)
    return startAnimation

## Set our animation to off by default
        
startAnimation = False

## Main loop, if button is pressed, then flip the value from False to True, or from True to False. 
while True:
    if button.value() == 0:
        if not startAnimation:
            startAnimation = True
            time.sleep(.5)
        else: 
            startAnimation = False
            time.sleep(.5)
            
## Now, if the value is true, we play the animations. If it's false, we erase the pixels.
               
    if startAnimation:
        LeftSweep(startAnimation)
        RightSweep(startAnimation)
        CrossSweep(startAnimation)
    else: ErasePixels()

