

# store all screens that are printed in game_data
import os
from colorama import Fore, Back, Style
import numpy as np
import sys

class Screen:




    def __init__(self, width, height,game):
        self.width = width
        self.height = height
        self.game = game
        self.screen = np.array([[Back.WHITE+' '+Back.RESET  for x in range(self.width)] for y in range(self.height)],dtype=object)
        self.clear()


    def blank(self):
        self.screen =np.array( [[Back.WHITE+' '+ Back.RESET  for x in range(self.width)] for y in range(self.height)],dtype=object)

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    def draw_object(self, Object):
        for y in range(Object.size_y):
            for x in range(Object.size_x):
                self.screen[int(y+Object.pos_y)][int(x+Object.pos_x)] = Object.color + Back.BLACK + Object.matrix[y][x] + Fore.RESET + Back.RESET
    def moveC (self,y, x):
        print("\033[%d;%dH" % (y, x))

    def prt(self):
        tmp = ''

        for y in range(self.height):
            for x in range(self.width):
                tmp += self.screen[y][x]
            tmp += '\n'
        tmp += "King's Health: "
        if(self.game.kingisalive):
            for i in range(int(self.game.troops[0].health/self.game.troops[0].maxhealth*10)):
                tmp += '|'
            for i in range(10-int(self.game.troops[0].health/self.game.troops[0].maxhealth*10)):
                tmp += ' '


        sys.stdout.write(tmp)

