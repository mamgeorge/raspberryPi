// cd /servers/nodejs , node nodeser.js , http://localhost:1337
// VARS MUST BE DEFINED BEFORE EXPORTS TO WORK IN STATIC AND NODE FILES

//*******************
// npm install ibm_db
var DB_URLs = [
	'DRIVER={DB2 for i5OS};DATABASE=slpapappdb;UID=MGEORGE;PWD=mmsg1607;HOSTNAME=jdbc:as400//cgil5;port=446;PROTOCOL=TCPIP' ,
	'DATABASE=slpapappdb;HOSTNAME=jdbc:as400//cgil5;PORT=446;PROTOCOL=jdbc;UID=MGEORGE;PWD=mmsg1607' ] ;
var SQLs = [ 'SELECT last_update FROM slpapappdb.xmlstore WHERE work_item_id = "2000304"' , 'SELECT 1 FROM sysibm.sysdummy1' ];
var ibmdb = require( 'ibm_db' ) ;

//
ibmdb.open( DB_URLs[ 0 ] , function ( err , connection )
{
	if ( err ) { return console.log( err ) ; }
	connection.query( SQLs[ 0 ] , function ( err , data )
	{
		if ( err ) { console.log( err ) ; } else
		console.log( data ) ;
		connection.close( function ( ) { console.log( 'DONE' ) ;  } ) ;
	} ) ;
} ) ;

//********************
// npm install sqlite3
var sqlite = require( 'sqlite3' ).verbose( ) ;
var dBaseURL =  'F:/dBase/sqlite/TEST.db' ;
var dBase = new sqlite.Database( dBaseURL ) ;
var SQLs = [ 'SELECT * FROM anyTable' , 'SELECT name FROM anyTable' ] ;

dBase.serialize( function( )
{
	dBase.each( SQLs[ 1 ] , function( err , row )
	{ console.log( row ) ; } ) ;
} ) ;
dBase.close( ) ;

//******************
// npm install mysql
var mysql	= require( 'mysql' ) ;
var connection = mysql.createConnection( {
	host	: 'localhost' ,
	user	: '< MySQL username >' ,
	password : '< MySQL password >' ,
	database : '<your database name>'
 } ) ;

connection.connect( ) ;
connection.query( 'SELECT * from < table name >' , function( err , rows , fields )
{
	if ( err ) { console.log( 'Error while performing Query.' ) ; } else
	{ console.log( 'The solution is: ' , rows ) ; }
 } ) ;
connection.end( ) ;