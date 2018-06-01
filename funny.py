import pygame
import time
import random
pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

car_width = 200
car_height=20

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('I am so boring')
clock = pygame.time.Clock()

carImg = pygame.image.load('character.png')
#
def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def car(x,y):
    pygame.draw.rect(gameDisplay, black, [x, y, 10, 10])

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8+50)

    x_change = 0
    y_change = 0
    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_change=-5
                elif event.key == pygame.K_DOWN:
                    y_change=5
                elif event.key == pygame.K_LEFT:
                    x_change=-5
                elif event.key ==pygame.K_RIGHT:
                    x_change=5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    y_change=0
                elif event.key == pygame.K_DOWN:
                    y_change=0
                elif event.key == pygame.K_LEFT:
                    x_change=0
                elif event.key ==pygame.K_RIGHT:
                    x_change=0
        x+=x_change
        y+=y_change
        gameDisplay.fill(white)
        car(x,y)
        
        pygame.display.update()
        clock.tick(60)



game_loop()
pygame.quit()
quit()