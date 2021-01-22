# sensehat_b9.py
#
# sudo apt-get install sense-hat
# https://pymotw.com/2/threading/

from sense_hat import SenseHat
from multiprocessing import Process
import threading
import sens_defn
import sys
import time
import random
import signal

## definitions
sensehat = SenseHat( )
sensehat.low_light = True
sensehat.set_rotation( 180 )

R = sens_defn.R
O = sens_defn.O
Y = sens_defn.Y
G = sens_defn.G
B = sens_defn.B
V = sens_defn.V
Q = sens_defn.Q
C = sens_defn.C
W = sens_defn.W
x = sens_defn.n

colorB9 = [ R, Y, G, B, x ]
colorMG = [ R, O, Y, G, B, V, W , x ]
blinkerType = sys.argv[1]

## functions
def B9( ):
	array = [
	x, R, R, x, x, G, G, x,
	x, R, R, x, x, G, G, x,
	x, x, x, x, x, x, x, x,
	x, Y, G, R, R, G, Y, x,
	x, Y, G, R, R, G, Y, x,
	x, x, x, x, x, x, x, x,
	x, B, Y, R, G, Y, B, x,
	x, Y, R, G, Y, B, Y, x,
	]
	return array

def keyboardInterruptHandler(signal, frame):

	print( "Keyboard Interrupt (ID: {}) OK!".format( signal ) )
	sensehat.clear( )
	exit(0)

def glower( ):

	incr =  .0001

	for clr in range( 0 , 255 , 1 ):

		sensehat.set_pixel( 1 , 0 , ( clr , 0 , 0 ) )
		sensehat.set_pixel( 2 , 0 , ( clr , 0 , 0 ) )
		sensehat.set_pixel( 1 , 1 , ( clr , 0 , 0 ) )
		sensehat.set_pixel( 2 , 1 , ( clr , 0 , 0 ) )

		time.sleep( incr )

	time.sleep( 1 )

	for clr in range( 255 , 0 , -1 ):

		sensehat.set_pixel( 1 , 0 , ( clr , 0 , 0 ) )
		sensehat.set_pixel( 2 , 0 , ( clr , 0 , 0 ) )
		sensehat.set_pixel( 1 , 1 , ( clr , 0 , 0 ) )
		sensehat.set_pixel( 2 , 1 , ( clr , 0 , 0 ) )

		time.sleep( incr )

	for clr in range( 0 , 255 , 1 ):

		sensehat.set_pixel( 5 , 0 , ( 0 , clr , 0 ) )
		sensehat.set_pixel( 6 , 0 , ( 0 , clr , 0 ) )
		sensehat.set_pixel( 5 , 1 , ( 0 , clr , 0 ) )
		sensehat.set_pixel( 6 , 1 , ( 0 , clr , 0 ) )

		time.sleep( incr )

	time.sleep( 1 )

	for clr in range( 255 , 0 , -1 ):

		sensehat.set_pixel( 5 , 0 , ( 0 , clr , 0 ) )
		sensehat.set_pixel( 6 , 0 , ( 0 , clr , 0 ) )
		sensehat.set_pixel( 5 , 1 , ( 0 , clr , 0 ) )
		sensehat.set_pixel( 6 , 1 , ( 0 , clr , 0 ) )

		time.sleep( incr )

def runner( ):

	ly = 3
	for lx in range ( 1 , 7 , 1 ):

		cq = sensehat.get_pixel( lx , ly )
		sensehat.set_pixel( lx , ly + 0 , x )
		sensehat.set_pixel( lx , ly + 1 , x )
		time.sleep( .2 )
		sensehat.set_pixel( lx , ly + 0 , cq )
		sensehat.set_pixel( lx , ly + 1 , cq )

	for lx in range ( 7 , 0 , -1 ):

		cq = sensehat.get_pixel( lx , ly )
		sensehat.set_pixel( lx , ly + 0 , x )
		sensehat.set_pixel( lx , ly + 1 , x )
		time.sleep( .2 )
		sensehat.set_pixel( lx , ly + 0 , cq )
		sensehat.set_pixel( lx , ly + 1 , cq )

def blinkB9( ):

	rng = len( colorB9 ) - 1

	for ctr in range ( 1 , rng*4 , 1 ):

		sensehat.set_pixel( 1 , 6 , B ) if 0 == random.randint( 0, 1 ) else sensehat.set_pixel( 1 , 6 , x )
		sensehat.set_pixel( 2 , 6 , Y ) if 0 == random.randint( 0, 1 ) else sensehat.set_pixel( 2 , 6 , x )
		sensehat.set_pixel( 3 , 6 , R ) if 0 == random.randint( 0, 1 ) else sensehat.set_pixel( 3 , 6 , x )
		sensehat.set_pixel( 4 , 6 , G ) if 0 == random.randint( 0, 1 ) else sensehat.set_pixel( 4 , 6 , x )
		sensehat.set_pixel( 5 , 6 , Y ) if 0 == random.randint( 0, 1 ) else sensehat.set_pixel( 5 , 6 , x )
		sensehat.set_pixel( 6 , 6 , B ) if 0 == random.randint( 0, 1 ) else sensehat.set_pixel( 6 , 6 , x )

		sensehat.set_pixel( 1 , 7 , Y ) if 0 == random.randint( 0, 1 ) else sensehat.set_pixel( 1 , 7 , x )
		sensehat.set_pixel( 2 , 7 , R ) if 0 == random.randint( 0, 1 ) else sensehat.set_pixel( 2 , 7 , x )
		sensehat.set_pixel( 3 , 7 , G ) if 0 == random.randint( 0, 1 ) else sensehat.set_pixel( 3 , 7 , x )
		sensehat.set_pixel( 4 , 7 , Y ) if 0 == random.randint( 0, 1 ) else sensehat.set_pixel( 4 , 7 , x )
		sensehat.set_pixel( 5 , 7 , B ) if 0 == random.randint( 0, 1 ) else sensehat.set_pixel( 5 , 7 , x )
		sensehat.set_pixel( 6 , 7 , Y ) if 0 == random.randint( 0, 1 ) else sensehat.set_pixel( 6 , 7 , x )
		time.sleep( .2 )

def blinkMG( ):

	rng = len( colorMG ) - 1
	#for ctr in range ( 1 , rng , 1 ):
	for ctr in range ( 1 , rng*40 , 1 ):

		lx = random.randint( 1, 6 )
		ly = random.randint( 6, 7 )
		cq = colorMG[ random.randint( 0, rng ) ]
		sensehat.set_pixel( lx , ly , cq )
		time.sleep( .01 )

def runInParallel( *functions ):

	procList = [ ]

	for func in functions:
		process = Process( target=func )
		process.start( )
		procList.append( process )

	for process in procList:
		process.join( )

signal.signal( signal.SIGINT, keyboardInterruptHandler )
sensehat.set_pixels( B9( ) )

## main
while True:

	# threading.Thread( target = glower ).start( )
	# threading.Thread( target = runner ).start( )
	# threading.Thread( target = blinkMG ).start( )
	if blinkerType == '9':
		runInParallel( glower, blinkB9 )
	else:
		runInParallel( glower, runner, blinkMG )
