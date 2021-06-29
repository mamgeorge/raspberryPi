// https://github.com/websockets/ws
// cd ..\servers\nodejs , NODE_OPTIONS=--experimental-modules
// node wsServer.mjs

import webSocket from 'ws' ;
import basics from './resources/basics.js' ;
import WsClient from './wsClient' ;

const PORT = 3000; 
const MAG1 = basics.COLORS.MAG1;
const NON0 = basics.COLORS.NON0; 
const wss = new webSocket.Server( { port: PORT } );
let color = '';

wss.on( 'connection' , ( ws , req ) => {
	//
	const ip = req.connection.remoteAddress;
	const title = req.url.substring( req.url.indexOf( '=' ) + 1 );
	color = new WsClient( ).getColor( title );
	ws.on( 'message' , ( msg ) => {
		//
		const msgServer = JSON.parse( msg ).server;
		console.log( MAG1 + 'SERVER READING: ' + NON0 
			+ color + 'JSON[' + ip + ']: ' + msgServer + NON0 );
		//
		const rsp = MAG1 + 'SERVER SENDING: ' + new Date( ).toISOString( ) + NON0;
		console.log( '\t' + rsp );
		ws.send( rsp );
		ws.close( );
	});
} );
//
console.log( MAG1 + `SERVER: ${PORT}` + NON0 );
