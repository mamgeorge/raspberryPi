# pwc: 900-2100, ang: 0-165, ms: 20, volts: 4.8-6, 'HS-81 Micro, sample'
# pwc: 500-2500, ang: 0-180, ms: 20, volts: 3-7.2, 'MG995 armature, TianKongRC'

import time
from adafruit_servokit import ServoKit

# setup
freq = 50
max_ang01 = 165 
min_pwc01 = 900
max_pwc01 = 2100

max_ang16 = 180 
min_pwc16 = 500
max_pwc16 = 2500

channel = 0
max_ang = max_ang16
min_pwc = min_pwc16
max_pwc = max_pwc16

PCA_ServoKit = ServoKit(channels=16,frequency=freq)
PCA_ServoKit.servo[ channel ].frequency = 50
PCA_ServoKit.servo[ channel ].actuation_range = max_ang 
PCA_ServoKit.servo[ channel ].set_pulse_width_range(min_pwc, max_pwc)

# main
PCA_ServoKit.servo[ channel ].angle = max_ang
time.sleep( 0.5 )
PCA_ServoKit.servo[ channel ].angle = 0
print( "DONE" )
