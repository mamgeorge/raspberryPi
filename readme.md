# raspberryPi
<table><tr>
<td><img src = "images/robot.png"	alt = "robot"		title = "robot"			width = "150"></td>
<td>Technologies:<div style = "white-space: nowrap;">
<img src = "images/raspberrypi.png"	alt = "raspberrypi"	title = "raspberrypi"	width = "50">
<img src = "images/bash.png"		alt = "bash"		title = "bash"			width = "50">
<img src = "images/python.png"		alt = "python"		title = "python"		width = "50">
<img src = "images/node.png"		alt = "node"		title = "node"			width = "50">
<img src = "images/i2c.png"			alt = "i2c"			title = "i2c"			width = "50"></td><td>
<img src = "images/sketchup.png"	alt = "sketchup"	title = "sketchup"		width = "50">
</td></tr></table>

## robotics

intent:

	Currently designed to act as programmable sentry.

	🔹 control	: RPI_0w using NodeJs server to access GPIO Python code
	🔹 movement	: 4 MG995 Servos, 2 subMicro Grippers & HS55 Servos, PCA9685 I2C Controller
	🔹 sensing	: RPI 2.1 Camera, Insiq Bluetooth Speaker, Microphone MI-305
	🔹 travel	: Tamiya Track, Double Gearbox, 2 F130 DC Motors, L293D
	🔹 added	: 10 mm color LED, USB mini microphone
	🔹 power	: rechargeable TL-PB 10400 & TL-PB 5200 mAh Powerbanks

	Explores various bare metal programming technologies. Future plans include:

	▶️ completion of the I2C servo operation
	▶️ VAC (Voice Activated Commands) for more autonomous response
	▶️ simple AI NLP for generalized communication
	▶️ ESA AstroPi SenseHat for environment detection

	The descriptions below show the most recent developments first.

---
### robot 3 / replaced Steppers with Servos

* control:	PCA9685 16 Channel 12-Bit PWM Servo Motor Driver
* servos:	(4) Servo Motor, PN: MG995
* speaker:	USB Bluetooth Speaker Insiq PN: 4326595940		🔹 (upgrades BT3500SLV)
* servos:	(2) Hitec subMicro Servo motor, PN: HS55		🔹 (upgrades HS300)
* grippers:	(2) Actobotics subMicro Gripper Kit, PN: 637104	🔹 (upgrades "A" Grippers)

*The SketchUp 3D drawing required only new Flange & Gripper drawings.
All the other components were accessible online.*<br />
<img src = "images/robot_3_ISO.jpg" alt = "robot_3_ISO" width = "600">

---
* steppers:	(4) Stepper Motor 28BYJ48	🔸 (later removed)

* control:	(4) ULN2003 Driver Board	🔸 (later removed)

*The Steppers were compact, but required too many GPIO leads for a RPI 40 pin J8 form factor.
Some website discussions implied that the RPI timing is not reliable enough for many I2C protocol calls.*<br />
<img src = "images/robot_3_steppers.jpg" alt = "robot_3_steppers" width = "600">

---
### robot 2 / added camera, grippers

* camera:	RPi Camera v2.1 with 8 Megapixel & 1080p resolution, PN: 2.1
* speaker:	GearHead Bluetooth Speaker, PN: BT3500SLV
* microphone:	USB mini microphone, PN: MI-305
* light:	10 mm color LED
* battery:	TPLink PowerBank 10400 mAh, PN: TP-PB10400 🔹 (upgrades 4 AA batteries)
* grippers:	(2) Actobotics Horizontal Gripper Kit "A", PN: 637094
* servos:	(2) HiTec Servo motor, PN: HS300, with C24T or H25T spline

*The Grippers and Speaker worked, but proved to be clunky.*
<img src = "images/robot_2.jpg" alt = "robot_2" width = "600">

*The LibreCad 2D CAD representation with BOM.*
<img src = "images/robot_2_CAD.png" alt = "robot_2_CAD" width = "600">

---
### robot 1 / travel control via SmartPhone

* computer:	RPi0WF 1.1 SOC with BCM2835 cpu
* control:	L293D Controller DriveShield
* gearbox:	Tamiya Double Motorized Gearbox, PN: 70168 with (2) F130 DC Motors
* chassis:	Tamiya Tracked Vehicle Chassis, PN: 70108-1500
* battery:	TPLink PowerBank 5200 mAh, PN: TP-PB5200 (for RPi)
* battery:	(4) AA batteries in case (for motors)

*The RPi operates the L293D thru GPIO ports using Python PWM code signaled by a NodeJS server.*
<img src = "images/robot_1.jpg" alt = "robot_1" width = "600">

### software
<img src = "images/raspberrypi.png"	alt = "raspberrypi"	width = "20"> os base:	Raspbian, Bash, Putty, WinSCP, GitHub...<br />
<img src = "images/python.png"		alt = "python"		width = "20"> control:	Python & IDLE for DC motor PWM control<br />
<img src = "images/node.png"		alt = "node"		width = "20"> server:	NodeJS, Express, (JavaScript, HTML, CSS) for view<br />
<img src = "images/sketchup.png"	alt = "sketchup"	width = "20"> drawing:	LibreCad 2D CAD, Sketchup 3D

*The L293D Controller pinout diagram.*
<img src = "images/l293d.jpg" alt = "L293D_Controller" width = "600">

---
### xtra

[github image viewer](https://htmlpreview.github.io/)<br />
[stackoverflow github html discussion](https://stackoverflow.com/questions/8446218/how-to-see-an-html-page-on-github-as-a-normal-rendered-html-page-to-see-preview)

[HTML5 text folding](https://www.w3schools.com/tags/tag_summary.asp)<br />
[CSS&JS folding](https://levelup.gitconnected.com/collapsible-sections-with-or-without-javascript-3fd871955a9d)

[markdown guide](https://www.markdownguide.org/basic-syntax/) <br />
[collapsible markdown](https://gist.github.com/joyrexus/16041f2426450e73f5df9391f7f7ae5f)
