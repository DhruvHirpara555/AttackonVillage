

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
        tmp += "King's Health:"
        if(self.game.leadisalive):
            for i in range(int(self.game.troops[0].health/self.game.troops[0].maxhealth*10)):
                tmp += '|'
            for i in range(10-int(self.game.troops[0].health/self.game.troops[0].maxhealth*10)):
                tmp += ' '
        else:
            tmp += '          '

        # tmp += "Barb not spawned: {}".format(self.game.barbcount-self.game.barbspawned)
        tmp += " Lead : {}".format(self.game.lead)
        tmp += " Heal remaining: {}".format(self.game.healspellcount)
        tmp += " Rage remaining: {}".format(self.game.ragecount)
        tmp += "\n Barbs remaining: {}".format(self.game.barbcount - self.game.barbspawned)
        tmp += "\n Archers remaining: {}".format(self.game.archcount - self.game.archspawned)
        tmp += "\n Balloons remaining: {}".format(self.game.looncount - self.game.loonspawned)


        if(self.game.barbcount-self.game.barbspawned <10):
            tmp += " "
        self.game.screens_replay.append(tmp)


        sys.stdout.write(tmp)

