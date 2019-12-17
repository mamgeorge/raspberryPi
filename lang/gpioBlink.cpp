#include <stdio.h>
#include <wiringPi.h>
#include <string> 
#include <iostream> 
/*
	$ g++ -Wall -o lang/gpioBlink lang/gpioBlink.cpp -lwiringPi
	$ ./lang/gpioBlink 1
	wiringPi pin 0 = BCM_GPIO 17
	http://www.cplusplus.com/reference/cwchar/wprintf/
*/
#define	LED	29

int main ( int argc, char* argv[] ) {
	//
	wprintf( L"\033[35;1mRaspberry Pi Blink!\033[0m\n" ) ;
	wprintf( L"\t\u001b[47;1m\u001b[30mWHT\033[0m pin_39: ground short cathode\n" );
	wprintf( L"\t\u001b[41;1mRED\033[0m pin_40: BCM_21 long anode\n" );
	//
	wiringPiSetup () ;
	pinMode (LED, OUTPUT) ;
	//
	int delayed = 500; // mS
	int cycle = atoi(argv[1]);
	if ( cycle < 3 ) cycle = 3; 
	//
	for( int ictr = 0 ; ictr < cycle ; ictr++ ) {
	//
		digitalWrite ( LED , HIGH ) ; // On
		delay ( delayed ) ;			
		digitalWrite ( LED , LOW ) ; // Off
		delay ( delayed ) ;
	}
	return 0 ;
}
