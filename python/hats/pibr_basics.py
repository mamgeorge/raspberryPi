# pibrella.py
#
# requires python 2.7.3 run from root terminal
# sudo apt-get install python-pip
# sudo pip install pibrella

import pibrella , time

def show_inputs( ):

    pibrella.output.e.on( )
    pibrella.output.f.on( )
    pibrella.output.g.on( )
    pibrella.output.h.on( )
    time.sleep( 0.5 )
    pibrella.output.e.off( )
    pibrella.output.f.off( )
    pibrella.output.g.off( )
    pibrella.output.h.off( )

def show_lights( ):

    pibrella.light.red.pulse( 0.1 , 0.1 , 0.1 , 0 )
    pibrella.light.green.pulse( 0.1 , 0.1 , 0.1 , 0 )
    show_inputs( )

def play_buzzer( ):

    tune = [ 3 , 9 , 9 , 11 , 9 , 8 , 6 , 6 , 6 , 11 , 11 , 13 , 11 , 9 , 8 , 3 ]
    for note in tune:
        pibrella.buzzer.note( note )
        time.sleep( .3 )
        pibrella.buzzer.off( )

    show_inputs( )
    pibrella.light.stop( )

show_lights( )
play_buzzer( )
print( 'Merry Christmas!' )
