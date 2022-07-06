from requests import delete
from src.buildings.buildings import Buildings
import time
import numpy as np
from colorama import Fore, Back, Style


class Wizardtower(Buildings):
    def __init__(self,x,y,game):
        size_x = 1
        size_y = 2
        matrix = np.array([['W' for x in range(size_x)] for y in range(size_y)],dtype=object)
        maxhealth = 500
        self.attack = 50
        self.attack_speed = 1
        self.last_attack = time.time()
        self.AoE = 1

        super().__init__(x,y,size_x,size_y,matrix,game,maxhealth)


    # attack nearest troop in 7-tile range
    def distance(self,troop):
        return abs(troop.pos_x-self.pos_x) + abs(troop.pos_y-self.pos_y)

    def find_troop(self):
        mindistobject = None
        mindist = 7
        for troop in self.game.troops:
            if self.distance(troop) <= mindist:
                mindistobject = troop
                mindist = self.distance(troop)
        return mindistobject

    def trooponattackfeild(self,troop,mintroop):
        # for x in range(int(mintroop.pos_x)-self.AoE,int(mintroop.pos_x)+self.AoE+1):
        #     for y in range(int(mintroop.pos_y)-self.AoE,int(mintroop.pos_y)+self.AoE+1):
        #         if(troop.pos_x == x and troop.pos_y == y):
        #             return True
        if(abs(troop.pos_x-mintroop.pos_x) <= self.AoE and abs(troop.pos_y-mintroop.pos_y) <= self.AoE):
            return True
        return False




    def attack_troop(self):
        troopstoatack = []
        mintroop = self.find_troop()
        if mintroop is not None:
            for troop in self.game.troops:
                if(self.trooponattackfeild(troop,mintroop)):
                    troopstoatack.append(troop)
            for troop in troopstoatack:
                troop.health -= self.attack
                self.last_attack = time.time()
                self.color = Fore.MAGENTA
                troop.curr_status()

    def delete_building(self):
        self.game.wizardtower = np.delete(self.game.wizardtower,self.game.wizardtower.index(self)).tolist()
        self.game.objects = np.delete(self.game.objects,self.game.objects.index(self)).tolist()
        self.game.buildings = np.delete(self.game.buildings,self.game.buildings.index(self)).tolist()
        del self
