// dir F:\servers\nodejs\public\resources\AnyClass.java
// "C:\Program Files\Java\jdk1.6.0_45\bin\javac" -cp F:\servers\nodejs\public\resources public\resources\AnyClass.java
// java -cp F:\servers\nodejs\public resources.AnyClass
package resources;

import java.util.Arrays;
import java.util.Properties;
import java.util.Set;
import java.util.logging.Logger;

public class AnyClass
{
	public static void main( final String[ ] strings )
	{
		System.out.println( AnyClass.showProperties( ) );
	}

	public static String showProperties( ) {
		//
		String txtLines = "\n";
		//
		// exec
		Properties properties = System.getProperties( );
		Set< ? > set = properties.keySet( );
		Object[ ] objects = set.toArray( );
		Arrays.sort( objects );
		String txtKey = "" , txtVal = "";
		int ictr = 0;
		int intMAX = 70;
		for( Object object : objects ) {
			//
			txtKey = ( String ) object;
			txtVal = properties.getProperty( txtKey );
			if ( txtKey.equals( "line.separator" ) ) {
				txtVal = "[ eol ]";
			}
			if ( txtVal == null ) {
				txtVal = "[ null ]";
			}
			if ( txtVal != null && txtVal.equals( "" ) ) {
				txtVal = "[ blank ]";
			}
			if ( txtVal != null && txtVal.length( ) > intMAX ) {
				txtVal = txtVal.substring( 0 , intMAX ) + "...";
			}
			txtLines += String.format( "\t%02d %-30s %s \n" , ++ictr , txtKey , txtVal );
		}
		// assertEquals( "54" , String.valueOf( txtLines.split( EOL ).length ) );
		return txtLines;
	}
}