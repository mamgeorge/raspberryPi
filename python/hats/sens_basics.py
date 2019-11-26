# sens_basics.py
#
# sudo apt-get install sense-hat
# https://trinket.io/sense-hat

from espeak import espeak
from sense_hat import SenseHat
import sens_defn
import time

# definitions
sensehat = SenseHat( )

#### header
msg = "JESUS!"
sensehat.low_light = True
sensehat.set_rotation( 180 )
sensehat.show_message( msg , text_colour = sens_defn.G )

sensehat.show_letter( "MG" , sens_defn.R )
time.sleep( 1 )
espeak.synth( "MG!" )

### sensor
print( sensehat.gamma )
tempFarenheit = ( sensehat.get_temperature( ) * ( 9.0/5.0 ) ) + 32.0
print( "Temp main: %.2f F" % tempFarenheit )

print time.strftime( "%Y-%m-%d %I:%M:%S %p %Z" , time.localtime( ) )
sensehat.clear( )
