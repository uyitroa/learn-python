import pygame,sys
from pygame import *
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
YELLOW = (255, 255, 0)
DISPLAYSURF = pygame.display.set_mode((800,800))
pygame.display.set_caption('Attack on titan')
distance = [500,1300,1900,2500,3500]
distancett = [800,1600,2100]
anotherdis = [800,1600,2100]
distance2 = [800]
#1600,2100,3000
ttt = False
n = 'ok'
touchbyr = False
pygame.init()
def base():
	pygame.draw.rect(DISPLAYSURF, BLACK, (0,750, 800 , 800))
def wipe(x,y,x2,y2):
	pygame.draw.line(DISPLAYSURF, BLACK, (x,y),(x2,y2),4)
def touchWall(xr,yr):
	global distance, ttt, n, distancett,distance2,touchbyr
	tach = False
	for x in range(len(distance)):
		if distance[x] < 800 and distance[x] > 0:
			if yr > 450:
				if xr >= distance[x] - 5 and xr <= distance[x] + 105:
					tach = True
					touchbyr = False
					break
				else:
					tach = False
	for b in range(len(distancett)):
		if distancett[b] < 800 and distancett[b] > 0:
			if yr > 250:
				if tach == True:
					break
				if xr >= distancett[b] - 5 and xr <= distancett[b] + 200:
					tach = True
					ttt = True
					n = b
					touchbyr = False
					break
				else:
					tach = False
					ttt = False
	for c in range(len(distance2)):
		print('yr: ',yr)
		print('distance2: ',distance2[c])
		print('xr: ',xr)
		if distance2[c] < 900 and distance2[c] > 0:
			if yr < 500:
				if tach == True:
					break
				if xr >= distance2[c] - 50 and xr <= distance2[c] + 50:
					tach = True
					touchbyr = True
					break
				else:
					tach = False
	return tach
def font(e,g,b,x,y,s):
	fontObj = pygame.font.Font('freesansbold.ttf', s)
	textSurfaceObj = fontObj.render(str(e), True, g, b)
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.center = (x, y)
	DISPLAYSURF.blit(textSurfaceObj,textRectObj)
def helpme():
	global help,ym,xm
	DISPLAYSURF.fill(WHITE)
	font('KEY a,d: MOVE',BLACK,WHITE,80,15,20)
	font('Key w: jump',BLACK,WHITE,70,60,20)
	font('Left mouse: attack',BLACK, WHITE,100,105,20)
	font('KEY q:Fire a grapple',BLACK,WHITE,120,145,20)
	font('KEY e: pull yourself toward the grapple',BLACK,WHITE,200,200,20)
	font('To kill Titan, you must slashing his nape. His nape is red.',WHITE,BLACK,300,250,20)
	font('QUIT',BLACK,WHITE,35,750,32)
	if clicked == True:
		if xm >= 10 and xm <= 70 and ym >= 740 and ym <= 755:
			help = False
eren = pygame.image.load('Eren')
eren2 = pygame.image.load('Eren2')
sensor = pygame.image.load('Sensor')
sword = pygame.image.load('Sword')
sword2 = pygame.image.load('Sword2')
atk = pygame.image.load('Atk')
atk2 = pygame.image.load('Atk2')
titan = pygame.image.load('Titan')
titanatk = pygame.image.load('titan2')
titanatk2 = pygame.image.load('Titan3')
xposi = 0
yposi = 0
xeren = 350
yeren = 680
xm = -1
ym = -2
direren = 'shit'
dirren = 'Z'	
count = 0
use = False
fly = False
touch = False
just = True
counte = 25
clicked = False
perso = 0
attack = False
kill = False
timewin = 30
d = 's'
dirt = ['left','right','left']
titanrest = len(distancett)
start = False
help = False
modest = False
win = 30
timeatk = 20
coldatk = 100
numberti = ''
atktitan = False
costitan = 1
while True:
	DISPLAYSURF.fill(BLACK)
	font('PLAY',BLACK,WHITE,375,375,32)
	font('HELP',BLACK,WHITE,375,475,32)
	if clicked == True:
		if xm >= 325 and xm <= 425 and ym >= 350 and ym <= 400:
			start = True
	if clicked == True:
		if xm >= 325 and xm <= 450 and ym >= 425 and ym <= 525:
			help = True
	if xm >= 325 and xm <= 425 and ym >= 350 and ym <= 400:
		modest = True
	else:
		modest = False
	if modest == True:
		font('PLAY',BLACK,WHITE,375,375,45)
	if xm >= 325 and xm <= 450 and ym >= 425 and ym <= 525:
		font('HELP',BLACK,WHITE,375,475,45)
	if help == True:
		helpme()
	if start == True:	
		DISPLAYSURF.fill(WHITE)
		base()
		font('TITAN: '+str(titanrest),BLACK,WHITE,700,50,32)
		#font(str(xposi >= distance[0] - 5 or xposi <= distance[0] + 105),BLACK,WHITE,100,375,32)
		for f in range(len(distancett)):
			if xeren <= distancett[f]:
				numberti = f
				atktitan = True
		if xm > xeren:
			perso = eren
			sao = sword
		if xm < xeren:
			perso = eren2
			sao = sword2
		if clicked == True:
			if out != 0:
				if sao == sword:
					sao = atk
				else:
					sao = atk2
				out -= 1
				attack = True
			else:
				clicked = False
				attack = False
		if attack == True:
			for x in range(len(distancett)):
				if yeren >= 430 and yeren <= 480:
					if xeren >= distancett[x] + 170 and xeren <= distancett[x] + 230:
						if sao == atk2 or sao == sword2:
							kill = True
							d = x
							break
		'''if atktitan == True:
			if timeatk != 0:
				timeatk -= 1
			else:
				if costitan == 1:
					costitan = 2
					timeatk = 20
				else:
					costitan = 1
					timeatk = 20
					atktitan = False'''
		if kill == True:
			if timewin != 0:
				font('Killed',WHITE,BLACK,375,100,32)
				timewin -= 1
			else:
				timewin = 30
				titanrest -= 1
				kill = False
				distancett.remove(distancett[d])
		if titanrest == 0:
			if win != 0:
				font('You Win',WHITE,BLACK,375,100,32)
				win -= 1
			else:
				win = 30
				distancett = [distance[0] + 300,distance[1] + 300,distance[2] + 200,distance[3] + 500]
				titanrest = 4
		for x in range(len(distancett)):
			if distancett[x] < 800 and distancett[x] >-200:
				#if atktitan != True:
				DISPLAYSURF.blit(titan,(distancett[x],325))
				'''else:
					if numberti == x:
						if costitan == 1:
							DISPLAYSURF.blit(titanatk,(distancett[x],325))
							distancett[x] -= 1
						else:
							DISPLAYSURF.blit(titanatk2,(distancett[x],325))
							distancett[x] -= 1'''
				if yeren > 350:
					if xeren < distancett[x] + 200 and xeren >= distancett[x] - 25:
						xeren -= 5
					elif xeren < distancett[x] + 225 and xeren >= distancett[x] + 90:
						xeren += 5
		for x in range(len(distance)):
			if distance[x] < 800 and distance[x] > -100:
				pygame.draw.rect(DISPLAYSURF, BLACK, (distance[x],450,100, 800))
				if yeren > 300:
					if xeren < distance[x] + 75 and xeren >= distance[x] - 50:
						if yeren > 500:
							xeren -= 5
						touch = True
					elif xeren < distance[x] + 105 and xeren >= distance[x] + 50:
						if yeren > 500:
							xeren += 5
						touch = True
					else:
						touch = False
		for x in range(len(distance2)):
			if distance2[x] < 900 and distance2[x] > -100:
				pygame.draw.rect(DISPLAYSURF, BLACK, (distance2[x],50,50, 75))
		for s in range(len(distancett)):
			if dirt[s] == 'right':
				distancett[s] += 2
				anotherdis[s] += 2
				if s == 0:
					if anotherdis[s] >= 1050:
						dirt[s] = 'left'
				if s == 1:
					if anotherdis[s] >= 1650:
						dirt[s]  = 'left'
				if s == 2:
					if anotherdis[s] >= 2200:
						dirt[s] = 'left'
			elif dirt[s] == 'left':
				distancett[s] -= 2
				anotherdis[s] -= 2
				if s == 0:
					if anotherdis[s] <= 600:
						dirt[s] = 'right'
				if s == 1:
					if anotherdis[s] <= 1600:
						dirt[s] = 'right'
				if s == 2:
					if anotherdis[s] <= 2000:
						dirt[s] = 'right' 
		if xeren < 200:
			if distance[0] != 500:
				xeren += 5
				for x in range(len(distance)):
					distance[x] += 5
				for x in range(len(distancett)):
					distancett[x] += 5
				for x in range(len(distance2)):
					distance2[x] += 5
		if xeren > 600:
			xeren -= 5
			for x in range(len(distance)):
				distance[x] -= 5
			for x in range(len(distancett)):
				distancett[x] -= 5
			for x in range(len(distance2)):
				distance2[x] -= 5
		if direren == 'left':
			perso = eren2
			sao = sword2
			if xeren >= 0:
				xeren -= 5
		if direren == 'right':
			perso = eren
			sao = sword
			if xeren <= 600:
				xeren += 5
		if dirren == 'jump':
			yeren -= 5
			count += 1
			if count == 15:
				count = 0
				dirren = 'down'
				dowing = True
		if dirren == 'down':
			yeren += 5
			if yeren > 680:
				yeren = 680
				dowing = False
			if yeren >= 385 and yeren < 495:
				if touch == True:
					yeren = 390
					dowing = False
		if use == True:
			if xposi - xeren < 600:
				if yposi - yeren > -600:
					if touchWall(xposi,yposi) == True:
						if ttt != True:
							wipe(xeren + 30,yeren + 35,xposi,yposi)
						if ttt == True:
							if xposi > xeren:
								wipe(xeren + 30, yeren + 35, distancett[n] + 30,yposi )
							else:
								wipe(xeren + 30, yeren + 35, distancett[n] + 190, yposi)
						if fly == True:
							if c != 40:
								if xm > xeren:
									if touch != True:
										xeren += xposi / 40
										if touchbyr != True:
											yeren -= (yposi / 40) 
										else:
											yeren -= (yposi / 40) + 15
								else:
									if touch != True:
										xeren -= xposi / 40
										if touchbyr != True:
											yeren -= (yposi / 40)
										else:
											yeren -= (yposi / 40) + 15
							c += 1
							if c == 40:
								xeren = int(xeren)
								yeren = int(yeren)
								c = 40
					else:
						use = False
						fly = False
						c = 40
		else:
			if dirren != 'jump':
				dirren = 'down'
		if sao == sword:
			DISPLAYSURF.blit(sao,(xeren,yeren - 25))
		elif sao == sword2:
			DISPLAYSURF.blit(sao,(xeren - 50, yeren - 25))
		elif sao == atk:
			DISPLAYSURF.blit(sao,(xeren,yeren))
		else:
			DISPLAYSURF.blit(sao,(xeren - 50, yeren))
		DISPLAYSURF.blit(perso,(xeren,yeren))
		DISPLAYSURF.blit(sensor,(xm - 10,ym - 10))
	for event in pygame.event.get():
		if event.type == MOUSEBUTTONUP:
			xm,ym = event.pos
			clicked = True
			out = 10
		else:
			if start != True:
				clicked = False
		if event.type == 4:
			xm,ym = event.pos
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if event.type == KEYDOWN:
			counte = 25
			if event.key == K_a:
				direren = 'left'
			if event.key == K_d:
				direren = 'right'
			if event.key == K_w:
				if dirren != 'jump':
					if dowing == False:
						if use != True:
							dirren = 'jump'
						else:
							dirren = 'down'
			if event.key == K_q:
				use = True
				if just == True:
					just = False
					xposi = xm
					yposi = ym
					xs = xm
					ys = ym
					c = 0
			if event.key == K_e:
				use = True
				fly = True
		else:
			direren = 'shit'
			use = False
			just = True
			fly = False
			ttt = False
	pygame.display.update()
