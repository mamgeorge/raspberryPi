# python\sens_pacman.py

from espeak import espeak
from sense_hat import SenseHat
import sens_defn
import curses
import time

## definitions
sensehat = SenseHat( )
sensehat.low_light = True
sensehat.set_rotation( 180 )

stdscr = curses.initscr( )
curses.noecho( )
curses.cbreak( )
stdscr.keypad( True )

msg = "GO!"
px = 4 ; py = 4
qx = 2 ; qy = 2

## beg
sensehat.show_message( msg , text_colour = sens_defn.G )
sensehat.set_pixel( qx , qy , 255 , 0 , 0 )
sensehat.set_pixel( px , py , 255 , 255 , 0 )

## exec
while True:

	akey = stdscr.getch( )

	##
	if akey == ord( 'q' ) or akey == ord( ' ' ): break
	elif akey == curses.KEY_LEFT	: px = px - 1
	elif akey == curses.KEY_RIGHT	: px = px + 1
	elif akey == curses.KEY_UP		: py = py - 1
	elif akey == curses.KEY_DOWN	: py = py + 1

	if px > 7 : px = 7
	if px < 0 : px = 0
	if py > 7 : py = 7
	if py < 0 : py = 0

	##
	sensehat.set_pixel( px , py , 255 , 255 , 0 )
	time.sleep( 0.1 )
	sensehat.set_pixel( px , py , 0 , 0 , 0 )

	if px == qx and py == qy:
		print( "BANG!" )
		espeak.synth( "BANG!" ) # espeak not closing connection
		sensehat.set_pixel( qx , qy , 255 , 0 , 0 )

## end
curses.nocbreak( )
stdscr.keypad( False )
curses.echo( )
curses.endwin( )

print( "DONE" )
sensehat.clear( sens_defn.V )
time.sleep( 2 )
sensehat.clear( )

