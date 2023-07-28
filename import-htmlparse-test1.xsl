<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
  version="3.0"
  xmlns:xs="http://www.w3.org/2001/XMLSchema"
  xmlns:dc="data:,dpc"
  exclude-result-prefixes="#all"
  expand-text="yes">

  <xsl:param name="json-uri" as="xs:string" select="'input-sample1.json'"/>

  <xsl:import href="htmlparse.xsl"/>

  <xsl:output indent="yes" />

  <xsl:template name="xsl:initial-template">
    <xsl:apply-templates select="json-doc($json-uri)"/>
  </xsl:template>

  <xsl:template match=".">
    <Root>
      <process>{?process}</process>
      <title>{?title}</title>
      <content>
        <xsl:sequence select="dc:htmlparse(?content, '', true())" />
      </content>
    </Root>
  </xsl:template>

</xsl:stylesheet>