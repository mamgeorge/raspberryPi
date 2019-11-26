## python\servo\servo_both.py
#####################################
## Model: HiTec HS-311 Standard Servo
#####################################
## Voltage Range		4.8V - 6.0V
## NoLoad Speed @4.8V	0.19sec/60 Deg
## Stall Torque @4.8V	42 oz/in ( 3.0 kg/cm )
## Product Weight		1.52oz ( 43g )
## PWM Signal MaxRange	575-2460 ms
## Max Travel			202.5 Deg
## 000 Deg: 0.5 ms , DC: 0.5/20 = 02.5%
## Neutral: 1.5 ms , DC: 1.5/20 = 07.5%
## 180 Deg: 2.5 ms , DC: 2.5/20 = 12.5%
#####################################

## minimum code ; runs both once
import RPi.GPIO as GPIO
import time

## setup
pinRGHT = 4			# YLW BCM04(p07): 5V+ , RED pin04: 5V+ , BLK pin06: ground-
pinLEFT = 18		# YLW BCM18(p12): 5V+ , RED pin?4: 5V+ , BLK pin14: ground-
srvFREQ = 50
srvINCR = 0.0015	# not used
dc_cls = 2.5		# 000 close
dc_ntr = 7.5		# nuetral
dc_opn = 12.5		# 180 open
sleepLen = 1

GPIO.setmode( GPIO.BCM ) # GPIO.setmode( GPIO.BOARD )
GPIO.setwarnings( False ) # RuntimeWarning: This channel is already in use , continuing anyway. Use GPIO.setwarnings( False ) to disable warnings.

## exec
print( "runs both" )

def flexClaw( gripper ):
	##
	if gripper == ( "A" ): pinCTRL = pinLEFT
	if gripper == ( "B" ): pinCTRL = pinRGHT
	GPIO.setup( pinCTRL , GPIO.OUT )
	pwmCTRL = GPIO.PWM( pinCTRL , srvFREQ )
	##
	pwmCTRL.start( dc_ntr ) # nuetral
	pwmCTRL.ChangeDutyCycle( dc_ntr ) # nuetral
	time.sleep( sleepLen )
	
	if gripper == ( "A" ):
		pwmCTRL.ChangeDutyCycle( dc_opn ) # 180 open
		time.sleep( sleepLen )
		pwmCTRL.ChangeDutyCycle( dc_cls ) # 000 close
		time.sleep( sleepLen )

	if gripper == ( "B" ):
		pwmCTRL.ChangeDutyCycle( dc_cls ) # 180 open
		time.sleep( sleepLen )
		pwmCTRL.ChangeDutyCycle( dc_opn ) # 000 close
		time.sleep( sleepLen )
	##
	pwmCTRL.stop( )

try:
	
	for x in range( 1 ):
		flexClaw( 'A' )
		flexClaw( 'B' )
	
except KeyboardInterrupt:
	GPIO.cleanup( )

## fini
print( "DONE" )
