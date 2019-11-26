# /home/pi/python/mat/robot.py

import sys
import motor_motions
import iface_actions

########################
# setup

sleepLen = .01
frequency = 50
dtyCycleRng = 100

pinM1_POS = 26	# mLFT + wht
pinM1_NEG = 19	# mLFT - grn
pinM2_POS = 20	# mRGT + blu
pinM2_NEG = 16	# mRGT - ylw

motorData = { "dtyCycleRng":dtyCycleRng , "sleepLen":sleepLen , "frequency":frequency ,
	"pinM1_NEG":pinM1_NEG , "pinM1_POS":pinM1_POS , "pinM2_NEG":pinM2_NEG , "pinM2_POS":pinM2_POS }

lights = 0
camera = 0
speaker= 0
action = 0
sensor = 0
txtCommand = ""

ifaceData = { "lights":lights , "camera":camera , "speaker":speaker , "action":action , "sensor":sensor }

########################
# exec

motor_motions.setupGPIO( motorData )
# print( sys.version )

# while txtCommand != "0":

try:

	# txtCommand = sys.stdin.readline( ).strip( )
	txtCommand = sys.stdin.readline( ).strip( )
	print( "ACTION: [" + txtCommand + "]" )
	sys.stdout.flush( )
	
	# phase 1
	if txtCommand == ( "8" or "FORWARD" )	: motor_motions.moveForward	( motorData )
	if txtCommand == ( "2" or "BACKWARD" )	: motor_motions.moveBackward( motorData )
	if txtCommand == ( "6" or "PIVOTRIGHT")	: motor_motions.pivotRight	( motorData )
	if txtCommand == ( "4" or "PIVOTLEFT" )	: motor_motions.pivotLeft	( motorData )
	if txtCommand == ( "+" or "FAST" )		: motor_motions.speedFast	( motorData )
	if txtCommand == ( "-" or "SLOW" )		: motor_motions.speedSlow	( motorData )
	if txtCommand == ( "5" or "STOP" )		: motor_motions.cleanUp		( )

	# phase 2
	if txtCommand == ( "l" or "LIGHTS" )	: iface_actions.lightToggle	( ifaceData )
	if txtCommand == ( "c" or "CAMERA" )	: iface_actions.camMonitor	( ifaceData )
	if txtCommand == ( "s" or "SPEAKER" )	: iface_actions.speakerSound( ifaceData )	
	if txtCommand == ( "a" or "ACTION" )	: iface_actions.articulation( ifaceData )
	if txtCommand == ( "x" or "SENSOR" )	: iface_actions.environment ( ifaceData )

except KeyboardInterrupt:
	motor_motions.cleanUp( )

########################
# fini

print( "DONE" )
sys.stdout.flush( )