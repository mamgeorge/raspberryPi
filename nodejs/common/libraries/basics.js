// basics.js ; VARS MUST BE DEFINED BEFORE EXPORTS TO WORK IN STATIC AND NODE FILES
exports.date = new Date( ).toISOString( );
exports.EOL = '\n' ;
exports.TAB = '\t' ;

exports.CHAR_TYPE = { utf8 : 'UTF8' , ascii : 'ASCII' , hex : 'hex' ,
	base64 : 'base64' , binary : 'binary' , ucs2 : 'ucs2' } ;
	
exports.MIME_TYPE = {
	//
	// http://www.freeformatter.com/mime-types-list.html
	txt		: 'text/plain'					 ,
	html	: 'text/html'					 ,
	css		: 'text/css'					 ,
	js		: 'application/javascript'		 ,
	json	: 'application/json'			 ,
	xml		: 'application/xml'				 ,
	dtd		: 'application/xml-dtd'			 ,
	csv		: 'text/csv'					 ,

	jpg		: 'image/jpeg'					 ,
	gif		: 'image/gif'					 ,
	png		: 'image/png'					 ,
	ico		: 'image/x-icon'				 ,
	tiff	: 'image/tiff'					 ,
	svg		: 'image/svg+xml'				 ,
	wav		: 'audio/x-wav'					 ,
	mpeg	: 'video/mpeg'					 ,

	pdf		: 'application/pdf'				 ,
	doc		: 'application/msword'			 ,
	rtf		: 'application/rtf'				 ,
	sxw		: 'application/vnd.sun.xml.writer'	 ,
	xls		: 'application/vnd.ms-excel'		 ,
	xslt	: 'application/xslt+xml'			 ,
	ppt		: 'application/vnd.ms-powerpoint'	 ,
	zip		: 'application/zip'					 ,
	z:0
 } ;

exports.GREEKS = [ 'alpha' , 'beta' , 'gamma' , 'delta' , 'epsilon' , 'zeta' , 'eta' , 'theta' , 'iota' , 'kappa' , 'lambda' , 'mu' , 'nu' , 'xi' , 'omicron' , 'pi' , 'rho' , 'sigma' , 'tau' , 'upsilon' , 'phi' , 'chi' , 'psi' , 'omega' ];

exports.COLORS_BOW = [ 1 , 3 , 2 , 6 , 4 , 5 , 7 ];
exports.COLORS_SRV = [ 2 , 6 , 3 , 4 , 1 , 5 , 7 ]; // grn cyn yel blu red mag
exports.COLORS = {
	// http://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html
	NON0 : '\u001b[0m',
	BLK0 : '\u001b[30m',
	RED0 : '\u001b[31m',
	GRN0 : '\u001b[32m',
	YEL0 : '\u001b[33m',
	BLU0 : '\u001b[34m',
	MAG0 : '\u001b[35m',
	CYN0 : '\u001b[36m',
	WHT0 : '\u001b[37m',
	BLK8 : '\u001b[40m',
	RED8 : '\u001b[41m',
	GRN8 : '\u001b[42m',
	YEL8 : '\u001b[43m',
	BLU8 : '\u001b[44m',
	MAG8 : '\u001b[45m',
	CYN8 : '\u001b[46m',
	WHT8 : '\u001b[47m',
	BLK1 : '\u001b[30;1m',
	RED1 : '\u001b[31;1m',
	GRN1 : '\u001b[32;1m',
	YEL1 : '\u001b[33;1m',
	BLU1 : '\u001b[34;1m',
	MAG1 : '\u001b[35;1m',
	CYN1 : '\u001b[36;1m',
	WHT1 : '\u001b[37;1m',
	BLK9 : '\u001b[40;1m',
	RED9 : '\u001b[41;1m',
	GRN9 : '\u001b[42;1m',
	YEL9 : '\u001b[43;1m',
	BLU9 : '\u001b[44;1m',
	MAG9 : '\u001b[45;1m',
	CYN9 : '\u001b[46;1m',
	WHT9 : '\u001b[47;1m',
}

function dateTime( dateOld )
{
	var dateNew = new Date( ) ;
	if ( dateOld != null && dateOld != '' ) { dateNew = dateOld ; }

	var dateYear = dateNew.getFullYear( ) ;
	var dateMonth = new String( dateNew.getMonth( )+1 ) ;
	var dateDay = new String( dateNew.getDate( ) ) ;
	var timeHour = dateNew.getHours( ) ; if ( timeHour>12 ) { timeHour = new String( timeHour - 12 ) ; } else { timeHour = new String( timeHour ) ; }
	var timeMinutes = new String( dateNew.getMinutes( ) ) ;
	var timeSeconds = new String( dateNew.getSeconds( ) ) ;
	var timeMilliseconds = new String( dateNew.getMilliseconds( ) ) ;
	//
	if ( dateMonth.length	< 2 )	{ dateMonth	= '0' + dateMonth ; }
	if ( dateDay.length		< 2 )	{ dateDay	= '0' + dateDay ; }
	if ( timeHour.length	< 2 )	{ timeHour	= '0' + timeHour ; }
	if ( timeMinutes.length	< 2 )	{ timeMinutes = '0' + timeMinutes ; }
	if ( timeSeconds.length	< 2 )	{ timeSeconds = '0' + timeSeconds ; }
	if ( timeMilliseconds.length< 3 ){ timeMilliseconds = '0' + timeMilliseconds ; }
	//
	var dateTotal = dateYear + '/' + dateMonth + '/' + dateDay ;
	var timeTotal = timeHour + ':' + timeMinutes + ':' + timeSeconds + '.' + timeMilliseconds ;
	var dateTimeFormatted = '' + dateTotal + ' - ' + timeTotal ;
	return dateTimeFormatted ;
 }
exports.dateTime = function( dateOld ) { return dateTime( dateOld ) ; }

// https://blog.risingstack.com/node-hero-async-programming-in-node-js/
// https://github.com/maxogden/art-of-node#callbacks
// http://javascriptissexy.com/understand-javascript-callback-functions-and-use-them/
// http://stackoverflow.com/questions/10058814/get-data-from-fs-readfile/10058879#10058879
// http://stackoverflow.com/questions/14220321/how-do-i-return-the-response-from-an-asynchronous-call/14220323#14220323
function dBaseSQLITE( dBaseURL , varSQL , response )
{
	// npm install sqlite3
	if( dBaseURL == null || dBaseURL == '' ) { dBaseURL = 'F:/dBase/sqlite/TEST.db' ; }
	if( varSQL == null || varSQL == '' ) { varSQL = 'SELECT name FROM anyTable' ; } // 'SELECT * FROM anyTable'
	var txtLines = '' ;
	//
	function readDbase( callback )
	{
		var sqlite = require( 'sqlite3' ).verbose( ) ;
		var dBase = new sqlite.Database( dBaseURL ) ;
		dBase.serialize( function( )
		{
			function readRow( err , row )
			{ txtLines += row.name ; console.log( row.name ) ; }
			dBase.each( varSQL , readRow ) ;
		} ) ;
		dBase.close( ) ;
		callback( ) ;
	 }
	//
	function handleData( )
	{
		console.log( 'readDbase results: [ ' + txtLines + ' ]' )
		var varHTML = buildDataHTML( 'dBase:sqlite' , txtLines ) ;
		response.end( varHTML ) ;
	 }
	 //
	 readDbase( handleData );
 }
exports.dBaseSQLITE = function( dBaseURL , varSQL , response ) { return dBaseSQLITE( dBaseURL , varSQL , response ) ; }

function docAddBytes( txtStrm )
{
	var txtChar = '' ;
	var bytes = [ ] ;
	for ( var ictr = 0 ; ictr < txtStrm.length ; ++ictr )
	{
		txtChar = txtStrm.charCodeAt( ictr ) ;
		bytes = bytes.concat( [ txtChar ] ) ;
	 }
	return bytes ;
 }
exports.docAddBytes = function( txtStrm ) { return docAddBytes( txtStrm ) ; }

function spawnPython( pathFile , args , response )
{
	const spawn = require( 'child_process' ).spawn;
	const child = spawn( 'python' , [ pathFile , args ] );
	//
	child.stdout.on( 'data' , ( data ) => {
		response.send( data );
	} );
	console.log( dateTime( ) + ' / ' + pathFile ) ;
 }
exports.spawnPython = function( pathFile , args , response ) { return spawnPython( pathFile , args , response ) ; }

function spawnJava( pathFile , file , response )
{
	var spawn = require( 'child_process' ).spawn ;
	var child = spawn( 'java' , [ '-cp' , pathFile , file ] ) ;
	var varHTML = '' ;

	// process.stdout.write( data.toString( ) ) ;
	child.stdout.on( 'data' , function( data ) { varHTML = buildDataHTML( 'stdout: ' + file , data ) ; response.end( varHTML ) ; } ) ;
	child.stderr.on( 'data' , function( data ) { varHTML = buildDataHTML( 'stderr: ' + file , data ) ; response.end( varHTML ) ; } ) ;
	child.on( 'close' , function ( exitCode ) { if ( exitCode !== 0 ) { varHTML = 'exitCode: ' + exitCode ; } else
		{ varHTML = 'on close ( exitCode == 0 ): EXIT' ; }
	 } ) ;
	console.log( dateTime( ) + ' / ' + varHTML ) ;
 }
exports.spawnJava = function( pathFile , file , response ) { return spawnJava( pathFile , file , response ) ; }

function buildDataHTML( header , data )
{
	var varHTML = '<link rel = "styleSheet" href = "styleAny.css" type = "text/css" />' ;
	varHTML += '<center><h3>' + header + '</h3><br /><br />' ;
	varHTML += '<table border = "1" cellspacing = "0" style = "width: 80% ;" ><tr><td>' ;
	varHTML += '<div style = "height: 150px ; overflow: auto;" >' ;
	varHTML += data.toString( ).replace( /\n/g , '<br />' ) ;
	varHTML += '</div></td></tr></table>' ;
	varHTML += '<br /><br /><a href = "/home" >return</a></center>' ;
	return varHTML ;
 }
exports.buildDataHTML = function( header , data ) { return buildDataHTML( header , data ) ; }

function reflectProc( varOs )
{
	var txtLines = EOL ;
	txtLines += TAB + 'process.arch	: '		+ process.arch + EOL ;
	txtLines += TAB + 'process.argv	: '		+ process.argv.length + ' , ' + process.argv[ 0 ] + EOL ;
	txtLines += TAB + 'process.config : '	+ process.config.variables.host_arch + EOL ;
	txtLines += TAB + 'process.connected: ' + process.connected + EOL ;
	txtLines += TAB + 'process.cwd	: '		+ process.cwd + EOL ;
	txtLines += TAB + 'process.env	: '		+ process.env + EOL ;
	txtLines += TAB + 'process.emitWarning: ' + process.emitWarning( 'emit!' ) + EOL ;
	txtLines += TAB + 'process.pid	: '		+ process.pid + EOL ;
	txtLines += TAB + 'process.platform: '	+ process.platform + EOL ;
	txtLines += TAB + 'process.release : '	+ process.release + EOL ;
	txtLines += TAB + 'process.title	:'	+ process.title + EOL ;
	txtLines += TAB + 'process.uptime : '	+ process.uptime + EOL ;
	txtLines += TAB + 'process.version : '	+ process.version + EOL ;
	txtLines += TAB + 'process.versions: '	+ process.versions.http_parser + EOL ;
	txtLines += TAB + '----------' + EOL ;
	//
	txtLines += TAB + 'os.arch( )	: '		+ varOs.arch( ) + EOL ;
	txtLines += TAB + 'os.cpus( )	: '		+ varOs.cpus( ).length + ' , ' + varOs.cpus( )[ 0 ].model + EOL ;
	txtLines += TAB + 'os.freemem( ) : '	+ varOs.freemem( ) + EOL ;
	txtLines += TAB + 'os.homedir( ) : '	+ varOs.homedir( ) + EOL ;
	txtLines += TAB + 'os.hostname( ): '	+ varOs.hostname( ) + EOL ;
	txtLines += TAB + 'os.platform( ): '	+ varOs.platform( ) + EOL
	txtLines += TAB + 'os.release( ) : '	+ varOs.release( ) + EOL
	txtLines += TAB + 'os.totalmem( ): '	+ varOs.totalmem( ) + EOL ;
	txtLines += TAB + 'os.type( )	: '		+ varOs.type( ) + EOL ;
	txtLines += TAB + 'os.uptime( ) : '		+ varOs.uptime( ) + EOL ;
	return txtLines ;
 }
exports.reflectProc = function( varOs ) { return reflectProc( varOs ) ; }

function reflectSrvr( varServer , varOs , varSprintf )
{
	var txtLines = EOL ;
	var osNetworkInterfaces = varOs.networkInterfaces( ) ;
	txtLines += EOL + TAB + JSON.stringify( osNetworkInterfaces , null , '\t' ) + EOL + EOL ;
	//
	var osNetworkInterface = '' ;
	var extIpAddr = '' ;
	for ( var ictr in osNetworkInterfaces )
	{
		osNetworkInterface = osNetworkInterfaces[ ictr ] ;
		// .filter( function( varDetails ) { return varDetails.family === 'IPv4' && varDetails.internal === false ; } ) ;
		if( osNetworkInterface.length > 0 )
		{
			for ( var jctr in osNetworkInterfaces[ ictr ] )
			{
				txtLines += varSprintf( '\t %-28s %-25s %-25s %s %s %s \n' ,
					ictr ,
					osNetworkInterface[ jctr ].address ,
					osNetworkInterface[ jctr ].netmask ,
					osNetworkInterface[ jctr ].family ,
					osNetworkInterface[ jctr ].mac ,
					osNetworkInterface[ jctr ].internal ) ;
					//
					if( osNetworkInterface[ jctr ].family === 'IPv4' && osNetworkInterface[ jctr ].internal === false )
					{ extIpAddr = osNetworkInterface[ jctr ].address ; }
			 }
		 }
	 }
	txtLines += EOL + 'addr: ' + JSON.stringify( varServer.address( ) , null , '\t' ) ;
	txtLines += EOL + 'IPv4: ' + extIpAddr ;
	return txtLines ;
 }
exports.reflectSrvr = function( http , varOs , varUtil ) { return reflectSrvr( http , varOs , varUtil ) ; }

function reflectDocs( )
{
	var delimiter = '<br />' ;
	var delim1 = '<tr><th style = "text-align: left;" ><b>' ;
	var delim2 = '</b></th><td style = "text-align: left;" >' ;
	var delim3 = ' ;</td></tr>' ;

	strReflect = '<br /><center><table border = "1" width = "100%" >' ;
	strReflect += delim1 + 'document.title'				+ delim2 + document.title				+ delim3 ;
	strReflect += delim1 + 'document.body.clientWidth'	+ delim2 + document.body.clientWidth	+ delim3 ;
	strReflect += delim1 + 'document.body.clientHeight'	+ delim2 + document.body.clientHeight	+ delim3 ;

	delim1 = '<tr><th class = "cont" ><b>' ;
	delim2 = '</b></th><td style = "text-align: left ; background: url( \"images/backStripes.gif\" ) ;" >' ;
	strReflect += delim1 + 'window.pageXOffset'			+ delim2 + window.pageXOffset		+ delim3 ;
	strReflect += delim1 + 'window.pageYOffset'			+ delim2 + window.pageYOffset		+ delim3 ;
	strReflect += delim1 + 'window.screen.availWidth'	+ delim2 + window.screen.availWidth + delim3 ;
	strReflect += delim1 + 'window.screen.availHeight'	+ delim2 + window.screen.availHeight + delim3 ;
	strReflect += delim1 + 'window.location'			+ delim2 + window.location			+ delim3 ;
	strReflect += delim1 + 'window.location.hash'		+ delim2 + window.location.hash		+ delim3 ;
	strReflect += delim1 + 'window.location.host'		+ delim2 + window.location.host		+ delim3 ;
	strReflect += delim1 + 'window.location.hostname'	+ delim2 + window.location.hostname + delim3 ;
	strReflect += delim1 + 'window.location.href'		+ delim2 + window.location.href		+ delim3 ;
	strReflect += delim1 + 'window.location.pathname'	+ delim2 + window.location.pathname + delim3 ;
	strReflect += delim1 + 'window.location.port'		+ delim2 + window.location.port		+ delim3 ;
	strReflect += delim1 + 'window.location.protocol'	+ delim2 + window.location.protocol + delim3 ;
	strReflect += delim1 + 'window.location.search'		+ delim2 + window.location.search	+ delim3 ;

	delim1 = '<tr><th style = "text-align: left;" ><b>' ;
	delim2 = '</b></th><td style = "text-align: left;" >' ;
	strReflect += delim1 + 'navigator.appCodeName'		+ delim2 + navigator.appCodeName	+ delim3 ;
	strReflect += delim1 + 'navigator.appName'			+ delim2 + navigator.appName		+ delim3 ;
	strReflect += delim1 + 'navigator.appVersion'		+ delim2 + navigator.appVersion		+ delim3 ;
	strReflect += delim1 + 'navigator.language'			+ delim2 + navigator.language		+ delim3 ;
	strReflect += delim1 + 'navigator.mimeTypes.length'	+ delim2 + navigator.mimeTypes.length + delim3 ;
	strReflect += delim1 + 'navigator.platform'			+ delim2 + navigator.platform		+ delim3 ;
	strReflect += delim1 + 'navigator.plugins.length'	+ delim2 + navigator.plugins.length + delim3 ;
	strReflect += delim1 + 'navigator.userAgent'		+ delim2 + navigator.userAgent		+ delim3 ;
	strReflect += '</table></center><br />' ;
	return strReflect ;
 }
exports.reflectDocs = function( ) { return reflectDocs( ) ; }

function popupSite( anyURL , wdth , hght )
{
	if ( wdth == 0 ) { wdth = 400 ; }
	if ( hght == 0 ) { hght = 200 ; }
	var popX = ( screen.width/2 )-( wdth/2 ) ;
	var popY = ( screen.height/2 )-( hght/2 ) ;
	var varOpts = 'scrollbars=1 , resizable=1 , menubar=0 , location=0 , directories=0 , toolbar=0 , status=0' ;
	var varStrg = 'width=' + wdth + ' , height=' + hght + ' , top=' + popY + ' , left=' + popX + ' , ' + varOpts ;
	var varWindow = window.open( anyURL , 'popupOptions' , varStrg ) ;
	//
	varWindow.self.focus( ) ;
	return ;
 }

function popupText( txtLines )
{
	var wdth = 400 , hght = 200 ;
	var popX = ( screen.width/2 )-( wdth/2 ) ;
	var popY = ( screen.height/2 )-( hght/2 ) ;
	var varOpts = 'scrollbars=0 , resizable=0 , menubar=0 , location=0 , directories=0 , toolbar=0 , status=0' ;
	var varStrg = 'width=' + wdth + ' , height=' + hght + ' , top=' + popY + ' , left=' + popX + ' , ' + varOpts ;
	var varWindow = window.open( '' , 'popupNote' , varStrg ) ;
	//
	// varWindow.document.writeln( '<script> setTimeout( 'self.close( )' , 5000 ) ; <\/script>' ) ;
	varWindow.document.writeln( '<html><head><title>HOG</title>' ) ;
	varWindow.document.writeln( '<link rel = "StyleSheet" href = "styleAny.css" type = "text/css" />' ) ;
	varWindow.document.writeln( '</head><body><center><h3>MLG</h3><br /><br />' ) ;
	varWindow.document.writeln( txtLines ) ;
	varWindow.document.writeln( '</center></body</html>' ) ;
	//
	varWindow.self.focus( ) ;
	return ;
 }
