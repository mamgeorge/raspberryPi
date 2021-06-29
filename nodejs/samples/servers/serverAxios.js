// serverAxios.js

const axios = require('axios');
const urlValue = 'https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY'

axios.get( urlValue )
	.then( response => { console.log( response.data.title ); } )
	.catch( error => { console.log( error ); } );