// \servers\nodejs\sample.mjs
// --experimental-modules 

import basics from './resources/basics.js' ;

// "\u001b[30m"; http://www.asciitable.com/
let txtLine = '';
let str = '▀▀▀▀▀▀▀▀▀▀';
for( let ictr = 30; ictr < 48; ictr++ )
{
	txtLine += "\u001b[" + ictr + ";1m" + str + basics.NON0; 
}
console.log( txtLine );

console.log( basics.RED1 + "HELLO" + basics.NON0 );
