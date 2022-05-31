# showConnections.py

import os
import sys
import time
import importlib

# init
txtLines = ''

def showUART( ):
	# UART is an asynchronous serial communication protocol
	loadCheck = importlib.util.find_spec('wiringpi')
	found = loadCheck is not None
	if found:
		import wiringpi
		wiringpi.wiringPiSetup()
		serial = wiringpi.serialOpen( '/dev/ttyAMA0', 9600 )
		wiringpi.serialPuts( serial,'hello world!' )
	print( "DONE wiringpi" )

def showSPI( ):
	# SPI ( Serial Peripheral Interface )
	# $ sudo /boot/config.txt > dtparam=spi=on
	# $ ls /dev/*spi* > returns /dev/spidev0.0  /dev/spidev0.1 which represent SPI devices on chip enable pins 0 and 1
	# $ lsmod | grep i2c_ > returns i2c_bcm2835 6465 0 , i2c_dev 6674 0
	# SCLK is the clock speed set by the master
	# MOSI (Master Out Slave In) 
	# MISO (Master In Slave Out) pins 
	# SS or Slave Select pin (marked CE0 or CE1 on the Pi) 
	loadCheck = importlib.util.find_spec('spidev')
	found = loadCheck is not None
	if found:
		import spidev
		CHIP_SELECT_0_OR_1 = 0
		value_8bit = 0 
		spi = spidev.SpiDev( )
		spi.open(0, CHIP_SELECT_0_OR_1)
		spi.max_speed_hz = 1000000
		spi.xfer( [ value_8bit ] )
	print( "DONE SPI spidev" )

def showI2C( ):
	# I2C ( Inter-Integrated-Circuit bus )
	# $ sudo /boot/config.txt > dtparam=i2c_arm=on
	# $ ls /dev/*i2c* > returns /dev/i2c-1 which represents the user-mode I2C interface
	# $ sudo apt-get install -y i2c-tools python-smbus
	# $ i2cdetect -y 1
	# SCL (Serial Clock)
	# SDA (Serial Data) 
	loadCheck = importlib.util.find_spec('smbus')
	found = loadCheck is not None
	if found:
		import smbus            
		DEVICE_BUS = 1
		DEVICE_ADDR = 0x15
		bus = smbus.SMBus( DEVICE_BUS )
		bus.write_byte_data( DEVICE_ADDR , 0x00 , 0x01 )
	print( "DONE I2C smbus" )

# exec
print( txtLines )
showUART( )
showSPI( )
showI2C( )

# fini
sys.stdout.flush( )
print( "DONE" )
