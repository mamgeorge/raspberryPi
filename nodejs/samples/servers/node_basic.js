// http://127.0.0.1:3000/?q=1234
var http = require( 'http' ) ;
var basics = require( '../../common/resources/basics.js' ) ;
let port = 3000 ;

// request handler
var varServer = http.createServer( ) ;

varServer.on( 'request' , function requestor( request , response )
{
	var varDate = basics.dateTime( new Date( ) ) ;
	console.log( 'varDate: ' + varDate ) ;
	//
	response.writeHead( 200 , { 'Content-Type': basics.MIME_TYPE.html } ) ;
	response.write( varDate ) ;
	response.end( 'MLG' ) ;
} ) ;

varServer.listen( port , '127.0.0.1' ) ;

console.log( 'Server running at: http://127.0.0.1:' + port) ;
