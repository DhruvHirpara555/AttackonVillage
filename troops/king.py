from troops.troops import Troops

from colorama import Fore, Back, Style
import numpy as np
import time
class King(Troops):

    def __init__(self, x, y, game, damage, attack_speed, attack_range):
        size_x = 1
        size_y = 1
        matrix = np.array([['K' for x in range(size_x)] for y in range(size_y)], dtype=object)
        maxhealth = 500.0
        self.last_moved = time.time()
        self.movespeed = 20
        self.last_moved = time.time()

        super().__init__(x, y, size_x, size_y, matrix, game, maxhealth, damage, attack_speed, attack_range)


    def curr_status(self):
        if(self.health/self.maxhealth > 0.5):
            self.color = Fore.RED
        elif(self.health/self.maxhealth > 0.2):
            self.color = Fore.CYAN
        elif(self.health/self.maxhealth > 0):
            self.color = Fore.YELLOW
        else:
            self.game.kingisalive = False
            self.delete_troops()
