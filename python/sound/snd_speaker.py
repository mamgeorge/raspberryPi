# /home/pi/python/speaker.py

import os
import pygame.mixer
import time

#### init
snd_path = "/opt/sonic-pi/etc/samples/"
pth_files = [ "" ]

#### play sounds
def play_wavs( list_wavs , cmax ):
    ictr = 0
    pygame.mixer.init( )
    for pth_file in pth_files:
        while ictr  < cmax:
            snd_item = snd_path + list_wavs[ ictr ]
            snd_size = os.stat( snd_item ).st_size
            if list_wavs[ ictr ] != "README.md":
                pygame.mixer.Sound( snd_item ).play( )
            print( "  %02d | %8d %s" % ( ictr , snd_size , list_wavs[ ictr ] ) )
            time.sleep( 2 )
            ictr += 1

play_wavs( [ "ambi_swoosh.wav" ] , 1 )
#play_wavs( pth_files , len( pth_files ) )
