#include <iostream>
#include <string> 
// #include <fcntl.h> 
// #include <io.h> 
using namespace std;
/*
	\home\pi\lang\strings.cpp
	$ g++ -o lang/strings lang/strings.cpp
	$ ./lang/strings
*/
int main(int argc, char **argv)
{
	// _setmode( _fileno(stdout), _0_U16TEXT);
	// wprintf(L"Greetings! \x263a \x263b \n" );
	printf( "Hello World!\n" );
	char charVal = '!';
	cout << "ASCII Value of ( " << charVal << " ) is: " << int(charVal) << endl;

	//
	string txtNum = "";
	charVal = ' ';
	for( int ictr = 0 ; ictr < 256 ; ictr++ ) {
		//
		txtNum = std::to_string( ictr );
		if( ictr < 100 ) txtNum = "0" + txtNum ;
		if( ictr < 10  ) txtNum = "0" + txtNum ;
		charVal = (char)ictr;
		if( charVal == '\0' ) charVal = ' ';
		cout << "" << txtNum << ":" << (char)ictr << " | " ;
		if( ictr % 10 == 0 ) cout << endl;
	}
	cout << endl;

	//
	return 0;
}
