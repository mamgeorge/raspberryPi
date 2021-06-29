// simply reads http response

const request = require( 'request' ) ;
const urls = [ 'https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY' ,
	'https://jsonplaceholder.typicode.com/' ] ;
let data = '';

request( urls[ 0 ] , { json: true } , ( err , res , body ) => {
	//
	if ( err ) { return console.log( "Error: " + err.message ); }
	data = body.explanation;
	console.log( body.url ) ;
	console.log( data ) ;
 } ) ;

console.log( "DONE: " + data ) ;
