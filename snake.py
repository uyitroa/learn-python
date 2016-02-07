import pygame,sys
from pygame import *
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
YELLOW = (255, 255, 0)
DISPLAYSURF = pygame.display.set_mode((800,800))
pygame.display.set_caption('Snake')
def snake(x,y,s,t):
	pygame.draw.line(DISPLAYSURF, BLACK, (x,y),(s,t), 10)
x = 350
y = 375
dir = 'right'
axe = 'ngang'
s = 10
long = 10
t = y
pointx = 0
pointy = 0
while True:
	DISPLAYSURF.fill(WHITE)
	if axe == 'ngang':
		snake(x,y,s,y)
	if axe == 'doc':
		snake(s,y,s,t)
	if dir == 'right' or dir == 'left':
		snake(s,y,s,t)
		if t > y:
			t -= 1
		elif t < y:
			t += 1
		else:
			if dir == 'right':
				s += 1
			else:
				s -= 1
		if dir == 'right':
			x += 1
		if dir == 'left':
			x -= 1
	if dir == 'up' or dir == 'down':
		snake(x,y,s,y)
		if s > x:
			s -= 1
		elif s < x:
			s += 1
		else:
			if dir == 'up':
				t -= 1
			else:
				t += 1
		if dir == 'up':
			y -= 1
		else:
			y += 1
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if event.type == KEYDOWN:
			if event.key == K_RIGHT:
				if axe != 'ngang':
					dir = 'right'
			if event.key == K_LEFT:
				if axe != 'ngang':
					dir = 'left'
			if event.key == K_UP:
				if axe != 'doc':
					dir = 'up'
			if event.key == K_DOWN:
				if axe != 'doc':
					dir = 'down'
	pygame.display.update()
