from src.troops.troops import Troops
import time
import sys
from colorama import Fore, Back, Style
import numpy as np


class Archers(Troops) :

    def __init__(self, x, y, game, damage, attack_speed, attack_range):
        size_x = 1
        size_y = 1
        matrix = np.array([['A' for x in range(size_x)] for y in range(size_y)], dtype=object)
        maxhealth = 50
        self.last_moved = time.time()
        self.movespeed = 20
        self.attack_range = attack_range
        self.last_attacked = time.time()
        self.troop_type = "ground"

        super().__init__(x, y, size_x, size_y, matrix, game, maxhealth, damage, attack_speed)


    # The archers move similarly to barbarians, they will find the nearest non-wall
# building and move to attack it. In case a wall appears in their path to the building, they are
# required to destroy the wall and proceed.
    def getnextblock(self):
        mindistanceobj = None
        mindistance = -1
        for obj in self.game.buildings:
            objdistance = abs(obj.pos_x - self.pos_x) + abs(obj.pos_y - self.pos_y)
            if mindistanceobj == None:
                mindistance = objdistance
                mindistanceobj = obj
            else:
                if (objdistance < mindistance):
                    mindistance = objdistance
                    mindistanceobj = obj

        if mindistanceobj != None:

            next_x = 0 if (mindistanceobj.pos_x - self.pos_x) == 0 else abs(mindistanceobj.pos_x - self.pos_x) / (mindistanceobj.pos_x - self.pos_x)
            next_y = 0 if (mindistanceobj.pos_y - self.pos_y) == 0 else abs(mindistanceobj.pos_y - self.pos_y) / (mindistanceobj.pos_y - self.pos_y)

            if (abs(mindistanceobj.pos_x - self.pos_x) > abs(mindistanceobj.pos_y - self.pos_y)):
                return (self.pos_x + next_x, self.pos_y,mindistanceobj)
            else:
                return (self.pos_x, self.pos_y + next_y,mindistanceobj)
        else:
            return (self.pos_x, self.pos_y,mindistanceobj)

    def movetroop(self):

        x,y,mindistanceobj = self.getnextblock()
        if mindistanceobj != None:

            distance = abs(mindistanceobj.pos_x - self.pos_x) + abs(mindistanceobj.pos_y - self.pos_y)
            # print(self.attack_range)
            # print(distance)
            if ((self.game.frame.screen[int(y)][int(x)] == Back.WHITE+' '+Back.RESET or self.game.frame.screen[int(y)][int(x)] == Fore.RED + Back.BLACK + 'B' + Fore.RESET + Back.RESET or self.game.frame.screen[int(y)][int(x)] == Fore.YELLOW + Back.BLACK + 'B' + Fore.RESET + Back.RESET or self.game.frame.screen[int(y)][int(x)] == Fore.CYAN + Back.BLACK + 'B' + Fore.RESET + Back.RESET  or self.game.frame.screen[int(y)][int(x)] == Fore.RED + Back.BLACK + 'A' + Fore.RESET + Back.RESET or self.game.frame.screen[int(y)][int(x)] == Fore.YELLOW + Back.BLACK + 'A' + Fore.RESET + Back.RESET or self.game.frame.screen[int(y)][int(x)] == Fore.CYAN + Back.BLACK + 'A' + Fore.RESET + Back.RESET) and distance > self.attack_range):

                self.pos_x = x
                self.pos_y = y
                self.last_moved = time.time()

    def attack(self):

        next_x,next_y,mindistanceobj = self.getnextblock()

        if mindistanceobj != None:
            distance = abs(mindistanceobj.pos_x - self.pos_x) + abs(mindistanceobj.pos_y - self.pos_y)

            for obj in self.game.walls:
                if(obj.pos_x == next_x and obj.pos_y == next_y):
                    obj.health -= self.damage
                    self.last_attacked = time.time()
                    self.color = Fore.WHITE
                    obj.curr_status()
                    return

            if distance <= self.attack_range:
                mindistanceobj.health -= self.damage
                self.last_attacked = time.time()
                self.color = Fore.WHITE
                mindistanceobj.curr_status()
                return











