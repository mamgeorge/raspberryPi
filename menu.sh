#!/bin/bash
# \home\pi\menu.sh
# http://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html
# https://misc.flogisoft.com/bash/tip_colors_and_formatting
# https://theasciicode.com.ar/

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
BCKG="\u001b[42;1m"
BCKY="\u001b[43;1m"
BCKB="\u001b[44;1m"
BCKM="\u001b[45;1m"
BCKC="\u001b[46;1m"
BCKW="\u001b[47;1m\u001b[30m"

BOLD="\u001b[1m"
UNDR="\u001b[4m"
REVR="\u001b[7m"
ENDS="${BGRN}──────────────────────────────────────────────────────────── ${NCLR}"

##################

nodejs( )	{ ## 1

	echo Expects Node to be installed
	node -v
	node nodejs/samples/expressoMAT.js
}
camera( )	{ ## 2

	echo Expects Camera to be connected
	raspistill -t 100 -vf -o anyPic.jpg -md 6 -q 10
	feh -g 600x400 -d anyPic.jpg
}
lights( )	{ ## 3

	echo -e "${BMAG}3a) light1${NCLR}"
	echo -e "\t${BCKW}BLK${NCLR} pin_40: BCM_21 short cathode"
	echo -e "\t${BCKR}RED${NCLR} pin_01: 3V PWR long anode"

	echo -e "\n${BMAG}3b) light1${NCLR}"
	echo -e "\t${BRED}R${BGRN}G${BBLU}B${NCLR} LED 10mm facing east"
	echo -e "\t[ ${BBLU}20 - ${BGRN}16 - ${BWHT}34 - ${BRED}32 ${NCLR}]"

	echo -e "\n${BMAG}3c) light1${NCLR}"
	echo -e "\t${BMAG}PiTraffic if pin 01 is North: ${NCLR}"
	echo -e "\t[ ${BWHT}09 - ${BGRN}17 - ${BRED}27 - ${BBLU}22 ${NCLR}] # facing west"
	echo -e "\t[ ${BWHT}39 - ${BGRN}26 - ${BRED}19 - ${BBLU}13 ${NCLR}] # facing east"
}
light1( )	{ ## 3a

	echo -e "${BMAG}3a) light_ONE 3b) light_RGB 3c) light_MNY${NCLR}"
	echo -e "\t${BCKW}BLK${NCLR} pin_40: BCM_21 short cathode"
	echo -e "\t${BCKR}RED${NCLR} pin_01: 3V PWR long anode"
	python python/gpio/gpio_ledOne.py
}
light2( )	{ ## 3b

	echo -e "${BMAG}3a) light_ONE 3b) light_RGB 3c) light_MNY${NCLR}"
	echo -e "${BRED}R${BGRN}G${BBLU}B${NCLR} LED 10mm facing east"
	echo -e "[ ${BBLU}20 - ${BGRN}16 - ${BWHT}34 - ${BRED}32 ${NCLR}]"
	python python/gpio/pi_lamps.py
}
light3( )	{ ## 3c

	echo -e "${BMAG}3a) light_ONE 3b) light_RGB 3c) light_MNY${NCLR}"
	echo -e "${BYEL}PiTraffic if pin 01 is North: ${NCLR}"
	echo -e "[ ${BWHT}09 - ${BGRN}17 - ${BRED}27 - ${BBLU}22 ${NCLR}] # facing west"
	echo -e "[ ${BWHT}39 - ${BGRN}26 - ${BRED}19 - ${BBLU}13 ${NCLR}] # facing east"
	python python/gpio/pi_traffic.py
}

blue( )		{ ## 4

	echo -e "${BMAG}Expects BlueTooth enabled; device MAC addresses added${NCLR}\n"
	echo -e "\t${BCYN}4a) 12:12:28:6C:78:8C	GH_BT3500	( silver speaker )${NCLR}"
	echo -e "\t${BCYN}4b) 68:F7:FA:DF:79:FB	INSIQBS1	( tiny speaker )${NCLR}"
	echo -e "\t${BCYN}4c) 18:45:C9:1D:0B:ED	ProHT_88133	( black speaker )${NCLR}"
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
voice( )	{ ## 5

	echo Expects Speaker to be connected; wav files in Music directory
	aplay -D bluealsa Music/ping.wav
	espeak "Greetings. It is $DATE" -ven-us+m5 -p50 -k5 -s180 -a100 --stdout | aplay -f cd -D bluealsa
}

servos( )	{ ## 6

	echo -e "${BMAG}Expects Servos: [# 37,39,02]${NCLR}\n"
	echo -e "\t${BYEL}YLW${NCLR} pin_37: BCM26"
	echo -e "\t${BCKW}BLK${NCLR} pin_39: ground-"
	echo -e "\t${BCKR}RED${NCLR} pin_02: 5V+"
	python python/servos/servo_one.py
}
stepper( )	{ ## 7

	echo -e "${BMAG}Expects Stepper: [# 11,13,15,19]${NCLR}\n"
	echo -e "\t${BBLU}BLU${NCLR} pin_11: BCM_17"
	echo -e "\t${BMAG}PUR${NCLR} pin_13: BCM_27"
	echo -e "\t${BYEL}YEL${NCLR} pin_15: BCM_22"
	echo -e "\t${BORA}ORA${NCLR} pin_19: BCM_10"
	echo -e "\t${BCKW}BLK${NCLR} pin_06: ground-"
	echo -e "\t${BCKR}RED${NCLR} pin_04: 5V+"
	python python/servos/stepper_one.py
}
robot( )	{ ## 8

	echo -e "${BMAG}Expects L293D: [# 35,36,37,38]${NCLR}\n"
	echo -e "\t${BGRN}GRN${NCLR} pin_35: BCM_19 m1LFT-"
	echo -e "\t${BYEL}YEL${NCLR} pin_36: BCM_16 m2RGT-"
	echo -e "\t${BWHT}WHT${NCLR} pin_37: BCM_26 m1LFT+"
	echo -e "\t${BBLU}BLU${NCLR} pin_38: BCM_20 m2RGT+"
	echo -e ""
	echo -e "\t8 forw | 2 back | 6 right | 4 left | + fast | - slow | 5 stop"
	echo -e "\tL lights | C cam | S speak | A action | X sensor"
	python python/mat/robot.py
}
pins( )		{ ## 9

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

exits( )	{ ## 0

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

tabs 4
DATES=$(date +"It is %Y %B %-d, a %A at %-I:%M:%S %p.")
DATEM=$(date +"%Y-%M-%d @ %-I:%M:%S %p.")

while [ "$option" != "0" ]
do

	echo -e "${ENDS}\n${BGRN}Greetings. ${DATES} \n ${NCLR}"

	# echo -e "0 EXIT | 1 node | 2 cam | 3 ${BRED}L${BGRN}E${BBLU}D${NCLR} | 4 blue | 5 vox | 6 grip | 7 gears | x SHUT"
	echo -e "0 EXIT		exits menu"
	echo -e "1 node		http://192.168.1.22:3000"
	echo -e "2 cam		takes a picture & displays it"
	echo -e "3 lights	shows LED, ${BRED}R${BGRN}G${BBLU}B${NCLR}, Traffic"
	echo -e "4 blue		loads GH_BT3500 INSIQBS1 ProHT_88133"
	echo -e "5 vox		plays & speaks"
	echo -e "6 servos	runs servos for grippers"
	echo -e "7 stepper	runs stepper for armature"
	echo -e "8 robot		runs robot node interface"
	echo -e "9 pins		shows diagram of J8 pinout board"
	echo -e "r REBOOT	reboots PI, x shutsDown PI"
	echo -e "${ENDS}"

	read option

	case $option in

		## if [[ ( $option == "1" ) ]]; then nodejs; fi
		0) exits 	;;
		1) nodejs	;;
		2) camera	;;
		3) lights	;; 3a) light1 ;; 3b) light2 ;; 3c) light3 ;;
		4) blue		;; 4a) blue1 ;; 4b) blue2 ;; 4c) blue3 ;;
		5) voice	;;
		6) servos	;;
		7) stepper	;;
		8) robot	;;
		9) pins		;;
		r) reboots	;; x) shutdown	;;
		*) ;;
	esac
done
####
