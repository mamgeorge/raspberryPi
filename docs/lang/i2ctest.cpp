// \home\pi\lang\i2ctest.cpp
// https://learn.sparkfun.com/tutorials/raspberry-pi-spi-and-i2c-tutorial/all#i2c-on-pi
// MCP4725
// $ g++ i2ctest.cpp -lwiringPi

#include <iostream>
#include <errno.h>
#include <wiringPiI2C.h>

using namespace std;

int main()
{
   int fileDescrip, result;

   // Initialize the interface by giving it an external device ID.
   // MCP4725 defaults to address 0x60 and returns a standard file descriptor.
   fileDescrip = wiringPiI2CSetup(0x60);

   cout << "Init result: "<< fileDescrip << endl;

   for(int ictr = 0; ictr < 0x0000ffff; ictr++)
   {
      // register address is the concatenation of 
	  // command (010x = write DAC output) &
      // power down (x00x = power up) bits
      result = wiringPiI2CWriteReg16( fileDescrip , 0x40, ( ictr & 0xfff) );

      if(result == -1)
      {
         cout << "Error.  Errno is: " << errno << endl;
      }
   }
}
