from buildings import Buildings

import numpy as np
from colorama import Fore, Back, Style


class Cannons(Buildings):
    def __init__(self,x,y,game):
        size_x = 1
        size_y = 2
        matrix = np.array([['C' for x in range(size_x)] for y in range(size_y)],dtype=object)
        maxhealth = 1000
        self.attack = 50
        super().__init__(x,y,size_x,size_y,matrix,game,maxhealth)

    # attack nearest troop in 7-tile range
    def attack_troop(self):
        mindistobject = None
        mindist = 7
        for troop in self.game.troops:
            if mindistobject is None:
                mindistobject = troop
            else:
                if self.distance(troop) < mindist:
                    mindistobject = troop
                    mindist = self.distance(troop)
        if mindistobject is not None:
            mindistobject.health -= self.attack
            if mindistobject.health <= 0:
                self.game.troops = np.delete(self.game.troops,self.game.troops.index(troop))
                self.game.objects = np.delete(self.game.objects,self.game.objects.index(troop))
                del troop
                mindistobject = None
        return mindistobject




    def delete_building(self):
        self.game.cannons = np.delete(self.game.cannons,self.game.cannons.index(self))
        self.game.objects = np.delete(self.game.objects,self.game.objects.index(self))
        self.game.buildings = np.delete(self.game.buildings,self.game.buildings.index(self))
        del self