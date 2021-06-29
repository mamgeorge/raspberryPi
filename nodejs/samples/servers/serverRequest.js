// serverRequest.js

const request = require('request');
const urlValue = 'https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY'

request( urlValue, { json: true }, (err, res, data) => {
	if (err) { return console.log(err); }
	console.log( data.title );
});
