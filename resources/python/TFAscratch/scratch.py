#xwing nav

#initialization
import pygame
from pygame.locals import *
import sys
import math
import time

#initialize screen

#set screen size, and screen variable to contain
screen = pygame.display.set_mode((1024, 768))
#screen = pygame.display.set_mode((1024, 768), FULLSCREEN)

#screen must be flipped if DOUBLEBUF is used
#pygame.display.flip()


#clock mechanism
clock = pygame.time.Clock()
#FPS = 30
FPS = 60 # better for action-oriented game

#the clock object will paus until 1/30th of a second has passed
#since the last call to tick
delt = clock.tick(FPS)

print "Initialized Clock"

#load image function for easier use
def imgload(file):
    surface = pygame.image.load(file)
    return surface.convert()

#import and set icon
iconload = imgload('firstorder1.gif')
iconmain = pygame.transform.scale(iconload, (32,32))
pygame.display.set_icon(iconmain)

#set window title
pygame.display.set_caption("The Resistance Xwing")
pygame.mouse.set_visible(0)


#show load screen (or display a static image in general)
#screenrect = Rect(0, 0, 1024, 768)
loadscrn = imgload('xwing\XWingloadscrn1.jpg')
screen = pygame.display.set_mode(loadscrn.get_rect().size) 
background = pygame.Surface(loadscrn.get_rect().size)
#background = pygame.Surface(screenrect.size)
background.blit(loadscrn, (0,0))
screen.blit(background, (0,0))
pygame.display.flip()
#hold image
time.sleep(5)

"""
#fade out
for n in range(10):
    loadscrn = loadscrn
    screen = pygame.display.set_mode(loadscrn.get_rect().size) 
    background = pygame.Surface(loadscrn.get_rect().size)
    #background = pygame.Surface(screenrect.size)
    background.blit(loadscrn, (0,0))
    screen.blit(background, (0,0))
    pygame.display.flip()
"""

print "done with loading screen"

#return screen to standard size
screen = pygame.display.set_mode((1024, 768))

#create vehicle class
class XWingSprite(pygame.sprite.Sprite):
    MAX_FORWARD_SPEED = 20
    MAX_REVERSE_SPEED = 20
    ACCELERATION = 3
    TURN_SPEED = 7

    def __init__(self, image, position):
        pygame.sprite.Sprite.__init__(self)
        self.src_image = pygame.image.load(image)
        self.position = position
        self.speed = self.direction = 0
        self.k_left = self.k_right = self.k_down = self.k_up = 0

    def update(self, delt):
        #simulation
        self.speed += (self.k_up + self.k_down)
        if self.speed > self.MAX_FORWARD_SPEED:
            self.speed = self.MAX_FORWARD_SPEED
        if self.speed < -self.MAX_REVERSE_SPEED:
            self.speed = -self.MAX_REVERSE_SPEED
        self.direction += (self.k_right + self.k_left)
        #store the same value in two separate variables declared now
        x, y = self.position
        rad = self.direction * math.pi / 180
        x += -self.speed*math.sin(rad)
        y += -self.speed*math.cos(rad)
        self.position = (x, y)
        self.image = pygame.transform.rotate(self.src_image, self.direction)
        self.rect = self.image.get_rect()
        self.rect.center = self.position


#create a vehicle and  run main program
rect = screen.get_rect()
xwingpre = XWingSprite('xwingMainSprite.gif', rect.center)
xwingrot = pygame.transform.rotate(xwingpre, 270 * math.pi / 180)
xwinggroup = pygame.sprite.RenderPlain(xwingrot)

while 1:
    # User input
    #the clock object will pause until 1/FPSth of a second has passed
    #since the last call to tick
    delt = clock.tick(FPS)
    for event in pygame.event.get():
        if not hasattr(event, 'key'): continue
        down = event.type == KEYDOWN
        if event.key == K_RIGHT: car.k_right = down * -5
        elif event.key == K_LEFT: car.k_left = down * 5
        elif event.key == K_UP: car.k_up = down * 2
        elif event.key == K_DOWN: car.k_down = down * -2
        elif event.key == K_ESCAPE: sys.exit(0)

    #Rendering
    screen.fill((0,0,0))
    xwinggroup.update(delt)
    xwinggroup.draw(screen)
    pygame.display.flip()

