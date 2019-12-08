## python\servo\servo_one.py
#####################################
## Model: HiTec HS-311 Standard Servo
## Model: HiTec HS-55 Sub Micro Servo
## Model: HiTec HS-81 Sub Micro Servo
#####################################
## Voltage Range		4.8V - 6.0V
## duty_cycle control is from 0.5 ms - 2.5 ms
#####################################

## minimum code ; runs once
import RPi.GPIO as GPIO
import time

## setup
pinCTRL = 26		# YLW BCM26(p37), RED (p02): 5V+ , BLK ground(p39): ground-
srvINCR = 0.0015	# not used
srvFREQ = 50        # Hz ( 50 pulses a sec )
sleepLen = 1

## duty_cycle: 50; 1/50 = .02 = 20 ms
dc_min = 2.5		# 000 close	0.5 ms / 20 ms * 100 = 2.5%
dc_ntr = 7.5		# nuetral	1.5 ms / 20 ms * 100 = 7.5%
dc_max = 12.5		# 180 open	2.5 ms / 20 ms * 100 = 12.5%

GPIO.setmode( GPIO.BCM ) # GPIO.setmode( GPIO.BOARD )
GPIO.setwarnings( False ) # RuntimeWarning: This channel is already in use , continuing anyway. Use GPIO.setwarnings( False ) to disable warnings.

##
GPIO.setup( pinCTRL , GPIO.OUT )
pwmCTRL = GPIO.PWM( pinCTRL , srvFREQ )
print( "runs once" )

## exec
pwmCTRL.start( dc_ntr ) # neutral
try:

	while True:
		pwmCTRL.ChangeDutyCycle( dc_ntr )	# neutral
		time.sleep( sleepLen )

		pwmCTRL.ChangeDutyCycle( dc_max )	# 180 open
		time.sleep( sleepLen )

		pwmCTRL.ChangeDutyCycle( dc_min )	# 000 close
		time.sleep( sleepLen )

except KeyboardInterrupt:
	pwmCTRL.stop( )
	GPIO.cleanup( )

## fini
print( "DONE" )
