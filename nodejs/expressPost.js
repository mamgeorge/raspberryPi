// https://stackoverflow.com/questions/4295782/how-to-process-post-data-in-node-js
// cd c:\workspace\vscode\nodeSamples
// node expresso
// > curl -v http://localhost:3000/json
// > powershell (curl http://localhost:3000/json).content

const axios = require( 'axios' ) 
const express = require( 'express' ) 
const colors = require( 'colors/safe' )
const expressApp = express( ) 
const PORT = 3000

expressApp.use( express.urlencoded( ) )
expressApp.use( express.json( ) )
//
const varServer = expressApp.listen( PORT , ( )=> 
{ console.log( colors.brightGreen( new Date( ).toISOString( ) ) ) } ) 

expressApp.get( [ '/0' , '/exit' ] , ( request , response ) => 
{ console.log( colors.brightRed( 'EXIT!' ) ); process.exit(0) } ) 

expressApp.get( [ '/1' , '/' , '/root' ], ( request , response ) => {
	//
	let txtline = colors.brightCyan( 'Hello!' )
	txtline += '\n    0 ' + 'exit'
	txtline += '\n    1 ' + 'root'
	txtline += '\n    2 ' + 'posts'
	txtline += '\n    3 ' + 'axios'
	console.log( txtline ) 
	response.send( txtline )
	response.end( )
} ) 

expressApp.post( [ '/2' , '/posts' ] , (request, response) => {
	//
    console.log( colors.inverse( '[ received: ' + JSON.stringify( request.body ) + ' ]' ) )
    console.log( request.body.user.name )
    console.log( request.body.user.email )
	response.send( 'RECEIVED!' )
})

const axios = require('axios')
function postUrl( url, json ) {
	//
	process.env[ "NODE_TLS_REJECT_UNAUTHORIZED" ] = 0
	axios.post( url, json )
		.then function(response) {
			// 
			let msg =  '■'.repeat(20) + '\n' + JSON.stringify( response.data )
			console.log( colors.brightBlue( msg ); logger.info( msg ) 	
		} )
		.catch( function( error ) {
			//
			let err = error.name + ' : ' + error.message
			console.log( colors.brightRed( err ) )
			logger.error( err )
		} )
.then( function( ) { console.log( colors.yellow( 'POST DONE' + '\n' ) ) } )}		
}


