# sensehat_b9.py
#
# sudo apt-get install sense-hat
# https://pymotw.com/2/threading/

from sense_hat import SenseHat
import sensehat_defn
import time

# definitions
sensehat = SenseHat( )
sensehat.low_light = True

sensehat.set_pixels( sensehat_defn.MLG( ) )
time.sleep( 1 )

sensehat.clear( )
for loop in range( 0 , 4 ):

    for clr in range( 0 , 255 , 1 ):
        for loc in range( 1 , 7 , 1 ):
            sensehat.set_pixel( loc , 1 , clr , 0 , 0 )
        time.sleep( 0.001 )

    for clr in range( 255 , 0 , -1 ):
        for loc in range ( 1 , 7 , 1 ):
            sensehat.set_pixel( loc , 1 , clr , 0 , 0 )
        time.sleep( 0.001 )

    for loc in range ( 1 , 7 , 1 ):
        sensehat.set_pixel( loc , 6 , 255 , 0 , 0 )
        time.sleep( 0.1 )
        sensehat.set_pixel( loc , 6 , 0 , 0 , 0 )
        time.sleep( 0.1 )

sensehat.clear( )