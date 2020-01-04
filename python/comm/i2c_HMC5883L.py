# \\python\comm\i2c_HMC5883L.py
# https://github.com/ControlEverythingCommunity/HMC5883/blob/master/Python/HMC5883.py
#
#	ORA	VCC	pin_01 : 3V3
#	WHT	GND	pin_06 : GND
#	MAG	SDA	pin_03 : BCM_02
#	YEL	SCL	pin_05 : BCM_03

import smbus
import time

DEVICE_BUS = 1
DEVICE_ADDR = 0x0D # (13)
i2c_smbus = smbus.SMBus( DEVICE_BUS )

def reader( ):

	# HMC5883 address, DEVICE_ADDR(13)
	# Select configuration register A, DEVICE_ADDR(00)
	# 0x60(96) Normal measurement configuration, Data output rate = 0.75 Hz
	i2c_smbus.write_byte_data( DEVICE_ADDR , 0x00 , 0x60 )
	
	# HMC5883 address, DEVICE_ADDR(13)
	# Select mode register, 0x02(02)
	# 0x00(00) Continuous measurement mode
	i2c_smbus.write_byte_data( DEVICE_ADDR , 0x02 , 0x00 )

	time.sleep(0.5)

	# HMC5883 address, DEVICE_ADDR(13)
	# Read data back from 0x03(03), 6 bytes
	# X-Axis MSB, X-Axis LSB, Z-Axis MSB, Z-Axis LSB, Y-Axis MSB, Y-Axis LSB
	data = i2c_smbus.read_i2c_block_data( DEVICE_ADDR , 0x03 , 6 )

	# Convert the data
	xMag = data[0] * 256 + data[1]
	if xMag > 32767 :
		xMag -= 65536

	zMag = data[2] * 256 + data[3]
	if zMag > 32767 :
		zMag -= 65536

	yMag = data[4] * 256 + data[5]
	if yMag > 32767 :
		yMag -= 65536

	# Output data to screen
	print "Magnetic field in X-Axis : %d" %xMag
	print "Magnetic field in Y-Axis : %d" %yMag
	print "Magnetic field in Z-Axis : %d" %zMag

reader()
print "DONE"
