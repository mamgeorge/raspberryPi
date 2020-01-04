# \\python\comm\i2c_MCP4725_org.py
# https://learn.sparkfun.com/tutorials/raspberry-pi-spi-and-i2c-tutorial/all

#	ORA	VCC	pin_01 : 3V3
#	WHT	GND	pin_06 : GND
#	MAG	SDA	pin_03 : BCM_02
#	YEL	SCL	pin_05 : BCM_03

import smbus

DEVICE_BUS = 1 # channel
DEVICE_ADDR = 0x60

# Register addresses (with "normal mode" power-down bits)
REG_WRITE_DAC = 0x40

# Initialize I2C (SMBus)
bus = smbus.SMBus( DEVICE_BUS )

# Create a sawtooth wave 16 times
for ictr in range(0x10000):

	# Create our 12-bit number representing relative voltage
	voltage = ictr & 0xfff

	# Shift everything left by 4 bits and separate bytes
	msg = (voltage & 0xff0) >> 4
	msg = [msg, (msg & 0xf) << 4]

	# Write out I2C command: DEVICE_ADDR, REG_WRITE_DAC, msg[0], msg[1]
	bus.write_i2c_block_data(DEVICE_ADDR, REG_WRITE_DAC, msg)

print( "DONE" )
