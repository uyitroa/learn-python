import pygame, sys
from pygame import *
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
YELLOW = (255, 255, 0)
pygame.init()
DISPLAYSURF = pygame.display.set_mode((800,850))
xbed = [250]
ybed = [250]
stage = 0
xroom = [225]
yroom = [95]
xfridge = [380]
yfridge = [215]
xcomp = [225]
ycomp = [130]
dir = ''
custom = 1
ection = ''
start = True
change = 3
def font(e,g,b,x,y,s):
	fontObj = pygame.font.Font('freesansbold.ttf', s)
	textSurfaceObj = fontObj.render(str(e), True, g, b)
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.center = (x, y)
	DISPLAYSURF.blit(textSurfaceObj,textRectObj)
def graduation():
	for z in range(851):
		if z % 25 == 0:
			font(str(z),WHITE,BLACK,15,z,10)
			font(str(z),WHITE,BLACK,z,15,-10)
pygame.display.set_caption('Pokemon')
bed = pygame.image.load('Bed')
border = pygame.image.load('Border')
comp = pygame.image.load('Computer')
fridge = pygame.image.load('Fridge')
room1 = pygame.image.load('Room Home')
down = pygame.image.load('Down')
down1 = pygame.image.load('Down1')
down2 = pygame.image.load('Down2')
up = pygame.image.load('Up')
up1 = pygame.image.load('Up1')
up2 = pygame.image.load('Up2')
right = pygame.image.load('Right')
right1 = pygame.image.load('Right1')
right2 = pygame.image.load('Right2')
left = pygame.image.load('Left')
left1 = pygame.image.load('Left1')
left2 = pygame.image.load('Left2')
costume = down
while True:
	DISPLAYSURF.fill(BLACK)
	if start == True:
		if stage == 0:
			DISPLAYSURF.blit(room1,(xroom[0],yroom[0]))
			#DISPLAYSURF.blit(bed,(xbed[0],ybed[0]))
			#DISPLAYSURF.blit(fridge,(xfridge[0],yfridge[0]))
			#DISPLAYSURF.blit(comp,(xcomp[0],ycomp[0]))
			DISPLAYSURF.blit(border,(-50,-125))
		pygame.draw.rect(DISPLAYSURF, BLACK, (0,350, 800 , 800))
		graduation()
		if dir == 'down':
			if custom == 1:
				if change == 0:
					costume = down1
					custom = 2
					change = 3
				else:
					change -= 1
			elif custom == 2:
				if change == 0:
					costume = down2
					custom = 1
					change = 3 
				else:
					change -= 1
			for s in range(len(ybed)):
				ybed[s] -= 5
			yroom[stage] -= 5
			for s in range(len(yfridge)):
				yfridge[s] -= 5
			for s in range(len(ycomp)):
				ycomp[s] -= 5
		elif dir == 'up':
			if custom == 1:
				if change == 0:
					costume = up1
					custom = 2
					change = 3
				else:
					change -= 1
			elif custom == 2:
				if change == 0:
					costume = up2
					custom = 1
					change = 3
				else:
					change -= 1
			for s in range(len(ybed)):
				ybed[s] += 5
			yroom[stage] += 5
			for s in range(len(yfridge)):
				yfridge[s] += 5
			for s in range(len(ycomp)):
				ycomp[s] += 5
		elif dir == 'left':
			if custom == 1:
				if change == 0:
					costume = left1
					custom = 2
					change = 3
				else:
					change -= 1
			elif custom == 2:
				if change == 0:
					costume = left2
					custom = 1
					change = 3
				else:
					change -= 1
			for s in range(len(xbed)):
				xbed[s] += 5
			xroom[stage] += 5
			for s in range(len(xfridge)):
				xfridge[s] += 5
			for s in range(len(xcomp)):
				xcomp[s] += 5
		elif dir == 'right':
			if custom == 1:
				if change == 0:
					costume = right1
					custom = 2
					change = 3
				else:
					change -= 1
			elif custom == 2:
				if change == 0:
					costume = right2
					custom = 1
					change = 3
				else:
					change -= 1
			for s in range(len(xbed)):
				xbed[s] -= 5
			xroom[stage] -= 5
			for s in range(len(xfridge)):
				xfridge[s] -= 5
			for s in range(len(xcomp)):
				xcomp[s] -= 5
		else:
			if ection == 'down':
				costume = down
			elif ection == 'up':
				costume = up
			elif ection == 'left':
				costume = left
			elif ection == 'right':
				costume = right
		DISPLAYSURF.blit(costume,(375,300))
	graduation()
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if event.type == KEYDOWN:
			if event.key == K_DOWN:
				dir = 'down'
				ection = 'down'
			if event.key == K_UP:
				dir = 'up'
				ection = 'up'
			if event.key == K_LEFT:
				dir = 'left'
				ection = 'left'
			if event.key == K_RIGHT:
				dir = 'right'
				ection = 'right'
		else:
			dir = ''
			change = 0
	pygame.display.update()
