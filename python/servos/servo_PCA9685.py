#!/usr/bin/env python
# \\5Personal\Technology\raspberryPi\python\servos\servo_PCA9685.py
# https://www.aranacorp.com/en/using-a-pca9685-module-with-raspberry-pi/
# https://servodatabase.com/servos/hitec
# pw: pulse widths, pc: pulse cycle (20ms width for 50Hz frequency), ang: angle rotational range

import time
import sys
from adafruit_servokit import ServoKit

# setup
pca_channel_number = 16
#pca_control_object = ServoKit( channels=16 )
#pca_control_object = ServoKit( channels=16, address=64 ) # address is 40 in hex
#pca_control_object = ServoKit( channels=16, i2c=None, address=64, reference_clock_speed=25000000, frequency=50)

pca_control_object = ServoKit( channels=16 )
chnl=16
i2cv=None
addr=64
clck=25000000
freq=50

MIN_IMP = 0	# min impluse width
MAX_IMP = 0	# max impluse width
MIN_ANG = 0	# min angle rotational range
MAX_ANG = 0	# max angle rotational range
channelUsed = 0

# methods
def init( ):

	global pca_control_object
	pca_control_object = ServoKit( channels=chnl, i2c=i2cv, address=addr, reference_clock_speed=clck, frequency=freq)
	print( "pca_control_object: channels={}, i2c={}, address={}, reference_clock_speed={}, frequency={}".format(chnl, i2cv, addr, clck, freq) )

	global MIN_IMP
	global MAX_IMP
	global MIN_ANG
	global MAX_ANG
	global channelUsed

	servos = [ #[pwmin, pwmax, angmin, angmax, pcfreq, 'type' ]
		[ 1, [ 500 , 2500, 0, 180, 20, 'MG90S AranaCorp sample'		]],
		[ 2, [ 900 , 2100, 0, 102, 20, 'HS-55 SubMicro, Gripper'	]],
		[ 3, [ 900 , 2100, 0, 165, 20, 'HS-81 Micro, sample'		]],
		[ 4, [ 900 , 2100, 0, 180, 20, 'HS311 Standard, Gripper'	]],
		[ 5, [ 1000, 2000, 0, 180, 20, 'MG995 armature, TowerPro'	]],
		[ 6, [ 500 , 2500, 0, 180, 20, 'MG995 armature, TianKongRC'	]]
	]
	servoSelected = sys.argv[1]

	SERVO = servos[ int( servoSelected ) - 1 ]
	MIN_IMP = SERVO[1][0]
	MAX_IMP = SERVO[1][1]
	MIN_ANG = SERVO[1][2]
	MAX_ANG = SERVO[1][3]
	SERVONM = SERVO[1][5] # servo name
	print( "Using servo: {}, pulseWidth({},{}), angleRange({},{}) ".format( SERVONM, MIN_IMP, MAX_IMP, MIN_ANG, MAX_ANG) )

	#-------------
	
	channelUsed = int( sys.argv[2] ) - 1
	print( "Using channel: {}".format( channelUsed + 1 ) )

	#-------------
	for ctrChannel in range( pca_channel_number ):
		# ( MIN_IMP[ ctrChannel ], MAX_IMP[ ctrChannel ] )
		pca_control_object.servo[ ctrChannel ].set_pulse_width_range( MIN_IMP, MAX_IMP )

def pcaTestItem( ):

	for ctrAngle in range( MIN_ANG, MAX_ANG, 1 ): # MIN_ANG[ channelUsed ], MAX_ANG[ channelUsed ]

		print("Send angle {:03d} to Servo {}".format( ctrAngle, channelUsed + 1 ) , end = "\r" )
		pca_control_object.servo[ channelUsed ].angle = ctrAngle
		time.sleep( 0.01 )

	for ctrAngle in range( MAX_ANG, MIN_ANG, -1 ):

		print("Send angle {:03d} to Servo {}".format( ctrAngle, channelUsed + 1 ) , end = "\r" )
		pca_control_object.servo[ channelUsed ].angle = ctrAngle
		time.sleep( 0.01 )

	pca_control_object.servo[ channelUsed ].angle = None #disable channel
	time.sleep( 0.5 )

def pcaTestLoop( ):

	for ctrChannel in range( pca_channel_number ):

		for ctrAngle in range( MIN_ANG, MAX_ANG, 10 ):

			print("Send angle {:03d} to Servo {}".format( ctrAngle, ctrChannel + 1 ) , end = "\r" )
			pca_control_object.servo[ ctrChannel ].angle = ctrAngle
			time.sleep( 0.01 )

		for ctrAngle in range( MAX_ANG, MIN_ANG, -10 ):

			print("Send angle {:03d} to Servo {}".format( ctrAngle, ctrChannel + 1 ) , end = "\r" )
			pca_control_object.servo[ ctrChannel ].angle = ctrAngle
			time.sleep( 0.01 )

		pca_control_object.servo[ ctrChannel ].angle = None #disable channel
		time.sleep( 0.5 )

# execute
init( )
if channelUsed < 0:
	pcaTestLoop( )
else:
	pcaTestItem( )

# finish
print( "DONE" )
