from turtle import color
from buildings import Buildings
import numpy as np
from colorama import Fore, Back, Style
class Townhall(Buildings):



    def __init__(self,x,y,game):
        matrix = np.array([['T' for x in range(size_x)] for y in range(size_y)],dtype=object)
        size_x = 3
        size_y = 4
        maxhealth = 1000
        color = Fore.GREEN
        super().__init__(x,y,size_x,size_y,matrix,game,maxhealth,color)

    def delete_building(self):
        self.game.townhall = np.delete(self.game.townhall)
        self.game.objects = np.delete(self.game.objects,self.game.objects.index(self))
        self.game.buildings = np.delete(self.game.buildings,self.game.buildings.index(self))
        del self

