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
x = 350
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
countair = random.randint(80,150)
ypo = -1
xpo = -1
y3 = 350
x3 = 15
dire = 'right'
bum3 = False
x4 = 750
xh = x + 25
yh = y
y4 = 5
xpos = x4
ypos = y4
countper = random.randint(150,250)
bum4 = False
where = random.randint(1,2)
dired = 'left'
touch = False
show2 = True
countw = 0
quit = False
counth = 100
weapon = False
def tankex(x,y):
	pygame.draw.rect(DISPLAYSURF, BLACK, (x,y, 50 , 50))
	pygame.draw.rect(DISPLAYSURF, BLACK, (x+60,y, 50 , 50))
def tank(x,y):
	pygame.draw.rect(DISPLAYSURF, BLACK, (x, y, 100, 50))
	pygame.draw.rect(DISPLAYSURF, BLACK, (x+25,50+y, 50, 25))
def tankc2(x,y):
	pygame.draw.rect(DISPLAYSURF, BLACK, (x, y, 100, 50))
	pygame.draw.rect(DISPLAYSURF, BLACK, (x,y+50,30,25))
	pygame.draw.rect(DISPLAYSURF, BLACK, (x+70,y+50,30,25))
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
def aircraft(x,y):
	pygame.draw.rect(DISPLAYSURF, BLACK, (x, y, 100, 50))
def per(x,y):
	pygame.draw.circle(DISPLAYSURF, BLACK, (x,y), 10,10)
	pygame.draw.line(DISPLAYSURF, BLACK, (x,y),(x,y + 15), 4)
def perban():
	global ypos, xpos, x2, life, life2
	fire(xpos,ypos)
	ypos += 5
	if ypos == 750:
		if xpos > x2 and xpos < x2 + 100:
			life2 -= 1
def spwea(x,y):
	pygame.draw.circle(DISPLAYSURF, BLACK, (x,y), 50,50)
def barcold(x,y,s):
	pygame.draw.rect(DISPLAYSURF, BLACK, (x, y, 100, 30))
	pygame.draw.rect(DISPLAYSURF, WHITE, (x, y, s, 50))
def permove():
	global dired, x4, touch
	if dired == 'left':
		x4 -= 5
		if x4 <= x + 100:
			dired = 'right'
			touch = True
	if dired == 'right':
		x4 += 5
		if x4 >= 750:
			dired = 'left'
def perfire():
	global countper, xpos, ypos, bum4, x4, y4
	per(x4,y4)
	if countper != 0:
		countper -= 1
	if countper == 0:
		countper = random.randint(150,250)
		ypos = y4 + 60
		xpos = x4 + 25
		bum4 = True
	if ypos > 750:
		DISPLAYSURF.blit(explosion,(xpos - 50,ypos - 100))
	if bum4 == True:
		perban()
def airban():
	global ypo, xpo, x2, life2, life, x, where
	fire(xpo,ypo)
	if where == 1:
		ypo += 5
	else:
		ypo -= 5
	if ypo == 750:
		if xpo > x2 and xpo < x2 + 100:
			life2 -= 1
	if ypo == 0:
		if xpo > x and xpo < x + 100:
			life -= 1
def airmove():
	global dire, x3
	if dire == 'right':
		x3 += 5
		if x3 == 700:
			dire = 'left'
	if dire == 'left':
		x3 -= 5
		if x3 == 10:
			dire = 'right'
def airfire():
	global countair, xpo, ypo, bum3, x3, y3, where
	aircraft(x3,y3)
	if countair != 0:
		countair -= 1
	if countair == 0:
		where = random.randint(1,2)
		countair = random.randint(150,250)
		ypo = y3 + 60
		xpo = x3 + 25
		bum3 = True
	if ypo > 750:
		DISPLAYSURF.blit(explosion,(xpo - 50,ypo - 100))
	if ypo < 10:
		DISPLAYSURF.blit(explosion,(xpo - 50,ypo - 100))
	if bum3 == True:
		airban()
def fire(x,y):
	pygame.draw.circle(DISPLAYSURF, BLACK, (x + 25,y), 5, 0)
def recta(x,y):
	pygame.draw.rect(DISPLAYSURF, BLACK, (x, y, 100, 50))
def font(e,g,b,x,y,s):
	fontObj = pygame.font.Font('freesansbold.ttf', s)
	textSurfaceObj = fontObj.render(str(e), True, g, b)
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.center = (x, y)
	DISPLAYSURF.blit(textSurfaceObj,textRectObj)
def helpme():
	global help
	DISPLAYSURF.fill(WHITE)
	font('LEFT ARROW, RIGHT ARROW: MOVE',BLACK,WHITE,200,15,20)
	font('UP ARROW: FIRE',BLACK,WHITE,100,60,20)
	font('SPACE: SPECIAL ATTACK',BLACK, WHITE,140,105,20)
	font('DOWN ARROW: SPECIAL WEAPON',BLACK,WHITE,200,145,20)
	font('QUIT',BLACK,WHITE,35,750,32)
	if clicked == True:
		if mousex >= 10 and mousex <= 70 and mousey >= 740 and mousey <= 755:
			help = False

def cos():
	global changec,clicked,costume
	DISPLAYSURF.fill(WHITE)
	font('QUIT',BLACK,WHITE,35,750,32)
	font('CUSTOM',BLACK,WHITE, 425, 375,32)
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
def heavy():
	global xh, yh, x2, life2,listxc, listyc,counth,just, listsp, listy
	recta(xh,yh)
	yh += 5
	if yh == 750:
		counth = 1000
		DISPLAYSURF.blit(explosion,(xh - 25,yh - 50))
		if x2 >= xh and x2 <= xh + 100:
			life2 -= 2
	for b in range(len(listxc)):
		if b >= len(listxc):
			break
		if listyc[b] <= yh and listyc[b] >= yh - 50:
			if listxc[b] >= xh and listxc[b] <= xh + 100:
				counth = 1000
				just = False
				listxc.remove(listxc[b])
				listyc.remove(listyc[b])
	for c in range(len(listsp)):
		if c >= len(listsp):
			break
		if listy[c] <= yh and listy[c] >= yh - 50:
			if listsp[c] >= xh and listsp[c] <= xh + 100:
				counth = 1000
				just = False
				listsp.remove(listsp[c])
				listy.remove(listy[c])
def specialattack():
		global lent,timefire,coldtime,special,listsp,listy,life, show2, x4
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
					if f >= len(listy):
						break
					if listy[f] == 5:
						DISPLAYSURF.blit(explosion,(listsp[f],listy[f]))
						if listsp[f] >= x and listsp[f] < x + 100:
							life -= 1
						if listsp[f] >= x4 - 10 and listsp[f] < x4 + 30:
							show2 = False
						listsp.remove(listsp[f])
						listy.remove(listy[f])
		else:
			special = False
			coldtime = 1000
			timefire = 200
			listsp = []
			listy = []
def ban():
	global pressed, lend, listxc,listyc,life, show2, x4
	if pressed == True:	
		if lend == 0:
			listxc.append(x2)
			listyc.append(y2)
			pressed = False
			lend = 60
	if listxc != []:
		for b in range(len(listxc)):
			if b >= len(listxc):
				break
			fire(listxc[b],listyc[b])
			for z in range(len(listyc)):
				listyc[z] -= 5
			for f in range(len(listyc)):
				if f >= len(listyc):
					break
				if listyc[f] == 5:
					DISPLAYSURF.blit(explosion,(listxc[f] - 25,listyc[f] - 50))
					if listxc[f] >= x and listxc[f] < x + 100:
						life -= 1
					if listxc[f] >= x4 - 10 and listxc[f] < x + 30:
						show2 = False
					listxc.remove(listxc[f])
					listyc.remove(listyc[f])

def specialweapon():
	global x2, y2, xw, yw, x, y, life, countw, weapon
	spwea(xw,yw)
	yw -= 5
	if xw > x:
		xw -= 5
	if xw < x:
		xw += 5
	if yw <= 10:
		DISPLAYSURF.blit(explosion,(xw - 25,yw + 50))
		life -= 1
		countw = 1000
		weapon = False
def reset():
	global start, x, y, ca, can2, x2, y2, bum, yposition, xposition, mousex, mousey, dir, bum2, dir2, life, life2, fie, counttime, timecount, xposition, show, count, counttime2, special, listsp
	global listy, timefire, coldtime,lent, listxc, listyc, lend
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
	listxc = []
	listyc = []
	lend = 60
	xlist = []
	ylist = []
	x3 = 15
	y3 = 350
	xpo = 0
	ypo = 0
	xpos = 750
	ypos = 5
	show2 = True
	bum4 = False
	touch = False
	countper = random.randint(150,250)
	countw = 0
	weapon = False
	x4 = 750
	y4 = 5
	xh = x + 25
	yh = y
	counth = 100
	just = False
def lose():
	global counttime2, start, life2
	counttime2 -= 1
	font('You lose!',BLACK, WHITE,350,375,32)
	if counttime2 == 0:
		start = False
		counttime2 = 50
		life2 = 5
def win():
	global counttime, life
	counttime -= 1
	font('You Win!',BLACK, WHITE, 350,375,32)
	if counttime == 0:
		life = 5
		counttime = 50
def pcmove():
	global dir, x, x4, touch
	if dir == 'right':
		if touch == True:
			dir = 'left'
			touch = False
		else:
			x += 5
		if x == 760:
			dir = 'left'
	elif dir == 'left':
		x -= 5
		if x <= 10:
			dir = 'right'
def pcban():
	global yposition, xposition, x2, life2
	fire(xposition,yposition)
	yposition += 5
	if yposition == 750:
		if xposition > x2 and xposition < x2 + 100:
			life2 -= 1
def pcban2():
	global ylist, xlist, x2, life2
	for b in range(len(xlist)):
		if b >= len(xlist):
			break
		fire(xlist[b],ylist[b])
		ylist[b] += 5
		if ylist[b] > 755:
			if xlist[b] > x2 and xlist[b] < x2 + 100:
				life2 -= 1
			xlist.remove(xlist[b])
			ylist.remove(ylist[b])

def move():
	global dir2, can2, x2
	if dir2 == 'right':
		if can2 == True:
			x2 += 5
	if dir2 == 'left':
		if can == True:
			x2 -= 5

def cosoftank():
	global costume
	if costume == 1:
		tank2(x2,y2)
	if costume == 2:
		tank2c2(x2,y2)
	if costume == 3:
		tank2c3(x2,y2)
	if costume == 4:
		tank2c4(x2,y2)
def level1():
	global life, timecount, xposition, yposition, bum
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
		pcban()
def level2():
	global life, timecount, xposition, yposition, bumlevel
	if life != 0:
		tankc2(x,y)
	if timecount != 0:
		timecount -= 1
	if timecount == 0:
		timecount = random.randint(150,250)
		ylist.append(y + 60)
		ylist.append(y + 60)
		xlist.append(x)
		xlist.append(x+100)
		bumlevel = True
	for c in range(len(ylist)):
		if ylist[c] > 750:
			DISPLAYSURF.blit(explosion,(xlist[c] - 50,ylist[c] - 100))
	if bumlevel == True:
		pcban2()
bumlevel = False
ylist = []
xlist = []
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
listxc = []
listyc = []
lend = 0
pressed = False
level = 1
modest = False
modec = False
while True:
	DISPLAYSURF.fill(BLACK)
	font('PLAY',BLACK,WHITE,375,375,32)
	font('CUSTOM',BLACK,WHITE,375,425,32)
	font('HELP',BLACK,WHITE,375,475,32)
	if clicked == True:
		if mousex >= 325 and mousex <= 425 and mousey >= 350 and mousey <= 400:
			start = True
	if clicked == True:
		if mousex >= 275 and mousex <= 450 and mousey >= 400 and mousey <= 450:
			changec = True
		if mousex >= 325 and mousex <= 450 and mousey >= 425 and mousey <= 525:
			help = True
	if mousex >= 325 and mousex <= 425 and mousey >= 350 and mousey <= 400:
		modest = True
	else:
		modest = False
	if modest == True:
		font('PLAY',BLACK,WHITE,375,375,45)
	if mousex >= 275 and mousex <= 450 and mousey >= 400 and mousey <= 450:
		modec = True
	else:
		modec = False
	if modec == True:
		font('CUSTOM',BLACK,WHITE,375,425,45)
	if help == True:
		helpme()
	if changec == True:
		cos()
	if start == True:
		DISPLAYSURF.fill(WHITE)
		cold = (1000 - coldtime) / 10
		barcold(645,75,cold)
		w = (1000 - countw) / 10
		barcold(645,115,w)
		font(life,BLACK,WHITE,15,15,32)
		font(life2,BLACK,WHITE,15,755,32)
		font('QUIT',BLACK,WHITE,750,400,32)
		font('Level: '+str(level),BLACK,WHITE, 740,750,32)
		aircraft(x3,y3)
		airmove()
		airfire()
		if show2 == True:
			per(x4,y4)
			permove()
			perfire()
		if mousex >= 730 and mousex <= 775 and mousey >= 390 and mousey <= 415:
			if click == True:
				reset()
		if life <= 0:
			win()
			tankex(x,y)
			show2 = True
			if level == 1:
				level = 2
		pcmove()
		if level == 1:
			level1()
			if life != 0:
				tank(x,y)
		else:
			level2()
			if life != 0:
				tankc2(x,y)
		if life2 == 0:
			lose()
			tankex(x2,y2)
		move()
		if life2 != 0:
			cosoftank()
		if fie == True:
			yposition2 = y2 - 50
			xposition2 = x2 + 50
			bum2 = True
		if bum2 == True:
			ban()
		if yposition2 < 1:
			if show == True:
				count -= 1
				DISPLAYSURF.blit(explosion,(xposition2 - 50,yposition2 - 125 ))
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
			specialattack()
	if countw != 0:
		countw -= 1
		weapon = False
	if weapon == True:
		if countw <= 0:
			specialweapon()
	if coldtime != 0:
		coldtime -= 1
	if lend != 0:
		lend -= 1
	if counth != 0:
		counth -= 1
		if counth == 0:
			just = True
	if counth == 0:	
		if just == True:
			xh = x
			yh = y
			just = False
		heavy()
	for event in pygame.event.get():
		if event.type == 4:
			mousex, mousey = event.pos
		if event.type == MOUSEBUTTONUP:
			clicked = True
			mousex, mousey = event.pos
		else:
			clicked = False
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == KEYDOWN:
			if event.key == 310:
				quit = True
			if event.key == 113:
				if quit == True:
					pygame.quit()
					sys.exit()
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
			if event.key == K_DOWN:
				weapon = True
				xw = x2
				yw = y2
			if event.key == K_UP:
				fie = True
				show = True
				pressed = True
			else:
				fie = False
				pressed = False
		elif event.type != KEYDOWN:
			dir2 = 'shit'
			fie = False
	pygame.display.update()
