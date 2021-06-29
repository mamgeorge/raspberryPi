// simply reads https response

const https = require( 'https' ) ;
const urls = [ 'https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY' , 
	'https://jsonplaceholder.typicode.com/' ];
let data = '' ;

https.get( urls[0] , ( response ) => {
	//
	response.on( "error" , ( err ) => { console.log( "Error: " + err.message ); } ) ;
	response.on( 'data' , ( chunk ) => { data += chunk ; } ) ;
	response.on( 'end' , ( ) => {
		//
		let body = JSON.parse( data );
		data = body.explanation;
		console.log( body.url ) ;
		console.log( data ) ;
	} ) ;

} );

console.log( "DONE: " + data ) ;
