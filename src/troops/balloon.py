from src.troops.troops import Troops
import time
import sys
from colorama import Fore, Back, Style
import numpy as np



class Balloon(Troops):
    def __init__(self, x, y, game, damage, attack_speed):
        size_x = 1
        size_y = 1
        matrix = np.array([['R' for x in range(size_x)] for y in range(size_y)], dtype=object)
        maxhealth = 100
        self.last_moved = time.time()
        self.movespeed = 20
        self.troop_type = "air"

        super().__init__(x, y, size_x, size_y, matrix, game, maxhealth, damage, attack_speed)

    def getnextblock(self):
        mindistanceobj = None
        mindistance = -1

        if(len(self.game.cannons) > 0 or len(self.game.wizardtower)> 0):
            for obj in self.game.cannons:
                for y in range(obj.size_y):
                    for x in range (obj.size_x):
                        objdistance = abs(self.pos_x - x - obj.pos_x) + abs(self.pos_y - y - obj.pos_y)
                        if(objdistance < mindistance or mindistance == -1):
                            mindistance = objdistance
                            mindistanceobj = obj
            for obj in self.game.wizardtower:
                for y in range(obj.size_y):
                    for x in range (obj.size_x):
                        objdistance = abs(self.pos_x - x - obj.pos_x) + abs(self.pos_y - y - obj.pos_y)
                        if(objdistance < mindistance or mindistance == -1):
                            mindistance = objdistance
                            mindistanceobj = obj
        else:
            for obj in self.game.buildings:
                for y in range(obj.size_y):
                    for x in range(obj.size_x):
                        objdistance = abs(self.pos_x - x - obj.pos_x) + abs(self.pos_y - y - obj.pos_y)
                        if(objdistance < mindistance or mindistance == -1):
                            mindistance = objdistance
                            mindistanceobj = obj
        if mindistanceobj != None:
            next_x = 0 if (mindistanceobj.pos_x-self.pos_x)==0 else abs(mindistanceobj.pos_x-self.pos_x)/(mindistanceobj.pos_x-self.pos_x)
            next_y = 0 if (mindistanceobj.pos_y - self.pos_y)==0 else abs(mindistanceobj.pos_y - self.pos_y)/(mindistanceobj.pos_y - self.pos_y)

            if(abs(mindistanceobj.pos_x-self.pos_x) > abs(mindistanceobj.pos_y - self.pos_y)):
                return(self.pos_x + next_x,self.pos_y)
            else :
                return(self.pos_x,self.pos_y+next_y)
        else:
            return(self.pos_x,self.pos_y)


    def movetroop(self):

        x,y = self.getnextblock()

        self.pos_x = x
        self.pos_y = y
        self.last_moved = time.time()


    def attack(self):
        next_x,next_y = self.getnextblock()
        attackedobj = None

        if(len(self.game.cannons) > 0 or len(self.game.wizardtower)> 0):
            for obj in self.game.cannons:
                for y in range(obj.size_y):
                    for x in range (obj.size_x):
                        if(int(x+obj.pos_x) == int(next_x)  and int(y+obj.pos_y) == int(next_y)):
                            attackedobj = obj
                            break
                    if(int(x+obj.pos_x) == int(next_x)  and int(y+obj.pos_y) == int(next_y)):
                        break
            for obj in self.game.wizardtower:
                for y in range(obj.size_y):
                    for x in range (obj.size_x):
                        if(int(x+obj.pos_x) == int(next_x)  and int(y+obj.pos_y) == int(next_y)):
                            attackedobj = obj
                            break
                    if(int(x+obj.pos_x) == int(next_x)  and int(y+obj.pos_y) == int(next_y)):
                        break

        else:
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
        if attackedobj != None:
            attackedobj.health -= self.damage
            attackedobj.curr_status()
            self.color = Fore.WHITE
            self.last_attacked = time.time()






