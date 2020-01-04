# \\python\comm\i2c_MCP4725.py
# https://learn.sparkfun.com/tutorials/raspberry-pi-spi-and-i2c-tutorial/all

#	ORA	VCC	pin_01 : 3V3
#	WHT	GND	pin_06 : GND
#	MAG	SDA	pin_03 : BCM_02
#	YEL	SCL	pin_05 : BCM_03

import board
import busio
import adafruit_mcp4725

i2c = busio.I2C( board.SCL , board.SDA )

dac = adafruit_mcp4725.MCP4725( i2c , address=0x60 )
# Optionally you can specify a different address if you override the A0 pin.
# amp = adafruit_max9744.MAX9744(i2c, address=0x63)

# There are a three ways to set the DAC output, you can use any of these:
# Use the value property with a 16-bit number just like the AnalogOut class.
# Note the MCP4725 is only a 12-bit DAC so quantization errors will occur.
# The range of values is 0 (minimum/ground) to 65535 (maximum/Vout).
dac.value = 65535 

# Use the raw_value property to directly read and write the 12-bit DAC value.
# The range of values is 0 (minimum/ground) to 4095 (maximum/Vout).
dac.raw_value = 4095

# Use the normalized_value property to set the output with a floating point value
# in the range 0 to 1.0 where 0 is minimum/ground and 1.0 is maximum/Vout.
dac.normalized_value = 1.0  

# Main loop will go up and down through the range of DAC values forever.
while True:
	# Go up the 12-bit raw range.
	print('Going up 0-3.3V...')
	for i in range(4095):
		print('i: %d' % i )
		dac.raw_value = i

	# Go back down the 12-bit raw range.
	print('Going down 3.3-0V...')
	for i in range(4095, -1, -1):
		print('i: %d' % i )
		dac.raw_value = i
		
print( "DONE" )
