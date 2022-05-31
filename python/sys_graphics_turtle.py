## \\python\sys_graphics_turtle.py

from turtle import *

colors = [ 'red' , 'orange' , 'yellow' , 'green' , 'blue' , 'purple' ]

getscreen( )
bgcolor( "black" )

for xctr in range( 360 ):
	pencolor( colors[ xctr % 6 ] )
	width( xctr / 100 + 1 )
	forward( xctr )
	left( 59 )
