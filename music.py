#import os
import os.path

def mushic():
	for song in "Stars.mp3":
		songPath = os.path.join("~/Downloads/", song)
		os.system('afplay "{}"'.format(songPath))
mushic()
