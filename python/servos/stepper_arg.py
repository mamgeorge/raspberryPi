## python/servos/stepper_one.py
#####################################
## Model: 28BYJ-48
## Input Voltage: 5V 
## SPR ( StepsPerRevolution ): 32
## Gear Reduction: 1/64
## Revolution: 2048 for full stepping , 4096 half stepping
## 1 rev = 8 cycles , geared @ 64, so 8 x 64 = 512 cycles for one full revolution
#####################################
## control: 17:blu, 27:pur, 22:yel, 10:ora ; #2:red, #6blk

## minimum code ; runs once
import RPi.GPIO as GPIO
import time
import sys

## setup
GPIO.setmode( GPIO.BCM ) # GPIO.setmode( GPIO.BOARD )
GPIO.setwarnings( False ) # RuntimeWarning disabled

controlPins = [ 17 , 27 , 22 , 10 ] # 11,13,15,19

sequenceHalf = [
	[ 1 , 0 , 0 , 0 ] ,
	[ 1 , 1 , 0 , 0 ] ,
	[ 0 , 1 , 0 , 0 ] ,
	[ 0 , 1 , 1 , 0 ] ,
	[ 0 , 0 , 1 , 0 ] ,
	[ 0 , 0 , 1 , 1 ] ,
	[ 0 , 0 , 0 , 1 ] ,
	[ 1 , 0 , 0 , 1 ] 
]

revolution = 512 # 512 cycles for one revolution
timerDelay = 0.001 # outside for loop so pins are set and motor has a chance to repond

for pin in controlPins:
	GPIO.setup( pin , GPIO.OUT )
	GPIO.output( pin , 0 ) #LOW

timerDelay = sys.argv[1] 
if timerDelay.isalpha() == True:
	timerDelay = 0
else:
	timerDelay = float( timerDelay )

print( "timerDelay: " + str( timerDelay ) )
if timerDelay >= .01	: timerDelay = .01
if timerDelay <= .001	: timerDelay = .001
print( "timerDelay: " + str( timerDelay ) )

## exec
for ictr in range( revolution ): 
	for halfstep in range( 8 ):
		for pin in range( 4 ):
			GPIO.output( controlPins[ pin ] , sequenceHalf[ halfstep ][ pin ] )
		time.sleep( timerDelay ) 

## fini
GPIO.cleanup( )
print( "DONE" )
