# //python/servos/motor_L293D.py
# Controlling a DC Motor / Gaven MacDonald
#
# L293D
#
# in1	in2
# 0		1	frwd
# 1		0	back

import RPi.GPIO as GPIO
import time

########################
# setup
print( "Setup L293D" )
GPIO.setmode( GPIO.BCM ) # BOARD
GPIO.setwarnings( False )
sleepLen = .01
frequency = 50
dtyCycleRng = 100

pinM1_POS = 26	# mLFT + wht37
pinM1_NEG = 19	# mLFT - grn35
pinM2_POS = 20	# mRGT + blu38
pinM2_NEG = 16	# mRGT - ylw36

GPIO.setup( pinM1_POS , GPIO.OUT )
GPIO.setup( pinM1_NEG , GPIO.OUT )
GPIO.setup( pinM2_POS , GPIO.OUT )
GPIO.setup( pinM2_NEG , GPIO.OUT )

pwmM1_POS = GPIO.PWM( pinM1_POS , frequency )
pwmM1_NEG = GPIO.PWM( pinM1_NEG , frequency )
pwmM2_POS = GPIO.PWM( pinM2_POS , frequency )
pwmM2_NEG = GPIO.PWM( pinM2_NEG , frequency )

pwmM1_POS.start( 0 )
pwmM1_NEG.start( 0 )
pwmM2_POS.start( 0 )
pwmM2_NEG.start( 0 )

########################
# motions

def moveWheelsForward( ):

	print( "moveWheelsForward" ) # run m1b m2b

	for dc in range ( 0 , dtyCycleRng ):
		pwmM1_POS.ChangeDutyCycle( dc )
		time.sleep( sleepLen )

	for dc in range ( dtyCycleRng , 0 , -1 ):
		pwmM1_POS.ChangeDutyCycle( dc )
		time.sleep( sleepLen )

	for dc in range ( 0 , dtyCycleRng ):
		pwmM2_POS.ChangeDutyCycle( dc )
		time.sleep( sleepLen )

	for dc in range ( dtyCycleRng , 0 , -1 ):
		pwmM2_POS.ChangeDutyCycle( dc )
		time.sleep( sleepLen )

	pwmM1_POS.ChangeDutyCycle( 0 )
	pwmM2_POS.ChangeDutyCycle( 0 )

def moveWheelsBackward( ):

	print( "moveWheelsBackward" ) # run m1a m2a

	for dc in range ( 0 , dtyCycleRng ):
		pwmM1_NEG.ChangeDutyCycle( dc )
		time.sleep( sleepLen )

	for dc in range ( dtyCycleRng , 0 , -1 ):
		pwmM1_NEG.ChangeDutyCycle( dc )
		time.sleep( sleepLen )

	for dc in range ( 0 , dtyCycleRng ):
		pwmM2_NEG.ChangeDutyCycle( dc )
		time.sleep( sleepLen )

	for dc in range ( dtyCycleRng , 0 , -1 ):
		pwmM2_NEG.ChangeDutyCycle( dc )
		time.sleep( sleepLen )

	pwmM1_NEG.ChangeDutyCycle( 0 )
	pwmM2_NEG.ChangeDutyCycle( 0 )

########################
# exec
print( "Execute Tractors" )
try:
	while True:

		moveWheelsForward( )
		moveWheelsBackward( )

except KeyboardInterrupt:
	pass

########################
# fini
print( "Cleanup" )
pwmM1_POS.stop( )
pwmM1_NEG.stop( )
pwmM2_POS.stop( )
pwmM2_NEG.stop( )
GPIO.cleanup( ) # sets pins to nuetral
print( "DONE" )
