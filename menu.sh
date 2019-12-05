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
NCLR="\033[0m"

nodejs( ) {

	echo Expects Node to be installed
	node -v
	# npm -v
	node nodejs/samples/expressoMAT.js
}

camera( ) {

	echo Expects Camera to be connected
	raspistill -t 100 -vf -oimg.jpg	-md 6 -q 10
	feh -g 600x400 -d img.jpg
}

blueTooth( ) {

	echo Expects BlueTooth to be enabled
	## echo -e 'connect GH_BT3500 \n quit' | sudo bluetoothctl // 12:12:28:6C:78:8C
	## echo -e 'connect 18:45:C9:1D:0B:ED \n quit' | sudo bluetoothctl 18:45:C9:1D:0B:ED // ProHT 88133
	echo -e 'connect 12:12:28:6C:78:8C\nquit\n' | sudo bluetoothctl
}

voice( ) {

	echo Expects Speaker to be connected; wav files in Music directory
	aplay -D bluealsa Music/ping.wav
	espeak "Greetings. It is $DATE" -ven-us+m5 -p50 -k5 -s180 -a100 --stdout | aplay -f cd -D bluealsa
}


light_ONE( ) {

	echo -e "${BMAG}5) light_ONE 5a) light_RGB 5b) light_MNY${NCLR}"
	echo -e "Expects LEDs on BLK on BCM 21 (pin 40)"
	echo -e "${BRED}RED long anode on 3V pwr (pin 1)${NCLR}"
	python python/gpio/gpio_ledOne.py
}

light_RGB( ) {

	echo -e "${BMAG}5) light_ONE 5a) light_RGB 5b) light_MNY${NCLR}"
	echo -e "${BRED}R${BGRN}G${BBLU}B${NCLR} LED 10mm facing east"
	echo -e "[ ${BBLU}20 - ${BGRN}16 - ${BWHT}34 - ${BRED}32 ${NCLR}]"
	python python/gpio/pi_lamps.py
}

light_MNY( ) {

	echo -e "${BMAG}5) light_ONE 5a) light_RGB 5b) light_MNY${NCLR}"
	echo -e "${BMAG}PiTraffic if pin 01 is North: ${NCLR}"
	echo -e "[ ${BWHT}09 - ${BGRN}17 - ${BRED}27 - ${BBLU}22 ${NCLR}] # facing west"
	echo -e "[ ${BWHT}39 - ${BGRN}26 - ${BRED}19 - ${BBLU}13 ${NCLR}] # facing east"
	python python/gpio/pi_traffic.py
}

grippers( ) {

	echo Expects Speaker to be connected
	for (( cctr=0; cctr<1; cctr++ ))
	do
	python python/servos/servo_both.py
	done
}

gears( ) {

	echo 'Expects Servos on control: 17:blu, 27:pur, 22:yel, 10:ora [# 11,13,15,19] ; #2:red, #6blk'
	python python/servos/stepper_any.py
}

robot( ) {

	echo Expects L293D on m1LFT_wht+ 26, m1LFT_grn- 19, m2RGT_blu+ 20, m2RGT_ylw- 16

	echo "8 forw | 2 back | 6 right | 4 left | + fast | - slow | 5 stop"
	echo "l lights | c cam | s speak | a action | x sensor"
	python python/mat/robot.py
}

breaker( ) {

	# espeak "Goodbye"
	echo -e "$BGRN Goodbye!"
	echo -e "------------------------------------------------------------ $NCLR"
}

shutdown( ) {

	# espeak "Shutting Down"
	echo -e "$BGRN Goodbye!"
	echo -e "------------------------------------------------------------ $NCLR"
	sudo shutdown -h now
}

## init
DATED=$(date +"%Y %B %-d, a %A at %-I:%M:%S %p.")

while [ "$option" != "0" ]
do

	echo -e "$BGRN\n------------------------------------------------------------"
	echo -e "Greetings. It is $DATED \n $NCLR"

	echo -e "0 EXIT | 1 node | 2 cam | 3 blue | 4 vox | 5 ${BRED}L${BGRN}E${BBLU}D${NCLR} | 6 grip | 7 gears | x SHUT"
	read option

	## if [[ ( $option == "1" ) ]]; then nodejs; fi
	case $option in

		0) breaker 	;;
		1) nodejs	;;
		2) camera	;;
		3) blueTooth ;;
		4) voice	;;
		5) light_ONE;; 5a) light_RGB ;; 5b) light_MNY ;;
		6) grippers	;;
		7) gears	;;
		x) shutdown	;;
		*) ;;
	esac
done
