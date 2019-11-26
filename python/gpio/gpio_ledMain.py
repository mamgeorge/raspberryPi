# /home/pi/python/gpio/pi_lamps.py

# https://thepihut.com/blogs/raspberry-pi-tutorials/27968772-turning-on-an-led-with-your-raspberry-pis-gpio-pins
# RPi ( 60mA )
# 330ohm resistor ( Orange, Orange, Brown, Gold )
# LED ( longer leg is anode )

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
