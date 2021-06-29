// https://github.com/websockets/ws
// cd ..\servers\nodejs
// node --experimental-modules wsScript.mjs

import WsClient from './wsClient.mjs' ;
import basics from './resources/basics.js' ;

const cycleSec = 2000;
const cycleMax = 4;
const RED1 = basics.COLORS.RED1;
const NON0 = basics.COLORS.NON0; 
let tctr = 0;

( ( ) => {
	//
	console.log( RED1 + 'wsScript' + NON0 );
	const wsClient = new WsClient( );
	const interval = setInterval( ( )=> {	
		//
		// console.log( RED1 + JSON.stringify( interval ) + NON0 );
		wsClient.caller( );
		if ( ++tctr >= cycleMax ) { clearInterval( interval ); }
	} , cycleSec );
} ) ( );
