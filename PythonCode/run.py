import pygame, sys
from pygame.locals import *
import time
pygame.init()
BLUE = (0, 0,255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DISPLAYSURF = pygame.display.set_mode((400,400))
pygame.display.set_caption('Hello World!')
yposition = 0
xposition = 150
fpsClock = pygame.time.Clock()
bomb = pygame.image.load('bomb.png')
explo = pygame.image.load('ex.png')
explosion = False
while True:
	if yposition > 250:
		yposition = 0
	else:
		yposition += 5
	if yposition != 250:
		img = bomb
	else:
		explosion = True
		img = explo
	DISPLAYSURF.fill(WHITE)
	DISPLAYSURF.blit(img,(xposition,yposition))
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()
	fpsClock.tick(120)
	if explosion == True:
		explosion = False
		time.sleep(1)

