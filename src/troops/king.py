from src.troops.troops import Troops

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
        self.attack_range = attack_range
        self.last_input = ''
        self.troop_type = "ground"
        self.last_input = ''

        super().__init__(x, y, size_x, size_y, matrix, game, maxhealth, damage, attack_speed)


    def curr_status(self):
        if(self.health/self.maxhealth > 0.5):
            self.color = Fore.RED
        elif(self.health/self.maxhealth > 0.2):
            self.color = Fore.CYAN
        elif(self.health/self.maxhealth > 0):
            self.color = Fore.YELLOW
        else:
            self.game.leadisalive = False
            self.delete_troops()


    def attack(self):
        if(self.last_input == ''):
            return False
        if(self.last_input == 'w'):
            for building in self.game.buildings:
                for x in range(building.size_x):
                    for y in range(building.size_y):
                        if(building.pos_x+x == self.pos_x and building.pos_y+y == self.pos_y - 1):
                            building.health -= self.damage
                            self.last_attacked = time.time()
                            self.color = Fore.WHITE
                            building.curr_status()
                            break
                    if(building.pos_x+x == self.pos_x and building.pos_y+y == self.pos_y - 1):
                        break

            for wall in self.game.walls:
                if wall.pos_x == self.pos_x and wall.pos_y == self.pos_y - 1:
                    wall.health -= self.damage
                    self.last_attacked = time.time()
                    self.color = Fore.WHITE
                    wall.curr_status()
                    break
        elif(self.last_input == 's'):
            for building in self.game.buildings:
                for x in range(building.size_x):
                    for y in range(building.size_y):
                        if(building.pos_x+x == self.pos_x and building.pos_y+y == self.pos_y + 1):
                            building.health -= self.damage
                            self.last_attacked = time.time()
                            self.color = Fore.WHITE
                            building.curr_status()
                            break
                    if(building.pos_x+x == self.pos_x and building.pos_y+y == self.pos_y + 1):
                        break

            for wall in self.game.walls:
                if wall.pos_x == self.pos_x and wall.pos_y == self.pos_y + 1:
                    wall.health -= self.damage
                    self.last_attacked = time.time()
                    self.color = Fore.WHITE
                    wall.curr_status()
                    break
        elif(self.last_input == 'a'):
            for building in self.game.buildings:
                for x in range(building.size_x):
                    for y in range(building.size_y):
                        if(building.pos_x+x == self.pos_x - 1 and building.pos_y+y == self.pos_y):
                            building.health -= self.damage
                            self.last_attacked = time.time()
                            self.color = Fore.WHITE
                            building.curr_status()
                            break
                    if(building.pos_x+x == self.pos_x - 1 and building.pos_y+y == self.pos_y):
                        break

            for wall in self.game.walls:
                if wall.pos_x == self.pos_x - 1 and wall.pos_y == self.pos_y:
                    wall.health -= self.damage
                    self.last_attacked = time.time()
                    self.color = Fore.WHITE
                    wall.curr_status()
                    break
        elif(self.last_input == 'd'):
            for building in self.game.buildings:
                for x in range(building.size_x):
                    for y in range(building.size_y):
                        if(building.pos_x+x == self.pos_x + 1 and building.pos_y+y == self.pos_y):
                            building.health -= self.damage
                            self.last_attacked = time.time()
                            self.color = Fore.WHITE
                            building.curr_status()
                            break
                    if(building.pos_x+x == self.pos_x + 1 and building.pos_y+y == self.pos_y):
                        break

            for wall in self.game.walls:
                if wall.pos_x == self.pos_x + 1 and wall.pos_y == self.pos_y:
                    wall.health -= self.damage
                    self.last_attacked = time.time()
                    self.color = Fore.WHITE
                    wall.curr_status()
                    break

    def attack_leva(self):
        objecttoattack = []
        for obj in self.game.buildings:
            if(self.buildingonattackfeild(obj)):
                objecttoattack.append(obj)
        for obj in self.game.walls:
            if(self.buildingonattackfeild(obj)):
                objecttoattack.append(obj)
        for obj in objecttoattack:
            obj.health -= self.damage
            self.last_attacked = time.time()
            self.color = Fore.WHITE
            obj.curr_status()