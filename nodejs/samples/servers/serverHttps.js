// serverHttps.js
// https://www.twilio.com/blog/2017/08/http-requests-in-node-js.html

const urlValue = 'https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY'
const https = require('https');

https.get( urlValue , (res) => {
	//
	let data = '';
	res.on('data', (chunk) => { data += chunk; } );
	res.on('end', () => { console.log( JSON.parse( data ).title ); });
}).on("error", (err) => { console.log("Error: " + err.message); });
