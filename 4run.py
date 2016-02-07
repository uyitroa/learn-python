import pygame,sys
import random
from pygame import *
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
YELLOW = (255, 255, 0)
DISPLAYSURF = pygame.display.set_mode((800,800))
pygame.display.set_caption('Hello World!')
xposition = [0,785]
yposition = [0,785]
direction = ['upleft',' ','upright',' ','up',' ','left',' ','right']
fpsClock = pygame.time.Clock()
mul = 2
def iftouching(n):
	for x in range(len(n)):
		for i in range(len(n)):
			if x != i:
				if n[x] == n[i] - 45 or n[x] == n[i]:
					touchx = 'TRUE'
					break
				else:
					touchx = 'FALSE'
	return touchx
plus = ['down','left','right']
while True:
	print("Xposition: ")
	for x in range(mul):
		pygame.draw.circle(DISPLAYSURF, RED,(xposition[x],yposition[x]),30,30)
		print("ok2 ",x)
		print("Xposition: ",xposition[x])
		print("Yposition: ",yposition[x])
	if iftouching(xposition) == 'TRUE':
		if iftouching(yposition) == 'TRUE':
			mul *= 2
			xposition.append(0)
			xposition.append(785)
			yposition.append(0)
			yposition.append(785)
			print("ok4")
			if mul / 2 >= 5:
				direction.append(random.choice(plus))
	fpsClock.tick(30)
	for x in range(mul):
		pygame.draw.circle(DISPLAYSURF, BLACK,(xposition[x],yposition[x]),30,30)
	print("INt(mul/2): ",int(mul/2))
	for x in range(int(mul/2)):
		print("ok5")
		if direction[x] == 'downleft':
			xposition[0] -= 5	
			yposition[0] -= 5
			xposition[1] += 5
			yposition[1] += 5
		elif direction[x] == 'upleft':
			xposition[0] += 5	
			yposition[0] += 5
			xposition[1] -= 5
			yposition[1] -= 5
		elif direction[x] == 'upright':
			xposition[2] -= 5
			yposition[2] += 5
			xposition[3] += 5
			yposition[3] -= 5
		elif direction[x] == 'downright':
			xposition[2] += 5
			yposition[2] -= 5
			xposition[3] -= 5
			yposition[3] += 5
		elif direction[x] == 'down':
			yposition[x] -= 5
			yposition[x+1] += 5
		elif direction[x] == 'left':
			xposition[x] += 5
			xposition[x+1] -= 5
		elif direction[x] == 'right':
			xposition[x] -= 5
			xposition[x+1] += 5
		elif direction[x] == 'up':
			yposition[x] += 5
			yposition[x+1] -= 5
	print("ok6")
	for x in range(int(mul/2)):
		if xposition[x] == 0 or xposition[x] == 785:
			if direction[x] == 'down':
				direction[x] = 'up'
			elif direction[x] == 'left':
				direction[x] = 'right'
			elif direction[x] == 'right':
				direction[x] = 'left'
			elif direction[x] == 'downleft':
				direction[x] = 'upleft'
			elif direction[x] == 'downright':
				direction[x] = 'upright'
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()
