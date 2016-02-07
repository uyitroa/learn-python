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
xposition = random.randint(100,700)
yposition = 0
xposition2 = random.randint(100,700)
yposition2 = 0
fpsClock = pygame.time.Clock()
explo = pygame.image.load('ex.png')
explosion = False
explosion2 = False
touch = False
excar = pygame.image.load('excar.png')
counter = -1
counter2 = -1
asd = False
asd2 = False
while True:
	print("Yposition: ",yposition)
	print("Yposition2: ",yposition2)
	if yposition2 > 675:
		if counter2 <= 0:
			yposition2 = 0
	else:
		if counter2 <= 0:
			yposition2 += 15
	if yposition2 != 675:
		img2 = bomb
	else:
		explosion2 = True
		img2 = explo
	if yposition > 680:
		if counter <= 0:
			yposition = 0
	else:
		if counter <= 0:
			yposition += 5
	if yposition != 680:
		img = bomb
	else:
		explosion = True
		img = explo
	DISPLAYSURF.fill(WHITE)
	if explosion == True:
		yposition -= 50
		yposition2 -= 50
	if explosion == False:
		if xposition < x + 60 and xposition > x - 60 and yposition == 675 or xposition2 < x + 90 and xposition2 > x - 90 and yposition2 == 675:
			touch = True
			care = excar
	if touch == False:
		care = car
	if counter > 0:
		counter -= 1
		img = explo
	else:
		if asd == True:
			xposition = random.randint(100,700)
			yposition = 0
			asd = False
	if counter2 > 0:
		counter2 -= 1
		img2 = explo
	else:
		if asd2 == True:
			asd2 = False
			xposition2 = random.randint(100,700)
			yposition2 = 0
	DISPLAYSURF.blit(img,(xposition,yposition))
	DISPLAYSURF.blit(img2,(xposition2,yposition2))
	DISPLAYSURF.blit(care,(x,y))
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
		counter = 10
		touch = False
		asd = True
	if explosion2 == True:
		explosion2 = False
		counter2 = 10
		touch = False
		asd2 = True

