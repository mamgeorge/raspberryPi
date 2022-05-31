# \\python\comm\spi_sample.py
# SPI ( Serial Peripheral Interface )
import sys
import spidev

# init
# pin_03 BCM_02 SDA (Serial Data) 
# pin_05 BCM_03 SCL (Serial Clock)
# pin_19 BCM_10 MOSI (Master Out Slave In) 
# pin_21 BCM_09 MISO (Master In Slave Out) pins 
# pin_23 BCM_11 SCLK is the clock speed set by the master
# pin_24 BCM_08 SS or Slave Select pin (marked CE0) 
# pin_26 BCM_07 SS or Slave Select pin (marked CE1) 
CHIP_SELECT_0_OR_1 = 0
VALUE_8BIT = 0 
MAX_SPEED_HZ = 1000000
	
def showSPI( ):


	spi_dev = spidev.SpiDev( )
	spi_dev.open( 0 , CHIP_SELECT_0_OR_1)
	spi_dev.max_speed_hz = MAX_SPEED_HZ
	spi_dev.xfer( [ VALUE_8BIT ] )
	print( "DONE SPI" )

# exec
showSPI( )

# fini
sys.stdout.flush( )
print( "DONE" )