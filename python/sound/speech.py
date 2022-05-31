## python python/speech.py

import os
import sys
import datetime

## setup
formatTime = 'It is %Y %B %-d, a %A. It is %-I %-M %p.'
timed = datetime.datetime.now( ).strftime( formatTime )
textLine = "'Hello. My name is Mat! {}'"

## 
espeakParms = " -ven+m5 -k5 -s180 --stdout"
aplayCommand = "aplay -f cd -D bluealsa"
speechCommand = "espeak " + textLine + espeakParms + " | " + aplayCommand

##
os.system( speechCommand.format( timed ) )

	