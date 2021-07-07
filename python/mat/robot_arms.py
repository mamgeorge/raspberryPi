# /python/mat/robot_arms.py
'''
PCA9685

arana		https://www.aranacorp.com/en/using-a-pca9685-module-with-raspberry-pi/

	sudo pip3 install adafruit-circuitpython-servokit
	sudo pip3 install adafruit-circuitpython-pca9685
	sudo pip3 install smbus2	
	sudo raspi-config
	i2cdetect -y 1
		40: 40 --
		70: 70 --

LEDs		https://learn.adafruit.com/16-channel-pwm-servo-driver/python-circuitpython
API			http://adafruit.github.io/Adafruit-PWM-Servo-Driver-Library/html/class_adafruit___p_w_m_servo_driver.html
MagPi		https://magpi.raspberrypi.org/articles/control-servos-circuitpython-raspberry-pi
overview	https://learn.adafruit.com/adafruit-16-channel-servo-driver-with-raspberry-pi

'''
import sys

########################
# setup


########################
# exec

try:

	txtCommand = sys.stdin.readline( ).strip( )
	print( "ACTION: [" + txtCommand + "]" )
	sys.stdout.flush( )

	if txtCommand == ( "a" or "ACTION" ) : print("MOVE ARMS")

except KeyboardInterrupt:
	print("CLEANUP")

########################
# fini

print( "DONE" )
sys.stdout.flush( )