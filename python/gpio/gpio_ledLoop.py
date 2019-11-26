# /home/pi/python/gpio_ledLoop.py

import RPi.GPIO as GPIO
import time

#### init
GPIO.setmode( GPIO.BCM )
GPIO.setwarnings( False )

#### func
def show_GPIO( lctr , txt_val ):
	pin_led = lctr
	GPIO.setup( pin_led , GPIO.OUT )
	GPIO.output( pin_led , 1 )
	time.sleep( 0.1 )
	GPIO.output( pin_led , 0 )
	print( txt_val , end = " / " )

#### exec
leds = [ "RED" , "GRN" , "BLU" ]
for qctr in range( 1 , 5 ):

	lctr , lmax , incr = 4 , 7 , 0

	for lctr in range( lctr , lmax ):
		show_GPIO( lctr , leds[ incr ] )
		lctr += 1
		incr += 1
	print( qctr )

#### fini
GPIO.cleanup( )
print( "DONE" )