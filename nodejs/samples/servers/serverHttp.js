// serverHttp.js
// https://www.twilio.com/blog/2017/08/http-requests-in-node-js.html

const http = require('http');
const portHttp = 3000;

const requestHandler = ( request, response ) => {
	//
	const date = new Date( ).toISOString( );
	const msg = 'Hello Client!';
	const obj = { msg: msg , date: date }; 
	console.log( request.url + " " + JSON.stringify( obj ) );
	response.end( msg + " " + JSON.stringify( obj ) );
}

const httpServer = http.createServer(requestHandler);

httpServer.listen( portHttp , (err) => {
	//
	const date = new Date( ).toISOString( );
	if (err) { return console.log('error!', err ); }
	console.log( `server listens on ${portHttp} at ${date}` );
});
