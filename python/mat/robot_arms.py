# /python/mat/robot_arms.py

import sys

########################
# setup


########################
# exec

try:

	txtCommand = sys.stdin.readline( ).strip( )
	print( "ACTION: [" + txtCommand + "]" )
	sys.stdout.flush( )
	
	if txtCommand == ( "a" or "ACTION" )	: print("MOVE ARMS")

except KeyboardInterrupt:
	print("CLEANUP")

########################
# fini

print( "DONE" )
sys.stdout.flush( )