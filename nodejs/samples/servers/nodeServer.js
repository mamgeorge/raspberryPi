// VARS MUST BE DEFINED BEFORE EXPORTS TO WORK IN STATIC AND NODE FILES

let http = require( 'http' ) ;
let fs = require( 'fs' ) ;
let basics = require( '../../common/resources/basics.js' ) ;

let port = 3000 ;
let info = process.env.USERNAME + ' / ' + process.env.COMPUTERNAME + ' / ' + port + ' / ';
//
function serveStatics( response , pathFile , contentType , responseCode ) {
	fs.readFile( pathFile , function( err , data ) {
		response.writeHead( 200 , { 'Content-Type': contentType } ) ; response.end( data ) ;
		console.log( pathFile + ' / ' + new Date( ).toISOString( ) ) ;
	} ) ;
 }

let varServer = http.createServer( function ( request , response ) {
	//
	let file = request.url ; if( file == '/' ) { file = '../../common/index.html' ; }
	if( file == '/java' ) { basics.spawnJava(  'C:\\servers\\nodejs\\public' , 'resources.AnyClass' , response ); } else
	if( file == '/base' ) { basics.dBaseSQLITE(  'C:/dBase/sqlite/TEST.db' , 'SELECT name FROM anyTable' , response ); } else
	{
		if( file.lastIndexOf( '.' ) == -1 ) { file = file + '.html' ; }
		let extension = file.substring( file.lastIndexOf( '.' ) + 1 ) ;
		let pathFile = __dirname + '' + file ; // ./public
		if( extension == 'html' ) { pathFile = './public/' + file ; }
		let contentType = basics.MIME_TYPE[ extension ] ;
		serveStatics( response , pathFile , contentType ) ;
	}
 } ) ;

varServer.listen( port ) ;
console.log( info + new Date( ).toISOString( ) ) ;
