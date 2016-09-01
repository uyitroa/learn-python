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
marioRight = pygame.image.load('mario character')
marioLeft = pygame.image.load('mario character left')
ground = pygame.image.load('ground mario')
block = pygame.image.load('mario block')
enemy = pygame.image.load('EnemyMario.png')
pygame.init()
def font(e,g,b,x,y,s):
	fontObj = pygame.font.Font('freesansbold.ttf', s)
	textSurfaceObj = fontObj.render(str(e), True, g, b)
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.center = (x, y)
	DISPLAYSURF.blit(textSurfaceObj,textRectObj)
class character:
	def __init__(self,xmario,ymario,point,xblock,yblock,xenemy,yenemy):
		self.xmario = xmario
		self.ymario = ymario
		self.point = point
		self.xblock = xblock
		self.yblock = yblock
		self.xenemy = xenemy
		self.yenemy = yenemy
	def moveRight(self,step):
		self.xmario += step
	def moveLeft(self,step):
		self.xmario -= step
	def jump(self,height):
		self.ymario -= height
	def down(self,height):
		self.ymario += height
	def showMario(self):
		DISPLAYSURF.blit(personnage,(self.xmario,self.ymario))
	def blockMario(self):
		DISPLAYSURF.blit(block,(self.xblock,self.yblock))
	def Enemy(self):
		DISPLAYSURF.blit(enemy,(self.xenemy,self.yenemy))
		self.xenemy -= 1
	def allMouvement(self):
		if self.xmario >= 650:
			self.xmario -= 5
			self.xblock -= 5
	def touchEnemy(self,down):
		if self.ymario == 600:
			if self.xmario <= (self.xenemy + self.xenemy + 10)/2 <= self.xmario + 10:
				GameOver = True
				font('Game Over',BLACK,WHITE,600,600,32)
			else:
				GameOver = None
		elif down == True and self.ymario >= 580:
			if self.xenemy <= (self.xmario + self.xmario + 10)/2 <= self.xenemy + 10:
				font('killed',BLACK,WHITE,550,600,32)
				kill = True
				self.xenemy = 775
			else:
				kill = None
	def touchBlock(self,timeshow,jump):
			ju = None
			if jump == True and self.ymario <= 500:
				ju =True
			if ju == True:	
				if self.xblock <= (self.xmario + self.xmario + 10)/2 <= self.xblock + 10:
					GameOver = True
					font('Game Over',BLACK,WHITE,600,600,32)
					if timeshow != 0:
						font('You think that you can really destroy a block with your head xD',BLACK,WHITE,500,300,28)
					else:
						ju = False
	def display(self):
		print('xmario: ',self.xmario)
		print('ymarioyy: ',self.ymario)
		print('xenemy',self.xblock)
		print('yenemy',self.yblock)
personnage = marioRight
mario = character(10,600,0,650,405,775,600)
move = ''
jump = ''
jumptime = 24
jumped = False
down = False
downtime = 20
downed = False
start = True
xground = 0
while True:
	DISPLAYSURF.fill(BLACK)
	if start == True:
		DISPLAYSURF.blit(ground,(xground,665))
		if jumped == True:
			jumped = False
			down = True
		if downed == True:
			downed = False
			down = False
		if jump == True:
			mario.jump(5)
			jumptime -= 1
			if jumptime == 0:
				jumptime = 24
				jump = ''
				jumped = True
		if move == 'right':
			personnage = marioRight
			mario.moveRight(5)
		if move == 'left':
			personnage = marioLeft
			mario.moveLeft(5)
		if down == True:
			mario.down(6)
			downtime -= 1
			if downtime == 0:
				downtime = 20
				down = ''
				downed = True
		mario.display()
		mario.showMario()
		mario.blockMario()
		mario.allMouvement()
		mario.Enemy()
		mario.touchEnemy(down)
		mario.touchBlock(150,jump)
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
