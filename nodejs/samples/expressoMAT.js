// https://www.tutorialspoint.com/nodejs/nodejs_express_framework.htm
const basics = require( '../common/libraries/basics.js' ) ;
const express = require( 'express' ) ;
const colors = require('colors/safe');
const path = require('path');

const dirPath = path.join( process.cwd(), '/nodejs');
const expressApp = express( ) ;
const PORT = 3000;
let date = new Date().toISOString();
	
expressApp.use( express.static( 'common' ) ) ;
expressApp.use( express.static( 'samples' ) ) ;
expressApp.use( '/images'	 , express.static( path.join( dirPath, 'common/images') ) ) ;
expressApp.use( '/resources' , express.static( path.join( dirPath, 'common/resources') ) ) ;

//
const varServer = expressApp.listen( PORT , ( )=> {
	//
	const host = varServer.address( ).address ;
	const port = varServer.address( ).port ;
	const txt = colors.brightGreen( date ) + ' | ' + colors.brightBlue( 'http://%s:%s' );
	console.log( txt , host , port ) ;
} ) ;

// https://flaviocopes.com/node-terminate-program/
process.on( 'SIGTERM', ( ) => { 
	varServer.close( ( ) => { 
		console.log('Process terminated') 
	} )
} );

expressApp.get( '/' , ( request , response ) => {
	const msg = new Date().toISOString();
	console.log( dirPath );
	console.log( process.cwd() );
	console.log( request.headers );
	console.log( msg ) ; 
	response.send( msg );
} ) ;

expressApp.get( '/home' , ( request , response ) => {
	let pathFile = dirPath + '/common/index.html';
	response.sendFile( pathFile );
} ) ;

expressApp.get( '/java' , ( request , response ) => {
	basics.spawnJava(  '\\common\\resources\\' , 'AnyClass' , response ); 
} ) ;

expressApp.get( '/python' , ( request , response ) => { 
	basics.spawnPython(  './common/resources/sample.py' , '' , response ); 
} ) ;

expressApp.get( '/exit' , ( request , response ) => { 
	//
	// process.exit(0); 
	process.kill( process.pid , 'SIGTERM' );
} ) ;
