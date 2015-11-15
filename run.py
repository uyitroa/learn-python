import pygame, sys
from pygame.locals import *
pygame.init()
BLUE = (0, 0,255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
DISPLAYSURF = pygame.display.set_mode((800,800))
pygame.display.set_caption('Hello World!')
yposition = 0
xposition = 0
fpsClock = pygame.time.Clock()
dir = 'down'
while True:
	pygame.draw.circle(DISPLAYSURF, BLUE,(xposition,yposition),30,30)
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()
	fpsClock.tick(30)
	pygame.draw.circle(DISPLAYSURF, BLACK,(xposition,yposition),30,30)
	if dir == 'down':
		if xposition != 770 and yposition != 770:
			xposition += 5
			yposition += 5
		else:
			dir = 'left'
	elif dir == 'left':
		if xposition != 25:
			xposition -= 5
		else:
			dir = 'up'
	elif dir == 'up':
		if yposition != 30:
			yposition -= 5
			xposition += 5
		else:
			dir = 'left1'
	elif dir == 'left1':
		if xposition != 25:
			xposition -= 5
		else:
			dir = 'down'
		
