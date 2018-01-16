import numpy as np

arr = np.array([[1,0,0,1,1,1,0],[0,1,1,1,0,1,0],[1,1,1,1,0,0,1]])
print arr

def analyze(arr,shapex,shapey,minIngre, maxCell):
	solution = []
	test = False
	mushroom = 0
	tomatoes = 0
	x_start = 0
	y_start = 0

	for x in range(shapex):
		for y in range(shapey):
			if mushroom + tomatoes > maxCell: # if total cell bigger than max cell
				mushroom = 0
				tomatoes = 0
				test = "more"
				break
			if arr[y,x] == 0:
				mushroom += 1
			else:
				tomatoes += 1


			if mushroom >= minIngre and tomatoes >= minIngre:
				test = True
		
		if test == True:
			mushroom = 0
			tomatoes = 0
			x_end = x
			y_end = y
			coord = (y_start,x_start,y_end,x_end)
			solution.append(coord)
			print coord
			test = False
			x_start = x + 1
			y_start = 0

	return solution

a = analyze(arr, arr.shape[1],arr.shape[0],1,6)






			
