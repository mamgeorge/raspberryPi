// https://www.tutorialspoint.com/nodejs/nodejs_express_framework.htm
// cd c:\workspace\vscode\nodeSamples
// node expresso
// > curl -v http://localhost:3000/json
// > powershell (curl http://localhost:3000/json).content

const basics = require( './common/libraries/basics.js' )
const express = require( 'express' )
const colors = require( 'colors/safe' )
const log4js = require( 'log4js' )
const path = require( 'path' )
const expressApp = express( )
const PORT = 3000

expressApp.use( express.static( path.join( __dirname, '/' ) ) )
expressApp.use( express.static( path.join( __dirname, '/images' ) ) )
expressApp.use( express.static( path.join( __dirname, '/common/resources' ) ) )
expressApp.use( express.static( path.join( __dirname, '/common/libraries' ) ) )
//
// logging setup
let date = new Date( ).toISOString( )
datestamp = '_' + date.replace(/-/g,'').replace(/T/g,'_').replace(/:/g,'').replace(/\./g,'')
fileSimpl = 'logs/' + 'expresso' + '.log'
fileTitle = 'logs/' + 'expresso' + datestamp.substr(0,16) + '.log'
log4js.configure( {
	appenders: { 'file' : { type: 'file', filename: fileSimpl } },
	categories: { default : { appenders: ['file'], level: 'info' } },
})
const logger = log4js.getLogger('testing')
logger.info( '\n' + '■'.repeat(20) + '\n' + 'Beginning batch run for expresso ' )

// server
const varServer = expressApp.listen( PORT , ( )=> {
	//
	const txt = colors.brightCyan( 'expresso' )
	+ `\n\t` + `user: ${ process.env.USERNAME }`
	+ `\n\t` + `date: ${ date }`
	+ `\n\t` + `drnm: ${__dirname}`
	console.log( colors.brightGreen( txt ) )
} )

function getGeneric( prefix, req ) {
	//
	date = new Date( ).toISOString( )
	let msg = prefix + ` : ${date}`
	msg += '\n' + process.cwd( )
	msg += '\n' + JSON.stringify( req.query )
	msg += '\n' + JSON.stringify( req.headers, null, '\t' ) + '\n'
	//
	const envr = Object.keys( process.env ).map( ( idx , ctr ) =>
		+ ctr.toString( ).padEnd(2) + ' '
		+ idx.padEnd(25) + ' | '
		+ process.env[ idx ] )
	msg += 	colors.brightBlue( envr )
	//
	return msg
}

expressApp.get( [ '/0' , '/exit' ] , ( request , response ) => {
	//
	console.log( colors.brightRed( 'EXIT!' ) )
	process.exit(0)
} )

expressApp.get( [ '/1' , '/' , '/root' ], ( request , response ) => {
	//
	let txtline = colors.brightCyan( 'Hello!' )
	txtline += '\n    0 ' + 'exit'
	txtline += '\n    1 ' + 'root'
	txtline += '\n    2 ' + 'home'
	txtline += '\n    3 ' + 'test'
	txtline += '\n    4 ' + 'json'
	txtline += '\n    5 ' + 'wav'
	txtline += '\n    6 ' + 'zip'
	txtline += '\n    7 ' + 'java'
	txtline += '\n    8 ' + 'python'
	console.log( txtline )
	response.send( txtline )
	response.end( )
} )

expressApp.get( [ '/2' , '/home' ] , ( request , response ) => {
	const fileName = __dirname + '/common/index.html'
	console.log( fileName )
	response.sendFile( fileName )
	response.end( )
} )

expressApp.get( [ '/3' , '/test' ] , ( request , response ) => {
	//
	let msg = getGeneric( 'test' , request )
	console.log( colors.brightMagenta(msg) )
	logger.info( msg )
	response.sendStatus( 200 )
	response.end( )
} )

expressApp.get( [ '/4' , '/json' ] , ( request , response ) => {
	//
	const fileName = __dirname + '/common/resources/books.json'
	console.log( fileName )
	// response.json( { ping: true } )
	response.sendFile( fileName )
	response.end( )
} )

expressApp.get( [ '/5' , '/wav' ] , ( request , response ) => {
	//
	const fileName = __dirname + '/common/resources/hal9000.wav'
	console.log( fileName )
	response.sendFile( fileName )
	response.end( )
} )

expressApp.get( [ '/6' , '/zip' ] , ( request , response ) => {
	//
	const fileName = __dirname + '/common/resources/xml/xml_wav_books_7zp.zip'
	console.log( fileName )
	response.sendFile( fileName )
	response.end( )
} )

expressApp.get( [ '/7' , '/java' ] , ( request , response ) => {
	//
	const pathName = 'C:\\servers\\nodejs\\'
	console.log( pathName )
	basics.spawnJava( pathName , 'resources.AnyClass' , response )
} )

expressApp.get( [ '/8' , '/python' ] , ( request , response ) => {
	//
	const fileName = './resources/sample.py'
	console.log( fileName )
	basics.spawnPython( fileName , '' , response )
} )
//----
