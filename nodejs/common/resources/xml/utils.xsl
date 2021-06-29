<?xml version = "1.0" ?>
<xsl:stylesheet version = "1.0" xmlns:xsl = "http://www.w3.org/1999/XSL/Transform">

<!-- CODESLING ( notice charsOld and charsNew must be inserted inside apostrophes ) -->
<xsl:template name = "replacer">
	<xsl:param name = "text" />
	<xsl:param name = "charsOld" />
	<xsl:param name = "charsNew" />
	<xsl:choose>
	<xsl:when test = "contains( $text , $charsOld )">
		<xsl:value-of select = "substring-before( $text , $charsOld )" />
		<xsl:value-of select = "$charsNew" />
		<xsl:call-template name = "replacer">
		<xsl:with-param name = "text" select = "substring-after( $text , $charsOld )" />
		<xsl:with-param name = "charsOld" select = "$charsOld" />
		<xsl:with-param name = "charsNew" select = "$charsNew" />
		</xsl:call-template>
	</xsl:when>
	<xsl:otherwise>
		<xsl:value-of select = "$text" />
	</xsl:otherwise>
	</xsl:choose>
</xsl:template>

<!-- xsl:value-of select = "$textNew" disable-output-escaping = "yes" /-->
<!-- xsl:with-param name = "charsNew" select = "'&lt;li /&gt;'" /-->
<!-- xsl:value-of select = "substring-before( //ACIC_ChoicePointCreditReport , '0000' )" /-->
<!-- xsl:value-of select = "substring-after( //ACIC_ChoicePointCreditReport , '0000' )" /-->
<!-- xsl:value-of select = "replace( //ACIC_ChoicePointCreditReport , '0000' , '&lt ;br /&gt ;' )" disable-output-escaping = "yes" /-->
<!-- xsl:value-of select = "translate( //ACIC_ChoicePointCreditReport , '0000' , 'q' )" /-->

</xsl:stylesheet>
