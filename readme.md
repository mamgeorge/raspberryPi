# RaspberryPi Robot Project
<table><tr>
<td><img src = "images/robot.png"	alt = "robot"		title = "robot"		width = "150"></td>
<td>Technologies:<div style = "white-space: nowrap;">
<img src = "images/raspberrypi.png"	alt = "raspberrypi"	title = "raspberrypi"	width = "50">
<img src = "images/bash.png"		alt = "bash"		title = "bash"		width = "50">
<img src = "images/python.png"		alt = "python"		title = "python"	width = "50">
<img src = "images/node.png"		alt = "node"		title = "node"		width = "50">
<img src = "images/i2c.png"		alt = "i2c"		title = "i2c"		width = "50"></td>
<td>Render:<br />
<img src = "images/sketchup.png"	alt = "sketchup"	title = "sketchup"	width = "50">
</td></tr></table>

## intent

	Currently designed to act as programmable sentry.

	🔹 control	: RPI_0w using NodeJs server to access GPIO Python code
	🔹 movement	: 4 MG995 Servos, 2 subMicro Grippers & HS55 Servos, PCA9685 I2C Controller
	🔹 sensing	: RPI 2.1 Camera, Insiq Bluetooth Speaker, Microphone MI-305
	🔹 travel	: Tamiya Track, Double Gearbox, 2 F130 DC Motors, L293D
	🔹 added	: 10 mm color LED, USB mini microphone
	🔹 power	: rechargeable TL-PB 10400 & TL-PB 5200 mAh Powerbanks

	Explores various inexpensive bare metal programming technologies. Future possibilities:

	▶️ completion of the I2C servo operation
	▶️ VAC (Voice Activated Commands) for more autonomous response
	▶️ simple AI NLP for generalized communication
	▶️ ESA AstroPi SenseHat for environment detection

	The descriptions below show the most recent developments first.

---
### robot 3 (MAT) / added Servo armature

Modular
* computer:	RPi0WF 1.1 SOC with BCM2835 cpu
* camera:	RPi Camera v2.1 with 8 Megapixel & 1080p resolution, PN: 2.1
* power:	TPLink PowerBank 5200 mAh, PN: TP-PB5200 (for RPi)
* software control:	Python & IDLE for DC motor PWM control
* software system:	Raspbian, Bash, Putty, WinSCP, GitHub...
* software server:	NodeJS, Express (JavaScript, HTML, CSS) for view

Articulation
* control:	PCA9685 16 Channel 12-Bit PWM Servo Motor Driver
* servos:	(4) Servo Motor, PN: MG995 (for shoulders, elbows)
* servos:	(2) Hitec subMicro Servo motor, PN: HS55 (replaces HS300)
* grippers:	(2) Actobotics subMicro Gripper Kit, PN: 637104 (replaces "A" Grippers)
* coupling:	(2) 25 Tooth (3F/H25T) Spline to 0.250 inch (replaces Servo Flanges)
* shafting:	(2) slotted set screw, 1/4" dia, 1" length (or M6 x 25mm+)

Transport
* control:	SN754410NE Controller DriveShield (replaces L293D)
* gearbox:	Tamiya Double Motorized Gearbox, PN: 70168 with (2) F130 DC Motors
* chassis:	Tamiya Tracked Vehicle Chassis, PN: 70108-1500
* power:	TPLink PowerBank 10400 mAh, PN: TP-PB10400 (replaces 4 AAs)

Peripherals
* speaker:		USB Bluetooth, Insiq PN: 4326595940 (replaces BT3500SLV)
? microphone:	USB mini microphone, PN: MI-305
? signal:		Color LED, 10 mm
? ligting		High Power LED, 1W, Cool White Light
? pointing		Red Dot Diode Laser, 6mm, 5V, 650nm 5mW

*The SketchUp 3D drawing required only new Coupling & Gripper drawings.<br />
All the other components were accessible online.*<br />
<img src = "images/robot_3_ISO_202303.jpg" alt = "robot_3_ISO_202303" width = "600"><br />

*Originally, the Steppers were used because they had an optimal fit & flexibility.<br />
However, they were not scalable; there were too many GPIO leads needed.<br />
A RPI 40 pin J8 form factor required a different addressing solution.<br />
Some websites suggest RPI timing is not reliable enough many protocol calls.*<br />
early attempts at steppers: (4) Stepper Motor 28BYJ48 (later removed)<br />
early attempts at controls: (4) ULN2003 Driver Board (later removed)<br />
early attempts at flanges: (2) Aluminum H25T gear, PN: ServoCity 525123 (later removed)<br />
see: "\\5Personal\Technology\raspberryPi\docs\projects_basics.txt"<br />
<img src = "images/robot_3_steppers.jpg" alt = "robot_3_steppers" width = "600"><br />

---
### robot 2 / added camera, grippers

* camera:	RPi Camera v2.1 with 8 Megapixel & 1080p resolution, PN: 2.1
* peripherals:	GearHead Bluetooth Speaker, PN: BT3500SLV
* peripherals:	USB mini microphone, PN: MI-305
* peripherals:	10 mm color LED
* power:	TPLink PowerBank 10400 mAh, PN: TP-PB10400 (upgrades 4 AA batteries)
* articulation:	(2) Actobotics Horizontal Gripper Kit "A", PN: 637094
* articulation:	(2) HiTec Servo motor, PN: HS300, with C24T or H25T spline

*The Grippers and Speaker worked, but proved to be clunky.*<br />
<img src = "images/robot_2.jpg" alt = "robot_2" width = "600"><br />

*The LibreCad 2D CAD representation with BOM.*<br />
<img src = "images/robot_2_CAD.jpg" alt = "robot_2_CAD" width = "600"><br />

---
### robot 1 / travel control via SmartPhone

* computer:	RPi0WF 1.1 SOC with BCM2835 cpu
* control:	L293D Controller DriveShield
* gearbox:	Tamiya Double Motorized Gearbox, PN: 70168 with (2) F130 DC Motors
* chassis:	Tamiya Tracked Vehicle Chassis, PN: 70108-1500
* power:	TPLink PowerBank 5200 mAh, PN: TP-PB5200 (for RPi)
* power:	(4) AA batteries in case (for DC motors)

*The RPi operates the L293D thru GPIO ports using Python PWM code signaled by a NodeJS server.*<br />
<img src = "images/robot_1.jpg" alt = "robot_1" width = "600"><br />

---
### software<br />
<img src = "images/raspberrypi.png"	alt = "raspberrypi"	width = "20"> os base:	Raspbian, Bash, Putty, WinSCP, GitHub...<br />
<img src = "images/python.png"		alt = "python"		width = "20"> control:	Python & IDLE for DC motor PWM control<br />
<img src = "images/node.png"		alt = "node"		width = "20"> server:	NodeJS, Express, (JavaScript, HTML, CSS) for view<br />
<img src = "images/sketchup.png"	alt = "sketchup"	width = "20"> drawing:	LibreCad 2D CAD, Sketchup 3D<br />

*The L293D Controller pinout diagram.*<br />
<img src = "images/chip_L293D_layout.jpg" alt = "L293D_Controller" width = "600"><br />

---
### xtra

[github image viewer](https://htmlpreview.github.io/)<br />
[stackoverflow github html discussion](https://stackoverflow.com/questions/8446218/how-to-see-an-html-page-on-github-as-a-normal-rendered-html-page-to-see-preview)

[HTML5 text folding](https://www.w3schools.com/tags/tag_summary.asp)<br />
[CSS&JS folding](https://levelup.gitconnected.com/collapsible-sections-with-or-without-javascript-3fd871955a9d)

[markdown guide](https://www.markdownguide.org/basic-syntax/) <br />
[collapsible markdown](https://gist.github.com/joyrexus/16041f2426450e73f5df9391f7f7ae5f)

Copyright 2021, Martin George, Columbus Ohio
