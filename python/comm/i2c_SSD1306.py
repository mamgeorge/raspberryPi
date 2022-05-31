# \\python\comm\i2c_SSD1306_org.py
# https://github.com/adafruit/Adafruit_Python_SSD1306

#	ORA	VCC	pin_01 : 3V3
#	WHT	GND	pin_06 : GND
#	MAG	SDA	pin_03 : BCM_02
#	YEL	SCL	pin_05 : BCM_03

from board import SCL, SDA
import busio
import adafruit_ssd1306

i2c = busio.I2C(SCL, SDA)

pix_width = 128
pix_height = 64

# create OLED class, change right size for display; address parm is optional
display = adafruit_ssd1306.SSD1306_I2C( pix_width , pix_height , i2c )

# clear display; always call show after changing pixels to make update visible!
display.fill( 0 )

display.show( )

print( "DONE" )
