import pygame
import time
import random
import sys

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Slime')
clock = pygame.time.Clock()
class Things():
    def __init__(self,thingx, thingy, thingw, thingh, color):
        self.x=thingx
        self.y=thingy
        self.width=thingw
        self.height=thingh
        self.color=color
    def display(self,Display):
        pygame.draw.rect(Display, self.color, [self.x, self.y, self.width, self.height])
    def get_x(self):
        return self.x, self.x+self.width
class Ground(Things):
    def grounding(self):
        return self.y-self.height

class Slime(object):
    def __init__(self,x,y):
        self.normal=pygame.image.load('slime/character/normal32re.png')
        self.up=pygame.image.load('slime/character/up32.png').convert_alpha()
        self.down=pygame.image.load('slime/character/down32.png').convert_alpha()
        self.x=x
        self.y=y
        self.xspeed=0
        self.yspeed=0
        self.ground=0
        self.jump=False
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def get_height(self):
        return self.normal.get_height()
    def get_ground(self):
        return self.ground
    def updateground(self,y):
        self.ground=y
    def display(self):
        gameDisplay.blit(self.normal,(self.x,self.y))
    def goleft(self):
        self.xspeed=-5
    def jumpok(self):
        return self.jump
    def goright(self):
        self.xspeed=5
    def move(self):
        self.x=self.x+self.xspeed
        try:
            if(self.y+10>self.ground):
                self.y=self.ground
                self.jump=False
            if(self.y<self.ground):
                self.y=self.y+3
            else:
                self.jump=False
        except:
            pass
    def xstop(self):
        self.xspeed=0
    def goup(self,map):
        try:
            if(self.y==self.ground):
                if(self.block(map)==0):
                    self.y=self.y-100
                    self.jump=True
                else:
                    self.y=self.block(map)
                    self.jump=True
        except:
            pass
    def block(self,map):
    
        for item in map:
            x1,x2=item.get_x()
                
            if self.get_x()>=x1 and self.get_x()<=x2 and self.get_y()>item.grounding() and self.get_y()-100<item.grounding():
                return item.grounding()
        return 0
def check(slime,map):
    hlist=[]
    for item in map:
        x1,x2=item.get_x()
                
        if slime.get_x()>=x1 and slime.get_x()<=x2 and slime.get_y()<item.grounding():
            hlist.append(item.grounding()-slime.get_height())
            
    return slime.updateground(min(hlist))
def map1():
    map=[]
    for num in range(5):
        map.append(num)
        map[num]=Ground(num*100,display_height * 0.95,display_width,5,black)
		
    return map

def game_loop():
    map=[]
    for num in range(5):
        map.append(num)
        map[num]=Ground(num*100,display_height * 0.95,display_width,5,black)
    print(map)
    slime=Slime(display_width * 0.45,map[0].grounding()-200)
    slime.updateground(map[0].grounding()-slime.get_height())
    
    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    slime.goleft()
                if event.key == pygame.K_RIGHT:
                    slime.goright()
                if event.key == pygame.K_UP:
                    slime.goup(map)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    slime.xstop()
        try:
            check(slime,map)    
        except:
            pass
        gameDisplay.fill(white)
        slime.display()
        for item in map:
            item.display(gameDisplay)
        slime.move()
        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()

