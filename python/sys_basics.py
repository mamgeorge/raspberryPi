## home/pi/python/sys_basics.py
## encoding: utf-8
## exec( open( './xtra/temp.py' ).read() )

import os
import sys
import sqlite3

## setup
GRN = "\N{ESC}[32;1m"
BLK = "\u001b[0m"
householdName = "George Household"
householdFolk = [ "Martin", "Mary", "Samuel", "Kenzie" ]
message = "Hello" # message = input("Enter message: ") , '\033[92m' 
numberEnv = 10
listFile = "C:/Users/mamge/OneDrive/Documents/" \
	+ "5Personal/Technology/raspberryPi/python/listFile.txt"

## processes
def loopArrays( ):

	print( "Arrays" )
	ictr = 0
	print( "\t" + message + ", " + householdName )
	print( "\t" + "number people: " + str( len( householdFolk ) ) )
	print()
	for name in householdFolk:
		ictr+=1
		print( "\t" + str(ictr) + " " + name )
	print()

def showEnv( numberToShow ):

	print( "EnvVars" )
	txtLines = ''
	ictr = 0
	for key , val in os.environ.items( ):
		ictr += 1
		if ictr <= numberToShow:
			txtLines += "\t%02d | %-15s\t\t%s\n" % ( ictr , key , val )
	##
	txtLines += "\t" + "os.environ.items( ): " + str( len( os.environ.items( ) ) ) + "\n"
	txtLines += "\t" + "os.environ['USERNAME']: " + os.environ['USERNAME'] 
	txtLines += "\t" + "sys.version: " + sys.version 
	txtLines += "\t" + "sys.version_info: " + str( sys.version_info ) 
	print( txtLines )
	print( )

def showFile( pathFile ):

	print( "File" )
	try:
		file = open( pathFile, "r" )
		for line in file:
			print( "\t" + line.strip( ) )
		file.close()
	except:
		print( "\t" + "WARNING: could not find file: " + pathFile )
	print()

def showFiles( soundFilePath ):

	print( "Files" )
	from os import listdir
	from os.path import isfile, join
	pth_files = [ pth_file
		for pth_file in listdir( soundFilePath )
		if isfile( join( soundFilePath , pth_file + "\n" ) )
	]
	pth_files.sort( )
	print( "\t" + "pth_files: " + str( len( pth_files ) ) )
	print( "\t" + str( pth_files ) )

	# https://stackoverflow.com/questions/5137497/find-current-directory-and-files-directory
	dir_cwdr = os.getcwd( )
	dir_path = os.path.dirname( os.path.realpath( __file__ ) )
	print( "\t" + "dir_cwdr: " + dir_cwdr  )
	print( "\t" + "dir_path: " + dir_path )
	print( "\t" + "__file__: " + __file__ )
	print( )

def showTime( ):

	print( "DateTimes" )	
	import importlib
	#loadCheck = importlib.util.find_spec('datetime')
	found = True #found = loadCheck is not None
	if found:	
	
		import datetime
		#timeFormat = 'It is %Y %B %-d, a %A. It is %-I %-M %p.'
		datetimeStandard = datetime.datetime.now( ) 
		datetimeCompacted = datetimeStandard.strftime( '%Y%m%d_%I%M%S' )
		#datetimeFormatted = datetimeStandard.strftime( timeFormat )
		print( "\t" + "datetimeStandard : " + str( datetimeStandard ) )
		print( "\t" + "datetimeCompacted: " + datetimeCompacted )
		#print( "datetimeFormatted: " + datetimeFormatted )
		print( )

def showDB( ):
        
	# https://docs.python.org/3/library/sqlite3.html
	print( "DataBase Sqlite" )
	connectDB = sqlite3.connect('C:\dbase\sqlite\chinook.db')
	cursor = connectDB.cursor()
	for row in cursor.execute('SELECT CustomerId, FirstName, LastName, City, Country '
		+ 'FROM customers '
		+ 'WHERE Country = \'Germany\' ORDER BY LastName'):
		print( "\t" + str( row[2] ) + "\t | " + str( row ) )
	connectDB.close()		
	print( ) 		

def speakWords( ):

	print( "Speech" )
	textLine = "'Hello. My name is Mat! {}'"
	espeakParms = " -ven+m5 -k5 -s180 --stdout"
	aplayCommand = "aplay -f cd -D bluealsa"
	speechCommand = "espeak " + textLine + espeakParms + " | " + aplayCommand
	os.system( speechCommand )
	print( )	
	
## close
loopArrays( )
showEnv( numberEnv )
showFile( listFile )
showFiles( "/dbase/" )
showTime(  )
showDB(  )
speakWords(  )
print( "[ 马丁乔治 ] " )
print( "[ " + GRN + "TEST" + BLK + " ]\n" )
print( "DONE" )
