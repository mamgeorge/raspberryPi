
import os
import sys
import datetime
sys.path.append( '/home/pi/python/gpio' )
sys.path.append( '/home/pi/python/hats' )
sys.path.append( '/home/pi/python/servos' )

def lightToggle( ifaceData ):

	if ifaceData[ "lights" ] == 0: ifaceData[ "lights" ] = 1
	elif ifaceData[ "lights" ] == 1: ifaceData[ "lights" ] = 0
	print( "lightToggle: " + str( ifaceData[ "lights" ] ) )
	import pi_lamps

def camMonitor( ifaceData ):

	if ifaceData[ "camera" ] == 0: ifaceData[ "camera" ] = 1
	elif ifaceData[ "camera" ] == 1: ifaceData[ "camera" ] = 0
	print( "camMonitor: " + str( ifaceData[ "camera" ] ) )
	import pi_camera 

def speakerSound( ifaceData ):

	if ifaceData[ "speaker" ] == 0: ifaceData[ "speaker" ] = 1
	elif ifaceData[ "speaker" ] == 1: ifaceData[ "speaker" ] = 0
	print( "speakerSound: " + str( ifaceData[ "speaker" ] ) )
	import speech
	
def articulation( ifaceData ):

	if ifaceData[ "action" ] == 0: ifaceData[ "action" ] = 1
	elif ifaceData[ "action" ] == 1: action[ "action" ] = 0
	print( "articulation: " + str( ifaceData[ "action" ] ) )
	import servo_both
	
def environment( ifaceData ):

	if ifaceData[ "sensor" ] == 0: ifaceData[ "sensor" ] = 1
	elif ifaceData[ "sensor" ] == 1: ifaceData[ "sensor" ] = 0
	print( "environment: " + str( ifaceData[ "sensor" ] ) )
