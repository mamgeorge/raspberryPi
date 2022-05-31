<?xml version = "1.0" encoding = "UTF-8"?>
<xsl:stylesheet version = "1.0" xmlns:xsl = "http://www.w3.org/1999/XSL/Transform">
<xsl:output method = "html" encoding = "UTF-8" indent = "yes" omit-xml-declaration = "yes" />
<!-- F:\servers\nodejs\public\resources\foods.xslt -->

<xsl:template match = "/">

<link type = "text/css" rel = "StyleSheet" href = "styleAny.css" />
<!--script type = "text/javascript" src = "temp.js" >&#160;</script-->

<div><center><br /><h3>foods</h3>

<table border = "1" cellspacing = "0">
<tr>
	<th>name</th>
	<th>calories</th>
	<th>price</th>
	</tr>

<xsl:for-each select = "foods/breakfast/dish" >
<xsl:sort select = "name" />
<xsl:if test = "price &gt; 0.00">
<tr>
	<td><xsl:value-of select = "name"			/></td>
	<td><xsl:value-of select = "calories"		/></td>
	<td><xsl:value-of select = "format-number( price , '$#.00' )" /></td>
	</tr>
	</xsl:if>
	</xsl:for-each>

</table>

<br /><a href = "/cgi" >return</a>
<br /><br /></center></div>

</xsl:template>

</xsl:stylesheet>
