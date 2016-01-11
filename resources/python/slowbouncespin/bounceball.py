import sys, pygame, math
from pygame.locals import *

pygame.init()

size = width, height = 960, 540
speed = [2,2]

#store color value as a tuple
black = 0, 0, 0

#create graphical window, a new surface object
#to represent actual displayed graphics
screen = pygame.display.set_mode(size)

tiepre = pygame.image.load("finalTIE.png")
tie = pygame.transform.rotate(tiepre, 270 * math.pi / 180)


#set up utility object type named Rect, representing
#a rectangular area
tierect = tie.get_rect()

#function to load images and prepare for main()
def load_image(file):
        surface = pygame.image.load(file)
        return surface.convert()

#change icon from default pygame
loadicon = load_image('tieicon.gif')
icon = pygame.transform.scale(loadicon, (32,32))
pygame.display.set_icon(icon)
pygame.display.set_caption("Bouncy TIE")
pygame.mouse.set_visible(0)

count = 1

while 1:
	for event in pygame.event.get():
        #if event.type in (pygame.QUIT, pygame.KEYDOWN) : sys.exit()
		if not hasattr(event, 'key'): continue
		down = event.type == KEYDOWN
		if event.key == K_ESCAPE: sys.exit(0)
                	
        #move method determines location on screen
	tierect = tierect.move(speed)

        #reverse velocity direction when the image hits the borders
	if tierect.left < 0 or tierect.right > width:
		speed[0] = -speed[0]
	if tierect.top < 0 or tierect.bottom > height:
		speed[1] = -speed[1]

	#fill screen with black to erase image
	screen.fill(black)

	#draw image using *surface*.blit() method
	#blit is the main method for changing onscreen pixels
	screen.blit(tie, tierect)

	#update display, since pygame manages display with double buffer
	pygame.display.flip()

	#update
	tie = pygame.transform.rotate(tiepre, count * math.pi / 180)
	tierect = tie.get_rect()
	count += 1
