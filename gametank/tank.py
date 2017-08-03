import pygame,sys,os,string
from pygame import *
# account,level,unlock,exp,expmax
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
YELLOW = (255, 255, 0)
DISPLAYSURF = pygame.display.set_mode((800,800))
DISPLAYSURF.fill(BLACK)
account = open("info.doc","a+")
account.seek(0)
pygame.draw.rect(DISPLAYSURF, WHITE, (375, 600, 10, 50))
accoun = account.read()
#print(accoun)
na = str(accoun).split(':')
#print(na)
info = []
name = []
rest = []
high = []
for s in range(len(na)):
	if s % 2 == 0:
		name.append(na[s])
	else:
		rest.append(na[s])
na = str(accoun).split(';')
for s in range(len(na)):
	if s != 0:
		info.append(na[s])
	if s % 8 == 7:
		print(na[s])
		high.append(na[s])
print(name)
print(info)
pygame.draw.rect(DISPLAYSURF, WHITE, (375, 600, 15, 50))
pygame.init()
pygame.display.set_caption('Hello World!')
pygame.draw.rect(DISPLAYSURF, WHITE, (375, 600, 20, 50))
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
pygame.draw.rect(DISPLAYSURF, WHITE, (375, 600, 22, 50))
dir2 = 'shit'
life = 20
life2 = 6
import time
import random
fie = False
counttime2 = 50
timecount = random.randint(85,150)
xposition = 1
show = True
count = 10
costume = 1
countair = random.randint(80,150)
pygame.draw.rect(DISPLAYSURF, WHITE, (375, 600, 25, 50))
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
pygame.draw.rect(DISPLAYSURF, WHITE, (375, 600, 27, 50))
countw = 0
modeh = False
quit = False
counth = 100
weapon = False
unlocked = [1]
locked = False
unlocked2 = False
def tankex(x,y):
	pygame.draw.rect(DISPLAYSURF, BLACK, (x,y, 50 , 50))
	pygame.draw.rect(DISPLAYSURF, BLACK, (x+60,y, 50 , 50))
def tank(x,y):
	pygame.draw.rect(DISPLAYSURF, BLACK, (x, y, 100, 50))
	pygame.draw.rect(DISPLAYSURF, BLACK, (x+25,50+y, 50, 25))
pygame.draw.rect(DISPLAYSURF, WHITE, (375, 600, 30, 50))
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
def tank2c5(x,y):
	pygame.draw.rect(DISPLAYSURF, BLACK, (x, y, 100, 50))
	pygame.draw.rect(DISPLAYSURF, BLACK, (x,y-50,30,50))
	pygame.draw.rect(DISPLAYSURF, BLACK, (x+70,y-50,30,50))
def tank2c6(x,y):
	pygame.draw.rect(DISPLAYSURF, BLACK, (x, y, 125, 100))
	pygame.draw.rect(DISPLAYSURF, BLACK, (x + 13, y - 25, 25, 50))
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

locked = False
pygame.draw.rect(DISPLAYSURF, WHITE, (375, 600, 40, 50))
def shortBubbleSort(alist):
	exchanges = True
	passnum = len(alist)-1
	while passnum > 0 and exchanges:
		exchanges = False
		for i in range(passnum):
			if alist[i]>alist[i+1]:
				exchanges = True
				temp = alist[i]
				alist[i] = alist[i+1]
				alist[i+1] = temp
			passnum = passnum-1
def cos():
	global changec,clicked,costume,locked,unlocked,money,unlocked2,life2,timefire
	DISPLAYSURF.fill(WHITE)
	font('BACK',BLACK,WHITE,35,750,32)
	font('CUSTOM',BLACK,WHITE, 425, 375,32)
	pygame.draw.polygon(DISPLAYSURF, BLACK, ((450,400), (450,425), (475,412)))
	pygame.draw.polygon(DISPLAYSURF, BLACK, ((425,400), (425,425), (400,412)))
	font(costume,BLACK, WHITE, 433, 412,32)
	if clicked == True:
		if mousex >= 450 and mousex <= 475 and mousey >= 400 and mousey <= 425:
			if costume + 1 > 6:
				costume = 1
			else:
				costume += 1
			clicked = False
		if mousex >= 400 and mousex <= 425 and mousey >= 400 and mousey <= 425:
			if costume - 1 < 1:
				costume = 6
			else:
				costume -= 1
			clicked = False
		if mousex >= 10 and mousex <= 70 and mousey >= 740 and mousey <= 755:
			if locked == False:
				changec = False
	if costume == 1:
		tank2(x2,y2)
		locked = False
	elif costume == 2:
		tank2c2(x2,y2)
		if perlevel >= 2:
			locked = False
		else:
			font('Locked! Level 2 will unlock',BLACK,WHITE,x2,y2 - 50,32)
			locked = True
	elif costume == 3:
		tank2c3(x2,y2)
		if perlevel >= 3:
			locked = False
		else:
			font('Locked! Level 3 will unlock',BLACK,WHITE,x2,y2 - 100,32)
			locked = True
	elif costume == 4:
		tank2c4(x2,y2)
		if perlevel >= 4:
			locked = False
		else:
			font('Locked! Level 4 will unlock',BLACK,WHITE,x2,y2 - 50,32)
			locked = True
	elif costume == 5:
		tank2c5(x2,y2)
		effect()
		if unlocked == 'True':
			locked = False
		else:
			font('Locked! Buy: 3000',BLACK,WHITE,x2,y2 - 50,32)
			font('BUY',WHITE,BLACK,375,150,32)
			locked = True
			if mousex >= 300 and mousex <= 450 and mousey >= 100 and mousey <= 200:
				font('BUY',WHITE,BLACK,375,150,45)
				if clicked == True:
					if money >= 3000:
						money -= 3000
						unlocked = 'True'
						locked = False
						clicked = False
	elif costume == 6:
		tank2c6(x2,y2)
		effect()
		if unlocked2 == 'True':
			locked = False
			life2 = 10
			timefire = 1000
		else:
			font('Locked! Buy: 4000',BLACK,WHITE,x2,y2 - 50,32)
			font('BUY',WHITE,BLACK,375,150,32)
			locked = True
			if mousex >= 300 and mousex <= 450 and mousey >= 100 and mousey <= 200:
				font('BUY',WHITE,BLACK,375,150,45)
				if clicked == True:
					if money >= 4000:
						money -= 4000
						unlocked2 = 'True'
						locked = False
						clicked = False
						life2 = 10
	if costume != 6:
		life2 = 6
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
		global lent,timefire,coldtime,special,listsp,listy,life, show2, x4, costume
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
			if costume != 6:
				timefire = 200
			else:
				timefire = 1000
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
def banc5():
	global pressed, lend, listxc,listyc,life, show2, x4, mun
	if pressed == True:	
		if lend == 0:
			if mun == 'r':
				listxc.append(x2)
				listyc.append(y2)
				pressed = False
				lend = 25
				mun = 'l'
			elif mun == 'l':
				listxc.append(x2 + 50)
				listyc.append(y2)
				pressed = False
				lend = 25
				mun = 'r'
	if listxc != []:
		for b in range(len(listxc)):
			if b >= len(listxc):
				break
			fire(listxc[b],listyc[b])
			for z in range(len(listyc)):
				listyc[z] -= 5
			for f in range(len(listyc)):
				if f >= len(listyc) :
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
	global x2, y2, xw, yw, x, y, life, countw, weapon,costume
	spwea(xw,yw)
	yw -= 5
	if xw > x:
		xw -= 5
	if xw < x:
		xw += 5
	if yw <= 10:
		DISPLAYSURF.blit(explosion,(xw - 25,yw + 50))
		if costume != 6:
			life -= 1
		else:
			life -= 2
		countw = 1000
		weapon = False
def reset():
	global start, x, y, ca, can2, x2, y2, bum, yposition, xposition, mousex, mousey, dir, bum2, dir2, life, life2, fie, counttime, timecount, xposition, show, count, counttime2, special, listsp
	global listy, timefire, coldtime,lent, listxc, listyc, lend, costume
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
	life = 20
	if costume != 6:
		life2 = 6
	if costume == 6:
		life2 = 10
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
	global counttime2, start, life2, money, costume
	counttime2 -= 1
	font('You lose!',BLACK, WHITE,350,375,32)
	if counttime2 == 0:
		start = False
		counttime2 = 50
		if costume != 6:
			life2 = 6
		if costume == 6:
			life2 = 10
		if money != 0:
			money -= 50
def win():
	global counttime, life, exp, money
	counttime -= 1
	font('You Win!',BLACK, WHITE, 350,375,32)
	if counttime == 0:
		life = 20
		counttime = 50
		exp += 2
		money += 100
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
	global yposition, xposition, x2, life2,costume
	fire(xposition,yposition)
	yposition += 5
	if yposition == 750:
		if xposition > x2 and xposition < x2 + 100:
			if costume != 6:
				life2 -= 1
			else:
				life2 -= 0.5
def pcban2():
	global ylist, xlist, x2, life2,costume
	for b in range(len(xlist)):
		if b >= len(xlist):
			break
		fire(xlist[b],ylist[b])
		ylist[b] += 5
		if ylist[b] > 755:
			if xlist[b] > x2 and xlist[b] < x2 + 100:
				if costume != 6:
					life2 -= 1
				else:
					life2 -= 0.5
			xlist.remove(xlist[b])
			ylist.remove(ylist[b])

def move():
	global dir2, can2, x2,costume
	if dir2 == 'right':
		if can2 == True:
			if costume != 6:
				x2 += 5
			else:
				x2 += 1
	if dir2 == 'left':
		if can == True:
			if costume != 6:
				x2 -= 5
			else:
				x2 -= 1
pygame.draw.rect(DISPLAYSURF, WHITE, (375, 600, 45, 50))
def effect():
	global costume
	if costume == 5:
		font('Effect: Speed of normal attack is higher than normal(double gun barrel)',BLACK,WHITE,500,300,15)
	if costume == 6:
		font('Effect: Move slower than normal but it has more life. No normal attack but the time of special attack is more than normal. The power of special weapon is more than normal.',BLACK,WHITE,600,300,10)
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
	if costume == 5:
		tank2c5(x2,y2)
	if costume == 6:
		tank2c6(x2,y2)
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
def bartype(x,y):
	pygame.draw.rect(DISPLAYSURF, WHITE, (x,y, 200 , 25))
def replace(file, search_for, replace_with):
	#print('search: ',search_for,' replace: ',replace_with)
	# replace strings in a text file
	back = os.path.splitext(file)[0] + ".bak"
	temp = os.path.splitext(file)[0] + ".tmp"
	try:
		# remove old temp file, if any
		os.remove(temp)
	except os.error:
		pass
	fi = open(file)
	fo = open(temp, "w")
	for s in fi.readlines():
		fo.write(str.replace(s, search_for, replace_with))
		#print('s: ',s)
	fi.close()
	fo.close()
	try:
		# remove old backup file, if any
		os.remove(back)
	except os.error:
		pass
	# rename original to backup...
	os.rename(file, back)
	# ...and temporary to original
	os.rename(temp, file)
def tkmk():
	global info, name, rest
	account = open("info.doc", "a+")
	account.seek(0)
	accoun = account.read()
	na = str(accoun).split(':')
	info = []
	name = []
	rest = []
	for s in range(len(na)):
		if s % 2 == 0:
			name.append(na[s])
		else:
			rest.append(na[s])
	na = str(accoun).split(';')
	for s in range(len(na)):
		if s != 0:
			info.append(na[s])
timport = 100
def log_in():
	global p,let,pas,finish,restr,printlogin,clicked,mousex,mousey,typeletter,letteraccount,typepass,passaccount,finishletter,finishpass,p,info,perlevel,unlocked,exp,expmax,money,unlocked2,defaut,loged,logout,login,timport
	tkmk()
	restr = False
	if printlogin == True:
		bartype(600,100)
		font('Account:',WHITE,BLACK,700,80,25)
		bartype(600,200)
		font('Password:',WHITE,BLACK,700,150,25)
		font('Login',BLACK,WHITE,600,275,32)
	if clicked == True:
		if mousex >= 450 and mousex <= 750 and mousey >= 75 and mousey <= 125:
			typeletter = True
			letteraccount = ''
			clicked = False
			typepass = False
			finishpass = True
			pas = p * len(passaccount)
		if mousex >= 450 and mousex <= 750 and mousey >= 175 and mousey <= 225:
			typepass = True
			passaccount = ''
			clicked = False
			typeletter = False
			finishletter = True
			let = letteraccount
	if mousex >= 400 and mousex <= 700 and mousey >= 235 and mousey <= 325:
		font('Login',BLACK,WHITE,600,275,45)
		if clicked == True:
			finishletter = True
			finishpass = True
	if typeletter == True:
		typepass = False
		finishpass = True
		font(str(letteraccount),BLACK,WHITE,700,110,20)
		let = letteraccount
		if finish == True:
			finishletter = True
			let = letteraccount
			typeletter = False
	if finishletter == True:
		font(str(let),BLACK,WHITE,700,110,20)
	if typepass == True:
		typeletter = False
		finishletter = True
		font(str(p * len(passaccount)),BLACK,WHITE,700,210,20)
		pas = p * len(passaccount)
		if finish == True:
			finishpass = True
			pas = p * len(passaccount)
			typepass = False
	if finishpass == True:
		font(str(pas),BLACK,WHITE,700,210,20)
	if finish == True:
		if finishletter == True:
			if finishpass == True:
				for a in range(len(name)):
					#print('let: ',let,' name[a]: ',name[a])
					if let == name[a]:
						if passaccount == info[(a * 8)]:
							perlevel = info[(a * 8) + 1]
							perlevel = int(perlevel)
							unlocked = info[(a * 8) + 2]
							exp = info[(a * 8) + 3]
							exp = int(exp)
							expmax = perlevel * 10
							expmax = int(expmax)
							money = info[(a * 8) + 5]
							money = int(money)
							unlocked2 = info[(a * 8) + 6]
							highscore = info[(a * 8) + 7]
							defaut = a
							printlogin = False
							finish = False
							loged = True
							logout = False
							letteraccount = ''
							passaccount = ''
							let = None
							pas = None
							finishpass = False
							finishletter = False
							login = False
							break
						else:
							if timport != 0:
								font('Wrong!',BLACK,WHITE,375,375,32)
								timport -= 1
							else:
								finish = False
								finishletter = False
								finishpass = False
								timport = 50
					else:
						if timport != 0:
							font('Wrong!',BLACK,WHITE,375,320,32)
							timport -= 1
						else:
							finish = False
							finishletter = False
							finishpass = False
							timport = 50
def signup():
	global login,printre,clicked,mousex,mousey,typeletter,letteraccount,typepass,passaccount,pas,p,let,finish,finishletter,finishpass,name,already,passe,restr,account,accoun,name,info,rest
	login = False
	tkmk()
	if printre == True:
		bartype(450,100)
		bartype(450,200)
	if clicked == True:
		if mousex >= 150 and mousex <= 550 and mousey >= 75 and mousey <= 125:
			typeletter = True
			letteraccount = ''
			clicked = False
			typepass = False
			finishpass = True
			pas = p * len(passaccount)
		if mousex >= 150 and mousex <= 550 and mousey >= 175 and mousey <= 225:
			typepass = True
			passaccount = ''
			clicked = False
			typeletter = False
			finishletter = True
			let = letteraccount
	if typeletter == True:
		font(str(letteraccount),BLACK,WHITE,550,110,20)
		if finishletter == True:
			finishletter = True
			let = letteraccount
			typeletter = False
	if finishletter == True:
		font(str(let),BLACK,WHITE,550,110,20)
	if typepass == True:
		font(str(p * len(passaccount)),BLACK,WHITE,550,210,20)
		if finish == True:
			finishpass = True
			pas = p * len(passaccount)
			typepass = False
	if finishpass == True:
		font(str(pas),BLACK,WHITE,550,210,20)
	if finish == True:
		#print(name)
		for a in range(len(name)):
			#print('sign up let: ',let,' name[a]: ',name[a])
			if let == name[a]:
				already = True
				passe = False
				break
			else:
				already = False
				if finishletter == True:
					if finishpass == True:
						passe = True
	#print('account: ',let,' pass: ',passaccount)
	if passe == True:
		if already == False:
			if letteraccount != '' and passaccount != '':
				new = ':' + str(let)+':;'+str(passaccount)+';1;False;0;10;100;False;0'
				account.write(new)
				account.close()
				tkmk()
				finish = False
				finishpass = False
				finishletter = False
				letteraccount = ''
				passaccount = ''
				restr = False
				printre = False
				passe = False
	#print('account: ',let,'pass: ',passaccount)
def savegame():
	old = name[(defaut)]+':;'+info[(defaut * 8)]+';'+info[(defaut * 8) + 1] + ';' + info[(defaut * 8) + 2] + ';' + info[(defaut * 8) + 3] + ';' + info[(defaut * 8) + 4] + ';' + info[(defaut * 8) + 5]+';'+info[(defaut * 8) + 6] + ';' + info[(defaut*8) + 7]
	new = name[defaut] + ':;'+ info[(defaut * 7)]+';'+ str(perlevel) + ';'+ str(unlocked) + ';'+ str(exp) + ';'+ str(expmax) + ';' + str(money) + ';' + str(unlocked2)
	replace('info.doc',old,new)
def startgame():
	global coldtime,countw,perlevel,show2,level,exp,expmax,fie,bum2,count,show,yposition2,xposition2,x2,special,weapon,lend,counth,just,xh,yh,y2,score,speed
	DISPLAYSURF.fill(WHITE)
	cold = (1000 - coldtime) / 10
	barcold(645,75,cold)
	w = (1000 - countw) / 10
	barcold(645,115,w)
	score += int(speed)
	speed += 0.00001
	font(score,BLUE,WHITE,600,15,20)
	font(life,BLACK,WHITE,15,15,32)
	font(life2,BLACK,WHITE,30,755,32)
	font('QUIT',BLACK,WHITE,750,400,32)
	font('Level: '+str(perlevel),BLACK,WHITE, 740,750,32)
	aircraft(x3,y3)
	airmove()
	airfire()
	if show2 == True:
		per(x4,y4)
		permove()
		perfire()
	if mousex >= 730 and mousex <= 775 and mousey >= 390 and mousey <= 415:
		if clicked == True:
			reset()
	if life <= 0:
		win()
		tankex(x,y)
		show2 = True
		if level == 1:
			level = 2
	if exp >= expmax:
		perlevel += 1
		exp = 0
		expmax += 10
	pcmove()
	if level == 1:
		level1()
		if life != 0:
			tank(x,y)
	else:
		level2()
		if life != 0:
			tankc2(x,y)
	if life2 <= 0:
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
		if costume != 5:
			if costume != 6:
				ban()
		else:
			banc5()
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
pygame.draw.rect(DISPLAYSURF, WHITE, (375, 600, 50, 50))
bumlevel = False
ylist = []
xlist = []
score = 0
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
speed = 1
listxc = []
listyc = []
lend = 0
pressed = False
level = 1
modest = False
modec = False
letteraccount = ''
passaccount = ''
login = False
typepass = False
typeletter = False
letterac = ''
finish = False
perlevel = 1
exp = 0
expmax = 10
printlogin = True
printre = True
defaut = ''
loged = False
restr = False
already = False
timemachine = 50
passe = False
logout = True
just = True
money = 0
mun = 'r'
finishletter = False
finishpass = False
p = '*'
let = ''
pas = ''
pygame.draw.rect(DISPLAYSURF, WHITE, (375, 600, 100, 50))
while True:
	DISPLAYSURF.fill(BLACK)
	'''if typeletter == False:
		letteraccount = ''
	if typepass == False:
		passaccount = '' '''
	tkmk()
	shortBubbleSort(high)
	if printlogin == True:
		font('LOG IN',BLACK,WHITE,700, 50,32)
	else:
		font('Welcome back '+str(name[defaut])+'!',WHITE,BLACK,450,50,24)
	if loged == True:
		font('Log out',BLACK,WHITE,700,50,32)
		'''for f in range(3):
			font(high[f],WHITE,BLACK,125,400 + (f * 10),32)'''
	font('Money: '+str(money) + ' $',WHITE,BLACK,100,125,32)
	font('PLAY',BLACK,WHITE,375,375,32)
	font('CUSTOM',BLACK,WHITE,375,425,32)
	font('HELP',BLACK,WHITE,375,475,32)
	font('Level: '+str(perlevel),WHITE,BLACK,100,50,32)
	font('Exp: '+str(exp)+'/'+str(expmax),WHITE,BLACK,100,80,32)
	font('Save',BLACK,WHITE,375,700,32)
	if printlogin != False:
		font('REGISTER',BLACK,WHITE,550,50,32)
	if login == True:
		log_in()
	else:
		if restr != True:
			passaccount = ''
			letteraccount = ''
			finish = False
			login = False
			finishetter = False
			finishpass = False
	if logout == True:
		if just == True:
			perlevel = 1
			unlocked = [1]
			exp = 0
			expmax = 10
			money = 0
			loged = False
			printlogin = True
			printre = True
			letteraccount = ''
			just = False
	if restr == True:
		signup()
	if already == True:
		font("It has already!",BLACK,WHITE,375,375,70)
		timemachine -= 1
		if timemachine == 0:
			timemachine = 50
			already = False
	if clicked == True:
		if mousex >= 325 and mousex <= 425 and mousey >= 350 and mousey <= 400:
			start = True
		if mousex >= 650 and mousex <= 750 and mousey >= 25 and mousey <= 75:
			if logout == True:
				if login == False:
					login = True
				else:
					login = False
			else:
				logout = True
				just = True
			clicked = False
		if mousex >= 500 and mousex <= 600 and mousey >= 25 and mousey <= 75:
			if restr == False:
				restr = True
			else:
				restr = False
			clicked = False
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
	if mousex >= 325 and mousex <= 425 and mousey >= 675 and mousey <= 725:
		font('Save',BLACK,WHITE,375,700,45)
		if clicked == True:
			if loged == True:
				savegame()
	if modec == True:
		font('CUSTOM',BLACK,WHITE,375,425,45)
	if mousex >= 325 and mousex <= 450 and mousey >= 475 and mousey <= 525:
		font('HELP',BLACK,WHITE,375,475,45)
	if help == True:
		helpme()
	if changec == True:
		cos()
	if start == True:
		startgame()
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
			'''if login == True:
				if event.key != 13:
					if event.key != 8:
						letteraccount += str(chr(int(event.key)))
						passaccount += str(chr(int(event.key)))'''
			if event.key == K_a:
				letteraccount += 'a'
				passaccount += 'a'
			if event.key == K_b:
				letteraccount += 'b'
				passaccount += 'b'
			if event.key == K_c:
				letteraccount += 'c'
				passaccount += 'c'
			if event.key == K_d:
				letteraccount += 'd'
				passaccount += 'd'
			if event.key == K_e:
				letteraccount += 'e'
				passaccount += 'e'
			if event.key == K_f:
				letteraccount += 'f'
				passaccount += 'f'
			if event.key == K_g:
				letteraccount += 'g'
				passaccount += 'g'
			if event.key == K_h:
				letteraccount += 'h'
				passaccount += 'h'
			if event.key == K_i:
				letteraccount += 'i'
				passaccount += 'i'
			if event.key == K_k:
				letteraccount += 'k'
				passaccount += 'k'
			if event.key == K_l:
				letteraccount += 'l'
				passaccount += 'l'
			if event.key == K_m:
				letteraccount += 'm'
				passaccount += 'm'
			if event.key == K_n:
				letteraccount += 'n'
				passaccount += 'n'
			if event.key == K_o:
				letteraccount += 'o'
				passaccount += 'o'
			if event.key == K_p:
				letteraccount += 'p'
				passaccount += 'p'
			if event.key == K_q:
				letteraccount += 'q'
				passaccount += 'q'
			if event.key == K_r:
				letteraccount += 'r'
				passaccount += 'r'
			if event.key == K_s:
				letteraccount += 's'
				passaccount += 's'
			if event.key == K_t:
				letteraccount += 't'
				passaccount += 't'
			if event.key == K_u:
				letteraccount += 'u'
				passaccount += 'u'
			if event.key == K_v:
				letteraccount += 'v'
				passaccount += 'v'
			if event.key == K_w:
				letteraccount += 'w'
				passaccount += 'w'
			if event.key == K_x:
				letteraccount += 'x'
				passaccount += 'x'
			if event.key == K_y:
				letteraccount += 'y'
				passaccount += 'y'
			if event.key == K_z:
				letteraccount += 'z'
				passaccount += 'z'
			if event.key == 8:
				for s in range(len(letteraccount)):
					if s == len(letteraccount) - 1:
						break
					letterac += letteraccount[s]
				letteraccount = letterac
				for s in range(len(passaccount)):
					if s == len(passaccount) - 1:
						break
					passac += passaccount[s]
				passaccount = passac
			else:
				letterac = ''
				passac = ''
			if event.key == 13:
				finish = True
			else:
				finish = False
		elif event.type != KEYDOWN:
			dir2 = 'shit'
			fie = False
			letterac = ''
	pygame.display.update()
