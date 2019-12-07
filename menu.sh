#!/bin/bash
# menu.sh

BRED="\033[31;1m"
BGRN="\033[32;1m"
BYEL="\033[33;1m"
BBLU="\033[34;1m"
BMAG="\033[35;1m"
BCYN="\033[36;1m"
BWHT="\033[37;1m"
NCLR="\033[0m"

exitor( )	{ ## 0

	echo -e "$BGRN Goodbye!"
	echo -e "------------------------------------------------------------ $NCLR"
}
nodejs( )	{ ## 1

	echo Expects Node to be installed
	node -v
	node nodejs/samples/expressoMAT.js
}
camera( )	{ ## 2

	echo Expects Camera to be connected
	raspistill -t 100 -vf -oimg.jpg	-md 6 -q 10
	feh -g 600x400 -d img.jpg
}
lights( )	{ ## 3

	echo -e "${BMAG}3a) light1${NCLR}"
	echo -e "\tExpects LEDs on BLK on BCM 21 (pin 40)"
	echo -e "\t${BRED}RED long anode on 3V pwr (pin 1)${NCLR}"

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
	echo -e "Expects LEDs on BLK on BCM 21 (pin 40)"
	echo -e "${BRED}RED long anode on 3V pwr (pin 1)${NCLR}"
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

	echo -e "Expects BlueTooth to be enabled; devices must already have references"
	echo -e "${BCYN}"
	echo -e "\t4a) 12:12:28:6C:78:8C	GH_BT3500	( silver speaker )"
	echo -e "\t4b) 68:F7:FA:DF:79:FB	INSIQBS1	( tiny speaker )"
	echo -e "\t4c) 18:45:C9:1D:0B:ED	ProHT_88133	( black speaker ) ${NCLR}"
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

	echo -e "Expects Servos on control: ${BYEL}YLW${NCLR} BCM26(p37), ${BRED}RED${NCLR} (p02): 5V+ , ${BWHT}BLK${NCLR} ground(p39): ground-"
	python python/servos/servo_once.py
}
stepper( )	{ ## 7

	echo 'Expects Servos on control: 17:blu, 27:pur, 22:yel, 10:ora [# 11,13,15,19] ; #2:red, #6blk'
	python python/servos/stepper_any.py
}
robot( )	{ ## 8

	echo Expects L293D on m1LFT_wht+ 26, m1LFT_grn- 19, m2RGT_blu+ 20, m2RGT_ylw- 16
	echo "8 forw | 2 back | 6 right | 4 left | + fast | - slow | 5 stop"
	echo "l lights | c cam | s speak | a action | x sensor"
	python python/mat/robot.py
}

shutdown( )	{ ## x

	echo -e "$BGRN Goodbye!"
	echo -e "------------------------------------------------------------ $NCLR"
	sudo shutdown -h now
}

## init
tabs 4
DATED=$(date +"%Y %B %-d, a %A at %-I:%M:%S %p.")

while [ "$option" != "0" ]
do

	echo -e "$BGRN\n------------------------------------------------------------"
	echo -e "Greetings. It is $DATED \n $NCLR"

	# echo -e "0 EXIT | 1 node | 2 cam | 3 ${BRED}L${BGRN}E${BBLU}D${NCLR} | 4 blue | 5 vox | 6 grip | 7 gears | x SHUT"
	echo -e "0 EXIT"
	echo -e "1 node		http://192.168.1.22:3000"
	echo -e "2 cam		takes a picture & displays it"
	echo -e "3 ${BRED}L${BGRN}E${BBLU}D${NCLR}		shows LED, RGB, Traffic"
	echo -e "4 blue		loads GH_BT3500 INSIQBS1 ProHT_88133"
	echo -e "5 vox		plays & speaks"
	echo -e "6 servos	runs servos for grippers"
	echo -e "7 stepper	runs stepper for armature"
	echo -e "8 robot		runs robot node interface"
	echo -e "x SHUT		exits PI"
	echo -e "$BGRN------------------------------------------------------------${NCLR}"

	read option

	case $option in

		## if [[ ( $option == "1" ) ]]; then nodejs; fi

		0) exitor 	;;
		1) nodejs	;;
		2) camera	;;
		3) lights	;; 3a) light1 ;; 3b) light2 ;; 3c) light3 ;;
		4) blue		;; 4a) blue1 ;; 4b) blue2 ;; 4c) blue3 ;;
		5) voice	;;
		6) servos	;;
		6) stepper	;;
		7) gears	;;
		x) shutdown	;;
		*) ;;
	esac
done
####
