# raspberryPi/python/mat/robot_arms.py
'''
Copyright 2021, Martin George, Columbus Ohio

arana		https://www.aranacorp.com/en/using-a-pca9685-module-with-raspberry-pi/
LEDs		https://learn.adafruit.com/16-channel-pwm-servo-driver/python-circuitpython
MagPi		https://magpi.raspberrypi.org/articles/control-servos-circuitpython-raspberry-pi
Ada			https://learn.adafruit.com/adafruit-16-channel-servo-driver-with-raspberry-pi
ServoKit	https://circuitpython.readthedocs.io/projects/servokit/en/latest/api.html

https://servodatabase.com/servos/hitec

	pw: pulse widths, ang: angle rotational range, pc: pulse cycle (20ms width for 50Hz frequency)

	i2cdetect -y 1
		40: 40 --
		70: 70 --

'''
import time
import sys
from adafruit_servokit import ServoKit

#### setup
chnl=16
i2cv=None
addr=64
clck=25000000
freq=50

servoList = [ #[ pwmin, pwmax, angmin, angmax, pcfreq, 'type' ]
	[ 1, [ 500 , 2500, 0, 180, 20, '4.8-6v', 'MG90S AranaCorp, Towerpro '	] ],
	[ 2, [ 900 , 2100, 0, 102, 20, '4.8-6v', 'HS-55 SubMicro, Gripper'		] ],
	[ 3, [ 900 , 2100, 0, 165, 20, '4.8-6v', 'HS-81 Micro, sample'			] ],
	[ 4, [ 900 , 2100, 0, 180, 20, '4.8-6v', 'HS311 Standard, Gripper'		] ],
	[ 5, [ 1000, 2000, 0, 180, 20, '4.8-6v', 'MG995 armature, TowerPro'		] ],
	[ 6, [ 500 , 2500, 0, 180, 20, '3-7.2v', 'MG995 armature, TianKongRC'	] ]
]

channelsUsed = 6
timeSlices = 0.01
angIncrements = 1

#### methods
def init( ):

	global PCA_ServoKit
	PCA_ServoKit.servo[  0 ].set_pulse_width_range( servoList[5][1][0], servoList[5][1][1] )
	PCA_ServoKit.servo[  1 ].set_pulse_width_range( servoList[5][1][0], servoList[5][1][1] )
	PCA_ServoKit.servo[  2 ].set_pulse_width_range( servoList[1][1][0], servoList[1][1][1] )
	PCA_ServoKit.servo[ 12 ].set_pulse_width_range( servoList[1][1][0], servoList[1][1][1] )
	PCA_ServoKit.servo[ 13 ].set_pulse_width_range( servoList[5][1][0], servoList[5][1][1] )
	PCA_ServoKit.servo[ 14 ].set_pulse_width_range( servoList[5][1][0], servoList[5][1][1] )
	#print ( servoList[5][1][6] )

def pcaFlex( ):

	print ('pcaFlex')
	global servoList

	for ctrChannel in range( channelsUsed ):

		if ctrChannel in [ 0, 1, 3, 4 ]		: servoItem = servoList[5]
		if ctrChannel == 2 or ctrChannel == 5	: servoItem = servoList[1]

		angInc = angIncrements
		minAng = servoItem[1][2]
		maxAng = servoItem[1][3]

		if ctrChannel == 0 or ctrChannel == 1:
			angInc = -angIncrements
			minAng = servoItem[1][3]
			maxAng = servoItem[1][2]

		for ctrAngle in range( minAng, maxAng, angInc ):

			PCA_ServoKit.servo[ ctrChannel ].angle = ctrAngle
			print ( '\t' + 'chn: {}, ang: {:03d}, serv: {}'.format(ctrChannel+1, ctrAngle, servoItem[1][6]), end = '\r' )
			time.sleep( timeSlices )

		for ctrAngle in range( maxAng, minAng, -angInc ):

			PCA_ServoKit.servo[ ctrChannel ].angle = ctrAngle
			print ( '\t' + 'chn: {}, ang: {:03d}, serv: {}'.format(ctrChannel+1, ctrAngle, servoItem[1][6]), end = '\r' )
			time.sleep( timeSlices )

		PCA_ServoKit.servo[ ctrChannel ].angle = None # disable channel
		time.sleep( 0.25 )
		print('')

	print('')

def pcaStretch( ):

	print ('pcaStretch')
	global servoList

	servoItem = servoList[5]
	angInc = angIncrements
	minAng = servoItem[1][2]
	maxAng = servoItem[1][3]

	PCA_ServoKit.servo[  0 ].angle = maxAng
	PCA_ServoKit.servo[ 14 ].angle = maxAng

	for ctrAngle in range( maxAng, minAng, -angIncrements ):

		PCA_ServoKit.servo[  0 ].angle = ctrAngle
		PCA_ServoKit.servo[ 14 ].angle = ctrAngle
		print ( '\t' + 'chn: {}, ang: {:03d}, serv: {}'.format('x', ctrAngle, servoItem[1][6]), end = '\r' )
		time.sleep( timeSlices )

	print('')

	for ctrAngle in range( minAng, maxAng, angIncrements ):

		PCA_ServoKit.servo[  0 ].angle = ctrAngle
		PCA_ServoKit.servo[ 14 ].angle = ctrAngle
		print ( '\t' + 'chn: {}, ang: {:03d}, serv: {}'.format('x', ctrAngle, servoItem[1][6]), end = '\r' )
		time.sleep( timeSlices )

	print('')

	PCA_ServoKit.servo[  0 ].angle = None # disable channel
	PCA_ServoKit.servo[ 14 ].angle = None # disable channel
	time.sleep( 0.25 )

def pcaGrasp( ):

	print ('pcaGrasp')

	global servoList

	servoItem = servoList[1]

	for ctrAngle in range( servoItem[1][3], servoItem[1][2], -angIncrements ):

		PCA_ServoKit.servo[  2 ].angle = ctrAngle
		PCA_ServoKit.servo[ 12 ].angle = ctrAngle
		print ( '\t' + 'chn: {}, ang: {:03d}, serv: {}'.format('x', ctrAngle, servoItem[1][6]), end = '\r' )
		time.sleep( timeSlices )


	for ctrAngle in range( servoItem[1][2], servoItem[1][3], angIncrements ):

		PCA_ServoKit.servo[  2 ].angle = ctrAngle
		PCA_ServoKit.servo[ 12 ].angle = ctrAngle
		print ( '\t' + 'chn: {}, ang: {:03d}, serv: {}'.format('x', ctrAngle, servoItem[1][6]), end = '\r' )
		time.sleep( timeSlices )

	PCA_ServoKit.servo[  2 ].angle = None # disable channel
	PCA_ServoKit.servo[ 12 ].angle = None # disable channel
	time.sleep( 0.25 )

	print('')

#### execute
print ('Python: ' + sys.version)
action = sys.argv[1]
options = {
	'f' : pcaFlex,
	's' : pcaStretch,
	'g' : pcaGrasp
}

try:
	PCA_ServoKit = ServoKit( channels=16 )
	#PCA_ServoKit = ServoKit( channels=chnl, i2c=i2cv, address=addr, reference_clock_speed=clck, frequency=freq )
	init( )
	options[ action ]( )

except (RuntimeError, ValueError) as err:
	print( 'Error:', sys.exc_info()[0], err )

# finish
print( 'DONE' )
