from turtle import color
from numpy import delete
from objects_game import Object_Game
from colorama import Fore, Back, Style

class Buildings(Object_Game):
    def __init__(self,x,y,size_x,size_y,matrix,game,maxhealth):
        color = Fore.GREEN
        super().__init__(x,y,size_x,size_y,matrix,game,maxhealth,color)

    def delete_building(self):
        self.game.buildings = delete(self.game.buildings,self.game.buildings.index(self))
        self.game.objects = delete(self.game.objects,self.game.objects.index(self))
        del self

    def curr_status(self):
        if(self.health/self.maxhealth > 0.5):
            self.color = Fore.GREEN
        elif(self.health/self.maxhealth > 0.2):
            self.color = Fore.YELLOW
        elif(self.health/self.maxhealth > 0):
            self.color = Fore.RED
        else:
            self.delete_building()










