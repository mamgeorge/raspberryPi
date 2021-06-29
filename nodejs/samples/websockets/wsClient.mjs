// https://github.com/websockets/ws
// cd ..\servers\nodejs
// node --experimental-modules wsClient.mjs

import webSocket from 'ws' ;
import basics from './resources/basics.js' ;
const URL = 'ws://localhost:3000/?parm=';
const NON0 = basics.COLORS.NON0;

const payload = {
	'USER'		: 'mamgeorge',
	'PASS'		: 'password',
	'server'	: '192.168.1.1' ,
	'startDate'	: '2019-06-20',
	'client'	: 'PC_DEV_1000'
}
let color = '', title = '';

class WsClient {
	//
	getColor( title ) {
		//
		let color = '';
		for( let cctr = 0 ; cctr < basics.GREEKS.length ; cctr++ ) {
			// '\u001b[31;1m'
			if( basics.GREEKS[ cctr ] === title ) 
			{ color = '\u001b[3' + basics.COLORS_SRV[ cctr ] + ';1m'; }
		}
		return color;
	}
	//
	caller( ) {
		//
		title = process.title.slice( 0 , process.title.indexOf( ' ' ) );
		color = this.getColor( title ); 
		console.log( color + `CLIENT CALLING: ${ URL + title }` + NON0 );
		const ws = new webSocket( URL + title );
		//
		ws.on( 'open', ( ) => { ws.send( JSON.stringify( payload ) ); } );

		ws.on( 'message', ( data ) => { console.log( '\tRECIEVED: ' + data ); } );
	}
}
	
export { WsClient as default };
