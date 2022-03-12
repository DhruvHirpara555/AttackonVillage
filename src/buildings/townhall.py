
from src.buildings.buildings import *
import numpy as np
from colorama import Fore, Back, Style
class Townhall(Buildings):



    def __init__(self,x,y,game):
        size_x = 4
        size_y = 3
        maxhealth = int(1000)
        matrix = np.array([['T' for x in range(size_x)] for y in range(size_y)],dtype=object)



        super().__init__(x,y,size_x,size_y,matrix,game,maxhealth)

    def delete_building(self):
        self.game.townhall = np.delete(self.game.townhall,self.game.townhall.index(self)).tolist()
        self.game.objects = np.delete(self.game.objects,self.game.objects.index(self)).tolist()
        self.game.buildings = np.delete(self.game.buildings,self.game.buildings.index(self)).tolist()
        del self

