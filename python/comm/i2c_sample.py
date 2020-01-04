# \\python\comm\i2c_sample.py
# I2C ( Inter-Integrated-Circuit bus )

#	ORA	VCC	pin_01 : 3V3
#	WHT	GND	pin_06 : GND
#	MAG	SDA	pin_03 : BCM_02
#	YEL	SCL	pin_05 : BCM_03

import sys
import smbus

DEVICE_BUS = 1
DEVICE_ADDR = 0x0D

def showI2C( ):

	i2c_smbus = smbus.SMBus( DEVICE_BUS )

	for DEV_ADD in range( 0x00, 0x77 ):

		# DEV_CHR = chr( DEV_ADD )
		# i2c_smbus.write_byte_data( DEV_ADD , 0x00 , 0x01 )
		# print( "I2C read at address: %d" % DEV_ADD )
		try:
			lngVal = i2c_smbus.read_word_data( DEV_ADD , 0x00 )
			print( "I2C address: %s active %d" % ( hex( DEV_ADD ) , DEV_ADD ) )

		except:

			print( "%d | " % DEV_ADD ),
			lngVal=0
# exec
showI2C( )

# fini
sys.stdout.flush( )
print( "DONE" )