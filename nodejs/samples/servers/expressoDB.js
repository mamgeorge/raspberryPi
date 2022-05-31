// http://www.sqlitetutorial.net/sqlite-nodejs

var express = require( 'express' ) ;
var expressApp = express( ) ;
var sqlite3 = require( 'sqlite3' ).verbose( ) ;
var port = 3000 ;
//
var txtHtml = 'Hello World! ' + new Date( ) ;
var urlDB = { inline: ':memory:' , filedisk: 'C:/dbase/sqlite/chinook.db' } ; // './db/chinook.db'
var sqlDB = 'SELECT * FROM customers WHERE company IS NOT null' ;
//
const dataVals = '' ;
let dBase = new sqlite3.Database( urlDB.filedisk , sqlite3.OPEN_READWRITE ,
	( err ) => { if ( err ) { return console.error( err.message ) ; }
	console.log( 'Connected SQlite3 DB' ) ;
 } ) ;

dBase.serialize( ( ) => {
	dBase.each( sqlDB , ( err , row ) => {
		if ( err ) { console.error( err.message ) ; }
		txtHtml = "<br />\t" + row.FirstName + " " + row.LastName + "\t" ;
		console.log( txtHtml ) ;
	 } ) ;
 } ) ;

dBase.close( ( err ) => {
 if ( err ) { return console.error( err.message ) ; }
 console.log( 'Closed SQlite3 DB' ) ;
 } ) ;

expressApp.get( '/' , function ( request , response ) {
	txtHtml = 'Hello World! ' + new Date( ) + '<br /><br />' + dataVals ;
	response.send( txtHtml ) ;
	console.log( txtHtml ) ;
 } ) ;
//
console.log( txtHtml ) ;
expressApp.listen( port ) ;
