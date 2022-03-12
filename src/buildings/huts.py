from src.buildings.buildings import Buildings
from colorama import Fore, Back, Style
import numpy as np


class Huts(Buildings):

    def __init__(self,x,y,game):
        size_x = 2
        size_y = 2
        matrix = np.array([['H' for x in range(size_x)] for y in range(size_y)],dtype=object)
        maxhealth = 1000

        super().__init__(x,y,size_x,size_y,matrix,game,maxhealth)
