---
author: vitraag
comments: true
date: 2009-10-27 22:27:50+00:00
layout: post
link: https://vitraagblog.wordpress.com/2009/10/27/understanding-ccr/
slug: understanding-ccr
title: Understanding CCR
wordpress_id: 204
categories:
- HealthVault
- Vocabularies
---

CCR or Continuity of Care Record is a standard meant to ease the exchange of clinical information with a relatively easy to read and practical data-format and schema. There is ton of great information about CCR on its [resource site](http://www.ccrstandard.com/). CCR document format is supported by majority of personal Health clouds, both - Microsoft HealthVault & Google Health.

The CCR specification comprises an implementation guide, XML schema definition and a guidance spreadsheet for each data element that makes up the standard. These resources can be [bought](http://www.astm.org/Standards/E2369.htm) from ASTM. 

The document format of CCR is very straight forward, consisting of a header, body and a footer with the following top-level elements:

<table cellpadding="1" cellspacing="0" border="1px" width="602" > <tbody > <tr >
<td width="200" valign="top" >**Header**
</td>
<td width="178" valign="top" >**Body**
</td>
<td width="155" valign="top" >**Body**
</td>
<td width="67" valign="top" >**Footer**
</td> </tr> <tr >
<td width="200" valign="top" >
<pre>
* CCR Document ID 
* Language 
* Version 
* Creation Date 
* Patient 
* From 
* To 
* Purpose 
</pre>
</td>
<td width="178" valign="top" >
<pre>
* Payers 
* Advance Directives 
* Support 
* Functional Status 
* Problems 
* Family History 
* Social History 
* Alerts 
* Medications 
</pre>
</td>
<td width="155" valign="top" >
<pre>
* Medical Equipment 
* Immunizations 
* Vital Signs 
* Results 
* Procedures 
* Encounters 
* Plan Of Care 
* HealthCareProviders 
</pre>
</td>
<td width="67" valign="top" >
<pre>
* Actors 
* Signatures 
* References 
* Comments ****
</pre>
</td> </tr> </tbody> </table>

Google Health supports only a [limited set of entities](http://code.google.com/apis/health/ccrg_imagemap.gif) from the above, while HealthVault supports the entire standard and also allows transformation of some of these entities in to native HealthVault types. You can read more about working with [CCR in HealthVault](http://msdn.microsoft.com/en-us/dd797577.aspx) and various [input](http://msdn.microsoft.com/en-us/ee663895.aspx) [mappings](http://msdn.microsoft.com/en-us/ee663894.aspx), [output](http://msdn.microsoft.com/en-us/ee663897.aspx) [mappings](http://msdn.microsoft.com/en-us/ee663896.aspx), and [CCR vocabularies](http://msdn.microsoft.com/en-us/ee663898.aspx).

Here are some illustrative CCR figures from Dr. Waldren’s presentation (see end of article). *Update 2019* no longer available.
<!-- [![image]({{site.images}}/2009/10/image7_thumb.png)]({{site.images}}/2009/10/image7.png) [![image]({{site.images}}/2009/10/image5_thumb.png)]({{site.images}}/2009/10/image8.png)-->

Using the SNOMED-CT concepts one can write the Systolic Blood pressure reading in CCR as the following (**UPDATE**: Well-formatted the CCR to include source, object-id and actors, thanks to Matt Wagner):

<span>
    <font size="2"><span style="color:blue;"><?</span><span style="color:#a31515;">xml </span><span style="color:red;">version</span><span style="color:blue;">=</span>"<span style="color:blue;">1.0</span>" <span style="color:red;">encoding</span><span style="color:blue;">=</span>"<span style="color:blue;">utf-8</span>"</font><font size="2"><span style="color:blue;">?> <</span><span style="color:#a31515;">ContinuityOfCareRecord </span><span style="color:red;">xmlns</span><span style="color:blue;">=</span>'<span style="color:blue;">urn:astm-org:CCR</span>'</font><font size="2"><span style="color:blue;">> <</span><span style="color:#a31515;">CCRDocumentObjectID</span><span style="color:blue;">></span>Doc<span style="color:blue;"></</span><span style="color:#a31515;">CCRDocumentObjectID</span></font><font size="2"><span style="color:blue;">> <</span><span style="color:#a31515;">Language</span></font><font size="2"><span style="color:blue;">> <</span><span style="color:#a31515;">Text</span><span style="color:blue;">></span>English<span style="color:blue;"></</span><span style="color:#a31515;">Text</span></font><font size="2"><span style="color:blue;">> </</span><span style="color:#a31515;">Language</span></font><font size="2"><span style="color:blue;">> <</span><span style="color:#a31515;">Version</span><span style="color:blue;">></span>V1.0<span style="color:blue;"></</span><span style="color:#a31515;">Version</span></font><font size="2"><span style="color:blue;">> <</span><span style="color:#a31515;">DateTime</span></font><font size="2"><span style="color:blue;">> <</span><span style="color:#a31515;">ExactDateTime</span><span style="color:blue;">></span>2008<span style="color:blue;"></</span><span style="color:#a31515;">ExactDateTime</span></font><font size="2"><span style="color:blue;">> </</span><span style="color:#a31515;">DateTime</span></font><font size="2"><span style="color:blue;">> <</span><span style="color:#a31515;">Patient</span></font><font size="2"><span style="color:blue;">> <</span><span style="color:#a31515;">ActorID</span><span style="color:blue;">></span>Patient<span style="color:blue;"></</span><span style="color:#a31515;">ActorID</span></font><font size="2"><span style="color:blue;">> </</span><span style="color:#a31515;">Patient</span></font><font size="2"><span style="color:blue;">> <</span><span style="color:#a31515;">Body</span></font><font size="2"><span style="color:blue;">> <</span><span style="color:#a31515;">VitalSigns</span></font><font size="2"><span style="color:blue;">> <</span><span style="color:#a31515;">Result</span></font><font size="2"><span style="color:blue;">> <</span><span style="color:#a31515;">CCRDataObjectID</span><span style="color:blue;">></span>0001<span style="color:blue;"></</span><span style="color:#a31515;">CCRDataObjectID</span></font><font size="2"><span style="color:blue;">> <</span><span style="color:#a31515;">Description</span></font><font size="2"><span style="color:blue;">> <</span><span style="color:#a31515;">Text</span><span style="color:blue;">></span>Blood Pressure<span style="color:blue;"></</span><span style="color:#a31515;">Text</span></font><font size="2"><span style="color:blue;">> </</span><span style="color:#a31515;">Description</span></font><font size="2"><span style="color:blue;">> <</span><span style="color:#a31515;">Source</span></font><font size="2"><span style="color:blue;">> <</span><span style="color:#a31515;">Description</span></font><font size="2"><span style="color:blue;">> <</span><span style="color:#a31515;">Text</span><span style="color:blue;">></span>Unknown<span style="color:blue;"></</span><span style="color:#a31515;">Text</span></font><font size="2"><span style="color:blue;">> </</span><span style="color:#a31515;">Description</span></font><font size="2"><span style="color:blue;">> </</span><span style="color:#a31515;">Source</span></font><font size="2"><span style="color:blue;">> <</span><span style="color:#a31515;">Test</span></font><font size="2"><span style="color:blue;">> <</span><span style="color:#a31515;">CCRDataObjectID</span><span style="color:blue;">></span>0002<span style="color:blue;"></</span><span style="color:#a31515;">CCRDataObjectID</span></font><font size="2"><span style="color:blue;">> <</span><span style="color:#a31515;">Description</span></font><font size="2"><span style="color:blue;">> <</span><span style="color:#a31515;">Text</span><span style="color:blue;">></span>Systolic<span style="color:blue;"></</span><span style="color:#a31515;">Text</span></font><font size="2"><span style="color:blue;">> <</span><span style="color:#a31515;">Code</span></font><font size="2"><span style="color:blue;">> <</span><span style="color:#a31515;">Value</span><span style="color:blue;">></span>163030003<span style="color:blue;"></</span><span style="color:#a31515;">Value</span></font><font size="2"><span style="color:blue;">> <</span><span style="color:#a31515;">CodingSystem</span><span style="color:blue;">></span>SNOMEDCT<span style="color:blue;"></</span><span style="color:#a31515;">CodingSystem</span></font><font size="2"><span style="color:blue;">> </</span><span style="color:#a31515;">Code</span></font><font size="2"><span style="color:blue;">> </</span><span style="color:#a31515;">Description</span></font><font size="2"><span style="color:blue;">> <</span><span style="color:#a31515;">Source</span></font><font size="2"><span style="color:blue;">> <</span><span style="color:#a31515;">Description</span></font><font size="2"><span style="color:blue;">> <</span><span style="color:#a31515;">Text</span><span style="color:blue;">></span>Unknown<span style="color:blue;"></</span><span style="color:#a31515;">Text</span></font><font size="2"><span style="color:blue;">> </</span><span style="color:#a31515;">Description</span></font><font size="2"><span style="color:blue;">> </</span><span style="color:#a31515;">Source</span></font><font size="2"><span style="color:blue;">> <</span><span style="color:#a31515;">TestResult</span></font><font size="2"><span style="color:blue;">> <</span><span style="color:#a31515;">Value</span><span style="color:blue;">></span>120<span style="color:blue;"></</span><span style="color:#a31515;">Value</span></font><font size="2"><span style="color:blue;">> <</span><span style="color:#a31515;">Units</span></font><font size="2"><span style="color:blue;">> <</span><span style="color:#a31515;">Unit</span><span style="color:blue;">></span>mmHg<span style="color:blue;"></</span><span style="color:#a31515;">Unit</span></font><font size="2"><span style="color:blue;">> </</span><span style="color:#a31515;">Units</span></font><font size="2"><span style="color:blue;">> </</span><span style="color:#a31515;">TestResult</span></font><font size="2"><span style="color:blue;">> </</span><span style="color:#a31515;">Test</span></font><font size="2"><span style="color:blue;">> <</span><span style="color:#a31515;">Test</span></font><font size="2"><span style="color:blue;">> <</span><span style="color:#a31515;">CCRDataObjectID</span><span style="color:blue;">></span>0003<span style="color:blue;"></</span><span style="color:#a31515;">CCRDataObjectID</span></font><font size="2"><span style="color:blue;">> <</span><span style="color:#a31515;">Description</span></font><font size="2"><span style="color:blue;">> <</span><span style="color:#a31515;">Text</span><span style="color:blue;">></span>Diastolic<span style="color:blue;"></</span><span style="color:#a31515;">Text</span></font><font size="2"><span style="color:blue;">> <</span><span style="color:#a31515;">Code</span></font><font size="2"><span style="color:blue;">> <</span><span style="color:#a31515;">Value</span><span style="color:blue;">></span>163031004<span style="color:blue;"></</span><span style="color:#a31515;">Value</span></font><font size="2"><span style="color:blue;">> <</span><span style="color:#a31515;">CodingSystem</span><span style="color:blue;">></span>SNOMEDCT<span style="color:blue;"></</span><span style="color:#a31515;">CodingSystem</span></font><font size="2"><span style="color:blue;">> </</span><span style="color:#a31515;">Code</span></font><font size="2"><span style="color:blue;">> </</span><span style="color:#a31515;">Description</span></font><font size="2"><span style="color:blue;">> <</span><span style="color:#a31515;">Source</span></font><font size="2"><span style="color:blue;">> <</span><span style="color:#a31515;">Description</span></font><font size="2"><span style="color:blue;">> <</span><span style="color:#a31515;">Text</span><span style="color:blue;">></span>Unknown<span style="color:blue;"></</span><span style="color:#a31515;">Text</span></font><font size="2"><span style="color:blue;">> </</span><span style="color:#a31515;">Description</span></font><font size="2"><span style="color:blue;">> </</span><span style="color:#a31515;">Source</span></font><font size="2"><span style="color:blue;">> <</span><span style="color:#a31515;">TestResult</span></font><font size="2"><span style="color:blue;">> <</span><span style="color:#a31515;">Value</span><span style="color:blue;">></span>75<span style="color:blue;"></</span><span style="color:#a31515;">Value</span></font><font size="2"><span style="color:blue;">> <</span><span style="color:#a31515;">Units</span></font><font size="2"><span style="color:blue;">> <</span><span style="color:#a31515;">Unit</span><span style="color:blue;">></span>mmHg<span style="color:blue;"></</span><span style="color:#a31515;">Unit</span></font><font size="2"><span style="color:blue;">> </</span><span style="color:#a31515;">Units</span></font><font size="2"><span style="color:blue;">> </</span><span style="color:#a31515;">TestResult</span></font><font size="2"><span style="color:blue;">> </</span><span style="color:#a31515;">Test</span></font><font size="2"><span style="color:blue;">> </</span><span style="color:#a31515;">Result</span></font><font size="2"><span style="color:blue;">> </</span><span style="color:#a31515;">VitalSigns</span></font><font size="2"><span style="color:blue;">> </</span><span style="color:#a31515;">Body</span></font><font size="2"><span style="color:blue;">> <</span><span style="color:#a31515;">Actors</span></font><font size="2"><span style="color:blue;">> <</span><span style="color:#a31515;">Actor</span></font><font size="2"><span style="color:blue;">> <</span><span style="color:#a31515;">ActorObjectID</span><span style="color:blue;">></span>Patient<span style="color:blue;"></</span><span style="color:#a31515;">ActorObjectID</span></font><font size="2"><span style="color:blue;">> <</span><span style="color:#a31515;">Person</span></font><font size="2"><span style="color:blue;">> <</span><span style="color:#a31515;">Name</span></font><font size="2"><span style="color:blue;">> <</span><span style="color:#a31515;">CurrentName</span></font><font size="2"><span style="color:blue;">> <</span><span style="color:#a31515;">Given</span><span style="color:blue;">></span>John<span style="color:blue;"></</span><span style="color:#a31515;">Given</span></font><font size="2"><span style="color:blue;">> <</span><span style="color:#a31515;">Family</span><span style="color:blue;">></span>Doe<span style="color:blue;"></</span><span style="color:#a31515;">Family</span></font><font size="2"><span style="color:blue;">> </</span><span style="color:#a31515;">CurrentName</span></font><font size="2"><span style="color:blue;">> </</span><span style="color:#a31515;">Name</span></font><font size="2"><span style="color:blue;">> </</span><span style="color:#a31515;">Person</span></font><font size="2"><span style="color:blue;">> <</span><span style="color:#a31515;">Source</span></font><font size="2"><span style="color:blue;">> <</span><span style="color:#a31515;">Description</span></font><font size="2"><span style="color:blue;">> <</span><span style="color:#a31515;">Text</span><span style="color:blue;">></span>Unknown<span style="color:blue;"></</span><span style="color:#a31515;">Text</span></font><font size="2"><span style="color:blue;">> </</span><span style="color:#a31515;">Description</span></font><font size="2"><span style="color:blue;">> </</span><span style="color:#a31515;">Source</span></font><font size="2"><span style="color:blue;">> </</span><span style="color:#a31515;">Actor</span></font><font size="2"><span style="color:blue;">> </</span><span style="color:#a31515;">Actors</span></font><font size="2"><span style="color:blue;">> </</span><span style="color:#a31515;">ContinuityOfCareRecord</span></font><span style="color:blue;"><font size="2">></font> </span>
</span>

Note **CodingSystem** element. It allows CCR to interpret various medical vocabularies.

**Relevant Tools**:

(Thanks to Kathleen Connor)

  * The [CCR Validator](http://chit.dyndns.org/CCRValidation), is an important resource to test/validate a CCR instance, is a now available Not only does it validate the CCR against the XSD but also the constraints of the implementation guide. 
  * An Open Source [StyleSheet](http://sourceforge.net/projects/ccr-resources/) to view CCR files.
  * [CCR to CCD & HL7 Mappers](http://wiki.hl7.org/index.php?title=Mappings_and_Translations) – tools which Map CCR to CCD and HL7 V2 & V3. You can access them directly [here](http://gforge.hl7.org/gf/project/v2v3-mapping/frs/).
  * [Application](http://rubyforge.org/projects/ccredit/) to embed CCR in PDF-HealthCare.

**Related Article(s):**

  * To get familiar with CCR I would highly recommended [this](http://www.veoh.com/collection/astmccr/watch/v14141513WQRzgjzc) 13 minute video by Dr. Steve Waldren. 
  * Adam Bosworth [posted](http://adambosworth.net/2009/10/29/talking-to-dc/) an interesting read on standards, his take (simple, human readable, focus on known structured data, etc.) favors CCR.

**In this series:**

  1. [Understanding Vocabularies. Wait! What did you say?](/2009/04/understanding-vocabularies-wait-what-did-you-say/)
  2. [Understanding Vocabularies #2 – HealthVault Recommendations](/2009/07/understanding-vocabularies-2-healthvault-recommendations/)
  3. [Understanding SNOMED CT](/2009/10/understanding-snomed-ct/)
  4. [Understanding CCR](/2009/10/understanding-ccr/)

Special thanks to Kathy Osborne for proof reading this post.
