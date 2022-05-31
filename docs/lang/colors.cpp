#include <iostream>
#include <string>
#include <fcntl.h>
using namespace std;
/*
	$ g++ -o lang/colors lang/colors.cpp
	$ ./lang/colors
*/

int main(int argc, char **argv)
{
	wprintf( L"\t\u001b[47;1m\u001b[30m WHT \033[0m \n" );
	wprintf( L"\t\u001b[41;1m RED \033[0m \n" );
	wprintf( L"\t\u001b[43;1m YEL \033[0m \n" );
	wprintf( L"\t\u001b[42;1m GRN \033[0m \n" );
	wprintf( L"\t\u001b[46;1m CYN \033[0m \n" );
	wprintf( L"\t\u001b[44;1m BLU \033[0m \n" );
	wprintf( L"\t\u001b[45;1m MAG \033[0m \n" );
	wprintf( L"\t\u001b[48;1m BLK \033[0m \n" );

	char charVal = '!';
	cout << "ASCII Value of ( " << charVal << " ) is: " << int(charVal) << endl;

	//
	return 0;
}