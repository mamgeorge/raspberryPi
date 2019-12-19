#!/usr/bin/python

# \\python\comm\gpio_distance.py
# HCSR04 distance

import RPi.GPIO as GPIO
import time

GPIO_ECHO = 20 # pin_38 , BCM_20 orange
GPIO_TRIG = 21 # pin_40 , BCM_21 blue
GPIO.setmode( GPIO.BCM )
GPIO.setup( GPIO_TRIG, GPIO.OUT )
GPIO.setup( GPIO_ECHO, GPIO.IN )

def distance( ):

	GPIO.output( GPIO_TRIG, True )
	time.sleep( 0.00001 )
	GPIO.output( GPIO_TRIG, False )
	startTime = time.time( )
	stopTime = time.time( )

	while GPIO.input( GPIO_ECHO ) == 0:
		startTime = time.time( )

	while GPIO.input( GPIO_ECHO ) == 1:
		stopTime = time.time( )

	# multiply with sonic speed ( 34300 cm/s ) and div by 2 because there and back
	timeElapsed = stopTime - startTime
	dist_CM = ( timeElapsed * 34300 ) / 2
	dist_IN = dist_CM / 2.54
	dist_FT = dist_IN / 12
	print ( "dist: {0:.2f} cm, {1:.2f} in, {2:.2f} ft".format( dist_CM , dist_IN, dist_FT ) )

	return dist_CM

if __name__ == '__main__':

	try:
		while True:

			distance( )
			time.sleep( 1 )

	except KeyboardInterrupt:

		print( "Measurement stopped by User" )
		GPIO.cleanup( )
