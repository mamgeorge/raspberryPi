# /home/pi/python/gpio/gpio_ledOne.py

# https://thepihut.com/blogs/raspberry-pi-tutorials/27968772-turning-on-an-led-with-your-raspberry-pis-gpio-pins
# RPi max 51mA from all pins
# resistor 206 ohm for 10mm drawing 3.3V
# LED ( longer leg is anode )

import RPi.GPIO as GPIO
import time

#### init
GPIO.setmode( GPIO.BCM )
GPIO.setwarnings( False )
pin10mm = 21 #pin_40 = BCM_21 longer anode

sleepLen = .02
frequency = 500
dtyCycleRng = 50

#### func
def blink( pin ):

	GPIO.setup( pin , GPIO.OUT )
	#GPIO.output( pin , GPIO.LOW ) # if reversing pins
	GPIO.output( pin , GPIO.HIGH )
	time.sleep( 1 )
	print( "BLINK: " + str( GPIO.HIGH ) + " / " + str( GPIO.LOW ) )

def glows( pin ):
	GPIO.setup( pin , GPIO.LOW )
	pwm_led = GPIO.PWM( pin , frequency )
	pwm_led.start( dtyCycleRng )

	for dc in range ( 0 , dtyCycleRng ):
		pwm_led.ChangeDutyCycle( dc )
		time.sleep( sleepLen )

	for dc in range ( dtyCycleRng , 0 , -1 ):
		pwm_led.ChangeDutyCycle( dc )
		time.sleep( sleepLen )

	pwm_led.ChangeDutyCycle( 0 )
	print( "GLOW" )

#### exec
blink( pin10mm )
glows( pin10mm )

#### fini
GPIO.cleanup( )
print( "DONE (anode: pwr, cathode: " + str(pin10mm)  + ")" )
