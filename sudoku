import numpy as np
grille = [
[9,0,0,1,0,0,0,0,5],
[0,0,5,0,9,0,2,0,1],
[8,0,0,0,4,0,0,0,0],
[0,0,0,0,8,0,0,0,0],
[0,0,0,7,0,0,0,0,0],
[0,0,0,0,2,6,0,0,9],
[2,0,0,3,0,0,0,0,6],
[0,0,0,2,0,0,9,0,0],
[0,0,1,9,0,4,5,7,0]
]

class Loli:
	def __init__(self,grille):
		self.grille = grille
		self.number = [1,2,3,4,5,6,7,8,9]
	
	def main(self):

		for y in range(len(self.grille)):
			line = self.grille[y]
			indices = [i for i, x in enumerate(my_list) if x == 0] # indexes of 0
			for x in indices:
				square_y,square_x = self.get_square(y,x)
				# start with square
				known = self.grille[square_x:square_x+3] + self.grille[square_y:square_y+3]
				squarelist = self.remove_list([1,2,3,4,5,6,7,8,9],list(set(self.number).intersection(known)))
				#line
				linelist = self.remove_list([1,2,3,4,5,6,7,8,9],list(set(self.number).intersection(line)))
				#column
				my_grille = np.array(self.grille)
				columnlist = self.remove_loist([1,2,3,4,5,6,7,8,9],list(set(self.number).intersection(list(my_grille[:,x]))))
				

	def get_square(self,y,x): # which square at the position
		# args: y,x
		# return square y, square x
		square_line = int(x/3) * 3
		square_column = int(y/3) * 3

		return square_column,square_line

	def remove_list(self,lst,removelst):
		# args: list to remove, remove list element
		#return list removed
		for x in removelst:
			lst.remove(removelst)
		return lst

	
