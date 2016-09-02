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
marioRight = pygame.image.load('mariocharacter.png')
marioLeft = pygame.image.load('mariocharacterleft.png')
ground = pygame.image.load('groundmario.png')
block = pygame.image.load('marioblock.png')
enemy = pygame.image.load('EnemyMario.png')
pygame.init()
def font(e,g,b,x,y,s):
	fontObj = pygame.font.Font('freesansbold.ttf', s)
	textSurfaceObj = fontObj.render(str(e), True, g, b)
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.center = (x, y)
	DISPLAYSURF.blit(textSurfaceObj,textRectObj)
class characterMario:
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
	def showMario(self):
		DISPLAYSURF.blit(personnage,(self.xmario,self.ymario))
	def Enemy(self):
		DISPLAYSURF.blit(enemy,(self.xenemy,self.yenemy))
		self.xenemy -= 1
	def display(self):
		print('xmario: ',self.xmario)
		print('ymarioyy: ',self.ymario)
class EnemyMario:
	def __init__(self,xenemy,yenemy):
		self.xenemy = xenemy
		self.yenemy = yenemy
	def MoveEnemy(self,step):
		self.xenemy -= step
	def ShowEnemy(self):
		DISPLAYSURF.blit(enemy,(self.xenemy,self.yenemy))
class BlockMario:
	def __init__(self,xblock,yblock):
		self.xblock = xblock
		self.yblock = yblock
	def ShowBlock(self):
		DISPLAYSURF.blit(block,(self.xblock,self.yblock))
	def MoveBlock(self,step):
		self.xblock -= step
personnage = marioRight
mario = characterMario(10,600,0)
Enemy = EnemyMario(775,600)
Block = BlockMario(650,405)
move = ''
jump = ''
jumptime = 24
jumped = False
down = False
downtime = 20
downed = False
start = True
xground = 0
def GameOver():
	global mario,enemy
	if mario.ymario == 600:
		if mario.xmario <= (Enemy.xenemy + Enemy.xenemy + 10)/2 <= mario.xmario + 10:
			GameOver = True
			font('Game Over',BLACK,WHITE,600,600,32)
		else:
			GameOver = False
def killEnemy():
	global mario,Enemy,down
	if down == True and mario.ymario >= 580:
		if Enemy.xenemy <= (mario.xmario + mario.xmario + 10)/2 <= Enemy.xenemy + 10:
			font('killed',BLACK,WHITE,550,600,32)
			kill = True
			Enemy.xenemy = 775
		else:
			kill = False
def touchBlock():
		global mario,Block,jump
		ju = False
		timeshow = 50
		if jump == True and mario.ymario <= 500:
			ju = True
		if ju == True:	
			if Block.xblock <= (mario.xmario + mario.xmario + 10)/2 <= Block.xblock + 10:
				GameOver = True
				font('Game Over',BLACK,WHITE,600,600,32)
				if timeshow != 0:
					font('You think that you can really destroy a block with your head xD',BLACK,WHITE,500,300,28)
				else:
					ju = False
			else:
				GameOver = False
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
		touchBlock()
		GameOver()
		killEnemy()
		mario.display()
		mario.showMario()
		Enemy.MoveEnemy(1)
		Enemy.ShowEnemy()
		if mario.xmario >= 650:
			Block.MoveBlock(5)
			mario.moveLeft(5)
		Block.ShowBlock()
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
