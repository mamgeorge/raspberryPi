<?xml version = "1.0" encoding = "UTF-8"?>
<xsl:stylesheet version = "1.0" xmlns:xsl = "http://www.w3.org/1999/XSL/Transform" >
<xsl:output method = "html" encoding = "UTF-8" indent = "yes" omit-xml-declaration = "yes" />
<!-- http://stackoverflow.com/questions/2863422/how-to-format-the-date-in-xslt -->

<xsl:template match = "/">

<link type = "text/css" rel = "StyleSheet" href = "styleAny.css" />
<style>
.turn {
	padding: 0; margin: 0px; border: 1px; width: 100px; height: 20px;
	-ms-transform: rotate( -90deg ) ; /* IE 9 */
	-webkit-transform: rotate( -90deg ) ; /* Chrome , Safari , Opera */
	transform: rotate( -90deg ) ;
 }
</style>
<script type = "text/javascript" src = "temp.js" >&#160;</script>

<div><center><br /><h3 onclick = "collapser( )" >books</h3>

<table id = "books" border = "1" cellspacing = "0" width = "80%">
<tr><th class = "turn" >title</th>
	<th class = "turn" >genre</th>
	<th class = "turn" >price</th>
	<th>description<br /><br /><br /><br /><br /><br /><br /></th>
	</tr>

<xsl:for-each select = "catalog/book" >
<xsl:sort select = "genre" />
<xsl:if test = "price &gt; 0.00">
<tr>
	<td class = "turn" ><xsl:value-of select = "title" /></td>
	<td class = "turn" ><xsl:value-of select = "genre" /></td>
	<td class = "turn"><xsl:value-of select = "format-number( price , '$#.00' )" /></td>
	<td><xsl:value-of select = "description" /><br /><br /><br /><br /><br /><br /></td>
	</tr>
	</xsl:if>
	</xsl:for-each>
</table>

<br /><a href = "/cgi" >return</a>
<br /><br /></center></div>

</xsl:template>

</xsl:stylesheet>
