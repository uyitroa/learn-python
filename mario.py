import pygame,sys
from pygame import *
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
YELLOW = (255, 255, 0)
DISPLAYSURF = pygame.display.set_mode((800,800))
pygame.display.set_caption('Hello World!')
class character:
	def __init__(self,xmario,ymario,point):
		self.xmario = xmario
		self.ymario = ymario
		self.point = point
	def moveRight(self,step):
		self.xmario += step
	def moveLeft(self,step):
		self.xmario -= step
	def jump(self,height):
		self.ymario -= height
	def down(self,height):
		self.ymario += height
	def display(self):
		print('xmario: ',self.xmario)
		print('ymario: ',self.ymario)
mario = character(10,600,0)
move = ''
jump = ''
jumptime = 6
jumped = False
down = False
downtime = 3
downed = False
start = True
while True:
	if start == True:
		if jumped == True:
			jumped = False
			down = True
		if downed == True:
			downed = False
			down = False
		if jump == True:
			mario.jump(1)
			jumptime -= 1
			if jumptime == 0:
				jumptime = 6
				jump = ''
				jumped = True
		if move == 'right':
			mario.moveRight(5)
		if move == 'left':
			mario.moveLeft(5)
		if down == True:
			mario.down(2)
			downtime -= 1
			if downtime == 0:
				downtime = 3
				down = ''
				downed = True
		mario.display()
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if event.type == KEYDOWN:
			if event.key == K_UP:
				jump = True
			if event.key == K_RIGHT:
				move = 'right'
			if event.key == K_LEFT:
				move = 'left'
		else:
			move = ''
	pygame.display.update()
