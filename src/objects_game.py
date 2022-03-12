from colorama import Fore, Back, Style
class Object_Game:

    def __init__(self,x,y,size_x,size_y,matrix,game,maxhealth,color=Fore.GREEN):


        self.pos_x = x
        self.pos_y = y
        self.size_x = size_x
        self.size_y = size_y
        self.matrix = matrix
        self.game = game



        self.maxhealth = maxhealth
        self.health = self.maxhealth

        self.color = color

        self.got_hit = False



    def check(self):
        if(self.pos_x < 0 or self.pos_x > self.game.frame.width - self.size_x):
            return False
        if(self.pos_y < 0 or self.pos_y > self.game.frame.height - self.size_y):
            return False
        for y in range(self.size_y):
            for x in range(self.size_x):
                if(self.game.frame.screen[y+self.pos_y][x+self.pos_x] != Back.WHITE + ' ' + Back.RESET):

                    return False



        return True




