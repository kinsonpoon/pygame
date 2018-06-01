import pygame
import sys
from pygame.locals import *

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()
wS = pygame.display.set_mode((500, 500), 0, 32)


# Method works as intended by itself
def create_text(x, y, phrase, color):
    """
    Create and displays text onto the globally-defined `wS` Surface
    (params in docstring omitted)
    """
    # Assume that the font file exists and is successfully found
    font_obj = pygame.font.Font("freesansbold.ttf", 32)
    text_surface_obj = font_obj.render(phrase, True, color)
    text_rect_obj = text_surface_obj.get_rect()
    text_rect_obj.center = (x, y)
    wS.blit(text_surface_obj, text_rect_obj)


while True:
    wS.fill(BLACK)
    for event in pygame.event.get():
        if event.type == KEYDOWN and event.key == K_SPACE:

            # Snippet containing unexpected behavior
            create_text(250, 250, "Hello world!", WHITE)
            pygame.display.update()
            pygame.time.delay(2000)
            wS.fill(BLACK)
            pygame.display.update()
            # Snippet end

        if event.type == QUIT:
            pygame.quit()
            sys.exit(0)
    pygame.display.update()