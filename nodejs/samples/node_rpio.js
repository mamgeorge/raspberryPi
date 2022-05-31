// http://127.0.0.1:3000/?q=1234
// http://192.168.1.22:3000/blink
// https://www.npmjs.com/package/rpio

const http		= require( 'http' ) ;
const express	= require( 'express' ) ;
const rpio		= require( 'rpio' );
const colors	= require( 'colors/safe' );
const expressApp = express( ) ;
const PORT		= 3000;
const path		= require( 'path' );
const dirPath	= path.join( process.cwd( ), '/nodejs' );
let date = new Date( ).toISOString( );

const varServer = expressApp.listen( PORT , ( )=> {
	console.log( colors.green( date ) , PORT ) ;
} ) ;

process.on( 'SIGTERM', ( ) => { varServer.close( ( ) => { console.log('Process terminated') } ) } );
expressApp.get( '/exit' , ( request , response ) => { process.kill( process.pid , 'SIGTERM' ); } ) ;
expressApp.use( '/images'	 , express.static( path.join( dirPath, 'common/images') ) ) ;

expressApp.get( '/' , ( request , response ) => {
	//
	const msg =  new Date().toISOString( );
	console.log( colors.cyan( msg ) ) ; 
	//
	let pathFile = dirPath + '/common/index.html';
	response.sendFile( pathFile );
} ) ;

expressApp.get( '/blink' , ( request , response ) => {
	//
	let pin = 15;
	rpio.open( pin , rpio.INPUT);
	console.log( 'Pin [' + pin + '] = ' + ( rpio.read( pin ) ? 'high' : 'low') );
	blinker( 100 );
	//
	const msg =  new Date().toISOString( );
	console.log( colors.yellow( new Date().toISOString( ) ) ) ; 
} ) ;

function blinker( timer ) {
	//
	let pin = 40; // 21 = 40
	rpio.open( pin , rpio.OUTPUT, rpio.LOW);
	for ( let ictr = 0; ictr < 5; ictr++ ) {
        //
        rpio.write( pin , rpio.HIGH );
        rpio.msleep( timer );
		//
        rpio.write( pin , rpio.LOW );
        rpio.msleep( timer );
	}
}

//
console.log( colors.brightGreen( 'Server running' ) );
