
import imp
from screen import Screen
import sys
from input import *
import time
from objects_game import Object_Game
from colorama import Fore, Back, Style

class Game:

    kbin = Get()

    def __init__(self):

        self.frame = Screen(80,25)
        self.frame_rate = 1/60
        self.last_frame = time.time()
        self.objects = []
        self.townhall = []
        self.buildings = []
        self.barbarian = []
        self.king = []
        self.cannons = []



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

