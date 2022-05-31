# \\python\comm\uart_sample.py
# UART Universal Asynchronous Receiver/Transmitter
# UART is a hardware device for asynchronous serial communication 
import sys
import wiringpi
import serial

# init
DEVICE = '/dev/ttyAMA0'
BAUD = 9600
TXTLINE = 'Hello World!'

def showUART( ):
	wiringpi.wiringPiSetup()
	uart_serial = serial.Serial ( DEVICE , BAUD )
	wiringpi.serialPuts( uart_serial , TXTLINE )

# exec
print( txtLines )
showUART( )

# fini
sys.stdout.flush( )
print( "DONE" )