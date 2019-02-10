---
author: vitraag
comments: true
date: 2009-10-09 22:11:00+00:00
layout: post
link: https://vitraagblog.wordpress.com/2009/10/09/understanding-snomed-ct/
slug: understanding-snomed-ct
title: Understanding SNOMED CT
wordpress_id: 153
categories:
- HealthVault
- Vocabularies
---

I have [previously posted](http://www.vitraag.com/2009/07/understanding-vocabularies-2-healthvault-recommendations/) about Understanding Health Ontologies and Standards. In this post I’ll focus on SNOMED-CT ([Systematized Nomenclature of Medicine Clinical Terms](http://en.wikipedia.org/wiki/SNOMED_CT)). SNOMED-CT is the most comprehensive vocabulary to express clinical terms - it spans languages, specialties and geographic borders.

 

SNOMED-CT includes:

 

  
  * Terms or synonyms relating to a clinical concept 
   
  * Links between different concepts 
 

To give you a taste here is an example of Blood pressure reading represented using SNOMED-CT from the [linked](http://delivery.acm.org/10.1145/1280000/1273668/p69-ryan.pdf?key1=1273668&key2=3916594521&coll=GUIDE&dl=GUIDE&CFID=56633091&CFTOKEN=23055582) paper (_“Towards semantic interoperability in healthcare: ontology mapping from SNOMED-CT to [HL7](http://en.wikipedia.org/wiki/Health_Level_7) version 3”_, Amanda Ryan):

 

[![Ontology_Mapping]({{site.images}}/2009/10/Ontology_Mapping_thumb.png)]({{site.images}}/2009/10/Ontology_Mapping.png)

 

In addition to having a model to represent concepts and linkages the biggest draw of SNOMED CT is a staggering number of coded qualifiers (which belong to one concept or other). According to [IHTSO](http://www.ihtsdo.org/snomed-ct/snomed-ct0/) there are about 311,000 actively used SNOMED CT concepts.

 

You can register for SNOMED CT [here](http://wwwcf.nlm.nih.gov/umlslicense/snomed/license.cfm). Its free for companies and individuals in United States, however your registration is processed by NLM and it might take over 3 days to receive a confirmation and access.

 

Once you are through with registration and have an account, start by downloading the core subset of SNOMED CT concepts [here](http://download.nlm.nih.gov/umls/kss/SNOMEDCT_CORE_SUBSET/SNOMEDCT_CORE_SUBSET_200907.zip), this list consists of about 5000 most frequently used terms by institutions across US. Its a good set to get familiar with, it consists of the following concept area:

 

  
  * Clinical finding : 4,550 codes in total 
   
  * Procedure : 414 codes in total 
   
  * Situation with explicit context : 132 codes in total 
   
  * Event : 38 codes in total 
   
  * Body structure : 46 codes in total 
   
  * Social context : 2 codes in total
 

[![Snomed_Subset]({{site.images}}/2009/10/Snomed_Subset_thumb.png)]({{site.images}}/2009/10/Snomed_Subset.png)

 

We can use [BCP](http://msdn.microsoft.com/en-us/library/ms162802.aspx) to copy the files from SNOMED CT Core in to our local database, and do more interesting queries & data analysis like find distribution on these terms, co-relate problems vs. findings and of course work on the larger SNOMED CT database to find synonyms etc.; but I’ll keep that for another day. Here very quickly I’ll show how one can use a web-based browser, Snowflake, [http://snomed.dataline.co.uk/](http://snomed.dataline.co.uk/) (requires registration) to lookup a SNOMED code and see what else it relates to. We can see that in line 3 above SNOMED CT concept 10085004 is marked as Metatarsalgia (finding), however using the Snowflake browser we can see in that in addition to being a finding this concept is a problem as well.

 

[![Snomed_Snowflake]({{site.images}}/2009/10/Snomed_Snowflake_thumb.png)]({{site.images}}/2009/10/Snomed_Snowflake.png)

 

This was just tip of the ice-berg, please leave comments for future posts / areas to consider in the Ontology domain.

 

Further reading / relevant links:

 

  
  * LexGrid: [Wiki](https://cabig-kc.nci.nih.gov/Vocab/KC/index.php?title=LexGrid_Resources&amp;diff=5039&amp;oldid=prev)
 

In this series:

 

  
  1. [Understanding Vocabularies. Wait! What did you say?](http://healthblog.vitraag.com/2009/04/understanding-vocabularies-wait-what-did-you-say/)
   
  2. [Understanding Vocabularies #2 – HealthVault Recommendations](http://healthblog.vitraag.com/2009/07/understanding-vocabularies-2-healthvault-recommendations/)
   
  3. [Understanding SNOMED CT](http://healthblog.vitraag.com/2009/10/understanding-snomed-ct/)
 
