var boolTgl = false ;
function collapser( )
{
	// table columns begin at 0
	// table tr does NOT begin at 0 if th is used
	// table does NOT begin at 0 if th is used
	// var can not be null!
	var varStyle = '' ; var varCol = 3 ; var varCellTds = '';
	if( boolTgl )
	{ boolTgl = false ; varStyle = 'none' ; } else
	{ boolTgl = true ; varStyle = 'block' ; }
	//
	var varTable = document.getElementById( 'books' ) ;
	var varRows = varTable.getElementsByTagName( 'tr' ) ;
	//
	// alert( varStyle + ' / ' +  varRows.length );
	var varCellTds = varRows[ 0 ].getElementsByTagName( 'th' );
	varCellTds[ varCol ].style.display = varStyle ;
	for ( var ictr = 1 ; ictr < varRows.length ; ictr++ )
	{
		varCellTds = varRows[ ictr ].getElementsByTagName( 'td' );
		varCellTds[ varCol ].style.display = varStyle ;
	 }
}
