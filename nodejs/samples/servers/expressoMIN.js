//
var express = require( 'express' );
var expressApp = express( );
var port = 3000;
var txtHtml = '';
//
expressApp.get( '/' , function ( request , response ) {
	txtHtml = 'Greetings! ' + new Date( ).toISOString( );
	response.send( txtHtml );
	console.log( txtHtml ) ;
})
//
console.log( `port: ${ port }` ) ;
expressApp.listen( port );
