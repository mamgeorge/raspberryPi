// https://www.tutorialspoint.com/nodejs/nodejs_express_framework.htm

import basics from '../../common/resources/basics.js' ;
import express from 'express' ;
const expressApp = express( ) ;
const PORT = 3000;
const __dirname = process.cwd( );
	
expressApp.use( express.static( 'common' ) ) ;
expressApp.use( express.static( 'common/resources' ) ) ;
expressApp.use( express.static( 'public' ) ) ;
expressApp.use( express.static( 'images' ) ) ;
expressApp.use( express.static( 'resources' ) ) ;
expressApp.use( express.static( 'special' ) ) ;

//
const varServer = expressApp.listen( PORT , ( )=> {
	//
	const date = new Date().toISOString();
	const host = varServer.address( ).address ;
	const port = varServer.address( ).port ;
	const txt = `${ basics.COLORS.GRN1 }${ date }` 
	+ `${ basics.COLORS.WHT1 } | `
	+ `${ basics.COLORS.BLU1 }http://%s:%s${ basics.COLORS.NON0 }`;
	//
	console.log( txt , host , port ) ;
	console.log( '__dirname: ' + __dirname ) ;
} ) ;

expressApp.get( '/' , ( request , response ) => {
	response.send( 'Hi!' ); 
} ) ;

expressApp.get( '/home' , ( request , response ) => {
	console.log( request.headers );
	const fileName = __dirname + '/common/index.html';
	console.log( fileName ) ;
	response.sendFile( path.resolve( fileName ) );
} ) ;

expressApp.get( '/hello' , ( request , response ) => {
	response.send( 'Hello World!' ); 
} ) ;

expressApp.get( '/java' , ( request , response ) => {
	basics.spawnJava(  'C:\\servers\\nodejs\\' , 'resources.AnyClass' , response ); 
} ) ;

expressApp.get( '/python' , ( request , response ) => { 
	basics.spawnPython(  './resources/sample.py' , '' , response ); 
} ) ;
