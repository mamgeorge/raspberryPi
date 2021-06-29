// alert( 'jQuery' ) ;

$( document ).ready( function( )
{
	$( "button#one" ).click( function( ) { $( "b#one" ).toggle( ) ; } ) ;
	$( "button.two" ).click( function( ) { $( "b.two" ).toggle( ) ; } ) ;

	$( "h3" ).on(
	{
		mouseenter: function( )	{ $( this ).css( "color" , "blue" ) ; } ,
		mouseleave: function( )	{ $( this ).css( "color" , "black" ) ; } ,
		click: function( )		{ $( this ).css( "color" , "red" ) ; }
	 } ) ;

	$( "qq" ).click( function( ) { $( "qq" ).fadeToggle ( 1000 ).fadeIn   ( 1000 ) } ) ;

	$( "ww" ).click( function( ) { $( "ww" ).slideToggle( 1000 ).slideDown( 1000 ) } ) ;

 } ) ;
