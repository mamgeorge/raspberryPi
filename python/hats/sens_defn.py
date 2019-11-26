
R = ( 255 , 000 , 000 )
O = ( 255 , 128 , 000 )
Y = ( 255 , 255 , 000 )
G = ( 000 , 255 , 000 )
B = ( 000 , 000 , 255 )
V = ( 255 , 000 , 255 )
Q = ( 128 , 64 , 000 )
C = ( 153 , 217 , 234 )
W = ( 255 , 255 , 255 )
n = ( 000 , 000 , 000 )

def MLG( ):
	array = [
	n , n , n , n , n , n , n , n ,
	n , R , n , n , n , n , R , n ,
	n , R , R , n , n , R , R , n ,
	n , R , R , R , R , R , R , n ,
	n , R , R , R , R , R , R , n ,
	n , R , R , n , n , R , R , n ,
	n , R , R , n , n , R , R , n ,
	n , n , n , n , n , n , n , n ,
	 ]
	return array

def GEO( ):
	array = [
	n , n , n , R , n , n , n , R ,
	n , n , R , R , R , n , n , O ,
	n , R , R , R , R , R , n , Y ,
	R , R , R , R , R , R , R , G ,
	n , R , R , R , R , R , n , B ,
	n , n , R , R , R , n , n , V ,
	n , n , n , R , n , n , n , W ,
	n , n , n , n , n , n , n , n ,
	 ]
	return array

def SPRG( ):
	array = [
	n , n , n , G , G , n , n , n ,
	n , n , G , G , G , G , n , n ,
	n , n , G , G , G , G , n , n ,
	n , n , n , G , G , n , n , n ,
	n , G , G , G , G , G , G , n ,
	G , G , G , G , G , G , G , G ,
	G , G , G , G , G , G , G , G ,
	n , G , G , n , n , G , G , n ,
	 ]
	return array

def SMMR( ):
	array = [
	n , n , Y , Y , Y , Y , n , n ,
	n , Y , Y , Y , Y , Y , Y , n ,
	Y , Y , Y , Y , Y , Y , Y , Y ,
	Y , Y , Y , Y , Y , Y , Y , Y ,
	Y , Y , Y , Y , Y , Y , Y , Y ,
	Y , Y , Y , Y , Y , Y , Y , Y ,
	n , Y , Y , Y , Y , Y , Y , n ,
	n , n , Y , Y , Y , Y , n , n ,
	 ]
	return array

def ATMN( ):
	array = [
	n , n , R , O , O , R , n , n ,
	n , R , O , Y , Y , O , R , n ,
	R , O , Y , R , O , Y , O , R ,
	R , Y , R , O , R , Y , O , R ,
	R , O , Y , R , O , Y , O , R ,
	n , R , O , Y , Y , O , R , n ,
	n , n , n , Q , Q , n , n , n ,
	n , n , n , Q , Q , n , n , n ,
	 ]
	return array

def WNTR( ):
	array = [
	n , n , n , C , C , n , n , n ,
	n , C , C , n , n , C , C , n ,
	n , C , C , n , n , C , C , n ,
	C , n , n , C , C , n , n , C ,
	C , n , n , C , C , n , n , C ,
	n , C , C , n , n , C , C , n ,
	n , C , C , n , n , C , C , n ,
	n , n , n , C , C , n , n , n ,
	 ]
	return array

def FLAG( ): # SUMMER
	array = [
	n , n , n , n , n , n , n , n ,
	n , W , W , W , W , W , W , n ,
	n , R , O , Y , G , B , V , n ,
	n , R , O , Y , G , B , V , n ,
	n , R , O , Y , G , B , V , n ,
	n , R , O , Y , G , B , V , n ,
	n , W , W , W , W , W , W , n ,
	n , n , n , n , n , n , n , n ,
	 ]
	return array

def TREE( ): # SUMMER
	array = [
	n , n , G , G , G , G , n , n ,
	n , G , G , G , G , G , G , n ,
	G , G , G , G , G , G , G , G ,
	G , G , G , G , G , G , G , G ,
	G , G , G , G , G , G , G , G ,
	n , G , G , G , G , G , G , n ,
	n , n , n , Q , Q , n , n , n ,
	n , n , n , Q , Q , n , n , n ,
	 ]
	return array

def TREE_XMAS( ): # WINTER
	array = [
	n , n , n , n , n , n , n , n ,
	n , n , n , G , G , n , n , n ,
	n , n , n , G , G , n , n , n ,
	n , n , G , G , G , G , n , n ,
	n , n , G , G , G , G , n , n ,
	n , G , G , G , G , G , G , n ,
	G , G , G , G , G , G , G , G ,
	n , n , n , Q , Q , n , n , n ,
	 ]
	return array