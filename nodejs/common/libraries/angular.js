
var anyApp = angular.module( 'anyApp' , [ ] ) ;

anyApp.controller
(
	'anyControl' , function( $scope )
	{
		$scope.frstName = "John" ;
		$scope.lastName = "Doe" ;
		$scope.fullName = function( )
		{
			return $scope.frstName + " " + $scope.lastName ;
		 }
		//
		$scope.names = [
		{ name:'Jani' , country:'Norway' } ,
		{ name:'Hege' , country:'Sweden' } ,
		{ name:'Kai' , country:'Denmark' }
	 ] ;
	 }
 ) ;
