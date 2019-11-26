# piezo.py
# run on root sudo idle3
# use GPIO pin #03 for black lead

import RPi.GPIO as GPIO
import time

pin_buzz = 18 # normal gpio for red lead ; also for pibrella buzzer

GPIO.setmode( GPIO.BCM )
GPIO.setwarnings( False )
GPIO.setup( pin_buzz , GPIO.OUT )

def buzzer( pitch , duration ):

    if pitch == 0:
        pitch = 1
    period = 1.0 / pitch
    delay = period / 2
    cycles = int( duration * pitch )
    #print( str( pitch ) + ' , ' , end='' )
    for ictr in range( cycles ):
        GPIO.output( pin_buzz , True )
        time.sleep( delay )
        GPIO.output( pin_buzz , False )
        time.sleep( delay )

def play_range( ):

    duration = .03
    for pitch in range( 200 , 2000 + 100 , 100 ):
        buzzer( pitch , duration )
        #print( str( pitch ) + ' , ' , end='' )
        #sys.stdout.write('a')

def play_scale( ):

    scale = [ 20 , 50 , 100 ,  200 , 400 , 600 , 800 , 1000 ] ;
    duration = .3
    for notes in scale:
        buzzer( notes , duration )

play_scale( )
