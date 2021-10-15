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
BG = (0, 3, 23)
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
        # house main body
        pygame.draw.polygon(screen, self.color, ((self.x_val, self.y_val), (self.x_val, self.y_val - 300), (self.x_val+150, self.y_val - 350), (self.x_val+300, self.y_val - 300), (self.x_val+300, self.y_val)))
        # house windows
        pygame.draw.rect(screen, self.color3, ((self.x_val+20, self.y_val-270),(self.x_val+60, self.y_val-440)))
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
        pygame.draw.circle(screen, self.color, (self.x_val, self.y_val), 20)
        pygame.draw.polygon(screen, self.color, ((self.x_val-20, self.y_val), (self.x_val-20, self.y_val+50), (self.x_val-10, self.y_val+20), (self.x_val, self.y_val+50), (self.x_val+10, self.y_val+20), (self.x_val+20, self.y_val+50), (self.x_val+20, self.y_val)))
        pygame.draw.circle(screen, self.color2, (self.x_val-10, self.y_val-5), 5)
        pygame.draw.circle(screen, self.color2, (self.x_val+10, self.y_val-5), 5)


ghost_x = 10
x_velo = 3
ghost_y = 10
y_velo = 3
ghost_side = 21
ghost_height = 100
ghost_area = 300

class Cat: 
  def __init__(self, x1, y1, legx1, legy1, legx2, legy2, legx3, legy3, legx4, legy4, color):
    self.x1 = x1
    self.y1 = y1
    self.legx1 = legx1
    self.legy1 = legy1
    self.legx2 = legx2
    self.legy2 = legy2
    self.legx3 = legx3
    self.legy3 = legy3
    self.legx4 = legx4
    self.legy4 = legy4
  
  def draw_cat(self):
    pygame.draw.circle(screen, self.color, (self.x1, self.y1), 20)



pygame.init()


screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
clock = pygame.time.Clock()


running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if ghost_x + ghost_side > DISPLAY_WIDTH or ghost_x < 0:
        x_velo *= -1
    if ghost_y + ghost_height > ghost_area or ghost_y < 0:
        y_velo *= -1

    ## functions ##


    ## drawing ##
    house.draw_house()
    ground.draw_ground()
    ghost = Ghost(ghost_x, ghost_y, WHITE, BLACK)
    ghost.draw_ghost()
    ghost_x += x_velo
    ghost_y += y_velo

    pygame.display.flip()

    screen.fill(BG)

    clock.tick(FPS)

pygame.quit()
