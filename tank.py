import pygame,sys
from pygame import *
import time
import random
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
mousex = 0
mousey = 0
dir = 'right'
bum2 = False
dir2 = 'shit'
life = 5
life2 = 5
fie = False
counttime2 = 50
timecount = random.randint(85,150)
xposition = 1
show = True
count = 10
costume = 1
def tank(x,y):
	pygame.draw.rect(DISPLAYSURF, BLACK, (x, y, 100, 50))
	pygame.draw.rect(DISPLAYSURF, BLACK, (x+25,50+y, 50, 25))
def tank2(x,y):
	pygame.draw.rect(DISPLAYSURF, BLACK, (x, y, 100, 50))
	pygame.draw.rect(DISPLAYSURF, BLACK, (x+25,y-25, 50, 25))
def tank2c2(x,y):
	tank2(x,y)
	pygame.draw.polygon(DISPLAYSURF, BLACK, ((x,y), (x,y+25), (x-25,y)))
	pygame.draw.polygon(DISPLAYSURF, BLACK, ((x+100,y), (x+100,y+25), (x+125,y)))
def tank2c3(x,y):
	pygame.draw.circle(DISPLAYSURF, BLACK, (x + 45,y), 50,50)
	pygame.draw.rect(DISPLAYSURF, BLACK, (x+35,y -100, 15,50))
def tank2c4(x,y):
	pygame.draw.polygon(DISPLAYSURF, BLACK, ((x,y+50),(x+100,y+50),(x+50,y),(x+35,y)))
	pygame.draw.rect(DISPLAYSURF, BLACK, (x+35,y - 25, 15,50))
def fire(x,y):
	pygame.draw.circle(DISPLAYSURF, BLACK, (x,y), 5, 0)
def font(e,g,b,x,y,s):
	fontObj = pygame.font.Font('freesansbold.ttf', s)
	textSurfaceObj = fontObj.render(str(e), True, g, b)
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.center = (x, y)
	DISPLAYSURF.blit(textSurfaceObj,textRectObj)
explosion = pygame.image.load('ex.png')
counttime = 50
start = False
clicked = False
changec = False
help = False
special = False
listsp = []
listy = []
timefire = 200
coldtime = 0
lent = 15
while True:
	DISPLAYSURF.fill(BLACK)
	font('PLAY',BLACK,WHITE,375,375,32)
	font('COSTUME',BLACK,WHITE,375,425,32)
	font('HELP',BLACK,WHITE,375,475,32)
	if clicked == True:
		if mousex >= 325 and mousex <= 425 and mousey >= 350 and mousey <= 400:
			start = True
	if clicked == True:
		if mousex >= 275 and mousex <= 450 and mousey >= 400 and mousey <= 450:
			changec = True
		if mousex >= 325 and mousex <= 450 and mousey >= 425 and mousey <= 525:
			help = True
	if help == True:
		DISPLAYSURF.fill(WHITE)
		font('LEFT ARROW, RIGHT ARROW: MOVE',BLACK,WHITE,200,15,20)
		font('UP ARROW: FIRE',BLACK,WHITE,100,60,20)
		font('SPACE: SPECIAL ATTACK',BLACK, WHITE,140,105,20)
		font('QUIT',BLACK,WHITE,35,750,32)
		if clicked == True:
			if mousex >= 10 and mousex <= 70 and mousey >= 740 and mousey <= 755:
				help = False
	if changec == True:
		DISPLAYSURF.fill(WHITE)
		font('QUIT',BLACK,WHITE,35,750,32)
		font('COSTUME',BLACK,WHITE, 425, 375,32)
		pygame.draw.polygon(DISPLAYSURF, BLACK, ((450,400), (450,425), (475,412)))
		pygame.draw.polygon(DISPLAYSURF, BLACK, ((425,400), (425,425), (400,412)))
		font(costume,BLACK, WHITE, 433, 412,32)
		if clicked == True:
			if mousex >= 450 and mousex <= 475 and mousey >= 400 and mousey <= 425:
				if costume + 1 > 4:
					costume = 1
				else:
					costume += 1
				clicked = False
			if mousex >= 400 and mousex <= 425 and mousey >= 400 and mousey <= 425:
				if costume - 1 < 1:
					costume = 4
				else:
					costume -= 1
				clicked = False
			if mousex >= 10 and mousex <= 70 and mousey >= 740 and mousey <= 755:
				changec = False
		if costume == 1:
			tank2(x2,y2)
		elif costume == 2:
			tank2c2(x2,y2)
		elif costume == 3:
			tank2c3(x2,y2)
		elif costume == 4:
			tank2c4(x2,y2)
	if start == True:
		print('listsp: ',listsp)
		print('listy: ',listy)
		DISPLAYSURF.fill(WHITE)
		font('Cold time: '+str(coldtime),BLACK,WHITE,650,75,32)
		font(life,BLACK,WHITE,15,15,32)
		font(life2,BLACK,WHITE,15,755,32)
		font('QUIT',BLACK,WHITE,750,400,32)
		if mousex >= 730 and mousex <= 775 and mousey >= 390 and mousey <= 415:
			start = False
			x = 400
			y = 0
			can = True
			can2 = True
			x2 = 400
			y2 = 750
			bum = False
			yposition = y + 60
			yposition2 = 231
			mousex = 0
			mousey = 0
			dir = 'right'
			bum2 = False
			dir2 = 'shit'
			life = 5
			life2 = 5
			fie = False
			counttime2 = 50
			timecount = random.randint(85,150)
			xposition = 1
			show = True
			count = 10
			counttime = 50
			special = False
			listsp = []
			listy = []
			timefire = 200
			coldtime = 0
			lent = 15

		if life == 0:
			counttime -= 1
			font('You Win!',BLACK, WHITE, 350,375,32)
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
			timecount = random.randint(150,250)
			yposition = y + 60
			xposition = x + 25
			bum = True
		if yposition > 750:
			DISPLAYSURF.blit(explosion,(xposition - 50,yposition - 100))
		if bum == True:
			fire(xposition,yposition)
			yposition += 5
			if yposition == 750:
				if xposition > x2 - 90 and xposition < x2 + 90:
					life2 -= 1
		if life2 == 0:
			counttime2 -= 1
			font('You lose!',BLACK, WHITE,350,375,32)
			if counttime2 == 0:
				start = False
				counttime2 = 50
				life2 = 5
		if dir2 == 'right':
			if can2 == True:
				x2 += 5
		if dir2 == 'left':
			if can == True:
				x2 -= 5
		if life2 != 0:
			if costume == 1:
				tank2(x2,y2)
			if costume == 2:
				tank2c2(x2,y2)
			if costume == 3:
				tank2c3(x2,y2)
			if costume == 4:
				tank2c4(x2,y2)
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
		if special == True:
			if timefire != 0:
				timefire -= 1
				if lent == 0:
					lent = 15
					listsp.append(x2)
					listy.append(y2)
				else:
					lent -= 1
				for b in range(len(listsp)):
					if b >= len(listsp):
						break
					fire(listsp[b],listy[b])
					for z in range(len(listy)):
						listy[z] -= 5
					for f in range(len(listy)):
						#print('y: ',y)
						#print(listy)
						if f >= len(listy):
							break
						if listy[f] == 5:
							DISPLAYSURF.blit(explosion,(listsp[f],listy[f]))
							if listsp[f] > x - 90 and listsp[f] < x + 90:
								life -= 1
							listsp.remove(listsp[f])
							listy.remove(listy[f])
			else:
				special = False
				coldtime = 1000
				timefire = 200
				listsp = []
				listy = []
	if coldtime != 0:
		coldtime -= 1
	for event in pygame.event.get():
		if event.type == MOUSEBUTTONUP:
			clicked = True
			mousex, mousey = event.pos
		else:
			clicked = False
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == KEYDOWN:
			#space
			if event.key == 32:
				if coldtime <= 0:
					special = True
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
