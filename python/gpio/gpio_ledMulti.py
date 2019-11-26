# /home/pi/python/gpio_ledMulti.py

# http://www.instructables.com/id/Using-a-RPi-to-Control-an-RGB-LED/

import RPi.GPIO as GPIO
import time

#### init
GPIO.setmode( GPIO.BCM )
GPIO.setwarnings( False )
pinRed = 16
pinGrn = 20
pinblu = 21

#### func
def blink( pin ):

	GPIO.setup( pin , GPIO.OUT )
	GPIO.output( pin , GPIO.HIGH )
	time.sleep( 1 )
	GPIO.output( pin , GPIO.LOW )

#### exec
blink( pinRed )
blink( pinGrn )
blink( pinblu )

#### fini
GPIO.cleanup( )
print( "DONE" )
