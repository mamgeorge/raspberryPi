# https://picamera.readthedocs.io/en/release-1.13/recipes1.html

import datetime
from time import sleep
from picamera import PiCamera

# setup
defaultOpt = 'p'
defaultDir = '/home/pi/Pictures/xtra/'
#
photoWait = 1
movieLen = 10
#
piCam = PiCamera( )
piCam.resolution = ( 600 , 400 )

def takePhoto( ):
	timed = datetime.datetime.now( ) 
	timed = timed.strftime( 'snap_%Y%m%d%I%M%S.jpg' )
	photoFile = defaultDir + timed
	#	
	piCam.rotation = 180	# piCam.start_preview( )	
	sleep( photoWait ) 
	piCam.capture( photoFile )
	print( "photo: " + photoFile )
	
def takeMovie( ):
	timed = datetime.datetime.now( ) 
	timed = timed.strftime( 'snap_%Y%m%d%I%M%S.h264' )
	movieFile = defaultDir + timed
	#
	piCam.start_recording( movieFile )
	piCam.wait_recording( movieLen )
	piCam.stop_recording( )
	print( "movie: " + movieFile )

# main	
if defaultOpt == ( "p" or "photo" ) : takePhoto( )
if defaultOpt == ( "m" or "movie" ) : takeMovie( )

	