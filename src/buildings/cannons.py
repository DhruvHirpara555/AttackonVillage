from src.buildings.buildings import Buildings
import time
import numpy as np
from colorama import Fore, Back, Style


class Cannons(Buildings):
    def __init__(self,x,y,game):
        size_x = 1
        size_y = 2
        matrix = np.array([['C' for x in range(size_x)] for y in range(size_y)],dtype=object)
        maxhealth = 500
        self.attack = 50
        self.attack_speed = 1
        self.last_attack = time.time()

        super().__init__(x,y,size_x,size_y,matrix,game,maxhealth)


    # attack nearest troop in 7-tile range
    def distance(self,troop):
        return abs(troop.pos_x-self.pos_x) + abs(troop.pos_y-self.pos_y)

    def attack_troop(self):
        mindistobject = None
        mindist = 7
        for troop in self.game.troops:
            if self.distance(troop) <= mindist:
                mindistobject = troop
                mindist = self.distance(troop)
        if mindistobject is not None:
            mindistobject.health -= self.attack
            self.last_attack = time.time()
            self.color = Fore.MAGENTA
            mindistobject.curr_status()
            if mindistobject.health <= 0:
                mindistobject = None
        return mindistobject




    def delete_building(self):
        self.game.cannons = np.delete(self.game.cannons,self.game.cannons.index(self)).tolist()
        self.game.objects = np.delete(self.game.objects,self.game.objects.index(self)).tolist()
        self.game.buildings = np.delete(self.game.buildings,self.game.buildings.index(self)).tolist()
        del self