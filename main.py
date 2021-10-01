# go to terminal (@ bottom of screen) and write "pip install pygame" after PS C: line
# USE OBJECT ORIENTED
import pygame
import math
import random

# color constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
ORANGE = (255, 50, 0)
YELLOW = (255, 234, 0)
GREEN = (10, 100, 10)
BLUE = (10, 10, 150)
PURPLE = (70, 0, 70)

TAUPE = (70, 50, 60)
PINK = (250, 70, 90)

NEW2 = (85, 15, 10)

# math constants

# game constants
DISPLAY_WIDTH = 700
DISPLAY_HEIGHT = 500
FPS = 60

############################################################
############################################################

pygame.init()

screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
clock = pygame.time.Clock()

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ## functions ##
    #house
    def house(place, fill, )


    ## drawing ##



    pygame.display.flip()

    screen.fill(NEW2)

    clock.tick(FPS)

pygame.quit()