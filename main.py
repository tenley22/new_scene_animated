# go to terminal (@ bottom of screen) and write "pip install pygame" after PS C: line
# USE OBJECT ORIENTED
import pygame
import math
import random

# color constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (77, 0, 0)
ORANGE = (166, 45, 0)
YELLOW = (255, 153, 0)
BG = (26, 0, 0)
GREY = (4, 2, 2)


# math constants

# game constants
DISPLAY_WIDTH = 700
DISPLAY_HEIGHT = 500
FPS = 60

############################################################
############################################################

class House:

    def __init__(self, x_val, y_val, color, color2, color3):
        self.x_val = x_val
        self.y_val = y_val
        self.color = color
        self.color2 = color2
        self.color3 = color3

    def draw_house(self):
        pygame.draw.polygon(screen, self.color, ((self.x_val, self.y_val), (self.x_val, self.y_val - 300), (self.x_val+150, self.y_val - 350), (self.x_val+300, self.y_val - 300), (self.x_val+300, self.y_val)))
        pygame.draw.rect(screen, self.color3, ((self.x_val+20, self.y_val-270),(self.x_val+60, self.y_val-440)))
        pygame.draw.rect(screen, self.color3, ((self.x_val+220, self.y_val-270), (self.x_val+60, self.y_val-440)))
        pygame.draw.rect(screen, self.color3, ((self.x_val + 20, self.y_val - 170), (self.x_val + 60, self.y_val - 340)))

house = House(0, DISPLAY_HEIGHT, BLACK, GREY, ORANGE)

class Ground:
    def __init__(self, x_val, y_val, color):
        self.x_val = x_val
        self.y_val = y_val
        self.color = color

    def draw_ground(self):
        pygame.draw.rect(screen, self.color, ((self.x_val, self.y_val),(self.x_val+DISPLAY_WIDTH, self.y_val + 50)))

ground = Ground(0, 450, BLACK)


pygame.init()

screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
clock = pygame.time.Clock()

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ## functions ##


    ## drawing ##
    house.draw_house()
    ground.draw_ground()




    pygame.display.flip()

    screen.fill(BG)

    clock.tick(FPS)

pygame.quit()