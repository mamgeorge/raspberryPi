# /home/pi/python/gpio/pi_traffic.py

import RPi.GPIO as GPIO
import time
import signal
import sys

# setup for PiTraffic; has (3) 470 ohm resistors
# if pin 1 is North...
# pi_traffic EAST  | pi_traffic WEST facing
yval = 13 # pin 33 | yval = 22 # pin 15
rval = 19 # pin 35 | rval = 27 # pin 13
gval = 26 # pin 37 | gval = 17 # pin 11
grnd = 39 # pin 39 | grnd = 09 # pin 09, not used programmatically

piTraffic = [ rval , yval , gval ]

base = 1 # seconds

GPIO.setmode( GPIO.BCM )
GPIO.setwarnings( False )
for pin in piTraffic:
	GPIO.setup( pin , GPIO.OUT )

def allLightsOff( signal , frame ):

	for pin in piTraffic:
		GPIO.output( pin , False )
	GPIO.cleanup( )
	sys.exit( 0 )

def clear ( ):
	signal.signal( signal.SIGINT, allLightsOff )

def showLights( ):

	for pin in piTraffic:
		GPIO.output( pin , True ) ; time.sleep( base )

	time.sleep( 2 )

	for pin in piTraffic:
		GPIO.output( pin , False) ; time.sleep( base )

# main
print( "lights" )

clear( )
showLights( )

