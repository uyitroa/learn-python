import pygame,sys
from pygame import *
import time
import random
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
YELLOW = (255, 255, 0)
DISPLAYSURF = pygame.display.set_mode((800,800))
pygame.display.set_caption('Hello World!')
bomb = pygame.image.load('bomb.png')
car = pygame.image.load('car.png')
x = 400
y = 700
xposition = 400
yposition = 0
fpsClock = pygame.time.Clock()
explo = pygame.image.load('ex.png')
explosion = False
while True:
	if yposition > 680:
		yposition = 0
	else:
		yposition += 5
	if yposition != 680:
		img = bomb
	else:
		explosion = True
		img = explo
	DISPLAYSURF.fill(WHITE)
	if explosion == True:
		yposition -= 50
		xposition = random.randint(100,700)
	DISPLAYSURF.blit(img,(xposition,yposition))
	DISPLAYSURF.blit(car,(x,y))
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == KEYDOWN:
			if event.key == K_LEFT:
				x -= 10
			if event.key == K_RIGHT:
				x += 10
	pygame.display.update()
	fpsClock.tick(30)
	if explosion == True:
		explosion = False
		time.sleep(1)
		xposition = 400
		yposition = 0

