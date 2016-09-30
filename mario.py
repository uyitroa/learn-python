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
	def __init__(self,xmario,ymario,point,life):
		self.xmario = xmario
		self.ymario = ymario
		self.point = point
		self.life = life
	def moveRight(self,step):
		self.xmario += step
	def moveLeft(self,step):
		self.xmario -= step
	def jump(self,height):
		self.ymario -= height
	def down(self,height):
		self.ymario += height
	def showMario(self,timerevive):
		if timerevive % 3 == 1 or timerevive % 3 == 2:
			DISPLAYSURF.blit(personnage,(self.xmario,self.ymario))
	def LifeCount(self,number,over,OVER,OVer,timerevive):
		print(timerevive)
		if over == True or OVER == True or OVer == True:
			if timerevive == 17:
				self.life -= number
				timerevive -= 1
		if timerevive != 17:
			timerevive -= 1
		if timerevive <= 0:
			timerevive = 17
		return timerevive
	def PointCount(self,number,kill,killl):
		if kill == True or killl == True:
			self.point += number
		print(kill)
	def display(self):
		print('xmario: ',self.xmario)
		print('ymarioyy: ',self.ymario)
class EnemyMario:
	def __init__(self,xenemy,yenemy):
		self.xenemy = xenemy
		self.yenemy = yenemy
	def MoveEnemy(self,step):
		self.xenemy -= step
	def resetX(self):
		if self.xenemy <= -10:
			self.xenemy = 1000
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
groundMario = 595
mario = characterMario(10,groundMario,0,3)
Enemy = EnemyMario(775,600)
Enemy2 = EnemyMario(900,600)
Block = BlockMario(650,405)
move = ''
jump = ''
distMario = 10
jumptime = 24
jumped = False
down = False
downtime = 20
downed = False
start = True
xground = 0
ju = 50
timerevive = 17
def GameOVer(Enemy):
	global mario,timerevive
	GameOver = False
	if mario.ymario == 595:
		#if mario.xmario <= (Enemy.xenemy + Enemy.xenemy + 10)/2 <= mario.xmario + 10:
		if Enemy.xenemy + 20 <= mario.xmario <= Enemy.xenemy + 50 or Enemy.xenemy + 20 >= mario.xmario + 50 >= Enemy.xenemy:
			GameOver = True
			font('-1 life',BLACK,WHITE,600,600,32)
		else:
			GameOver = False
		return GameOver
def killEnemy(Enemy):
	global mario,down
	kill = False
	if down == True and mario.ymario >= 580:
		#if Enemy.xenemy <= mario.xmario and mario.xmario + 50 <= Enemy.xenemy + 20:
		if Enemy.xenemy + 50 <= mario.xmario <= Enemy.xenemy + 50 or Enemy.xenemy + 50 >= mario.xmario + 20 >= Enemy.xenemy:
			font('killed',BLACK,WHITE,550,600,32)
			kill = True
			Enemy.xenemy = 1000
		else:
			kill = False
	return kill
def touchBlock():
		global mario,Block,jump
		timeshow = 50
		ju = 50
		GameOver = False
		if jump == True and mario.ymario <= 500:
			ju = True
		if ju == True:	
			if Block.xblock <= mario.xmario and mario.xmario + 20 <= Block.xblock + 50:
				GameOver = True
				font('-1 life',BLACK,WHITE,600,600,32)
				if timeshow != 0:
					font('You think that you can really destroy a block with your head xD',BLACK,WHITE,500,300,28)
				else:
					ju = False
			else:
				GameOver = False
		return GameOver
while True:
	DISPLAYSURF.fill(BLACK)
	if start == True:
		DISPLAYSURF.blit(ground,(xground,665))
		font('Life: '+str(mario.life),WHITE,BLACK,700,100,32)
		font('Point: '+str(mario.point),WHITE,BLACK,100,100,32)
		if mario.life <= 0:
			font('Game Over',BLACK,WHITE,500,500,32)
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
			distMario += 5
		if move == 'left':
			personnage = marioLeft
			mario.moveLeft(5)
			distMario -= 5
		if down == True:
			mario.down(6)
			downtime -= 1
			if downtime == 0:
				downtime = 20
				down = ''
				downed = True
		GameOver = touchBlock()
		GameOVEr = GameOVer(Enemy)
		GameOVER = GameOVer(Enemy2)
		killl = killEnemy(Enemy)
		kill = killEnemy(Enemy2)
		timerevive = mario.LifeCount(1,GameOVER,GameOver,GameOVEr,timerevive)
		mario.PointCount(10,kill,killl)
		mario.display()
		mario.showMario(timerevive)
		Enemy.MoveEnemy(1)
		Enemy2.MoveEnemy(2)
		Enemy.ShowEnemy()
		Enemy2.ShowEnemy()
		Enemy.resetX()
		Enemy2.resetX()
		if mario.xmario >= 650:
			Block.MoveBlock(5)
			mario.moveLeft(5)
		Block.ShowBlock()
		print('dist',distMario)
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
