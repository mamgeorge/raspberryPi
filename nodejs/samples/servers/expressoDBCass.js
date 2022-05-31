// http://www.sqlitetutorial.net/sqlite-nodejs

var express = require( 'express' ) ;
var expressApp = express( ) ;
var cassandra = require( 'cassandra-driver' ) ;
var async = require( 'async' ) ;
var port = 3000 ;
//
var txtHtml = 'Hello World! ' + new Date( ) ;
var sqlDB = 'SELECT * FROM anytable' ;
let dataVals = null;
//
var client = new cassandra.Client( { contactPoints: [ '127.0.0.1' ] , keyspace: 'anykeyspace' } ) ;
client.execute( sqlDB , function ( err , result )
{
	if ( err ) { console.error( err.message ) ;	} else
	{
		console.log( 'Opened Cassandra DB' ) ;
		if ( result.rows.length > 0 ) {
			dataVals = result.rows;
			// result.rows.map( (row) => console.log( row.firstname + " " + row.lastname + " / " + row.nationality + " / " + row.lat_long ) );
		}
		else { console.log( "No results" ) ; }
	}
	// process.exit();
	console.log( 'Closed Cassandra DB' ) ;
} ) ;

expressApp.get( '/' , function ( request , response ) {
	txtHtml = '<center>Hello World!<br />' + new Date( ).toISOString( ) + '<br />'
		+ '<table border = "1" cellspacing = "0" cellpadding = "4" >'
		+ dataVals.map( (row) => '<tr>'
			+ '<td>' + row.firstname + ' ' + row.lastname + '</td>'
			+ '<td>' + row.nationality + '</td>'
			+ '<td>' + row.lat_long + '</td>'
			+ '</tr>'
		) ;
		txtHtml += '</table></center>';
	response.send( txtHtml ) ;
	console.log( txtHtml ) ;
 } ) ;
//
console.log( txtHtml ) ;
expressApp.listen( port ) ;
