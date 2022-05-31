
import os
import sys

def showEnv( ):

	txtLines = "{ [ "	
	ictr = 0
	for key , val in os.environ.items( ):
		ictr += 1
		# if ictr < 10:
		# txtLines += "\n\t" + "os.environ.items( ): " % str( len( os.environ.items( ) ) ) + "\n"
		txtLines += "{ '%-15s' : '%s' } , " % ( key , val )

	return txtLines + " ] }"

print( showEnv( ) )
sys.stdout.flush( )
