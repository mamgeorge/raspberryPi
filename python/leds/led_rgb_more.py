# /home/pi/python/leds/led_rgb_more.py

# python python/gpio/pi_lamps.py
# Common Cathode RGB LEDs are R, (-), G, B 
# Common Anode.. RGB LEDs are R, (+), G, B 
# RGB LED diffused , 10mm dia , 4 Pin 
# red: 700 mcd	, grn: 2100 mcd	 , blu: 900 mcd ( milliCandela typical brightness ) 
# red: 623 nm	, grn: 523 nm	 , blu: 467 nm ( wavelength ) 
# red: 1.8-2.2V, grn: 3.0-3.4V	 , blu: 3.0-3.4V ( @ 20mA current ) 
# 50 degree viewing angle

import RPi.GPIO as GPIO
import time

#### init
GPIO.setmode( GPIO.BCM ) # BOARD
GPIO.setwarnings( False )
pinRed = 12 # pin 32 | pinRed = 25 # pin 22
pinGRD = 34 # pin 34 | pinGRD = 20 # pin 20 ( not used programmatically )
pinGrn = 16 # pin 36 | pinGrn = 24 # pin 18
pinBlu = 20 # pin 38 | pinBlu = 23 # pin 16 

pins = [ pinRed , pinGrn , pinBlu ] # red , grn , blu
sleepLen = .02
frequency = 500
dtyCycleRng = 50

#### func
def blink( pin ):

	GPIO.setup( pin , GPIO.OUT )
	GPIO.output( pin , GPIO.HIGH )
	time.sleep( 1 )
	GPIO.output( pin , GPIO.LOW )

def varies( pin ):

	GPIO.setup( pin , GPIO.OUT )
	pwm_led = GPIO.PWM( pin , frequency )
	pwm_led.start( dtyCycleRng )

	for dc in range ( 0 , dtyCycleRng ):
		pwm_led.ChangeDutyCycle( dc )
		time.sleep( sleepLen )

	for dc in range ( dtyCycleRng , 0 , -1 ):
		pwm_led.ChangeDutyCycle( dc )
		time.sleep( sleepLen )

	pwm_led.ChangeDutyCycle( 0 )	
	
def mixed( pinOne , pinTwo ):

	for x in range( 1 ):
	
		GPIO.setup( pinOne , GPIO.OUT )
		GPIO.setup( pinTwo , GPIO.OUT )
		pwm_one = GPIO.PWM( pinOne , frequency )
		pwm_two = GPIO.PWM( pinTwo , frequency )
		pwm_one.start( dtyCycleRng )
		pwm_two.start( dtyCycleRng )

		for dc in range ( 0 , dtyCycleRng ):
			pwm_one.ChangeDutyCycle( dc )
			pwm_two.ChangeDutyCycle( dc )
			time.sleep( sleepLen )

		for dc in range ( dtyCycleRng , 0 , -1 ):
			pwm_one.ChangeDutyCycle( dc )
			pwm_two.ChangeDutyCycle( dc )
			time.sleep( sleepLen )

		pwm_one.ChangeDutyCycle( 0 )	
		pwm_two.ChangeDutyCycle( 0 )	
	
## exec

for pin in pins:
	blink( pin )

for pin in pins:
	varies( pin )

mixed( pinRed , pinBlu )
mixed( pinRed , pinGrn )
mixed( pinBlu , pinGrn )

## fini
GPIO.cleanup( ) # sets pins to nuetral
print( "DONE" )
