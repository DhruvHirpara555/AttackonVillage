from buildings import Buildings
from colorama import Fore, Back, Style
import numpy as np


class Walls(Buildings):
    def __init__(self,x,y,game) :
        matrix = np.array([['W' for x in range(size_x)] for y in range(size_y)],dtype=object)
        size_x = 1
        size_y = 1
        maxhealth = 50
        color = Fore.GREEN
        super().__init__(x,y,size_x,size_y,matrix,game,maxhealth,color)

    def delete_building(self):
        self.game.walls = np.delete(self.game.walls,self.game.walls.index(self))
        self.game.objects = np.delete(self.game.objects,self.game.objects.index(self))
        self.game.buildings = np.delete(self.game.buildings,self.game.buildings.index(self))
        del self


