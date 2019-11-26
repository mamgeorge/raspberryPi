## python\servo\servo_loop.py
## python\servo\servo_loop.py
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

## loops ( open/closes ) continuously
import RPi.GPIO as GPIO
import time

## setup
pinCTRL = 4			# pin4: 5V+ , pin6: ground-
srvFREQ = 50
srvINCR = 0.0015	# not used
dc_cls = 2.5		# 000 close
dc_ntr = 7.5		# nuetral
dc_opn = 12.5		# 180 open
sleepLen = 1

GPIO.setmode( GPIO.BCM ) # GPIO.setmode( GPIO.BOARD )
GPIO.setwarnings( False ) # RuntimeWarning: This channel is already in use , continuing anyway. Use GPIO.setwarnings( False ) to disable warnings.
GPIO.setup( pinCTRL , GPIO.OUT )

pwmCTRL = GPIO.PWM( pinCTRL , srvFREQ )
print( "loops continuously" )

## exec
pwmCTRL.start( dc_ntr ) # nuetral
try:
	while True:

		pwmCTRL.ChangeDutyCycle( dc_ntr ) # nuetral
		time.sleep( sleepLen )
		pwmCTRL.ChangeDutyCycle( dc_opn ) # 180 open
		time.sleep( sleepLen )
		pwmCTRL.ChangeDutyCycle( dc_cls ) # 000 close
		time.sleep( sleepLen )

except KeyboardInterrupt:
	pwmCTRL.stop( )
	GPIO.cleanup( )

## fini
print( "DONE" )
