import pygame,sys
from pygame import *
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
YELLOW = (255, 255, 0)
DISPLAYSURF = pygame.display.set_mode((1260,720))
pygame.display.set_caption('Hello World!')
pygame.init()
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
def graduation():
	for x in range(13):
		pygame.draw.line(DISPLAYSURF, BLACK, (x * 100,-10),(x * 100,800), 4)
	for y in  range(8):
		pygame.draw.line(DISPLAYSURF, BLACK, (-10,y * 100),(1300,y * 100), 4)
def che():
	pygame.draw.rect(DISPLAYSURF, BLACK, (0, 700, 1260, 100))
	pygame.draw.rect(DISPLAYSURF, BLACK, (1200, 0, 100, 800))
def font(e,g,b,x,y,s):
	fontObj = pygame.font.Font('freesansbold.ttf', s)
	textSurfaceObj = fontObj.render(str(e), True, g, b)
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.center = (x, y)
	DISPLAYSURF.blit(textSurfaceObj,textRectObj)
squarex= []
squarey = []
freespacex = []
freespacey = []
def makesquare():
	global squarex, squarey
	for x in range(13):
		squarex.append((x * 100) + 1)
		squarex.append((x * 100) + 100)
		freespacex.append((x * 100) + 1)
		freespacex.append((x* 100) + 100)
	for y in range(8):
		squarey.append((y * 100) + 1)
		squarey.append((y * 100) + 100)
		freespacey.append((y * 100) + 1)
		freespacey.append((y * 100) + 100)
def cross(x,y):
	pygame.draw.line(DISPLAYSURF, BLACK, (x,y),(x + 95,y + 95), 6)
	pygame.draw.line(DISPLAYSURF, BLACK, (x + 95,y),(x,y + 95), 6)
def cercle(x,y):
	pygame.draw.circle(DISPLAYSURF, BLACK, (x + 50,y + 50), 50,3)
makesquare()
mustcross = []
mustcercle = []
def ngang():
	shortBubbleSort(mustcercle)
	shortBubbleSort(mustcross)
	for x in range(len(mustcercle)):
		if x % 2 == 0:
			chose = mustcercle[x]
			naligne = 0
			for y in range(len(mustcercle)):
				if y % 2 == 0:
					if chose + 100 == mustcercle[y]:
						if mustcercle[x + 1] == mustcercle[y]:
							chose = mustcercle[y]
							naligne += 1
					if naligne == 4:
						return True
	for x in range(len(mustcross)):
		chose = mustcross[x]
		naligne = 0
		for y in range(len(mustcross)):
			if chose + 100 == mustcross[y]:
					chose = mustcross[y]
					naligne += 1
			if naligne == 4:
				return True

xm = 0
ym = 0
clicked = False
turn = 'first'
while True:
	DISPLAYSURF.fill(WHITE)
	graduation()
	che()
	font('x: ' + str(xm) + '      y: '+ str(ym),WHITE,BLACK,150,700,32)
	for x in range(len(mustcross)):
		if x % 2 == 0:
			cross(mustcross[x],mustcross[x + 1])
	for x in range(len(mustcercle)):
		if x % 2 == 0:
			cercle(mustcercle[x],mustcercle[x + 1])
	if clicked == True:
		clicked = False
		for x in range(len(squarex)):
			if x % 2 == 0:
				if xm <= squarex[x + 1] and xm >= squarex[x]:
					for y in range(len(squarey)):
						if y % 2 == 0:
							if ym <= squarey[y + 1] and ym >= squarey[y]:
								#cross(squarex[x],squarey[y])
								if turn == 'first':
									mustcross.append(squarex[x])
									mustcross.append(squarey[y])
									turn = 'second'
								else:
									mustcercle.append(squarex[x])
									mustcercle.append(squarey[y])
									turn = 'first'
								freespacex.remove(squarex[x])
								freespacex.remove(squarex[x + 1])
								freespacey.remove(squarey[y])
								freespacey.remove(squarey[y + 1])
	'''if ngang() == True:
		font('Win!',BLACK,WHITE,375,375,32)'''
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if event.type == 4:
			xm,ym = event.pos
		if event.type == MOUSEBUTTONUP:
			xm,ym = event.pos
			clicked = True
		else:
			clicked = False
	pygame.display.update()
