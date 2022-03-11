from buildings.buildings import Buildings
from colorama import Fore, Back, Style
import numpy as np


class Walls(Buildings):
    def __init__(self,x,y,game) :
        size_x = 1
        size_y = 1
        matrix = np.array([['@' for x in range(size_x)] for y in range(size_y)],dtype=object)
        maxhealth = 50
        super().__init__(x,y,size_x,size_y,matrix,game,maxhealth)

    def delete_building(self):
        self.game.walls = np.delete(self.game.walls,self.game.walls.index(self))
        self.game.objects = np.delete(self.game.objects,self.game.objects.index(self))
        del self


