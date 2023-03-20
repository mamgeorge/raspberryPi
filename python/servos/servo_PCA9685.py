# \\5Personal\Technology\raspberryPi\python\servos\servo_PCA9685.py
'''
arana

	https://www.aranacorp.com/en/using-a-pca9685-module-with-raspberry-pi/

	sudo pip3 install adafruit-circuitpython-servokit
		ERROR: Could not find a version that satisfies the requirement adafruit-circuitpython-servokit (from versions: )
			update, upgrade
		ERROR: Command "python setup.py egg_info" failed with error code 1 in /tmp/pip-build-uc571csj/sysv-ipc/
			sudo -H pip3 install --upgrade pip
			sudo pip3 install setuptools wheel
			sudo pip3 install --upgrade setuptools
	sudo pip3 install adafruit-circuitpython-pca9685
	sudo pip3 install smbus2
	sudo raspi-config
	i2cdetect -y 1
		40: 40 --
		70: 70 --

	LEDs	https://learn.adafruit.com/16-channel-pwm-servo-driver/python-circuitpython
	MagPi	https://magpi.raspberrypi.org/articles/control-servos-circuitpython-raspberry-pi
	Ada		https://learn.adafruit.com/adafruit-16-channel-servo-driver-with-raspberry-pi

	API ServoKit		https://circuitpython.readthedocs.io/projects/servokit/en/latest/api.html
	API	pca9685 		https://github.com/adafruit/Adafruit_CircuitPython_PCA9685
	API	PWMServoDriver	http://adafruit.github.io/Adafruit-PWM-Servo-Driver-Library/html/class_adafruit___p_w_m_servo_driver.html

HiTec DB

	https://servodatabase.com/servos/hitec
	pw: pulse widths, pc: pulse cycle (20ms width for 50Hz frequency), ang: angle rotational range
'''
import time
import sys
from adafruit_servokit import ServoKit

# setup
pca_channel_number = 16
#pca_control_object = ServoKit( channels=16 )
#pca_control_object = ServoKit( channels=16, address=64 ) # address is 40 in hex
#pca_control_object = ServoKit( channels=16, i2c=None, address=64, reference_clock_speed=25000000, frequency=50)

chnl=16
i2cv=None
addr=64
clck=25000000
freq=50

MIN_IMP = 0	# min impluse width
MAX_IMP = 0	# max impluse width
MIN_ANG = 0	# min angle rotational range
MAX_ANG = 0	# max angle rotational range
entryChannel = ''
channelUsed = 0
increments = 0.01

# methods
def init( ):

	print('running init')
	################
	global MIN_IMP
	global MAX_IMP
	global MIN_ANG
	global MAX_ANG

	servos = [ #[pwmin, pwmax, angmin, angmax, pcfreq, 'type' ]
		[ 1, [ 500 , 2500, 0, 180, 20, 'MG90S AranaCorp sample'		] ],
		[ 2, [ 900 , 2100, 0, 102, 20, 'HS-55 SubMicro, Gripper'	] ],
		[ 3, [ 900 , 2100, 0, 165, 20, 'HS-81 Micro, sample'		] ],
		[ 4, [ 900 , 2100, 0, 180, 20, 'HS311 Standard, Gripper'	] ],
		[ 5, [ 1000, 2000, 0, 180, 20, 'MG995 armature, TowerPro'	] ],
		[ 6, [ 500 , 2500, 0,  90, 20, 'MG995 armature, TianKongRC'	] ]
	#	[ 6, [ 500 , 2500, 0, 180, 20, 'MG995 armature, TianKongRC' ] ]
	]
	servoSelected = sys.argv[1]

	SERVO = servos[ int( servoSelected ) - 1 ]
	MIN_IMP = SERVO[1][0]
	MAX_IMP = SERVO[1][1]
	MIN_ANG = SERVO[1][2]
	MAX_ANG = SERVO[1][3]
	SERVONM = SERVO[1][5] # servo name
	print( '\t' + 'Using servo: {}, pulseWidth({},{}), angleRange({},{}) '.format( SERVONM, MIN_IMP, MAX_IMP, MIN_ANG, MAX_ANG) )

	################
	global entryChannel
	global channelUsed
	global pca_control_object

	entryChannel = sys.argv[2]
	print( '\t' + 'entryChannel: [{}]'.format( entryChannel ) )
	if entryChannel.isnumeric():

		if int(entryChannel) >= 1 and int(entryChannel) <= 16:

			channelUsed = int( sys.argv[2] ) - 1
		else:
			entryChannel = 'a'
	else:
		entryChannel = 'a'
	print( '\t' + 'entryChannel: [{}]'.format( entryChannel ) )
	print( '\t' + 'channelUsed : [{}]'.format( channelUsed + 1 ) )

	pca_control_object = ServoKit( channels=chnl, i2c=i2cv, address=addr, reference_clock_speed=clck, frequency=freq )
	print( '\t' + 'pca_control_object: channels={}, i2c={}, address={}, reference_clock_speed={}, frequency={}'.format(chnl, i2cv, addr, clck, freq) )

	for ctrChannel in range( pca_channel_number ):
		# ( MIN_IMP[ ctrChannel ], MAX_IMP[ ctrChannel ] )
		pca_control_object.servo[ ctrChannel ].set_pulse_width_range( MIN_IMP, MAX_IMP )

def pcaTestItem( ):

	print('\n' + 'running pcaTestItem')
	if channelUsed < 8:
	
		for ctrAngle in range( MIN_ANG, MAX_ANG, 1 ): # MIN_ANG[ channelUsed ], MAX_ANG[ channelUsed ]

			print('\t' + 'Send angle {:03d} to Servo {}'.format( ctrAngle, channelUsed + 1 ) , end = '\r' )
			pca_control_object.servo[ channelUsed ].angle = ctrAngle
			time.sleep( increments )

		for ctrAngle in range( MAX_ANG, MIN_ANG, -1 ):

			print('\t' + 'Send angle {:03d} to Servo {}'.format( ctrAngle, channelUsed + 1 ) , end = '\r' )
			pca_control_object.servo[ channelUsed ].angle = ctrAngle
			time.sleep( increments )
	else: 
	
		for ctrAngle in range( MAX_ANG, MIN_ANG, -1 ):

			print('\t' + 'Send angle {:03d} to Servo {}'.format( ctrAngle, channelUsed + 1 ) , end = '\r' )
			pca_control_object.servo[ channelUsed ].angle = ctrAngle
			time.sleep( increments )

		for ctrAngle in range( MIN_ANG, MAX_ANG, 1 ): # MIN_ANG[ channelUsed ], MAX_ANG[ channelUsed ]

			print('\t' + 'Send angle {:03d} to Servo {}'.format( ctrAngle, channelUsed + 1 ) , end = '\r' )
			pca_control_object.servo[ channelUsed ].angle = ctrAngle
			time.sleep( increments )

	pca_control_object.servo[ channelUsed ].angle = None #disable channel
	time.sleep( 0.5 )
	print('')

def pcaTestLoop( ):

	print('\n' + 'running pcaTestLoop')
	for ctrChannel in range( pca_channel_number ):

		for ctrAngle in range( MIN_ANG, MAX_ANG, 10 ):

			print('\t' + 'Send angle {:03d} to Servo {}'.format( ctrAngle, ctrChannel + 1 ) , end = '\r' )
			pca_control_object.servo[ ctrChannel ].angle = ctrAngle
			time.sleep( increments )

		for ctrAngle in range( MAX_ANG, MIN_ANG, -10 ):

			print('\t' + 'Send angle {:03d} to Servo {}'.format( ctrAngle, ctrChannel + 1 ) , end = '\r' )
			pca_control_object.servo[ ctrChannel ].angle = ctrAngle
			time.sleep( increments )

		pca_control_object.servo[ ctrChannel ].angle = None #disable channel
		time.sleep( 0.25 )

	print('')

# execute

try:
	pca_control_object = ServoKit( channels=16 )

	init( )
	if entryChannel == 'a':
		pcaTestLoop( )
	else:
		pcaTestItem( )

except (RuntimeError, ValueError) as err:
	print( "ServoKit pca_control_object not started" )
	print( "Error:", sys.exc_info()[0], err )

# finish
print( 'DONE' )
