# \\python\comm\i2c_sample.py
# I2C ( Inter-Integrated-Circuit bus )
import sys
import smbus

# init
# pin_03 BCM_02 SDA (Serial Data) 
# pin_05 BCM_03 SCL (Serial Clock)
DEVICE_BUS = 1
DEVICE_ADDR = 0x15
	
def showI2C( ):

	spi_smbus = smbus.SMBus( DEVICE_BUS )
	spi_smbus.write_byte_data( DEVICE_ADDR , 0x00 , 0x01 )
	print( "DONE I2C" )

# exec
showI2C( )

# fini
sys.stdout.flush( )
print( "DONE" )