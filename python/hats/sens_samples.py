# sens_samples.py
#
# sudo apt-get install sense-hat
# https://trinket.io/sense-hat

from sense_hat import SenseHat
import sens_defn
import time

# definitions
sensehat = SenseHat( )

#### header
msg = "JESUS!"
sensehat.low_light = True
sensehat.set_rotation( 180 )
sensehat.show_message ( msg , text_colour = sens_defn.G )

sensehat.show_letter( "M" , sens_defn.R )
time.sleep( 1 )
sensehat.show_letter( "G" , sens_defn.G )
time.sleep( 1 )

#### pix
varIMGs = [ sens_defn.MLG , sens_defn.SPRG , sens_defn.SMMR , sens_defn.ATMN , sens_defn.WNTR , sens_defn.FLAG , sens_defn.TREE ]
ictr = 0
while ictr < len( varIMGs ):
	sensehat.set_pixels( varIMGs[ ictr % len( varIMGs ) ]( ) )
	time.sleep( 1 )
	ictr += 1

####
sensehat.clear( )
for loop in range( 0 , 2 ):

	for clr in range( 0 , 255 , 1 ):
		sensehat.set_pixel( 4 , 4 , clr , 0 , 0 )
		time.sleep( 0.001 )

	for clr in range( 255 , 0 , -1 ):
		sensehat.set_pixel( 4 , 4 , clr , 0 , 0 )
		time.sleep( 0.001 )

sensehat.clear( )
time.sleep( .1 )
sensehat.clear( sens_defn.V )
time.sleep( .1 )
sensehat.clear( )
time.sleep( .1 )

### sensor
print( sensehat.gamma )
print( "Humidity : %.4f %%rH" %	sensehat.get_humidity( ) )
print( "Temp main: %.4f C" %	sensehat.get_temperature( ) )
print( "Temp humd: %.4f C" %	sensehat.get_temperature_from_humidity( ) )
print( "Temp prss: %.4f C" %	sensehat.get_temperature_from_pressure( ) )
print( "Pressure : %.4f mb" %	sensehat.get_pressure( ) ) # millibar

sensehat.set_imu_config( True , True , True )

print( "p: {pitch} , r: {roll} , y: {yaw}".format( **sensehat.get_orientation_radians( ) ) )
print( "p: {pitch} , r: {roll} , y: {yaw}".format( **sensehat.get_orientation_degrees( ) ) )
print( "p: {pitch} , r: {roll} , y: {yaw}".format( **sensehat.get_orientation( ) ) )
print( "p: {pitch} , r: {roll} , y: {yaw}".format( **sensehat.get_gyroscope( ) ) )
print( "p: {pitch} , r: {roll} , y: {yaw}".format( **sensehat.get_accelerometer( ) ) )
print( "North: %s" % sensehat.get_compass( ) )

print( sensehat.get_compass_raw( ) )
print( "x: {x} , y: {y} , z: {z}".format( **sensehat.get_compass_raw( ) ) )

print( "x: %.4f" % sensehat.get_compass_raw( )['x']
  + " , y: %.4f" % sensehat.get_compass_raw( )['y']
  + " , Z: %.4f" % sensehat.get_compass_raw( )['z'] )
print( "x: %.4f" % sensehat.get_gyroscope_raw( )['x']
  + " , y: %.4f" % sensehat.get_gyroscope_raw( )['y']
  + " , Z: %.4f" % sensehat.get_gyroscope_raw( )['z'] )
print( "x: %.4f" % sensehat.get_accelerometer_raw( )['x']
  + " , y: %.4f" % sensehat.get_accelerometer_raw( )['y']
  + " , Z: %.4f" % sensehat.get_accelerometer_raw( )['z'] )

print time.strftime( "%Y-%m-%d %I:%M:%S %p %Z" , time.localtime( ) )
