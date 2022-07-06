from src.troops.troops import Troops

from colorama import Fore, Back, Style
import numpy as np
import time

class Queen(Troops):
    def __init__(self, x, y, game, damage, attack_speed, attack_range):
        size_x = 1
        size_y = 1
        matrix = np.array([['Q' for x in range(size_x)] for y in range(size_y)], dtype=object)
        maxhealth = 500.0
        self.last_moved = time.time()
        self.movespeed = 20
        self.last_moved = time.time()
        self.attack_range = attack_range
        self.last_input = ''
        self.attackpos = 8
        self.troop_type = "ground"
        self.AoE = 2
        self.last_special = time.time()

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

    def buildingonattackfeild(self, building):
        if(self.last_input == ''):
            return False
        if(self.last_input == 'w'):
            for y in range(building.size_x):
                for x in range(building.size_y):
                    if(abs(building.pos_x+x - self.pos_x)) <= self.AoE  and abs (building.pos_y+y - self.pos_y + self.attackpos) <= self.AoE:
                        return True
        elif(self.last_input == 's'):
            for y in range(building.size_x):
                for x in range(building.size_y):
                    if(abs(building.pos_x+x - self.pos_x))<= self.AoE and abs (building.pos_y+y - self.pos_y - self.attackpos) <= self.AoE:
                        return True
        elif(self.last_input == 'a'):
            for y in range(building.size_x):
                for x in range(building.size_y):
                    if(abs(building.pos_x+x - self.pos_x + self.attackpos)) <= self.AoE and abs (building.pos_y+y - self.pos_y) <= self.AoE:
                        return True
        elif(self.last_input == 'd'):
            for y in range(building.size_x):
                for x in range(building.size_y):
                    if(abs(building.pos_x+x - self.pos_x - self.attackpos)) <= self.AoE and abs (building.pos_y+y - self.pos_y) <= self.AoE:
                        return True
        return False

    def attack(self):
        objecttoattack = []
        for obj in self.game.buildings:
            if(self.buildingonattackfeild(obj)):
                objecttoattack.append(obj)
        for obj in self.game.walls:
            if(self.buildingonattackfeild(obj)):
                objecttoattack.append(obj)
        for obj in objecttoattack:
            # print(type(obj))
            obj.health -= self.damage
            self.last_attacked = time.time()
            self.color = Fore.WHITE
            obj.curr_status()

    def special_attack(self):
        objecttoattack = []
        self.attackpos = 16
        self.AoE = 4

        for obj in self.game.buildings:
            if(self.buildingonattackfeild(obj)):
                objecttoattack.append(obj)
        for obj in self.game.walls:
            if(self.buildingonattackfeild(obj)):
                objecttoattack.append(obj)
        for obj in objecttoattack:
            # print(type(obj))
            obj.health -= self.damage
            self.last_attacked = time.time()
            obj.curr_status()

        self.attackpos = 8
        self.AoE = 2

