// https://www.twilio.com/blog/2017/08/http-requests-in-node-js.html
// https://codeburst.io/all-about-http-in-node-js-and-3-best-ways-for-http-requests-in-web-development-6e5b6876c3a4
// https://nodejs.org/en/docs/guides/anatomy-of-an-http-transaction/

const axios = require( 'axios' ) ;
const urls = [ 'https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY' , 'https://jsonplaceholder.typicode.com/' ] ;
let data = '' ;

axios.get( urls[0] ).then( response => {
	data = response.data.explanation;
	console.log( response.data.url ) ;
	console.log( data ) ;
} ).
catch( error => { console.log( error ) ; } ) ;

console.log( "DONE: " + data ) ;
