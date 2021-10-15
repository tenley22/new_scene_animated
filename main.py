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
GREEN = (18, 61, 0)
BG = (0, 3, 23)
GREY = (4, 2, 2)


# math constants

# game constants
DISPLAY_WIDTH = 700
DISPLAY_HEIGHT = 500
FPS = 60

############################################################
############################################################

screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
clock = pygame.time.Clock()

class House:

    def __init__(self, x_val, y_val, color, color2, color3):
        self.x_val = x_val
        self.y_val = y_val
        self.color = color
        self.color2 = color2
        self.color3 = color3

    def draw_house(self):
        # house main body
        pygame.draw.polygon(screen, self.color, ((self.x_val, self.y_val), (self.x_val, self.y_val - 300), (self.x_val+150, self.y_val - 350), (self.x_val+300, self.y_val - 300), (self.x_val+300, self.y_val)))
        # house windows
        pygame.draw.rect(screen, self.color3, ((self.x_val+20, self.y_val-270), (self.x_val+60, self.y_val-440)))
        pygame.draw.rect(screen, self.color3, ((self.x_val+220, self.y_val-270), (self.x_val+60, self.y_val-440)))
        pygame.draw.rect(screen, self.color3, ((self.x_val + 20, self.y_val - 170), (self.x_val + 60, self.y_val - 440)))
        pygame.draw.rect(screen, self.color3, ((self.x_val + 220, self.y_val - 170), (self.x_val + 60, self.y_val - 440)))
        # house windows details
        pygame.draw.line(screen, self.color, (self.x_val, self.y_val-240), (self.x_val+300, self.y_val - 240), width=5)
        pygame.draw.line(screen, self.color, (self.x_val, self.y_val-140), (self.x_val+300, self.y_val-140), width=5)
        pygame.draw.line(screen, self.color, (self.x_val+50, self.y_val-300), (self.x_val+50, self.y_val), width=5)
        pygame.draw.line(screen, self.color, (self.x_val+250, self.y_val-300), (self.x_val+250, self.y_val), width=5)


house = House(0, DISPLAY_HEIGHT, BLACK, GREY, ORANGE)


class Ground:
    def __init__(self, x_val, y_val, color):
        self.x_val = x_val
        self.y_val = y_val
        self.color = color

    def draw_ground(self):
        pygame.draw.rect(screen, self.color, ((self.x_val, self.y_val),(self.x_val+DISPLAY_WIDTH, self.y_val + 50)))


ground = Ground(0, 450, BLACK)


class Ghost:
    def __init__(self, x_val, y_val, color, color2):
        self.x_val = x_val
        self.y_val = y_val
        self.color = color
        self.color2 = color2

    def draw_ghost(self):
        # main body
        pygame.draw.circle(screen, self.color, (self.x_val, self.y_val), 20)
        pygame.draw.polygon(screen, self.color, ((self.x_val-20, self.y_val), (self.x_val-20, self.y_val+50), (self.x_val-10, self.y_val+20), (self.x_val, self.y_val+50), (self.x_val+10, self.y_val+20), (self.x_val+20, self.y_val+50), (self.x_val+20, self.y_val)))
        # eyes
        pygame.draw.circle(screen, self.color2, (self.x_val-10, self.y_val-5), 5)
        pygame.draw.circle(screen, self.color2, (self.x_val+10, self.y_val-5), 5)


ghost_x = 10
x_velo = 3
ghost_y = 10
y_velo = 3
ghost_side = 21
ghost_height = 100
ghost_area = 300


class Pumpkin:
    def __init__(self, color, color2, x, y):
        self.color = color
        self.color2 = color2
        self.x = x
        self.y = y

    def draw_pumpkin(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), 20)
        pygame.draw.rect(screen, self.color2, ((self.x-3, self.y-30), (6, 10)))


pumpx = 0
pumpy = 450
pump_velo = 2
px_2 = pumpx + 100
px_3 = pumpx + 200
px_4 = pumpx + 300
px_5 = pumpx + 400
px_6 = pumpx + 500
px_7 = pumpx - 100


pygame.init()



running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if ghost_x + ghost_side > DISPLAY_WIDTH or ghost_x < 0:
        x_velo *= -1
    if ghost_y + ghost_height > ghost_area or ghost_y < 0:
        y_velo *= -1

    if pumpx > DISPLAY_WIDTH:
        pumpx = 0
    if px_2 > DISPLAY_WIDTH:
        px_2 = 0
    if px_3 > DISPLAY_WIDTH:
        px_3 = 0
    if px_4 > DISPLAY_WIDTH:
        px_4 = 0
    if px_5 > DISPLAY_WIDTH:
        px_5 = 0
    if px_6 > DISPLAY_WIDTH:
        px_6 = 0
    if px_7 > DISPLAY_WIDTH:
        px_7 = 0

    ## drawing ##
    house.draw_house()
    ground.draw_ground()

    ghost = Ghost(ghost_x, ghost_y, WHITE, BLACK)
    ghost.draw_ghost()
    ghost_x += x_velo
    ghost_y += y_velo

    pumpkin1 = Pumpkin(ORANGE, GREEN, pumpx, pumpy)
    pumpkin1.draw_pumpkin()
    pumpx += pump_velo

    pumpkin2 = Pumpkin(ORANGE, GREEN, px_2, pumpy)
    pumpkin2.draw_pumpkin()
    px_2 += pump_velo

    pumpkin3 = Pumpkin(ORANGE, GREEN, px_3, pumpy)
    pumpkin3.draw_pumpkin()
    px_3 += pump_velo

    pumpkin4 = Pumpkin(ORANGE, GREEN, px_4, pumpy)
    pumpkin4.draw_pumpkin()
    px_4 += pump_velo

    pumpkin5 = Pumpkin(ORANGE, GREEN, px_5, pumpy)
    pumpkin5.draw_pumpkin()
    px_5 += pump_velo

    pumpkin6 = Pumpkin(ORANGE, GREEN, px_6, pumpy)
    pumpkin6.draw_pumpkin()
    px_6 += pump_velo

    pumpkin7 = Pumpkin(ORANGE, GREEN, px_7, pumpy)
    pumpkin7.draw_pumpkin()
    px_7 += pump_velo


    pygame.display.flip()

    screen.fill(BG)

    clock.tick(FPS)

pygame.quit()
