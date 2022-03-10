from curses import KEY_SAVE
import imp
from screen import Screen
import sys
from input import *
import time
class Game:

    kbin = Get()

    def __init__(self):

        self.frame = Screen(80,25)
        self.frame_rate = 1/24
        self.last_frame = time.time()




    def play(self):
        while True:

            key_stroke = input_to(self.kbin)

            if(key_stroke != None):
                ''' some key is pressed '''
                if(key_stroke == 'q'):
                    break

            if(time.time() - self.last_frame > self.frame_rate):
                self.frame.clear()
                self.frame.prt()
                self.frame.blank()
                self.last_frame = time.time()

