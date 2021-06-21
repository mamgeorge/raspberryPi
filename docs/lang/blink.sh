
# $ ./lang/blink.sh 5
NCLR="\033[0m"
BCKR="\u001b[41;1m"
BCKM="\u001b[45;1m"
BCKW="\u001b[47;1m\u001b[30m"

echo -e "${BCKM}Raspberry Pi Blink!${NCLR}"
echo -e "\t${BCKW}BLK${NCLR} pin_39: ground short cathode"
echo -e "\t${BCKR}RED${NCLR} pin_40: BCM_21 long anode"

PIN=29
delay=0.5
cycle=$1

gpio mode $PIN out
gpio write $PIN 0

# while true; do
if [ $cycle -lt 3 ]; then
	cycle=3
fi
	
for ictr in `seq 1 $cycle`; do

	gpio write $PIN 1
	sleep $delay
	gpio write $PIN 0
	sleep $delay

done
