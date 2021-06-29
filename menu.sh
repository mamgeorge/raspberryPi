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
nodejs( )	{ ## 1, 1a, 1b

	echo -e "${BMAG}Expects Node to be installed ${NCLR}"
	node -v
	echo
	echo -e "\t${BCYN}1a) run Node MAT Service ${NCLR}"
	echo -e "\t${BCYN}1b) run Node GPIO: ${BCKW}BLK${NCLR} pin_39 | ${BCKR}RED${NCLR} pin_40 ${NCLR}"
}
nodeMAT( )	{ ## 1a
	node nodejs/samples/expressoMAT.js
}
nodeGPIO( )	{ ## 1b
	node nodejs/samples/node_rpio.js
}

lights( )	{ ## 2, 2a, 2b, 2c

	echo -e "${BMAG}2a) light1 LED${NCLR}"
	echo -e "\t${BCKW}BLK${NCLR} pin_39: ground short cathode"
	echo -e "\t${BCKR}RED${NCLR} pin_40: BCM_21 long anode"

	echo -e "\n${BMAG}2b) light2 RGB${NCLR}"
	echo -e "\t${BRED}R${BGRN}G${BBLU}B${NCLR} LED 10mm facing east"
	echo -e "\tBCM [ ${BBLU}20 - ${BGRN}16 - ${BWHT}34 - ${BRED}12 ${NCLR}]"
	echo -e "\tPIN [ ${BBLU}38 - ${BGRN}36 - ${BWHT}34 - ${BRED}32 ${NCLR}]"

	echo -e "\n${BMAG}2c) light3 Traffic${NCLR}"
	echo -e "\t${BRED}P${NCLR}${BYEL}I${NCLR}${BGRN}T${NCLR}raffic if pin 01 is North: ${NCLR}"
	echo -e "\tBCM [ ${BWHT}39 - ${BGRN}26 - ${BRED}19 - ${BYEL}13 ${NCLR}] # facing east"
	echo -e "\tPIN [ ${BWHT}39 - ${BGRN}37 - ${BRED}35 - ${BYEL}33 ${NCLR}] # facing east"
}
light1( )	{ ## 2a
	python mamgeorge/python/leds/led_blink.py
}
light2( )	{ ## 2b
	python mamgeorge/python/leds/led_rgb_more.py
}
light3( )	{ ## 2c
	python mamgeorge/python/leds/led_traffic.py
}

pictures( )	{ ## 3, 3a, 3b, 3c, 3d

	echo -e "${BMAG}Camera & Images: May need HDMI or x11 server${NCLR}\n"
	echo -e "\t${BCYN}3a) Expects Camera to be connected${NCLR}"
	echo -e "\t${BCYN}3b) Showing ASCII view (but may take a minute)${NCLR}"
	echo -e "\t${BCYN}3c) FEH expects X11 server to be running${NCLR}"
	echo -e "\t${BCYN}3d) FBI expects X11 server to be running${NCLR}"
}
camera( )	{ ## 3a

	echo -e "${BMAG}Taking Picture!${NCLR}"
	#raspistill -t 100 -vf -o anyPic.jpg -md 6 -q 10
	echo -e "${BMAG}Done!${NCLR}"
}
images1( )	{ ## 3b

	cacaview mamgeorge/images/0_MEG.png
}
images2( )	{ ## 3c

	feh -g 600x400 --scale-down -d mamgeorge/images/0_MEG.png
}
images3( )	{ ## 3d

	fbi mamgeorge/images/0_MEG.png
}

speaker( )	{ ## 4, 4a, 4b, 4c, 4d, 4e

	echo -e "${BBLU}Expects BlueTooth enabled; device MAC addresses added${NCLR}\n"
	echo -e "\t${BCYN}4a) 12:12:28:6C:78:8C	GH_BT3500	( silver speaker )${NCLR}"
	echo -e "\t${BCYN}4b) 68:F7:FA:DF:79:FB	INSIQBS1	( tiny speaker )${NCLR}"
	echo -e "\t${BCYN}4c) 18:45:C9:1D:0B:ED	ProHT_88133	( black speaker )${NCLR}\n"
	echo -e "\t${BCYN}4d) espeak${NCLR}"
	echo -e "\t${BCYN}4e) aplay${NCLR}"
	echo -e "\t${BCYN}4f) espeak & aplay${NCLR}"
}
blue1( )	{ ## 4a
	echo -e 'connect 12:12:28:6C:78:8C\nquit\n' | sudo bluetoothctl
}
blue2( )	{ ## 4b
	echo -e 'connect 68:F7:FA:DF:79:FB\nquit\n' | sudo bluetoothctl
}
blue3( )	{ ## 4c
	echo -e 'connect 18:45:C9:1D:0B:ED\nquit\n' | sudo bluetoothctl
}
voice1( )	{ ## 4d

	echo Expects Speaker to be connected
	espeak "Greetings. It is $DATES" -ven-us+m5 -p50 -k5 -s180 -a100
}
voice2( )	{ ## 4e

	echo Expects Speaker connected; wav files in directory "mamgeorge/sound/"
	aplay -l
	aplay -L
	aplay mamgeorge/sound/ping.wav
}
voice3( )	{ ## 4f
	espeak "Welcome to the George Household" -ven-us+m5 -p50 -k5 -s180 -a100 --stdout | aplay -f cd
}

##################
motors( )	{ ## 5, 5a, 5b, 5c
	echo -e "${BMAG}Servos & Steppers!${NCLR}\n"
	echo -e "${BMAG}5a) Servos ! [# ${BYEL}37,${BWHT}39,${BRED}02${NCLR}${BMAG}]${NCLR}"
	echo -e "${BMAG}5b) Stepper! [# ${BBLU}11,${BMAG}13,${BYEL}15,${BORA}19 ${BMAG}| ${BWHT}06,${BRED}04${NCLR}${BMAG}]${NCLR}"
	echo -e "${BMAG}5c) Steppers [# ${BBLU}11,${BMAG}13,${BYEL}15,${BORA}19 ${BMAG}| ${BWHT}06,${BRED}04${NCLR}${BMAG}]${NCLR}\n"

}
servos( )	{ ## 5a

	echo -e "${BMAG}SERVOS${NCLR}\n"
	echo -e "\t${BYEL}YLW${NCLR} pin_37: BCM26"
	echo -e "\t${BCKW}BLK${NCLR} pin_39: ground-"
	echo -e "\t${BCKR}RED${NCLR} pin_02: 5V+"
	python mamgeorge/python/servos/servo_one.py
}
stepper( )	{ ## 5b

	echo -e "${BMAG}STEPPER${NCLR}\n"
	echo -e "\t${BBLU}BLU${NCLR} pin_11: BCM_17"
	echo -e "\t${BMAG}PUR${NCLR} pin_13: BCM_27"
	echo -e "\t${BYEL}YEL${NCLR} pin_15: BCM_22"
	echo -e "\t${BORA}ORA${NCLR} pin_19: BCM_10"
	echo -e "\t${BCKW}BLK${NCLR} pin_06: ground-"
	echo -e "\t${BCKR}RED${NCLR} pin_04: 5V+"
	python mamgeorge/python/servos/stepper_one.py
}
steppers( )	{ ## 5c

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

gpios( )		{ ## 6, 6a-g, 6s, 6m

	echo -e "${BMAG}gpio sensors${NCLR}"
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
}
gpio_HCSR04( )	{ ## 6a
	python mamgeorge/python/comm/gpio_HCSR04.py
}
i2c_sample( )	{ ## 6i

	ls /dev/i2c* /dev/spi*
	i2cdetect -y 1
	python mamgeorge/python/comm/i2c_sample.py
}
i2c_BMP180( )	{ ## 6b
	python mamgeorge/python/comm/i2c_BMP180.py
}
i2c_HMC5883L( )	{ ## 6c
	python mamgeorge/python/comm/i2c_HMC5883L.py
}
i2c_MCP4725( )	{ ## 6d
	python mamgeorge/python/comm/i2c_MCP4725.py
}
i2c_SSD1306( )	{ ## 6e
	python mamgeorge/python/comm/i2c_SSD1306.py
}
i2c_MCP23017( )	{ ## 6f
	python mamgeorge/python/comm/i2c_MCP23017.py
}
i2c_PCA9685( )	{ ## 6g
	python mamgeorge/python/comm/i2c_PCA9685.py
}
spi_sample( )	{ ## 6s

	ls /dev/i2c* /dev/spi*
	python mamgeorge/python/comm/spi_sample.py
}
spi_MCP3008( )	{ ## 6m
	python mamgeorge/python/comm/spi_MCP3008.py
}

robot( )		{ ## 8, 8a, 8b, 8c
	echo -e "${BMAG}robot${NCLR}"
	echo -e ""
	echo -e "${BMAG}8a) robot_ctl${NCLR} expects a lot!"
	echo -e ""
	echo -e "${BMAG}8b) robot_hat${NCLR} B9 expects SenseHat"
	echo -e "${BMAG}8c) robot_hat${NCLR} MG expects SenseHat"
}
robot_ctl( )	{ ## 8a

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
robot_hatB9( )	{ ## 8b

	python mamgeorge/python/hats/sens_b9.py 9
}
robot_hatMG( )	{ ## 8c

	python mamgeorge/python/hats/sens_b9.py 0
}

pins( )			{ ## 9, 9a, 9b
	echo -e "${BORA}GPIO${NCLR}"
	echo -e ""
	echo -e "${BORA}9a) GPIO diagram, detailed${NCLR}"
	echo -e "${BORA}9b) GPIO diagram, built-in${NCLR}"
}
pinsMG( )		{ ## 9a

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
pinsOT( )		{ ## 9b

pinout
}

##################
exits( )	{ ## 0

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
	echo -e "0 EXIT		exits menu"
	echo -e "1 node		http://$(hostname -I):3000"
	echo -e "2 lights	shows LED, ${BRED}R${BGRN}G${BBLU}B${NCLR}, Traffic"
	echo -e "3 camera	takes a picture & displays it"
	echo -e "4 speaker	loads GH_BT3500, INSIQBS1, ProHT_88133"
	echo -e "5 motors	runs servos, stepper"
	echo -e "6 gpio		runs gpio, i2c, or spi based programs"
	echo -e "─────────────────────────────────────────"
	echo -e "8 robot		runs robot node interface"
	echo -e "9 pins		shows diagram of J8 pinout board"
	echo -e "r REBOOT	reboots PI, x shutsDown PI"
	echo -e "${ENDS}"

	read option

	case $option in

		## if [[ ( $option == "1" ) ]]; then nodejs; fi
		0) exits 	;;
		1) nodejs	;; 1a) nodeMAT;; 1b) nodeGPIO;;
		2) lights	;; 2a) light1 ;; 2b) light2  ;; 2c) light3 ;;
		3) pictures	;; 3a) camera ;; 3b) images1 ;; 3c) images2 ;; 3d) images3 ;;
		4) speaker	;; 4a) blue1  ;; 4b) blue2   ;; 4c) blue3 ;;
			4d) voice1 ;;
			4e) voice2 ;;
			4f) voice3 ;;
		5) motors	;; 5a) servos ;; 5b) stepper ;; 5c) steppers ;;
		6) gpios	;;
			6a) gpio_HCSR04	;;
			6i) i2c_sample	;;
				6b) i2c_BMP180	 ;;
				6c) i2c_HMC5883L ;;
				6d) i2c_MCP4725	 ;;
				6e) i2c_SSD1306	 ;;
				6f) i2c_MCP23017 ;;
				6g) i2c_PCA9685	 ;;
				6m) spi_MCP3008	 ;;
			6s) spi_sample ;;
		7) ;;
		8) robot		;;
			8a) robot_ctl	;;
			8b) robot_hatB9 ;;	b9) robot_hatB9 ;;
			8c) robot_hatMG ;;	mg) robot_hatMG ;;
		9) pins			;;
			9a) pinsMG	;;
			9b) pinsOT	;;
		r) reboots		;; x) shutdown ;;
		## *) ;;
	esac
done
####
