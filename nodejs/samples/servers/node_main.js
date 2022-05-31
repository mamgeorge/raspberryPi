// cd /servers/nodejs , node root/node_paths.js , http://127.0.0.1:3000
// https://nodejs.org/en/docs/guides/anatomy-of-an-http-transaction/
// VARS MUST BE DEFINED BEFORE EXPORTS TO WORK IN STATIC AND NODE FILES

var http = require( 'http' ) ;
var basics = require( '../../common/resources/basics.js' ) ;
var varFs = require( 'fs' ) ;
let port = 3000 ;

function serveStatics( response , varPath , contentType , responseCode )
{
	varFs.readFile( varPath , function( err , data )
	{ response.writeHead( 200 , { 'Content-Type': contentType } ) ; response.end( data ) ; } ) ;
 }

var varServer = http.createServer( function ( request , response )
{
	var varFile = request.url ; if( varFile == '/' || varFile == '/dogs' ) { varFile = '/dogs.xml' ; }
	if( varFile.lastIndexOf( '.' ) == -1 ) { varFile = varFile + '.html' ; }
	var extension = varFile.substring( varFile.lastIndexOf( '.' ) + 1 ) ;
	var contentType = basics.MIME_TYPE[ extension ] ;
	var varPath = __dirname + '../../common/resources/' + varFile ; // ./public
	if( extension == 'jpg' || extension == 'png' ) { varPath = './public/images' + varFile ; }
	if( extension == 'html' ) { varPath = './public/html' + varFile ; }
	if( varFile == '/dogs.xml' ) { varPath = '../../common/resources' + '/dogsInfo.xml' ; }
	//
	console.log( basics.dateTime( new Date( ) ) + " / " + contentType + " / " + varPath ) ;
	serveStatics( response , varPath , contentType ) ;
 } ) ;

varServer.listen( port ) ;
//var varSprintf = require( "sprintf-js" ).sprintf , varOs = require( 'os' ) ;
//console.log( 'proc: ' + basics.reflectProc( varOs ) ) ; // JSON.stringify( process.env , null , 4 )
//console.log( 'srvr: ' + basics.reflectSrvr( varServer , varOs , varSprintf ) ) ;
console.log( process.env.USERNAME + ' / ' + process.env.COMPUTERNAME + ' / path: http://127.0.0.1:' + port ) ;
