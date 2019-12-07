# cd C:\Users\mamge\OneDrive\Documents\5Personal\Technology\raspberryPi\python
# pip install colorama
# http://svn.python.org/projects/stackless/trunk/Lib/encodings/cp720.py
from colorama import init, Fore, Back, Style
import datetime, time, sys, random

init()
def sampleLoad(count):

	spaces = 100
	anyProgress = [0] * count
	print("\n" * ( count + 0 ) ) # make space for bars
	while any( ctr < spaces for ctr in anyProgress):

		time.sleep(0.01)
		# Randomly increment one of our progress values
		unfinished = [(i, v) for (i, v) in enumerate(anyProgress) if v < spaces]
		index, _ = random.choice(unfinished)
		anyProgress[index] += 1

		# Draw the progress bars
		# f:u2588 l:u258c r:u2590 u:u2580 d:u2584
		print( u"\u001b[1000D" ), # Move left
		print( u"\u001b[" + str(count) + "A" ), # Move up
		for progress in anyProgress:
			width = progress / 4
			chars = Style.BRIGHT + Fore.CYAN + u"\u2584" * int(width) + Style.RESET_ALL
			blnks = " " * ( 25 - int(width) )
			print( "[" + chars + blnks + "] " + str( progress ) )

	timer = str( datetime.datetime.now( ) )
	print( Style.BRIGHT + Fore.GREEN + "DONE: " + timer + Style.RESET_ALL )

timer = str( datetime.datetime.now( ) )
print( Style.BRIGHT + Fore.GREEN + "INIT: " + timer + Style.RESET_ALL ),
sampleLoad(4)

