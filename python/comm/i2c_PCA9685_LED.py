
# outputs a 50% duty cycle PWM single on the 0th channel
# connect an LED & resistor in series to the pin to visualize duty cycle changes and its impact on brightness.

from board import SCL, SDA
import busio
import time
from adafruit_pca9685 import PCA9685

# setup
i2c_bus = busio.I2C(SCL, SDA)	# Create the I2C bus interface
pca = PCA9685(i2c_bus)			# Create a simple PCA9685 class instance
pca.frequency = 60				# Set the PWM frequency to 60hz.
channel01 = 0
channel16 = 15

# set the PWM duty cycle for channel zero to 50% 
# duty_cycle is 16 bits to match other PWM objects but PCA9685 will only give 12 bits of resolution
pca.channels[ channel01 ].duty_cycle = 0x7FFF
pca.channels[ channel16 ].duty_cycle = 0x7FFF
time.sleep( 2 )
pca.channels[ channel01 ].duty_cycle = 0x0
time.sleep( 2 )
pca.channels[ channel16 ].duty_cycle = 0x0

print( "DONE" )
