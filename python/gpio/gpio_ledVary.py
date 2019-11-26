# /home/pi/python/gpio_ledVary.py

import RPi.GPIO as GPIO
import time

#### init
GPIO.setmode( GPIO.BCM ) # BOARD
GPIO.setwarnings( False )

pins = [ 16 , 20 , 21 ] # red , grn , blu
sleepLen = .02
frequency = 500
dtyCycleRng = 50

#### exec
for pin in pins:

	GPIO.setup( pin , GPIO.OUT )
	pwm_led = GPIO.PWM( pin , frequency )
	pwm_led.start( dtyCycleRng )

	for dc in range ( 0 , dtyCycleRng ):
		pwm_led.ChangeDutyCycle( dc )
		time.sleep( sleepLen )

	for dc in range ( dtyCycleRng , 0 , -1 ):
		pwm_led.ChangeDutyCycle( dc )
		time.sleep( sleepLen )

	print( pin )
	pwm_led.ChangeDutyCycle( 0 )

#### fini
GPIO.cleanup( ) # sets pins to nuetral
print( "DONE" )
