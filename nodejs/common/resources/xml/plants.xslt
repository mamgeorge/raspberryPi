<?xml version = "1.0" encoding = "UTF-8"?>
<xsl:stylesheet version = "1.0" xmlns:xsl = "http://www.w3.org/1999/XSL/Transform">
<xsl:output method = "html" encoding = "UTF-8" indent = "yes" omit-xml-declaration = "yes" />
<!-- F:\servers\nodejs\public\resources\plants.xslt -->

<xsl:template match = "/">

<link type = "text/css" rel = "StyleSheet" href = "styleAny.css" />
<!--script type = "text/javascript" src = "temp.js" >&#160;</script-->

<div><center><br /><h3>plants</h3>

<table border = "1" cellspacing = "0">
<tr>
	<th>common</th>
	<th>botanical</th>
	<th>price</th>
	</tr>

<xsl:for-each select = "catalog/plant" >
<xsl:sort select = "common" />
<xsl:if test = "price &gt; 7.00">
<tr>
	<td><xsl:value-of select = "common"		/></td>
	<td><xsl:value-of select = "botanical"	/></td>
	<td><xsl:value-of select = "format-number( price , '$0.00' )" /></td>
	</tr>
	</xsl:if>
	</xsl:for-each>

</table>

<br /><a href = "/cgi" >return</a>
<br /><br /></center></div>

</xsl:template>

</xsl:stylesheet>
