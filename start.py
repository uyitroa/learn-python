print("What do you want to check? Enter the first word:")
letter=input()

if letter=='i':
	print("i: insert text left of cursor\n o: insert blank line below cursor\nO: insert blank line above cursor")

elif letter=='a':
	print("a: append text right of cursor")

elif letter=='d':
	print("nx: delete n charaters\nx: delete a charater\nX: delete charater before cursor\ndw: delete word\nndw: delete n word\ndd: delete line\nndd: delete n lines\nD: delete charater for cursor to end of line")

elif letter=='r':
	print("r: replace charater under cursor\ncw: replace a word\nncw: replace n words\nr: repeat last search in same direction\nN: repeat last search in opposite direction\nU: restore current line")

elif letter=='c':
	print("C: change text from cursor to end of line\n: scroll forward one screen\n: scroll backward one screen\n^D: scroll down one-half screen\n^U: scroll up one-half screen")

elif letter=='j':
	print("J: join suceeding line to current cursor line\nnJ: join suceeding n lines to current cursor line")

elif letter=='move':
	print("h: left one space\nj: down one line\nk: up one line\nl: right one space")
	print("$: to end of line\n0: to begining of line\nH: to top line of screen\nM: to middle line of screen\nL: to last line of screen\nG: to last line of file\n1G: to first line of screen")
	print("w: forward word by word\nb: backward word by word")
elif letter=='u':
	print("u: undo last change")
else:
	print("i: insert text left of cursor\no: insert blank line below cursor\nO: insert blank line above cursor\na: append text right of cursor\nnx: delete n charaters\nx: delete a charater\nX: delete charater before cursor\ndw: delete word\nndw: delete n word\ndd: delete line\nndd: delete n lines\nD: delete charater for cursor to end of line\nr: replace charater under cursor\ncw: replace a word\nncw: replace n words\nr: repeat last search in same direction\nN: repeat last search in opposite direction\nU: restore current line\nC: change text from cursor to end of line\n^F: scroll forward one screen\n^B: scroll backward one screen\n^D: scroll down one-half screen\n^U: scroll up one-half screen\nJ: join suceeding line to current cursor line\nnJ: join suceeding n lines to current cursor line\nh: left one space\nj: down one line\nk: up one line\nl: right one space\n$: to end of line\n0: to begining of line\nH: to top line of screen\nM: to middle line of screen\nL: to last line of screen\nG: to last line of file\n1G: to first line of screen\nw: forward word by word\nb: backward word by word\nu: undo last change")
