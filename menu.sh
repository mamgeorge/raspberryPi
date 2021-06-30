#!/bin/bash
# \home\pi\menu.sh
# http://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html
# https://misc.flogisoft.com/bash/tip_colors_and_formatting
# https://rosettacode.org/wiki/Terminal_control/Coloured_text
# https://theasciicode.com.ar/

initVars() {

	tabs 4
	DATES=$(date +"%Y %B %-d, a %A at %-I:%M:%S %p.")
	DATEM=$(date +"%Y-%M-%d @ %-I:%M:%S %p.")
	DATEI=$(date --utc +%FT%T.%3N%Z)
	IPADD=hostname -I

	BRED="\033[31;1m"
	BORA="\033[38;5;202m"
	BYEL="\033[33;1m"
	BGRN="\033[32;1m"
	BBLU="\033[34;1m"
	BMAG="\033[35;1m"
	BCYN="\033[36;1m"
	BWHT="\033[37;1m"
	BGRA="\u001b[37m"
	NCLR="\033[0m"

	BCKR="\u001b[41;1m"
	BCKO="\u001b[43;1;202m"
	BCKY="\u001b[43;1m"
	BCKG="\u001b[42;1m"
	BCKB="\u001b[44;1m"
	BCKM="\u001b[45;1m"
	BCKC="\u001b[46;1m"
	BCKW="\u001b[47;1m\u001b[30m"

	BOLD="\u001b[1m"
	UNDR="\u001b[4m"
	REVR="\u001b[7m"
	ENDS="${BGRN}──────────────────────────────────────────────────────────── ${NCLR}"
}

##################
nodejs( )		{ ## 1, 1a, 1b

	echo -e "${BMAG}Expects Node to be installed ${NCLR}"
	node -v
	echo -e ""
	echo -e "\t${BCYN}1a) run Node MAT Service ${NCLR}"
	echo -e "\t${BCYN}1b) run Node GPIO: ${BCKW}BLK${NCLR} pin_39 | ${BCKR}RED${NCLR} pin_40 ${NCLR}"
	echo -e ""
}
node_MAT( )		{ ## 1a

	node nodejs/samples/expressoMAT.js
}
node_GPIO( )	{ ## 1b

	node nodejs/samples/node_rpio.js
}

light_LEDs( )	{ ## 2, 2a, 2b, 2c

	echo -e "${BMAG}Lighting: LED, RGB, TrafficPi${NCLR}"
	echo -e ""
	echo -e "\t${BMAG}2a) light1 LED${NCLR}"
	echo -e "\t${BCKW}BLK${NCLR} pin_39: ground short cathode"
	echo -e "\t${BCKR}RED${NCLR} pin_40: BCM_21 long anode"
	echo -e ""
	echo -e "\t${BMAG}2b) light2 RGB${NCLR}"
	echo -e "\t${BRED}R${BGRN}G${BBLU}B${NCLR} LED 10mm facing east"
	echo -e "\tBCM [ ${BBLU}20 - ${BGRN}16 - ${BWHT}34 - ${BRED}12 ${NCLR}]"
	echo -e "\tPIN [ ${BBLU}38 - ${BGRN}36 - ${BWHT}34 - ${BRED}32 ${NCLR}]"
	echo -e ""
	echo -e "\t${BMAG}2c) light3 Traffic${NCLR}"
	echo -e "\t${BRED}P${NCLR}${BYEL}I${NCLR}${BGRN}T${NCLR}raffic if pin 01 is North: ${NCLR}"
	echo -e "\tBCM [ ${BWHT}39 - ${BGRN}26 - ${BRED}19 - ${BYEL}13 ${NCLR}] # facing east"
	echo -e "\tPIN [ ${BWHT}39 - ${BGRN}37 - ${BRED}35 - ${BYEL}33 ${NCLR}] # facing east"
	echo -e ""
}
light_blink( )	{ ## 2a

	python mamgeorge/python/leds/led_blink.py
}
light_RGB( )	{ ## 2b

	python mamgeorge/python/leds/led_rgb_more.py
}
light_Traffic( ){ ## 2c

	python mamgeorge/python/leds/led_traffic.py
}

pictures( )		{ ## 3, 3a, 3b, 3c, 3d

	echo -e "${BMAG}Camera & Images: May need HDMI or x11 server${NCLR}"
	echo -e ""
	echo -e "\t${BCYN}3a) Expects Camera to be connected${NCLR}"
	echo -e "\t────────────────────────────────────────"
	echo -e "\t${BCYN}3b) Showing ASCII view (but may take a minute)${NCLR}"
	echo -e "\t${BCYN}3c) FEH expects X11 server to be running${NCLR}"
	echo -e "\t${BCYN}3d) FBI expects X11 server to be running${NCLR}"
	echo -e ""
}
camera( )		{ ## 3a

	echo -e "${BMAG}Taking Picture!${NCLR}"
	#raspistill -t 100 -vf -o anyPic.jpg -md 6 -q 10
	echo -e "${BMAG}Done!${NCLR}"
}
image_caca( )	{ ## 3b

	cacaview mamgeorge/images/0_MEG.png
}
image_FEH( )	{ ## 3c

	feh -g 600x400 --scale-down -d mamgeorge/images/0_MEG.png
}
image_FBI( )	{ ## 3d

	fbi mamgeorge/images/0_MEG.png
}

speakers( )		{ ## 4, 4a, 4b, 4c / 4d, 4e, 4f, 4g, 4h

	echo -e "${BBLU}Expects BlueTooth enabled; device MAC addresses added${NCLR}"
	echo -e ""	
	echo -e "\t${BCYN}4a) 12:12:28:6C:78:8C | GH_BT3500	( silver speaker )${NCLR}"
	echo -e "\t${BCYN}4b) 68:F7:FA:DF:79:FB | INSIQBS1	( tiny speaker )${NCLR}"
	echo -e "\t${BCYN}4c) 18:45:C9:1D:0B:ED | ProHT_88133	( black speaker )${NCLR}"
	echo -e "\t────────────────────────────────────────"
	echo -e "\t${BCYN}4d) file aplay${NCLR}"
	echo -e "\t${BCYN}4e) tts espeak${NCLR}"
	echo -e "\t${BCYN}4f) tts flite${NCLR}"
	echo -e "\t${BCYN}4g) tts google${NCLR}"
	echo -e "\t${BCYN}4h) tts espeak & aplay${NCLR}"
	echo -e ""
}
blue_silver( )	{ ## 4a

	echo -e 'connect 12:12:28:6C:78:8C\nquit\n' | sudo bluetoothctl
}
blue_tiny( )	{ ## 4b

	echo -e 'connect 68:F7:FA:DF:79:FB\nquit\n' | sudo bluetoothctl
}
blue_black( )	{ ## 4c

	echo -e 'connect 18:45:C9:1D:0B:ED\nquit\n' | sudo bluetoothctl
}
file_aplay( )	{ ## 4d

	echo Expects Speaker connected; wav files in directory "mamgeorge/sound/"
	aplay -l
	aplay -L
	aplay mamgeorge/sound/ping.wav
}
tts_espeak( )	{ ## 4e

	echo Expects Speaker to be connected
	espeak "Greetings. It is $DATES" -ven-us+m5 -p50 -k5 -s180 -a100
}
tts_flite( )	{ ## 4f

	echo Expects Speaker to be connected
	flite -t "Greetings. It is $DATES"
}
tts_google( )	{ ## 4g

	./speech.sh "Hello, World!"

	mplayer -really-quiet "http://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&tl=en&q=HI"

	words="Hello There"
	link="http://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&tl=en&q="
	mplayer -ao alsa -really-quiet $link"$words"
}
tts_file( )		{ ## 4h

	espeak "Welcome to the George Household" -ven-us+m5 -p50 -k5 -s180 -a100 --stdout | aplay -f cd
}

##################
motors( )		{ ## 5, 5a, 5b, 5c

	echo -e "${BMAG}Servos & Steppers!${NCLR}"
	echo -e ""
	echo -e "\t${BMAG}5a) Servos ! [# ${BYEL}37,${BWHT}39,${BRED}02${NCLR}${BMAG}]${NCLR}"
	echo -e "\t${BMAG}5b) Stepper! [# ${BBLU}11,${BMAG}13,${BYEL}15,${BORA}19 ${BMAG}| ${BWHT}06,${BRED}04${NCLR}${BMAG}]${NCLR}"
	echo -e "\t${BMAG}5c) Steppers [# ${BBLU}11,${BMAG}13,${BYEL}15,${BORA}19 ${BMAG}| ${BWHT}06,${BRED}04${NCLR}${BMAG}]${NCLR}"
	echo -e ""
}
servos( )		{ ## 5a

	echo -e "${BMAG}SERVOS${NCLR}\n"
	echo -e "\t${BYEL}YLW${NCLR} pin_37: BCM26"
	echo -e "\t${BCKW}BLK${NCLR} pin_39: ground-"
	echo -e "\t${BCKR}RED${NCLR} pin_02: 5V+"
	python mamgeorge/python/servos/servo_one.py
}
stepper( )		{ ## 5b

	echo -e "${BMAG}STEPPER${NCLR}\n"
	echo -e "\t${BBLU}BLU${NCLR} pin_11: BCM_17"
	echo -e "\t${BMAG}PUR${NCLR} pin_13: BCM_27"
	echo -e "\t${BYEL}YEL${NCLR} pin_15: BCM_22"
	echo -e "\t${BORA}ORA${NCLR} pin_19: BCM_10"
	echo -e "\t${BCKW}BLK${NCLR} pin_06: ground-"
	echo -e "\t${BCKR}RED${NCLR} pin_04: 5V+"
	python mamgeorge/python/servos/stepper_one.py
}
steppers( )		{ ## 5c

	echo -e "${BMAG}STEPPERS${NCLR}\n"
	echo -e "\t${BBLU}BLU${NCLR} pin_11: BCM_17"
	echo -e "\t${BMAG}PUR${NCLR} pin_13: BCM_27"
	echo -e "\t${BYEL}YEL${NCLR} pin_15: BCM_22"
	echo -e "\t${BORA}ORA${NCLR} pin_19: BCM_10"
	echo -e "\t${BCKW}BLK${NCLR} pin_06: ground-"
	echo -e "\t${BCKR}RED${NCLR} pin_04: 5V+"

	#python mamgeorge/python/servos/stepper_arg.py
	# echo ${my_param_str}|xargs python -u pathFile.py

	echo -e "\nEnter a value between .01 (slow) and .001 (fast)"
	read MY_PARM
	python -u mamgeorge/python/servos/stepper_arg.py $MY_PARM
}

gpio_HATs( )	{ ## 6, 6a, 6b, 6c, 6d

	echo -e "${BMAG}GPIO HATs${NCLR}"
	echo -e ""
	echo -e "\t${BMAG}6a) SenseHat${NCLR} basics"
	echo -e "\t${BMAG}6b) SenseHat${NCLR} samples"
	echo -e "\t${BMAG}6c) SenseHat${NCLR} B9 display"
	echo -e "\t${BMAG}6d) SenseHat${NCLR} MG display"
	echo -e ""
}
hat_basics( )	{ ## 6a

	python mamgeorge/python/hats/sens_basics.py
}
hat_sample( )	{ ## 6b

	python mamgeorge/python/hats/sens_samples.py 0
}
hat_showB9( )	{ ## 6c

	python mamgeorge/python/hats/sens_b9.py 9
}
hat_showMG( )	{ ## 6d

	python mamgeorge/python/hats/sens_b9.py 0
}

gpio_chips( )	{ ## 7, 7a-g, 7s, 7m

	echo -e "${BMAG}gpio circuits${NCLR}"
	echo -e ""
	echo -e "\t6a ${BBLU}HCSR04	distance: [${NCLR} ${BCKR}VCC${NCLR}5V ${BCKW}GND${NCLR}-v ${BCKO}p38${NCLR}:B20 ${BCKB}p40${NCLR}:B21 ${BBLU}]${NCLR}"
	echo -e ""
	echo -e "${BMAG}6i) i2c_sample${NCLR}"
	echo -e ""
	echo -e "\t6b ${BBLU}BMP180	pressure	[${NCLR} ${BCKR}VCC${NCLR}5V ${BCKW}GND${NCLR}-v ${BCKB}p03${NCLR}:SDA ${BCKO}p05${NCLR}:SCL ${BBLU}]${NCLR}"
	echo -e "\t6c ${BBLU}HMC5883L	compass		[${NCLR} ${BCKR}VCC${NCLR}5V ${BCKW}GND${NCLR}-v ${BCKB}p03${NCLR}:SDA ${BCKO}p05${NCLR}:SCL ${BBLU}]${NCLR}"
	echo -e "\t6d ${BRED}MCP4725	DAC			${BBLU}[${NCLR} ${BCKR}VCC${NCLR}5V ${BCKW}GND${NCLR}-v ${BCKB}p03${NCLR}:SDA ${BCKO}p05${NCLR}:SCL ${BBLU}]${NCLR}"
	echo -e "\t6e ${BBLU}SSD1306	OLED		[${NCLR} ${BCKR}VCC${NCLR}5V ${BCKW}GND${NCLR}-v ${BCKB}p03${NCLR}:SDA ${BCKO}p05${NCLR}:SCL ${BBLU}]${NCLR}"
	echo -e "\t6f ${BWHT}MCP23017	expander	[]${NCLR}"
	echo -e "\t6g ${BWHT}PCA9685	controller	[]${NCLR}"
	echo -e ""
	echo -e "${BMAG}6s) spi_sample${NCLR}"
	echo -e ""
	echo -e "\t6m ${BWHT}MCP3008	DAC	${NCLR}"
	echo -e ""
}
gpio_HCSR04( )	{ ## 7a
	python mamgeorge/python/comm/gpio_HCSR04.py
}
i2c_sample( )	{ ## 7i

	ls /dev/i2c* /dev/spi*
	i2cdetect -y 1
	python mamgeorge/python/comm/i2c_sample.py
}
i2c_BMP180( )	{ ## 7b
	python mamgeorge/python/comm/i2c_BMP180.py
}
i2c_HMC5883L( )	{ ## 7c
	python mamgeorge/python/comm/i2c_HMC5883L.py
}
i2c_MCP4725( )	{ ## 7d
	python mamgeorge/python/comm/i2c_MCP4725.py
}
i2c_SSD1306( )	{ ## 7e
	python mamgeorge/python/comm/i2c_SSD1306.py
}
i2c_MCP23017( )	{ ## 7f
	python mamgeorge/python/comm/i2c_MCP23017.py
}
i2c_PCA9685( )	{ ## 7g
	python mamgeorge/python/comm/i2c_PCA9685.py
}
spi_sample( )	{ ## 7s

	ls /dev/i2c* /dev/spi*
	python mamgeorge/python/comm/spi_sample.py
}
spi_MCP3008( )	{ ## 7m
	python mamgeorge/python/comm/spi_MCP3008.py
}

##################
robot_cntl( )	{ ## 8, 8a

	echo -e "${BCKR}ROBOT${NCLR}"
	echo -e ""
	echo -e "\t${BRED}8a) Robot_Interface${NCLR} expects GPIO, Node, etc."
	echo -e ""
}
robot_iface( )	{ ## 8a

	echo -e "${BMAG}Expects L293D: [# ${BGRN}35,${BYEL}36,${BWHT}37,${BBLU}38${BMAG}]${NCLR}\n"
	echo -e "\t${BGRN}GRN${NCLR} pin_35: BCM_19 m1LFT-"
	echo -e "\t${BYEL}YEL${NCLR} pin_36: BCM_16 m2RGT-"
	echo -e "\t${BWHT}WHT${NCLR} pin_37: BCM_26 m1LFT+"
	echo -e "\t${BBLU}BLU${NCLR} pin_38: BCM_20 m2RGT+"
	echo -e "${BGRN}		   ┌─────────┐		 ┌────────┐${NCLR}"
	echo -e "${BGRN}	┌──────┘${BBLU} 8 forw ${BGRN} └──────┐${BGRN}│ + fast │${NCLR}"
	echo -e "${BGRN}	│${BBLU}4 left│${BRED} 5 stop ${BBLU} │6 rght${BGRN}│├────────┤${NCLR}"
	echo -e "${BGRN}	└──────┐${BBLU} 2 back ${BGRN} ┌──────┘${BGRN}│ - slow │${NCLR}"
	echo -e "${BGRN}		   └─────────┘		 ${BGRN}└────────┘${NCLR}"
	echo -e "${BGRN}	┌───────────────────────┐${NCLR}"
	echo -e "${BGRN}	│${BMAG} L lights	│  C camera ${BGRN}│${NCLR}"
	echo -e "${BGRN}	│${BMAG} A action	│  X sensor ${BGRN}│${NCLR}"
	echo -e "${BGRN}	└───────┐${BBLU} S speak ${BGRN}┌─────┘${NCLR}"
	echo -e "${BGRN}			└─────────┘		 ${NCLR}"
	python mamgeorge/python/mat/robot.py
}

show_pins( )	{ ## 9, 9a, 9b

	echo -e "${BORA}show GPIO${NCLR}"
	echo -e ""
	echo -e "\t${BORA}9a) GPIO diagram, MLG details${NCLR}"
	echo -e "\t${BORA}9b) GPIO diagram, pinout.xyz ${NCLR}"
	echo -e "\t${BORA}9c) GPIO diagram, WiringPi   ${NCLR}"
	echo -e ""
}
show_pinsMG( )	{ ## 9a

	echo -e "${REVR}40 pin is J8 pinout board; 26 pin is P1 pinout${NCLR}"
	echo -e "					┌────────────┐"
	echo -e "			${BCKR}pw:+3v3${NCLR}	│ 01 ${BRED}■${NCLR}	${BRED}■${NCLR} 02 │	${BCKR}pw:+5V${NCLR}				"
	echo -e "I2C_SDA1	${BGRA}BCM_02${NCLR}	│ 03 ${BYEL}■${NCLR}	${BRED}■${NCLR} 04 │	${BCKR}pw:+5V${NCLR}				"
	echo -e "I2C_SCL1	${BGRA}BCM_03${NCLR}	│ 05 ${BYEL}■${NCLR}	${BWHT}■${NCLR} 06 │	${BCKW}ground${NCLR}				"
	echo -e "	GCLK0	${BGRA}BCM_04${NCLR}	│ 07 ${BGRN}■${NCLR}	${BCYN}■${NCLR} 08 │	${BGRA}BCM_14${NCLR}	UART_TXD0	"
	echo -e "			${BCKW}ground${NCLR}	│ 09 ${BWHT}■${NCLR}	${BCYN}■${NCLR} 10 │	${BGRA}BCM_15${NCLR}	UART_RXD0	"
	echo -e "	GEN0	${BGRA}BCM_17${NCLR}	│ 11 ${BGRN}■${NCLR}	${BGRN}■${NCLR} 12 │	${BGRA}BCM_18${NCLR}	GEN1 , PWM0	"
	echo -e "	GEN2	${BGRA}BCM_27${NCLR}	│ 13 ${BGRN}■${NCLR}	${BWHT}■${NCLR} 14 │	${BCKW}ground${NCLR}				"
	echo -e "	GEN3	${BGRA}BCM_22${NCLR}	│ 15 ${BGRN}■${NCLR}	${BGRN}■${NCLR} 16 │	${BGRA}BCM_23${NCLR}	GEN4		"
	echo -e "			${BCKR}pw:+3v3${NCLR}	│ 17 ${BRED}■${NCLR}	${BGRN}■${NCLR} 18 │	${BGRA}BCM_24${NCLR}	GEN5		"
	echo -e "SPI_MOSI	${BGRA}BCM_10${NCLR}	│ 19 ${BMAG}■${NCLR}	${BWHT}■${NCLR} 20 │	${BCKW}ground${NCLR}	-			"
	echo -e "SPI_MISO	${BGRA}BCM_09${NCLR}	│ 21 ${BMAG}■${NCLR}	${BGRN}■${NCLR} 22 │	${BGRA}BCM_25${NCLR}	GEN6		"
	echo -e "SPI_SCLK	${BGRA}BCM_11${NCLR}	│ 23 ${BMAG}■${NCLR}	${BMAG}■${NCLR} 24 │	${BGRA}BCM_08${NCLR}	SPI_CE0_N	"
	echo -e "			${BCKW}ground${NCLR}	│ 25 ${BWHT}■${NCLR}	${BMAG}■${NCLR} 26 │	${BGRA}BCM_07${NCLR}	SPI_CE1_N	"
	echo -e "					├────────────┤"
	echo -e "I2C_IDSD	${BGRA}EEPROM${NCLR}	│ 27 ${BYEL}■${NCLR}	${BYEL}■${NCLR} 28 │	${BGRA}EEPROM${NCLR}	I2C_IDSC	"
	echo -e "	GCLK1	${BGRA}BCM_05${NCLR}	│ 29 ${BGRN}■${NCLR}	${BWHT}■${NCLR} 30 │	${BCKW}ground${NCLR}				"
	echo -e "	GCLK2	${BGRA}BCM_06${NCLR}	│ 31 ${BGRN}■${NCLR}	${BGRN}■${NCLR} 32 │	${BGRA}BCM_12${NCLR}	PWM0		"
	echo -e "	PWM1	${BGRA}BCM_13${NCLR}	│ 33 ${BGRN}■${NCLR}	${BWHT}■${NCLR} 34 │	${BCKW}ground${NCLR}				"
	echo -e "SPI_MISO	${BGRA}BCM_19${NCLR}	│ 35 ${BGRN}■${NCLR}	${BGRN}■${NCLR} 36 │	${BGRA}BCM_16${NCLR}				"
	echo -e "			${BGRA}BCM_26${NCLR}	│ 37 ${BGRN}■${NCLR}	${BGRN}■${NCLR} 38 │	${BGRA}BCM_20${NCLR}	SPI_MOSI	"
	echo -e "			${BCKW}ground${NCLR}	│ 39 ${BWHT}■${NCLR}	${BGRN}■${NCLR} 40 │	${BGRA}BCM_21${NCLR}	SPI_SCLK	"
	echo -e "					└────────────┘"
}
show_pinsOT( )	{ ## 9b from ????

pinout
}
show_pinsWP( )	{ ## 9c from WiringPi

gpio readall
}

##################
exits( )	{ ## 0

	echo
	echo -e MLG DATE: "$DATEM"
	echo -e ISO DATE: "$DATEI"
	echo -e model...: "$(cat /proc/device-tree/model | xargs --null)"
	echo -e release.: "$(cat /etc/os-release | grep PRETTY)"
	echo -e address.: "$(cat /sys/class/net/wlan0/address)"
	echo -e uname...: "$(uname -a)"
	echo -e hostname: "$(hostname -I)"
	echo -e ifconfig: "$(sudo ifconfig | grep 192 | xargs)"
	echo -e iwgetid.: "$(iwgetid)"
	echo -e files...: "$(df -h | grep root)"
	echo -e free....: "$(free -m | grep Mem)"

	echo -e "\n${BGRN}Exits Menu!${NCLR}\n${ENDS}"
}
reboots( )	{ ## r

	echo -e "\n${BGRN} Rebooting!${NCLR}\n${ENDS}"
	sudo reboot
}
shutdown( )	{ ## x

	echo -e "\n${BGRN} Shutting Down!${NCLR}\n${ENDS}"
	sudo shutdown -h now
}

##################
initVars

while [ "$option" != "0" ]
do

	echo -e "${ENDS}\n${BGRN}Greetings. ${DATES} \n ${NCLR}"

	## echo -e "0 EXIT | 1 node | 2 lights | 3 camera | 4 speaker | 5 motors | 6 comm | 7 xxxx | 8 robot | 9 pins | r REBOOT"
	echo -e "0 EXIT			exits menu"
	echo -e "1 nodejs		http://$(hostname -I):3000"
	echo -e "2 light_LEDs	shows LED, ${BRED}R${BGRN}G${BBLU}B${NCLR}, Traffic"
	echo -e "3 camera		takes a picture & displays"
	echo -e "4 speakers		loads GH_BT3500, INSIQBS1, ProHT_88133; plays tts & files"
	echo -e "5 motors		runs servos, stepper"
	echo -e "6 gpio_HATs		runs gpio based HAT attachments"
	echo -e "7 gpio_chips	runs gpio, i2c, or spi based programs"
	echo -e "─────────────────────────────────────────"
	echo -e "8 robot_cntl	runs Robot node interface"
	echo -e "9 show_pins		shows diagram of J8 pinout board"
	echo -e "r REBOOT		reboots PI, x shutsDown PI"
	echo -e "${ENDS}"

	read option

	case $option in

		## if [[ ( $option == "1" ) ]]; then nodejs; fi
		0) exits 		;;
		1) nodejs		;;
			1a) node_MAT	;;
			1b) node_GPIO	;;

		2) light_LEDs		;;
			2a) light_blink	;;
			2b) light_RGB	;;
			2c) light_Traffic ;;

		3) pictures			;;
			3a) camera		;;
			3b) image_caca	;;
			3c) image_FEH	;;
			3d) image_FBI	;;

		4) speakers			;;
			4a) blue_silver	;;
			4b) blue_timy	;;
			4c) blue_black	;;
			4d) file_aplay	;;
			4e) tts_espeak	;;
			4f) tts_flite	;;
			4g) tts_google	;;
			4h) tts_file	;;

		############################
		5) motors			;;
			5a) servos		;;
			5b) stepper		;;
			5c) steppers	;;

		6) gpio_HATs		;;
			6a) hat_basics	;;
			6b) hat_sample	;;
			6c) hat_showB9	;;	b9) hat_showB9 ;;
			6d) hat_showMG	;;	mg) hat_showMG ;;

		7) gpio_chips		;;
			7a) gpio_HCSR04	;;
			7i) i2c_sample	;;
				7b) i2c_BMP180	 ;;
				7c) i2c_HMC5883L ;;
				7d) i2c_MCP4725	 ;;
				7e) i2c_SSD1306	 ;;
				7f) i2c_MCP23017 ;;
				7g) i2c_PCA9685	 ;;
				7m) spi_MCP3008	 ;;
			7s) spi_sample ;;

		############################
		8) robot_cntl		;;
			8a) robot_iface	;;

		9) show_pins		;;
			9a) show_pinsMG	;;
			9b) show_pinsOT	;;
			9c) show_pinsWP	;;

		r) reboots		;; x) shutdown ;;
		## *) ;;
	esac
done
####
