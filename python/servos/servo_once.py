## python\servo\servo_once.py
#####################################
## Model: HiTec HS-311 Standard Servo
## Model: HiTec HS-55 Sub Micro Servo
## Model: HiTec HS-81 Sub Micro Servo
#####################################
## Voltage Range		4.8V - 6.0V
#####################################

## minimum code ; runs once
import RPi.GPIO as GPIO
import time

## setup
pinCTRL = 26		# YLW BCM26(p37), RED (p02): 5V+ , BLK ground(p39): ground-
srvINCR = 0.0015	# not used
srvFREQ = 50        # 
sleepLen = 1

dc_cls = 2.5		# 000 close
dc_ntr = 7.5		# nuetral
dc_opn = 12.5		# 180 open

GPIO.setmode( GPIO.BCM ) # GPIO.setmode( GPIO.BOARD )
GPIO.setwarnings( False ) # RuntimeWarning: This channel is already in use , continuing anyway. Use GPIO.setwarnings( False ) to disable warnings.

##
GPIO.setup( pinCTRL , GPIO.OUT )
pwmCTRL = GPIO.PWM( pinCTRL , srvFREQ )
print( "runs once" )

## exec
pwmCTRL.start( dc_ntr ) # neutral
try:
	
	pwmCTRL.ChangeDutyCycle( dc_ntr )	# neutral
	time.sleep( sleepLen )

	pwmCTRL.ChangeDutyCycle( dc_opn )	# 180 open
	time.sleep( 0 )
	
	pwmCTRL.ChangeDutyCycle( dc_cls )	# 000 close
	time.sleep( sleepLen )
	
except KeyboardInterrupt:
	pwmCTRL.stop( )
	GPIO.cleanup( )

## fini
print( "DONE" )
