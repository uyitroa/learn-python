import pygame,sys
from pygame import *
import time
pygame.init()
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
YELLOW = (255, 255, 0)
DISPLAYSURF = pygame.display.set_mode((800,800))
pygame.display.set_caption('Hello World!')
x = 400
y = 0
can = True
can2 = True
x2 = 400
y2 = 750
bum = False
yposition = y + 60
yposition2 = 231
dir = 'right'
bum2 = False
dir2 = 'shit'
life = 5
life2 = 5
fie = False
counttime2 = 50
timecount = 100
xposition = 1
show = True
count = 10
def tank(x,y):
	pygame.draw.rect(DISPLAYSURF, BLACK, (x, y, 100, 50))
	pygame.draw.rect(DISPLAYSURF, BLACK, (x+25,50+y, 50, 25))
def tank2(x,y):
	pygame.draw.rect(DISPLAYSURF, BLACK, (x, y, 100, 50))
	pygame.draw.rect(DISPLAYSURF, BLACK, (x+25,y-25, 50, 25))
def fire(x,y):
	pygame.draw.circle(DISPLAYSURF, BLACK, (x,y), 5, 0)
def font(e,g,b,x,y):
	fontObj = pygame.font.Font('freesansbold.ttf', 32)
	textSurfaceObj = fontObj.render(str(e), True, g, b)
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.center = (x, y)
	DISPLAYSURF.blit(textSurfaceObj,textRectObj)
explosion = pygame.image.load('ex.png')
counttime = 50
while True:
	DISPLAYSURF.fill(WHITE)
	font(life,BLACK,WHITE,15,15)
	font(life2,BLACK,WHITE,15,755)
	if life == 0:
		counttime -= 1
		font('You Win!',BLACK, WHITE, 350,375)
		if counttime == 0:
			life = 5
			counttime = 50
	if dir == 'right':
		x += 5
		if x == 700:
			dir = 'left'
	if dir == 'left':
		x -= 5
		if x == 10:
			dir = 'right'
	if life != 0:
		tank(x,y)
	if timecount != 0:
		timecount -= 1
	if timecount == 0:
		timecount = 200
		yposition = y + 60
		xposition = x + 25
		bum = True
	if yposition > 750:
		DISPLAYSURF.blit(explosion,(xposition,yposition - 100))
	if bum == True:
		fire(xposition,yposition)
		yposition += 5
		if yposition == 750:
			if xposition > x2 - 90 and xposition < x2 + 90:
				life2 -= 1
	if life2 == 0:
		counttime2 -= 1
		font('You lose!',BLACK, WHITE,350,375)
		if counttime2 == 0:
			counttime2 = 50
			life2 = 5
	if dir2 == 'right':
		if can2 == True:
			x2 += 5
	if dir2 == 'left':
		if can == True:
			x2 -= 5
	if life2 != 0:
		tank2(x2,y2)
	if fie == True:
		yposition2 = y2 - 50
		xposition2 = x2 + 50
		bum2 = True
	if bum2 == True:
		fire(xposition2,yposition2)
		yposition2 -= 5
		if yposition2 == 5:
			if xposition2 > x - 90 and xposition2 < x + 90:
				life -= 1
	if yposition2 < 1:
		if show == True:
			count -= 1
			DISPLAYSURF.blit(explosion,(xposition2,yposition2 - 50))
			if count == 0:
				show = False
				count = 10
		bum2 = False
	if x2 <= 0:
		can = False
	else:
		can = True
	if x2 >= 710:
		can2 = False
	else:
		can2 = True
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == KEYDOWN:
			if event.key == K_LEFT:
				if can == True:
					dir2 = 'left'
				else:
					dir2 = 'shit'
			if event.key == K_RIGHT:
				if can2 == True:
					dir2 = 'right'
				else:
					dir2 = 'shit'
			if bum2 == False:
				if event.key == K_UP:
					fie = True
					show = True
				else:
					fie = False
		elif event.type != KEYDOWN:
			dir2 = 'shit'
			fie = False
	pygame.display.update()
