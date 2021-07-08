# raspberryPi/python/mat/robot_arms.py
'''
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

# setup
chnl=16
i2cv=None
addr=64
clck=25000000
freq=50
PCA9685 = ServoKit( channels=chnl, i2c=i2cv, address=addr, reference_clock_speed=clck, frequency=freq )

servos = [ #[ pwmin, pwmax, angmin, angmax, pcfreq, 'type' ]
	[ 1, [ 500 , 2500, 0, 180, 20, '4.8-6v', 'MG90S AranaCorp, Towerpro '	] ],
	[ 2, [ 900 , 2100, 0, 102, 20, '4.8-6v', 'HS-55 SubMicro, Gripper'		] ],
	[ 3, [ 900 , 2100, 0, 165, 20, '4.8-6v', 'HS-81 Micro, sample'			] ],
	[ 4, [ 900 , 2100, 0, 180, 20, '4.8-6v', 'HS311 Standard, Gripper'		] ],
	[ 5, [ 1000, 2000, 0, 180, 20, '4.8-6v', 'MG995 armature, TowerPro'	] ],
	[ 6, [ 500 , 2500, 0, 180, 20, '3-7.2v', 'MG995 armature, TianKongRC'	] ]
]

channelsUsed = 3
timeSlices = 0.01
angIncrements = 1

# methods
def init( ):

	global PCA9685
	PCA9685.servo[ 0 ].set_pulse_width_range( servos[5][1][0], servos[5][1][1] )
	PCA9685.servo[ 1 ].set_pulse_width_range( servos[5][1][0], servos[5][1][1] )
	PCA9685.servo[ 2 ].set_pulse_width_range( servos[2][1][0], servos[2][1][1] )

def pcaFlex( ):

	global servos
	#print ( servos[5][1][6] )
	
	for ctrChannel in range( channelsUsed ):

		servo = servos[5]
		if ctrChannel == 2:
			servo = servos[1]
		print ( "ctrChannel {}, {}".format( ctrChannel+1 , servo[1][6] ) )

		for ctrAngle in range( servo[1][2], servo[1][3], angIncrements ):

			PCA9685.servo[ ctrChannel ].angle = ctrAngle
			time.sleep( timeSlices )

		for ctrAngle in range( servo[1][3], servo[1][2], -angIncrements ):

			PCA9685.servo[ ctrChannel ].angle = ctrAngle
			time.sleep( timeSlices )

		PCA9685.servo[ ctrChannel ].angle = None #disable channel
		time.sleep( 0.25 )

	print('')

# execute

try:
	PCA9685 = ServoKit( channels=16 )
	init( )
	pcaFlex( )

except (RuntimeError, ValueError) as err:
	print( "Error:", sys.exc_info()[0], err )

# finish
print( 'DONE' )
