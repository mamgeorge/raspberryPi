import RPi.GPIO as GPIO
import time

def setupGPIO( motorData ):

	print( "L293D setup" )
	GPIO.setmode( GPIO.BCM ) # BOARD
	GPIO.setwarnings( False )

	GPIO.setup( motorData[ "pinM1_POS" ] , GPIO.OUT )
	GPIO.setup( motorData[ "pinM1_NEG" ] , GPIO.OUT )
	GPIO.setup( motorData[ "pinM2_POS" ] , GPIO.OUT )
	GPIO.setup( motorData[ "pinM2_NEG" ] , GPIO.OUT )

	global pwm_M1POS
	global pwm_M1NEG
	global pwm_M2POS
	global pwm_M2NEG

	pwm_M1POS = GPIO.PWM( motorData[ "pinM1_POS" ] , motorData[ "frequency" ] )
	pwm_M1NEG = GPIO.PWM( motorData[ "pinM1_NEG" ] , motorData[ "frequency" ] )
	pwm_M2POS = GPIO.PWM( motorData[ "pinM2_POS" ] , motorData[ "frequency" ] )
	pwm_M2NEG = GPIO.PWM( motorData[ "pinM2_NEG" ] , motorData[ "frequency" ] )


	pwm_M1POS.start( 0 )
	pwm_M1NEG.start( 0 )
	pwm_M2POS.start( 0 )
	pwm_M2NEG.start( 0 )
	#print( "L293D setup complete" )

########################
# motions

def moveForward( motorData ):

	print( "moveForward" ) # run m1b m2b

	for dc in range ( 0 , motorData[ "dtyCycleRng" ] ):
		pwm_M1POS.ChangeDutyCycle( dc )
		pwm_M2POS.ChangeDutyCycle( dc )
		time.sleep( motorData[ "sleepLen" ] )

	time.sleep( 5 )

	for dc in range ( motorData[ "dtyCycleRng" ] , 0 , -1 ):
		pwm_M1POS.ChangeDutyCycle( dc )
		pwm_M2POS.ChangeDutyCycle( dc )
		time.sleep( motorData[ "sleepLen" ] )

	pwm_M1POS.ChangeDutyCycle( dc )
	pwm_M2POS.ChangeDutyCycle( 0 )

def moveBackward( motorData ):

	print( "moveBackward" ) # run m1a m2a

	for dc in range ( 0 , motorData[ "dtyCycleRng" ] ):
		pwm_M1NEG.ChangeDutyCycle( dc )
		pwm_M2NEG.ChangeDutyCycle( dc )
		time.sleep( motorData[ "sleepLen" ] )

	time.sleep( 5 )

	for dc in range ( motorData[ "dtyCycleRng" ] , 0 , -1 ):
		pwm_M1NEG.ChangeDutyCycle( dc )
		pwm_M2NEG.ChangeDutyCycle( dc )
		time.sleep( motorData[ "sleepLen" ] )

	pwm_M1NEG.ChangeDutyCycle( 0 )
	pwm_M2NEG.ChangeDutyCycle( 0 )

def pivotRight( motorData ):

	print( "pivotRight" ) # 0 1 frwd

	pwm_M1POS.ChangeDutyCycle( motorData[ "dtyCycleRng" ] )
	pwm_M1NEG.ChangeDutyCycle( 0 )

	pwm_M2POS.ChangeDutyCycle( 0 )
	pwm_M2NEG.ChangeDutyCycle( motorData[ "dtyCycleRng" ] )
	time.sleep( 1 )

	pwm_M1POS.ChangeDutyCycle( 0 )
	pwm_M1NEG.ChangeDutyCycle( 0 )
	pwm_M2POS.ChangeDutyCycle( 0 )
	pwm_M2NEG.ChangeDutyCycle( 0 )
	time.sleep( 1 )

def pivotLeft( motorData ):

	print( "pivotLeft" ) # 1 0 back

	pwm_M1NEG.ChangeDutyCycle( motorData[ "dtyCycleRng" ] )
	pwm_M1POS.ChangeDutyCycle( 0 )

	pwm_M2NEG.ChangeDutyCycle( 0 )
	pwm_M2POS.ChangeDutyCycle( motorData[ "dtyCycleRng" ] )
	time.sleep( 1 )

	pwm_M1POS.ChangeDutyCycle( 0 )
	pwm_M1NEG.ChangeDutyCycle( 0 )
	pwm_M2POS.ChangeDutyCycle( 0 )
	pwm_M2NEG.ChangeDutyCycle( 0 )
	time.sleep( 1 )

def speedFast( motorData ):

	print( "speedFast" ) #
	motorData[ "dtyCycleRng" ] = 100;

def speedSlow( motorData ):

	print( "speedSlow" ) #
	motorData[ "dtyCycleRng" ] = 50;

def cleanUp( ):

	print( "cleanUp" )
	pwm_M1POS.stop( )
	pwm_M1NEG.stop( )
	pwm_M2POS.stop( )
	pwm_M2NEG.stop( )
	GPIO.cleanup( ) # sets pins to nuetral
