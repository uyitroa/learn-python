import pygame,sys, random
from pygame import *
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
YELLOW = (255, 255, 0)
min = -5000
max = -4980
x = []
y = []
size = []
oldx = []
z = []
for f in range(95):
	d = random.randint(min,max)
	x.append(d)
	oldx.append(d)
	d = random.randint(100,400)
	y.append(d)
	d = random.randint(10,70)
	size.append(d)
	z.append(80 - d)
	min += 250
	max += 250
myx = 0
myz = -20
DISPLAYSURF = pygame.display.set_mode((800,800))
pygame.display.set_caption('l')
tree = pygame.image.load('Eren')
dir =  'shit'
count = 94
cold = 0
edge0 = False
edge1 = False
go = 's'
while True:
	DISPLAYSURF.fill(BLACK)
	if dir == 'left':
		for s in range(len(x)):
			x[s] += 5
		myx -= 5
	if dir == 'right':
		for s in range(len(x)):
			x[s] -= 5
		myx += 5
	if go == 'up':
		for w in range(len(x)):
			if x[w] <= 850 and x[w] >= - 50:
				size[w] += 1
		myz += 1
	if go == 'down':
		for d in range(len(x)):
			if x[d] <= 850 and x[d] >= - 50:
				size[d] -= 1
		myz -= 1
	if myx <= -4100:
		myx = 0
		#for s in range(len(x)):
		#	x[s] -= 3700
		edge0 = True
		#myx = 3500
	if edge0 == True:
		if cold != 94:
			x[cold] = oldx[count]
			cold += 1
			count -= 1
		else:
			cold = 0
			edge0 = False
			count = 94
			#myx = 3000
	if myx >= 3800:
		myx = 0
		#for s in range(len(x)):
		#	x[s] += 4200
		edge1 = True
		#myx = -4000
	if edge1 == True:
		if count != -1:
			x[count] = oldx[cold]
			count -= 1
			cold += 1
			#myx += 5
		else:
			count = 94
			cold = 0
			edge1 = False
	for f in range(len(x)):
		if x[f] <= 850 and x[f] >= -50:
			if x[f] <= 850 and x[f] >= 799 or x[f] >= -50 and x[f] <= 5:
				if size[f] <= 200:
					pygame.draw.circle(DISPLAYSURF, RED, (x[f],y[f]+1), size[f],size[f])
			else:
				if size[f] <= 200:
					pygame.draw.circle(DISPLAYSURF, RED, (x[f],y[f]), size[f],size[f])

	pygame.draw.line(DISPLAYSURF, WHITE, (175,225),(175,200), 4)
	pygame.draw.line(DISPLAYSURF, WHITE, (175,200),(185,200), 4)
	pygame.draw.line(DISPLAYSURF, WHITE, (625,225),(625,200), 4)
	pygame.draw.line(DISPLAYSURF, WHITE, (625,200),(615,200), 4)
	pygame.draw.line(DISPLAYSURF, WHITE, (175,625),(175,600), 4)
	pygame.draw.line(DISPLAYSURF, WHITE, (175,625),(185,625), 4)
	pygame.draw.line(DISPLAYSURF, WHITE, (625,625),(615,625), 4)
	pygame.draw.line(DISPLAYSURF, WHITE, (625,625),(625,600), 4)
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
				go = 'up'
			if event.key == K_s:
				go = 'down'
		else:
			dir = 'shit'
			go = 's'
	pygame.display.update()
