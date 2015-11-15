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
x = 785
y = 785
fpsClock = pygame.time.Clock()
while True:
	pygame.draw.circle(DISPLAYSURF, BLUE,(xposition,yposition),30,30)
	pygame.draw.circle(DISPLAYSURF, RED, (x,y),30,30)
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()
	fpsClock.tick(30)
	pygame.draw.circle(DISPLAYSURF, BLACK,(xposition,yposition),30,30)
	pygame.draw.circle(DISPLAYSURF, BLACK,(x,y),30,30)
	if xposition != x - 45 and yposition != y - 45:
		xposition += 5
		yposition += 5
		x -= 5
		y -= 5
	else:
		while xposition != 0:
			pygame.draw.circle(DISPLAYSURF, BLUE,(xposition,yposition),30,30)
			pygame.draw.circle(DISPLAYSURF, RED, (x,y),30,30)
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
			pygame.display.update()
			fpsClock.tick(30)
			pygame.draw.circle(DISPLAYSURF, BLACK,(xposition,yposition),30,30)
			pygame.draw.circle(DISPLAYSURF, BLACK,(x,y),30,30)
			xposition -= 5
			yposition -= 5
			x += 5
			y += 5

