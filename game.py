

from buildings.buildings import *
from buildings.townhall import Townhall
from buildings.huts import Huts
from buildings.walls import Walls

from screen import Screen
import sys
from input import *
import time
from objects_game import Object_Game
from colorama import Fore, Back, Style

class Game:

    kbin = Get()

    def __init__(self):

        self.frame = Screen(160,50)
        self.frame_rate = 1/60
        self.last_frame = time.time()
        self.objects = []
        self.townhall = []
        self.buildings = []
        self.walls = []
        self.barbarian = []
        self.king = []
        self.cannons = []

        self.gen_townhall()

        self.gen_huts()

        self.gen_walls()



    def gen_townhall(self):
        self.townhall.append(Townhall(80,24,self))
        self.objects.append(self.townhall[0])
        self.buildings.append(self.townhall[0])

    def gen_huts(self) :
        x_arr = [20,30,80,120, 120]
        y_arr = [32, 20, 34, 24, 20 ]
        for i in range(5):
            self.buildings.append(Huts(x_arr[i],y_arr[i],self))
            self.objects.append(self.buildings[len(self.buildings)-1])

    def gen_walls(self) :
        for x in (10,130):
            for y in range(11,40):
                self.walls.append(Walls(x,y,self))
                self.objects.append(self.walls[len(self.walls)-1])

        for y in (10,40):
            for x in range(11,130):
                self.walls.append(Walls(x,y,self))
                self.objects.append(self.walls[len(self.walls)-1])

        for x in (10,130):
            for y in (10,40):
                self.walls.append(Walls(x,y,self))
                self.objects.append(self.walls[len(self.walls)-1])








    def play(self):

        while True:


            key_stroke = input_to(self.kbin)

            if(key_stroke != None):
                ''' some key is pressed '''
                if(key_stroke == 'q'):
                    break
                if(key_stroke == 'w' and self.king[0].pos_y > 0 and self.king[0].check()):
                    self.king[0].pos_y -= 1
                if(key_stroke == 's' and self.king[0].pos_y < self.frame.height - self.king[0].size_y and self.king[0].check()):
                    self.king[0].pos_y += 1
                if(key_stroke == 'a' and self.king[0].pos_x > 0 and self.king[0].check()):
                    self.king[0].pos_x -= 1
                if(key_stroke == 'd' and self.king[0].pos_x < self.frame.width - self.king[0].size_x and self.king[0].check()):
                    self.king[0].pos_x += 1
            for obj in self.objects:
                self.frame.draw_object(obj)

            if(time.time() - self.last_frame > self.frame_rate):
                self.frame.clear()
                self.frame.prt()
                self.frame.blank()
                self.last_frame = time.time()
                # print(self.objects)

