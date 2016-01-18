#TFA Beta  game
#adapted from https://github.com/mlambir/Pygame-FPS/tree/master/src
#including worldManager.py

import pygame
from pygame.locals import *
import math
import worldManager
import time

worldMap =[
  [8,8,8,8,8,8,8,8,8,8,8,4,4,6,4,4,6,4,6,4,4,4,6,4],
  [8,0,0,0,0,0,0,0,0,0,8,4,0,0,0,0,0,0,0,0,0,0,0,4],
  [8,0,3,3,0,0,0,0,0,8,8,4,0,0,0,0,0,0,0,0,0,0,0,6],
  [8,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6],
  [8,0,3,3,0,0,0,0,0,8,8,4,0,0,0,0,0,0,0,0,0,0,0,4],
  [8,0,0,0,0,0,0,0,0,0,8,4,0,0,0,0,0,6,6,6,0,6,4,6],
  [8,8,8,8,0,8,8,8,8,8,8,4,4,4,4,4,4,6,0,0,0,0,0,6],
  [7,7,7,7,0,7,7,7,7,0,8,0,8,0,8,0,8,4,0,4,0,6,0,6],
  [7,7,0,0,0,0,0,0,7,8,0,8,0,8,0,8,8,6,0,0,0,0,0,6],
  [7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,6,0,0,0,0,0,4],
  [7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,6,0,6,0,6,0,6],
  [7,7,0,0,0,0,0,0,7,8,0,8,0,8,0,8,8,6,4,6,0,6,6,6],
  [7,7,7,7,0,7,7,7,7,8,8,4,0,6,8,4,8,3,3,3,0,3,3,3],
  [2,2,2,2,0,2,2,2,2,4,6,4,0,0,6,0,6,3,0,0,0,0,0,3],
  [2,2,0,0,0,0,0,2,2,4,0,0,0,0,0,0,4,3,0,0,0,0,0,3],
  [2,0,0,0,0,0,0,0,2,4,0,0,0,0,0,0,4,3,0,0,0,0,0,3],
  [1,0,0,0,0,0,0,0,1,4,4,4,4,4,6,0,6,3,3,0,0,0,3,3],
  [2,0,0,0,0,0,0,0,2,2,2,1,2,2,2,6,6,0,0,5,0,5,0,5],
  [2,2,0,0,0,0,0,2,2,2,0,0,0,2,2,0,5,0,5,0,0,0,5,5],
  [2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,5,0,5,0,5,0,5,0,5],
  [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5],
  [2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,5,0,5,0,5,0,5,0,5],
  [2,2,0,0,0,0,0,2,2,2,0,0,0,2,2,0,5,0,5,0,0,0,5,5],
  [2,2,2,2,1,2,2,2,2,2,2,1,2,2,2,5,5,5,5,5,5,5,5,5]
];

#worldMap =[
#  [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
#  [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
#  [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
#  [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
#  [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
#  [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
#  [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
#  [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
#  [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
#  [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
#  [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
#  [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
#  [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
#  [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
#  [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
#  [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
#  [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
#  [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
#  [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
#  [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
#  [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
#  [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
#  [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
#];

sprite_positions=[
  
  (20.5, 11.5, 2), #first order officer in front of playerstart
  (18.5,4.5, 2),
  (10.0,4.5, 2),
  (10.0,12.5,2),
  (3.5, 6.5, 2),
  (3.5, 20.5,2),
  (3.5, 14.5,2),
  (14.5,20.5,2),

  #computers
  (18.5, 10.5, 1),
  (18.5, 11.5, 1),
  (18.5, 12.5, 1),
  
  #rotj computers
  (21.5, 1.5, 0),
  (15.5, 1.5, 0),
  (16.0, 1.8, 0),
  (16.2, 1.2, 0),
  (3.5,  2.5, 0),
  (9.5, 15.5, 0),
  (10.0, 15.1,0),
  (10.5, 15.8,0),
]

def load_image(image, darken, colorKey = None):
    ret = []
    if colorKey is not None:
        image.set_colorkey(colorKey)
    if darken:
        image.set_alpha(127)
    for i in range(image.get_width()):
        s = pygame.Surface((1, image.get_height())).convert()
        #s.fill((0,0,0))
        s.blit(image, (- i, 0))
        if colorKey is not None:
            s.set_colorkey(colorKey)
        ret.append(s)
    return ret

def main():
  
    t = time.clock() #time of current frame
    oldTime = 0. #time of previous frame
    
    size = w, h = 640,480
    pygame.init()
    window = pygame.display.set_mode(size)

    loadicon = pygame.image.load('tieicon.gif').convert()
    icon = pygame.transform.scale(loadicon, (32,32))
    pygame.display.set_icon(icon)

    pygame.display.set_caption("Kylo Ren Freaks Out")
    screen = pygame.display.get_surface()
    #pixScreen = pygame.surfarray.pixels2d(screen)
    pygame.mouse.set_visible(False)
    clock = pygame.time.Clock()
    
    f = pygame.font.SysFont(pygame.font.get_default_font(), 20)
    
    
    
#==========================================================================
#play initialization screens

    def preloads(file):
        pane1 = pygame.image.load(file)
        return pane1.convert()

    def mainscrolls(file):
        loadscrn = preloads(file)
        screen = pygame.display.set_mode(loadscrn.get_rect().size)
        #screen = pygame.display.set_mode(loadscrn.get_rect().size, pygame.FULLSCREEN)
        loadback = pygame.Surface(loadscrn.get_rect().size)
        loadback.blit(loadscrn, (0,0))
        loadback.set_alpha(0)
        pygame.display.flip()

        for n in range(256):
            screen.fill((0,0,0))
            loadback.set_alpha(0+n)
            screen.blit(loadback, (0,0))
            pygame.display.flip()

        time.sleep(2)
        pygame.mixer.music.load('sounds/tieshot1.wav')
        pygame.mixer.music.play(0)

        for n in range(256):
            screen.fill((0,0,0))
            loadback.set_alpha(256-n)
            screen.blit(loadback, (0,0))
            pygame.display.flip()

        time.sleep(0.5)

    mainscrolls('tfafakelogo.png')
    mainscrolls('YodaDisclaimer.png')
    mainscrolls('initmain.png')
    
    #first order officer screen
    mus = pygame.mixer.music.load('kylorentheme_short.mp3')
    #infinite loop
    mus1 = pygame.mixer.music.play(-1)
    loadscrn1 = preloads('badnews.png')
    screen = pygame.display.set_mode(loadscrn1.get_rect().size)
    loadback1 = pygame.Surface(loadscrn1.get_rect().size)
    loadback1.blit(loadscrn1, (0,0))
    loadback1.set_alpha(0)
    pygame.display.flip()

    for n in range(256):
        screen.fill((0,0,0))
        loadback1.set_alpha(0+n)
        screen.blit(loadback1, (0,0))
        pygame.display.flip()

    time.sleep(5)

    #turn on LS
    pygame.mixer.music.load('sounds/csLSon.wav')
    pygame.mixer.music.play(0)
    for v in range(30):
        screen.fill((0,0,0))
        loadscrn2 = preloads('firstmov/onmov(%s).png' % (v + 1))
        loadback2 = pygame.Surface(loadscrn1.get_rect().size)
        screen.blit(loadscrn2, (0,0))
        pygame.display.flip()
        time.sleep(0.02)
    '''
    screen.fill((0,0,0))
    screen.blit(loadback, (0,0))
    pygame.display.flip()

    time.sleep(0.5)
    '''
#==========================================================================

    #window = pygame.display.set_mode(size, pygame.FULLSCREEN)
    window = pygame.display.set_mode(size)
    wm = worldManager.WorldManager(worldMap,sprite_positions, 22, 11.5, -1, 0, 0, .66)
    
    weapons = [Weapon("lightsaber")]
    weapon = weapons[0]
	
    while(True):
        clock.tick(60)
        
        wm.draw(screen)
        
        
        # timing for input and FPS counter
        
        frameTime = float(clock.get_time()) / 1000.0 # frameTime is the time this frame has taken, in seconds
        t = time.clock()
        text = f.render(str(clock.get_fps()), False, (255, 255, 0))
        #screen.blit(text, text.get_rect(), text.get_rect())
        weapon.draw(screen, t)
        pygame.display.flip()

        # speed modifiers
        moveSpeed = frameTime * 5.0 # the constant value is in squares / second
        rotSpeed = frameTime * 3.0 # the constant value is in radians / second

        
        
        for event in pygame.event.get(): 
            if event.type == QUIT: 
                return 
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.display.quit()
                    pygame.quit()
		    #return
                elif event.key == K_SPACE:
                    #slash
                    #pygame.mixer.quit()
                    weapon.play()
                elif event.key == K_v:
                    #load secondary attack
                    #pygame.mixer.quit()
                    weapon.secondatk()
                elif event.key == K_c:
                    #restore primary attack
                    #pygame.mixer.quit()
                    weapon.restart1()
            elif event.type == KEYUP:
                if event.key == K_SPACE:
                    weapon.stop()
                    #pygame.mixer.music.load('sounds/csLShum.wav')
                    #pygame.mixer.music.play(-1)
            else:
                pass 
        
        keys = pygame.key.get_pressed()
        if keys[K_UP]:
            # move forward if no wall in front of you
            moveX = wm.camera.x + wm.camera.dirx * moveSpeed
            if(worldMap[int(moveX)][int(wm.camera.y)]==0 and worldMap[int(moveX + 0.1)][int(wm.camera.y)]==0):wm.camera.x += wm.camera.dirx * moveSpeed
            moveY = wm.camera.y + wm.camera.diry * moveSpeed
            if(worldMap[int(wm.camera.x)][int(moveY)]==0 and worldMap[int(wm.camera.x)][int(moveY + 0.1)]==0):wm.camera.y += wm.camera.diry * moveSpeed
        if keys[K_DOWN]:
            # move backwards if no wall behind you
            if(worldMap[int(wm.camera.x - wm.camera.dirx * moveSpeed)][int(wm.camera.y)] == 0):wm.camera.x -= wm.camera.dirx * moveSpeed
            if(worldMap[int(wm.camera.x)][int(wm.camera.y - wm.camera.diry * moveSpeed)] == 0):wm.camera.y -= wm.camera.diry * moveSpeed
        if (keys[K_RIGHT] and not keys[K_DOWN]) or (keys[K_LEFT] and keys[K_DOWN]):
            # rotate to the right
            # both camera direction and camera plane must be rotated
            oldDirX = wm.camera.dirx
            wm.camera.dirx = wm.camera.dirx * math.cos(- rotSpeed) - wm.camera.diry * math.sin(- rotSpeed)
            wm.camera.diry = oldDirX * math.sin(- rotSpeed) + wm.camera.diry * math.cos(- rotSpeed)
            oldPlaneX = wm.camera.planex
            wm.camera.planex = wm.camera.planex * math.cos(- rotSpeed) - wm.camera.planey * math.sin(- rotSpeed)
            wm.camera.planey = oldPlaneX * math.sin(- rotSpeed) + wm.camera.planey * math.cos(- rotSpeed)
        if (keys[K_LEFT] and not keys[K_DOWN]) or (keys[K_RIGHT] and keys[K_DOWN]): 
            # rotate to the left
            # both camera direction and camera plane must be rotated
            oldDirX = wm.camera.dirx
            wm.camera.dirx = wm.camera.dirx * math.cos(rotSpeed) - wm.camera.diry * math.sin(rotSpeed)
            wm.camera.diry = oldDirX * math.sin(rotSpeed) + wm.camera.diry * math.cos(rotSpeed)
            oldPlaneX = wm.camera.planex
            wm.camera.planex = wm.camera.planex * math.cos(rotSpeed) - wm.camera.planey * math.sin(rotSpeed)
            wm.camera.planey = oldPlaneX * math.sin(rotSpeed) + wm.camera.planey * math.cos(rotSpeed)

fps = 8
class Weapon(object):
    
    def __init__(self, frameCount = 5):
        self.images = []
        self.loop = False
        self.playing = False
        self.frame = 0
        self.oldTime = 0
        for i in range(4):
            img = pygame.image.load("cgLS/attack1/LS(%s).png" % (i+1)).convert()
            img = pygame.transform.scale2x(img)
            img = pygame.transform.scale2x(img)
            img.set_colorkey(img.get_at((0,0)))
            self.images.append(img)
        pygame.mixer.music.load('sounds/csLSslash.wav')
    def secondatk(self, frameCount = 5):
        self.images = []
        self.loop = False
        self.playing = False
        self.frame = 0
        self.oldTime = 0
        for j in range(10):
            img2 = pygame.image.load("cgLS/attack2/LS(%s).png" % (j + 1)).convert()
            img2 = pygame.transform.scale2x(img2)
            img2 = pygame.transform.scale2x(img2)
            img2.set_colorkey(img2.get_at((0,0)))
            self.images.append(img2)
        pygame.mixer.music.load('sounds/csLSslashBreak.wav')
    def restart1(self, frameCount = 5):
        self.images = []
        self.loop = False
        self.playing = False
        self.frame = 0
        self.oldTime = 0
        for k in range(4):
            img1 = pygame.image.load("cgLS/attack1/LS(%s).png" % (k + 1)).convert()
            img1 = pygame.transform.scale2x(img1)
            img1 = pygame.transform.scale2x(img1)
            img1.set_colorkey(img1.get_at((0,0)))
            self.images.append(img1)
        pygame.mixer.music.load('sounds/csLSslash.wav')
    def play(self):
        self.playing = True
        self.loop = True
        #pygame.mixer.init()
        pygame.mixer.music.play(0)
    def stop(self):
        self.playing = False
        self.loop = False
    def draw(self, surface, time):
        if(self.playing or self.frame > 0):
            if(time > self.oldTime + 1./fps):
                self.frame = (self.frame+1) % len(self.images)
                if self.frame == 0: 
                    if self.loop:
                        self.frame = 1
                    else:
                        self.playing = False
                        
                self.oldTime = time
        img = self.images[self.frame]
        surface.blit(img, (surface.get_width()/2 - img.get_width()/2, surface.get_height()-img.get_height()))
            
if __name__ == '__main__':
    main()
