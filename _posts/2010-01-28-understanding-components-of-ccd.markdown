---
author: vitraag
comments: true
date: 2010-01-28 01:52:35+00:00
layout: post
link: https://vitraagblog.wordpress.com/2010/01/27/understanding-components-of-ccd/
slug: understanding-components-of-ccd
title: Understanding Components of CCD
wordpress_id: 250
categories:
- Vocabularies
---

Connectivity of Care Document (CCD) is a collaborative standard driven by HL7 & ASTM for exchanging **summary format **clinical information.

 

For ease of understanding one can think of CCD standard comprising of several elements in an hierarchical fashion: 

 

  
  1. HL7 V3 Data Types and Reference Information Model (RIM) : At the base of CCD standard are the HL7 [Data types](http://www.hl7.org/v3ballot2009JAN/html/help/v3guide/v3guide.htm#v3gdt) and [Reference Information Model](http://www.hl7.org/v3ballot2009JAN/html/infrastructure/rim/rim.htm#). HL7 V3 data types define the structural format of the data carried. The HL7 RIM expresses the information content of work done by HL7 working committee to define data types, relationships between them, and a state transition model for some entities.
   
  2. Clinical Document Architecture (CDA): The [HL7 CDA](http://www.hl7.org/v3ballot2009JAN/html/infrastructure/cda/cda.htm#What_is_the_CDA) defines the specific structure and semantics for any clinical document for purposes of exchange. CDA document can be encoded in XML. A CDA document if encoded in XML must comply to the schema. NIST has a good CDA validation [tool](http://xreg2.nist.gov/cda-validation/validation.html).
   
  3. CCD Implementation Guide: The CCD implementation guide describes the constraints on the HL7 Clinical Document Architecture R2 specification in accordance with requirements set forward by ASTM (the governing body behind CCR).
 

[![image]({{site.images}}/2010/01/image_thumb.png)]({{site.images}}/2010/01/image.png)

 

Fig 1. Components of CCD Standard

 

 

 

Related articles in this series :

 

  
  1. [Understanding Vocabularies. Wait! What did you say?](http://healthblog.vitraag.com/2009/04/understanding-vocabularies-wait-what-did-you-say/)
   
  2. [Understanding Vocabularies #2 – HealthVault Recommendations](http://healthblog.vitraag.com/2009/07/understanding-vocabularies-2-healthvault-recommendations/)
   
  3. [Understanding SNOMED CT](http://healthblog.vitraag.com/2009/10/understanding-snomed-ct/)
   
  4. [Understanding CCR](http://healthblog.vitraag.com/2009/10/understanding-ccr/)
