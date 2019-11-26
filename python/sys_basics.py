
# encoding: utf-8
# home/pi/python/sys_basics.py

import os
import sys

def showEnv( ):

    txtLines = ''
    ictr = 0
    for key , val in os.environ.items( ):
        ictr += 1
        if ictr < 10:
            txtLines += "\t%02d | %-15s\t\t%s\n" % ( ictr , key , val )
    # txtLines += "\n\t" + "os.environ.items( ): " % str( len( os.environ.items( ) ) ) + "\n"
    print( txtLines )
	print( os.environ['HOME'] )

def showFiles( snd_path ):

    from os import listdir
    from os.path import isfile, join
    pth_files = [ pth_file
        for pth_file in listdir( snd_path )
        if isfile( join( snd_path , pth_file + "\n" ) )
    ]
    pth_files.sort( )
    print( "\t" + "pth_files: " + str( len( pth_files ) ) )
    print( "\t" + "sys.version: " + sys.version )
    print( pth_files )

def speechTime( ):

	import datetime
	print( "TEST" )
	timed = datetime.datetime.now( ) 
	timed = timed.strftime( '%Y%m%d_%I%M%S' )
	print( timed )
	timed = datetime.datetime.now( ).strftime( 'It is %Y %B %-d, a %A. It is %-I %-M %p.' )
	print( timed )

	## setup
	formatTime = 'It is %Y %B %-d, a %A. It is %-I %-M %p.'
	timed = datetime.datetime.now( ).strftime( formatTime )
	textLine = "'Hello. My name is Mat! {}'"

	## 
	espeakParms = " -ven+m5 -k5 -s180 --stdout"
	aplayCommand = "aplay -f cd -D bluealsa"
	speechCommand = "espeak " + textLine + espeakParms + " | " + aplayCommand

	##	
	os.system( speechCommand.format( timed ) )	
	
print( "\n" + "???????" + "\n" )
showEnv( )
showFiles( "/dbase/" )
speechTime(  )

# https://stackoverflow.com/questions/5137497/find-current-directory-and-files-directory
dir_cwdr = os.getcwd( )
dir_path = os.path.dirname( os.path.realpath( __file__ ) )
print( "dir_cwdr: " + dir_cwdr + " , dir_path: " + dir_path )
print( "__file__: " + __file__ )
