
from troops.troops import Troops
import time
import sys
from colorama import Fore, Back, Style
import numpy as np

class Barbarian(Troops):

    def __init__(self, x, y, game, damage, attack_speed, attack_range):
        size_x = 1
        size_y = 1
        matrix = np.array([['B' for x in range(size_x)] for y in range(size_y)], dtype=object)
        maxhealth = 100
        self.last_moved = time.time()
        self.movespeed = 10

        super().__init__(x, y, size_x, size_y, matrix, game, maxhealth, damage, attack_speed, attack_range)



    def getnextblock(self):
        mindistanceobj = None
        mindistance = -1
        for obj in self.game.buildings :
            objdistance = abs(obj.pos_x-self.pos_x) + abs(obj.pos_y-self.pos_y)
            if mindistanceobj == None:
                mindistance = objdistance
                mindistanceobj = obj
            else:
                if(objdistance < mindistance):
                    mindistance = objdistance
                    mindistanceobj = obj

        next_x = 0 if (mindistanceobj.pos_x-self.pos_x)==0 else abs(mindistanceobj.pos_x-self.pos_x)/(mindistanceobj.pos_x-self.pos_x)
        next_y = 0 if (mindistanceobj.pos_y - self.pos_y)==0 else abs(mindistanceobj.pos_y - self.pos_y)/(mindistanceobj.pos_y - self.pos_y)

        if(abs(mindistanceobj.pos_x-self.pos_x) > abs(mindistanceobj.pos_y - self.pos_y)):
            return(self.pos_x + next_x,self.pos_y)
        else :
            return(self.pos_x,self.pos_y+next_y)

    def movebarb(self):
        x,y = self.getnextblock()

        if(self.game.frame.screen[int(y)][int(x)] == Back.WHITE+' '+Back.RESET or self.game.frame.screen[int(y)][int(x)] == self.color + Back.BLACK + 'B' + Fore.RESET + Back.RESET):

                self.pos_x = x
                self.pos_y = y


    # def coll_check(self):

    #     # find the object present at next coordinates
    #     if ():
    #         return True
    #     else:
    #         return False

    def attack_melee(self):
        coordinates = self.getnextblock()
        next_x = coordinates[0]
        next_y = coordinates[1]
        # attackedflag= self.game.frame.screen[next_y][next_x] != Back.WHITE+' '+Back.RESET
        # print(attackedflag)
        # if(attackedflag):
        attackedobj = None
        # print(self.game.buildings)
        # print()
        for obj in self.game.buildings :
            # print(obj)
            for y in range(obj.size_y):
                for x in range(obj.size_x):
                    # print(y+obj.pos_y,next_y,x+obj.pos_x,next_x,file=sys.stderr)
                    if(int(y+obj.pos_y) == int(next_y) and int(x + obj.pos_x) == int(next_x)):
                        attackedobj = obj

                        break
                if(int(y+obj.pos_y) == int(next_y) and int(x + obj.pos_x) == int(next_x)):
                        break





        for obj in self.game.walls:
            if(obj.pos_x == next_x and obj.pos_y == next_y):
                attackedobj =  obj
        # print(attackedobj,file=sys.stderr)
        if(attackedobj != None):
            attackedobj.health -= self.damage
            attackedobj.curr_status()
            self.color = Fore.WHITE
            self.last_attacked = time.time()



