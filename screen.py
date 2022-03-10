

# store all screens that are printed in game_data
import os
from colorama import Fore, Back, Style
import numpy as np
import sys

class Screen:




    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = np.array([[Back.GREEN+' '+Back.RESET  for x in range(self.width)] for y in range(self.height)],dtype=object)
        self.clear()


    def blank(self):
        self.screen =np.array( [[Back.GREEN+' '+ Back.RESET  for x in range(self.width)] for y in range(self.height)],dtype=object)
    #cleat terminal for next frame to render
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    def draw(self, x, y, char):
        self.screen[y][x] = char
    def moveC (self,y, x):
        print("\033[%d;%dH" % (y, x))

    def prt(self):
        tmp = ''

        for y in range(self.height):
            for x in range(self.width):
                tmp += self.screen[y][x]
            tmp += '\n'

        sys.stdout.write(tmp)

