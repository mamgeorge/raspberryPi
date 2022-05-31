# /home/pi/python/motor.py
# Controlling a DC Motor / Gaven MacDonald
#
# [ * ] 1 ) SSH Putty / Python / GPIO-L293D-F130 / GearBox
# [ _ ] 2 ) Node ( MEAN ) / HTML
# [ _ ] 3 ) Motion Cam integration / SenseHat
# [ _ ] 4 ) Articulation / SenseHat
# [ _ ] 5 ) VAC / AI
#
# L293D uses pin 2 for 5V source ( white ) pin 6 for ground ( black )
# in1: 0	in2: 1	| frwd
# in1: 1	in2: 0	| back

import motor_motions

########################
# setup

print( "Setup L293D" )
sleepLen = .01
frequency = 50
dtyCycleRng = 100

pinM1_POS = 26	# mLFT + wht
pinM1_NEG = 19	# mLFT - grn
pinM2_POS = 20	# mRGT + blu
pinM2_NEG = 16	# mRGT - ylw

motorData = { "dtyCycleRng":dtyCycleRng , "sleepLen":sleepLen , "frequency":frequency ,
	"pinM1_NEG":pinM1_NEG , "pinM1_POS":pinM1_POS , "pinM2_NEG":pinM2_NEG , "pinM2_NEG":pinM2_NEG }

motor_motions.setupGPIO( motorData )

########################
# exec

print( "Execute Tractors" )
try:
	while True:

		motor_motions.moveForward	( motorData )
		motor_motions.moveBackward	( motorData )
		motor_motions.pivotRight	( motorData )
		motor_motions.pivotLeft		( motorData )

except KeyboardInterrupt:
	pass

########################
# fini

motor_motions.cleanUp( )

print( "DONE" )
