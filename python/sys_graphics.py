
## home/pi/python/sys_graphics.py
## can display in CLI but not thru putty ; requires XShell?

import pygame
import sens_defn

## init
pygame.init( )
size = ( 700 , 500 )
screen = pygame.display.set_mode( size )
pygame.display.set_caption( "MLG" )

PI = 3.141592653
done = False
clock = pygame.time.Clock( )

## events read in loop
while not done:

		for event in pygame.event.get( ):
				if event.type == pygame.QUIT:
						done = True

		## game / drawing logic
		screen.fill( sens_defn.n )

		pygame.draw.line( screen , sens_defn.G , [ 0 , 0 ] , [ 100 , 100 ] , 5 )
		pygame.draw.rect( screen , sens_defn.R , [ 20 , 20 , 250 , 100 ] , 2 )
		pygame.draw.ellipse( screen , sens_defn.B , [ 20 , 20 , 250 , 100 ] , 2 )
		pygame.draw.polygon( screen , sens_defn.G , [ [ 100 , 100 ] , [ 0 , 200 ] , [ 200 , 200 ] ] , 5 )

		pygame.draw.arc( screen , sens_defn.R , [ 20 , 220 , 250 , 200 ] , 0 , PI / 2 , 2 )
		pygame.draw.arc( screen , sens_defn.B , [ 20 , 220 , 250 , 200 ] , PI / 2 , PI , 2 )
		pygame.draw.arc( screen , sens_defn.G , [ 20 , 220 , 250 , 200 ] , PI , 3 * PI / 2 , 2 )
		pygame.draw.arc( screen , sens_defn.Y , [ 20 , 220 , 250 , 200 ] , 3 * PI / 2 , 2 * PI , 2 )

		##
		pygame.display.flip( )
		clock.tick( 60 )

pygame.quit( )
