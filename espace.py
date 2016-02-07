import pygame,sys,random
from pygame import *
pygame.init()
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
YELLOW = (255, 255, 0)
star = pygame.image.load('Star')
def font(e,g,b,x,y,s):
	fontObj = pygame.font.Font('freesansbold.ttf', s)
	textSurfaceObj = fontObj.render(str(e), True, g, b)
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.center = (x, y)
	DISPLAYSURF.blit(textSurfaceObj,textRectObj)
def spaceship(x,y):
	pygame.draw.circle(DISPLAYSURF, WHITE, (x,y - 15), 50,50)
	pygame.draw.rect(DISPLAYSURF, WHITE, (x - 50, y - 20, 100, 110))
	pygame.draw.polygon(DISPLAYSURF, WHITE, ((x - 50,y - 25), (x - 100,y + 25), (x - 50,y + 25)))
	pygame.draw.polygon(DISPLAYSURF, WHITE, ((x + 50,y - 25), (x + 100,y + 25), (x + 50,y + 25)))
def ball(x,y):
	pygame.draw.rect(DISPLAYSURF, BLUE, (x, y, 20, 50))
	pygame.draw.rect(DISPLAYSURF, WHITE, (x + 4, y + 4, 10, 40))
min = 50
max = 750
xstar = []
ystar = []
xship = 375
yship = 600
for a in range(800):
	if a % 100 == 0:
		for s in range(10):
			xstar.append(random.randint(min,max))
			ystar.append(a)
xmeteo = []
ymeteo = []
damage = []
level = 1
def rite(level):
	global xmeteo, ymeteo
	for a in range(1):
		d = random.randint(1,40)
		if d <= level:
			xmeteo.append(random.randint(50,750))
			ymeteo.append(-50)
			damage.append(0)
DISPLAYSURF = pygame.display.set_mode((800,800))
pygame.display.set_caption('Hello World!')
meteorite = pygame.image.load('Meteorite')
start = True
dir = ' '
fire = False
xfire = []
yfire = []
countime = 5
br = False
lend = 0
pressed = False
while True:
	if start == True:
		DISPLAYSURF.fill(BLACK)
		rite(level)
		level += 0.0001
		for f in range(len(xmeteo)):
			if damage[f] != 2:
				DISPLAYSURF.blit(meteorite,(xmeteo[f],ymeteo[f]))
				ymeteo[f] += 7
				if ymeteo[f] >= 810:
					ymeteo.remove(ymeteo[f])
					xmeteo.remove(xmeteo[f])
					damage.remove(damage[f])
				if f >= len(ymeteo) - 1:
					break
			else:
				ymeteo.remove(ymeteo[f])
				xmeteo.remove(xmeteo[f])
				damage.remove(damage[f])
				if f >= len(ymeteo) - 1:
					break
		for s in range(len(xstar)):
			DISPLAYSURF.blit(star,(xstar[s],ystar[s]))
			ystar[s] += 10
			if ystar[s] >= 810:
				ystar[s] = 0
		spaceship(xship,yship)
		if dir == 'left':
			xship -= 4
		if dir == 'right':
			xship += 4
		if fire == True:
			if lend == 0:
				if pressed == True:
					xfire.append(xship)
					yfire.append(yship - 15)
					lend = 20
			for x in range(len(yfire)):
				if x == len(yfire) - 1:
					break
				ball(xfire[x],yfire[x])
				yfire[x] -= 15
				if yfire[x] <= -10:
					yfire.remove(yfire[x])
					xfire.remove(xfire[x])
				if x == len(yfire) - 1:
					break
		for a in range(len(yfire)):
			for s in range(len(xmeteo)):
				if yfire[a] >= ymeteo[s] - 15 and yfire[a] <= ymeteo[s] + 15:
					if xfire[a] >= xmeteo[s] - 50 and xfire[a] <= xmeteo[s] + 50:
						damage[s] += 1
						yfire.remove(yfire[a])
						xfire.remove(xfire[a])
				if a >= len(xfire) - 1:
					br = True
					break
			if br == True:
				br = False
				break
		if lend != 0:
			lend -= 1
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if event.type == KEYDOWN:
			if event.key == K_a:
				dir = 'left'
			if event.key == K_d:
				dir = 'right'
			if event.key == K_w:
				pressed = True
				fire = True
				countime = 5
		else:
			dir = ' '
			pressed = False
			if countime != 0:
				countime -= 1
			else:
				xfire = []
				yfire = []
	pygame.display.update()
