// java
// http://stackoverflow.com/questions/32039111/how-to-call-a-java-program-from-node-js
// http://stackoverflow.com/questions/30134236/use-child-process-execsync-but-keep-output-in-console
function spawnJava( cPathFile , file , response )
{
	var spawn = require( 'child_process' ).spawn ;
	var child = spawn( 'java' , [ '-cp' , cPathFile , file ] ) ;
	var varHTML = '';

	// process.stdout.write( data.toString( ) ) ;
	child.stdout.on( 'data' , function( data ) { varHTML = buildDataHTML( 'stdout: ' + file , data ) ; response.end( varHTML ) ; } ) ;
	child.stderr.on( 'data' , function( data ) { varHTML = buildDataHTML( 'stderr: ' + file , data ) ; response.end( varHTML ) ; } ) ;
	child.on( 'close' , function ( exitCode ) { if ( exitCode !== 0 ) { varHTML = 'exitCode: ' + exitCode ; } else
		{ varHTML = 'on close ( exitCode == 0 ): EXIT' ; }
	} ) ;
	console.log( varHTML ) ;
}
exports.spawnJava = function( cPathFile , file , response ) { return spawnJava( cPathFile , file , response ) ; }


// http://stackoverflow.com/questions/14332721/node-js-spawn-child-process-and-get-terminal-output-instantaneously
expressApp.get( '/java' , function ( request , response )
{
	var varParms = 'java -cp F:\\servers\\nodejs\\public\\resources AnyClass' ;
	var exec = require( 'child_process' ).exec ;
	var child = exec( varParms , function ( error , stdout , stderr ) { if( error !== null ) { console.log( "Error -> "+ error ) ; } } ) ;
	//
	child.stdout.on( 'data' , function( data ) {
		var varHTML += 'stdout: ' + data.toString( ) ;
		console.log( varHTML ) ; response.end( varHTML ) ;
	 } ) ;

 } ) ;
