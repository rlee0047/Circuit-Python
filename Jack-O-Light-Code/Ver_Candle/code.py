"""Jack-o'-Lantern flame example Adafruit M0 Feather with NeoPixel strip"""

from math import pow
from random import randint
import board
import neopixel

# Number of NeoPixels
NUMPIX = 7   

# Pin where NeoPixels are connected
PIXPIN = board.D12  

#Change order if output color is incorrect; i.e. RGB, RGBW, GRBW, GRB
STRIP = neopixel.NeoPixel(PIXPIN, NUMPIX, brightness=5.0, pixel_order=neopixel.GRBW) 

PREV = 128

#Lower the number the more wispy of the light
InitOffset = 12

#Random Start and End
ranSt = 40
ranEd = 191

def split(first, second, offset):

    if offset != 0:
        mid = ((first + second + 1) / 2 + randint(-offset, offset))
        offset = int(offset / 2)
        split(first, mid, offset)
        split(mid, second, offset)
    else:
        level = pow(first / 255.0, 2.7) * 255.0 + 0.5
        STRIP.fill((int(level/.7), int(level / .8), int(level / 20)))
        STRIP.write()


while True:  # Loop forever...
    LVL = randint(ranSt, ranEd)
    split(PREV, LVL, InitOffset)
    PREV = LVL
