# raspberryPi

## robotics

intent:

	Currently designed to act as programmable sentry.

	* control	: RPI_0w using NodeJs server to access GPIO Python code
	* travel	: Tamiya Track, Double Gearbox, 2 F130 DC Motors, L293D
	* movement	: 4 MG995 Servos, 2 subMicro Grippers, 2 HS55 Servos
	* sensing	: RPI 2.1 Camera, Insiq Bluetooth Speaker, Microphone MI-305
	* added		: 10 mm color LED
	* power		: Powered by rechargeable TL-PB 10400 & TL-PB 5200 mAh Powerbanks

	Descriptions below show most recent developments first.

---
### robot 3 / replaced Steppers with Servos

* control	PCA9685 16 Channel 12-Bit PWM Servo Motor Driver
* servos	(4) Servo Motor, PN: MG995
* speaker	USB Bluetooth Speaker Insiq PN: 4326595940 (upgrades BT3500SLV)
* servos	(2) Hitec SubMicro Servo motor, PN: HS55 (upgrades HS300)
* grippers	(2) Actobotics subMicro Gripper Kit, PN: 637104 (upgrades "A" Grippers)

*The SketchUp 3D drawing below required only new Flange & Gripper drawings. All the other components were accessible online.*<br />
<img src="images/robot_3_ISO.jpg" alt = "robot_3_ISO" width="600">

---
* steppers:	(4) Stepper Motor 28BYJ48 (later removed)

* control:	(4) ULN2003 Driver Board (later removed)

*The Steppers were compact, but required too many GPIO leads for a RPI 40 pin J8 form factor. Some website discussions implied that the RPI timing is not reliable enough for many I2C protocol calls.*
<img src="images/robot_3_steppers.jpg" alt = "robot_3_steppers" width="600">

---
### robot 2 / added camera, grippers

* camera:	RPi Camera v2.1 with 8 Megapixel & 1080p resolution, PN: 2.1
* speaker:	GearHead Bluetooth Speaker, PN: BT3500SLV
* microphone:	USB mini microphone, PN: MI-305
* light:	10 mm color LED
* battery:	TPLink PowerBank 10400 mAh, PN: TP-PB10400 (upgrades 4 AA batteries)
* grippers:	(2) Actobotics Horizontal Gripper Kit "A", PN: 637094
* servos:	(2) HiTec Servo motor, PN: HS300, with C24T or H25T spline

*The Grippers and Speaker worked, but proved to be clunky.*
<img src="images/robot_2.jpg" alt = "robot_2" width="600">

*LibreCad 2D CAD representation with BOM.*
<img src="images/robot_2_CAD.png" alt = "robot_2_CAD" width="600">

---
### robot 1 / travel control via SmartPhone

* computer:	RPi0WF 1.1 SOC with BCM2835 cpu
* control:	L293D Controller DriveShield
* gearbox:	Tamiya Double Motorized Gearbox, PN: 70168 with (2) F130 DC Motors
* chassis:	Tamiya Tracked Vehicle Chassis, PN: 70108-1500
* battery:	TPLink PowerBank 5200 mAh, PN: TP-PB5200 (for RPi)
* battery:	(4) AA batteries in case (for motors)

*Required using Python PWM coding for the L293D GPIOs thru NodeJS.*
<img src="images/robot_1.jpg" alt = "robot_1" width="600">

### software
* os base:	Raspbian, Bash, Putty, WinSCP, GitHub...
* control:	Python & IDLE for DC motor PWM control
* server:	NodeJS, Express (JavaScript, HTML, CSS) for view
* drawing:	LibreCad 2D CAD, Sketchup 3D

*L293D Controller pinout diagram.*
<img src="images/l293d.jpg" alt = "L293D_Controller" width="600">

---
### xtra

[markdown guide](https://www.markdownguide.org/basic-syntax/)
