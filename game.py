

import os


from numpy import append, save
from src.buildings.buildings import *
from src.buildings.townhall import Townhall
from src.buildings.huts import Huts
from src.buildings.walls import Walls
from src.buildings.cannons import Cannons

from src.screen import Screen

from src.input import *
import time
from src.objects_game import Object_Game
from colorama import Fore, Back, Style
from src.troops.king import King
from src.troops.barbarian import Barbarian
import pickle as pkl

from src.troops.troops import Troops

class Game:

    kbin = Get()

    def __init__(self):

        self.frame = Screen(160,50,self)
        self.frame_rate = 1/60
        self.last_frame = time.time()
        self.objects = []
        self.townhall = []
        self.buildings = []
        self.walls = []
        self.troops = []
        self.cannons = []
        self.kingisalive = True
        self.spawningpoints_x = []
        self.spawningpoints_y = []
        self.barbcount = 15
        self.totalspawned = 0
        self.healspellcount = 2
        self.ragecount = 2
        self.ragemultiplier = 1
        self.last_rage = time.time()
        self.screens_replay = []

        self.gen_spawningpoints()

        self.gen_king()
        self.gen_townhall()

        self.gen_huts()

        self.gen_walls()

        self.gen_cannons()

    def gen_spawningpoints(self):
        self.spawningpoints_x.append(3)
        self.spawningpoints_y.append(3)
        self.spawningpoints_x.append(157)
        self.spawningpoints_y.append(3)
        self.spawningpoints_x.append(3)
        self.spawningpoints_y.append(47)
        self.spawningpoints_x.append(157)
        self.spawningpoints_y.append(47)

    def gen_king(self):
        self.troops.append(King(1,1,self,10,3,4))
        self.objects.append(self.troops[0])

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

    def gen_cannons(self):
        self.cannons.append(Cannons(90,24,self))
        self.objects.append(self.cannons[0])
        self.buildings.append(self.cannons[0])
        self.cannons.append(Cannons(13,15,self))
        self.objects.append(self.cannons[1])
        self.buildings.append(self.cannons[1])


    def genbarb(self,num):
        if(self.totalspawned < self.barbcount):
            self.troops.append(Barbarian(self.spawningpoints_x[num-1],self.spawningpoints_y[num-1],self,10,3,4))
            self.objects.append(self.troops[len(self.troops)-1])
            self.totalspawned +=1




    def isgameover(self):
        if(self.kingisalive == False and len(self.troops) == 0 and self.totalspawned == self.barbcount):
            os.system('clear')
            print("You Loose")
            return True


        if(len(self.buildings) == 0):
            os.system('clear')
            print("You Win")
            return True

        return False



    def play(self):

        while not self.isgameover():




            for obj in self.objects:
                self.frame.draw_object(obj)
            for i in range(4):
                self.frame.screen[self.spawningpoints_y[i]][self.spawningpoints_x[i]] = Back.CYAN + Fore.RED + 'X' + Back.RESET + Fore.RESET
                # print(self.frame.screen[self.spawningpoints_y[i]][self.spawningpoints_x[i]])
            key_stroke = input_to(self.kbin)

            if(key_stroke != None):
                ''' some key is pressed '''
                if(key_stroke == 'q'):
                    break
                if(key_stroke == 'w' and self.kingisalive):
                    if(time.time() - self.troops[0].last_moved > 1/(self.troops[0].movespeed*self.ragemultiplier)):
                        self.troops[0].moveup()
                        self.troops[0].last_moved = time.time()



                if(key_stroke == 's' and self.kingisalive):
                    if(time.time() - self.troops[0].last_moved > 1/(self.troops[0].movespeed*self.ragemultiplier)):
                        self.troops[0].movedown()
                        self.troops[0].last_moved = time.time()
                if(key_stroke == 'd' and self.kingisalive):
                     if(time.time() - self.troops[0].last_moved > 1/(self.troops[0].movespeed*self.ragemultiplier)):
                        self.troops[0].moveright()
                        self.troops[0].last_moved = time.time()
                if(key_stroke == 'a' and self.kingisalive):
                     if(time.time() - self.troops[0].last_moved > 1/(self.troops[0].movespeed*self.ragemultiplier)):
                        self.troops[0].moveleft()
                        self.troops[0].last_moved = time.time()
                if(key_stroke == ' ' and self.kingisalive):
                    if(time.time() - self.troops[0].last_attacked > 1/(self.troops[0].movespeed*self.ragemultiplier)):
                        self.troops[0].attack_melee()
                if(key_stroke == '1'):
                    self.genbarb(1)
                if(key_stroke == '2'):
                    self.genbarb(2)
                if(key_stroke == '3'):
                    self.genbarb(3)
                if(key_stroke == '4'):
                    self.genbarb(4)

                if(key_stroke == 'h'):
                    if(self.healspellcount > 0):
                        self.healspellcount-=1
                        for obj in self.troops:
                            obj.health = min(obj.health*(1.5) , obj.maxhealth)
                if(key_stroke == 'r'):
                    if(self.ragecount>0):
                        self.ragecount-=1
                        self.ragemultiplier = 2*self.ragemultiplier
                        self.last_rage = time.time()

            if(time.time() - self.last_rage > 4):
                self.ragemultiplier = max(1,self.ragemultiplier/2)


            for obj in self.cannons:

                if (time.time() - obj.last_attack > 1/obj.attack_speed):
                    attacked = obj.attack_troop()
                if(time.time()-obj.last_attack > 0.5/obj.attack_speed):
                    obj.curr_status()
                    # obj.last_attack = time.time()

            if(self.kingisalive):
                for i in range(1,len(self.troops)):
                    obj = self.troops[i]

                    if(time.time()- obj.last_moved > 1/(obj.movespeed * self.ragemultiplier)):
                        obj.movebarb()
                        obj.last_moved = time.time()

                    if(time.time()-obj.last_attacked > 1/ (obj.attack_speed * self.ragemultiplier)):
                        obj.attack_melee()
                    if(time.time()-obj.last_attacked > 0.5/ (obj.attack_speed * self.ragemultiplier)):
                        obj.curr_status()

                if(time.time() - self.troops[0].last_attacked > 0.5/(self.troops[0].attack_speed*self.ragemultiplier)):
                    self.troops[0].curr_status()
            elif(self.kingisalive == False and len(self.troops) > 0) :
                for obj in self.troops :


                    if(time.time()- obj.last_moved > 1/(obj.movespeed * self.ragemultiplier)):
                        obj.movebarb()
                        obj.last_moved = time.time()

                    if(time.time()-obj.last_attacked > 1/ (obj.attack_speed * self.ragemultiplier)):
                        obj.attack_melee()
                    if(time.time()-obj.last_attacked > 0.5/ (obj.attack_speed * self.ragemultiplier)):
                        obj.curr_status()








            if(time.time() - self.last_frame > self.frame_rate):
                # self.frame.clear()
                self.frame.moveC(0,0)
                self.frame.prt()
                # screens_replay.append(self.frame.screen)
                self.last_frame = time.time()
                self.frame.blank()
                # print(self.troops[0].last_attacked,time.time())
                # print(self.kingisalive)

        # save
        filename = input("Enter filename for replay to be saved in: ")
        file = open("./replay/"+filename, 'wb')
        pkl.dump(self.screens_replay, file)
        file.close()
        print("Replay saved!")




game = Game()

game.play()
