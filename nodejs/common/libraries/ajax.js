// function ajaxLoad( )
// function ajaxDocLoad( )
// function transformXML( )

var pathFile = 'sample.txt' ;
var tagHome = 'ajaxTest' ;
var txtVal = '<a href = "/home" >return</a>' ;
var EOL = '<br /><br />\n' ;

function ajaxLoad( )
{
	var txtLines = EOL ;
	var xmlHttpRequest = new XMLHttpRequest( ) ;
	xmlHttpRequest.onreadystatechange = function( )
	{
		if ( this.readyState == 4 && this.status == 200 )
		{
			txtLines += this.responseText + EOL ;
			txtLines += docAddBytes( 'MLG!' ) + EOL + txtVal + EOL ;
			document.getElementById( tagHome ).innerHTML = txtLines ;
		 }
	 } ;
	xmlHttpRequest.open( 'GET' , pathFile ) ;
	xmlHttpRequest.send( ) ;
 }

function ajaxDocLoad( varPathFile )
{
	if ( window.ActiveXObject )
	{ xmlHttpRequest = new ActiveXObject( 'Msxml2.XMLHTTP' ) ; } else
	{ xmlHttpRequest = new XMLHttpRequest( ) ; }
	//
	xmlHttpRequest.open( 'GET' , varPathFile , false ) ;
	try { xmlHttpRequest.responseType = 'msxml-document' } catch( err ) { } // Helping IE11
	xmlHttpRequest.send( '' ) ;
	var varXML = xmlHttpRequest.responseXML ;
	return varXML;
 }

// onclick = 'transformXML( )'>
function transformXML( varTagNode , varPathFileXML , varPathFileXSL )
{
	varXML = ajaxDocLoad( varPathFileXML ) ;
	varXSL = ajaxDocLoad( varPathFileXSL ) ;
	var varHTML = '';
	if ( window.ActiveXObject || xmlHttpRequest.responseType == 'msxml-document' )
	{
		// code for IE
		varHTML = varXML.transformNode( varXSL ) ;
		document.getElementById( varTagNode ).innerHTML = varHTML ;
	 }
	else
	if ( document.implementation && document.implementation.createDocument )
	{
		// code for Chrome , Firefox , Opera , etc.
		xsltProcessor = new XSLTProcessor( ) ;
		xsltProcessor.importStylesheet( varXSL ) ;
		varHTML = xsltProcessor.transformToFragment( varXML , document ) ;
		//
		var varElementNew = document.createElement( 'div' );
		varElementNew.appendChild( varHTML );
		document.getElementById( varTagNode ).innerHTML = varElementNew.innerHTML;

		// document.getElementById( varTagNode ).appendChild( varHTML ) ;
	 }
	return false;
 }
