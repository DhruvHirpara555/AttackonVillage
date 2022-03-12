
import time
from objects_game import Object_Game
from colorama import Fore, Back, Style
import numpy as np


class Troops(Object_Game):
    def __init__(self, x, y, size_x, size_y, matrix, game, maxhealth, damage, attack_speed,attack_range):
        super().__init__(x, y, size_x, size_y, matrix, game, maxhealth )
        self.damage = damage
        self.attack_speed = attack_speed
        self.last_attacked = time.time()
        self.color = Fore.RED
        self.attack_range = attack_range
        self.health = maxhealth


    def buildingonattackfeild(self,building):
        for y in range(building.size_x):
            for x in range(building.size_y):
                if(abs(building.pos_x+x-self.pos_x) +  abs(building.pos_y+y-self.pos_y) <= self.attack_range):
                    return True
        return False

    def curr_status(self):
        if(self.health/self.maxhealth > 0.5):
            self.color = Fore.RED
        elif(self.health/self.maxhealth > 0.2):
            self.color = Fore.CYAN
        elif(self.health/self.maxhealth > 0):
            self.color = Fore.YELLOW
        else:
            self.delete_troops()


    def attack_melee(self):
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




    def delete_troops(self):
        self.game.troops = np.delete(self.game.troops, self.game.troops.index(self)).tolist()
        self.game.objects = np.delete(self.game.objects, self.game.objects.index(self)).tolist()
        del self

    def moveleft(self):
        if(self.pos_x-1 >0 and self.game.frame.screen[self.pos_y][self.pos_x-1] == Back.WHITE+' '+Back.RESET):
            self.pos_x -= 1
    def moveright(self):
        if(self.pos_x+1 < self.game.frame.width and self.game.frame.screen[self.pos_y][self.pos_x+1] == Back.WHITE+' '+Back.RESET):
            self.pos_x += 1

    def moveup(self):
        if(self.pos_y-1 >0 and self.game.frame.screen[self.pos_y-1][self.pos_x]== Back.WHITE+' '+Back.RESET):
            self.pos_y -= 1

    def movedown(self):
        if(self.pos_y+1 < self.game.frame.height and self.game.frame.screen[self.pos_y+1][self.pos_x] == Back.WHITE+' '+Back.RESET):
            self.pos_y += 1


