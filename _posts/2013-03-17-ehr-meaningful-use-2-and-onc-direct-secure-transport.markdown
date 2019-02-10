---
author: vitraag
comments: true
date: 2013-03-17 03:47:42+00:00
layout: post
link: https://vitraagblog.wordpress.com/2013/03/16/ehr-meaningful-use-2-and-onc-direct-secure-transport/
slug: ehr-meaningful-use-2-and-onc-direct-secure-transport
title: EHR Meaningful Use 2 and ONC Direct Secure Transport
wordpress_id: 398
categories:
- HealthIT
---

This is a series of blog posts touching on a few pertinent curiosities from HIMSS 2013.

**Meaningful Use 2** mandates Electronic Health Records to support secure health transport to specifically fulfill the following measures:



	
  * Measure #1: Providers should send a summary of care for more than 50% transitions of care and referrals.

	
  * Measure #2: Providers should **electronically** transmit summary of care for than 10% transitions of care and referrals.

	
  * Measure #3: At least one summary of care document sent electronically should be to a recipient with a different EHR vendor or to CMS test EHR.


<!-- more -->Above construct very clearly mandates EHR vendors (AllScripts, EPIC, eClinicalWorks etc.) to support a standards based mechanism to allow transitions of care and referrals electronically.

The certification of Meaning Use 2, specifies the following technologies to fulfill above requirements:

	
  1. **Document Type:** C-CDA document with requisite data specified for MU. The data elements are detailed by siframework [here](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=2&cad=rja&ved=0CFEQFjAB&url=http%3A%2F%2Fwiki.siframework.org%2Ffile%2Fview%2FCCDA_MU2_mapping_V18.xls&ei=9DNFUaniLMrGqgG104GgCQ&usg=AFQjCNHlZW_nckl4ZBtOyzYY8w0E_UlB4Q&sig2=WkjgSrGuvhk6Iwy-Fx5IIA), and constitute things like patient demographics, allergies, vital signs, lab tests, referrals or transitions, care team, preferred language, smoking status, problems, encounter diagnoses, procedures, medications, inpatient-info if applicable etc. As you walk through this list, it turns out to be pretty thorough and useful!

	
  2. **Document Transport**:

	
    1. Direct : Following are specified options for Direct

	
      * Option A: Direct (required) : This is Direct built in to the EHR.

	
      * Option B: Direct + XDR/ XDM (optional, but not alternative)

	
      * Option C: SOAP + XDR / XDM (optional, but not alternative)




	
    2. NwHIN Exchange: The documents can be transferred as part of Nationwide Health Information Network using the associated eHealth Exchange. The regulations for this are not established.





Under the [transport guidance](http://www.nationalehealth.org/ckfinder/userfiles/files/Helping%20Providers%20Meet%20Direct%20Requirements%20for%20Meaningful%20Use%20Stage%202.pdf) from ONC – Direct is required to be part of EHR application to be certified for meaningful use. There are really two options for EHR vendors and these were discussed at length in an EHRA ([http://www.himssehra.org/](http://www.himssehra.org/)) meeting I attended during the HIMSS conference. The options are detailed in a [document](http://www.himssehra.org/docs/EHRAStage2SecureHealthTransportCertificationandMeaningfulUse.pdf) released by the association, and following is my summary on what an EHR should do:



	
  1. Provide a robust C-CDA and have ONC Direct as part of the application (this is equivalent to Option A). The downside of this is that the EHR has to implement all the technology like certificate management, SMTP gateways, direct address management as part of the offering. I’m not aware of many (except a couple of big ones) going this route.

	
  2. Partner with a HISP to do meaningful use certification by implementing a XDR capability in the EHR (this is equivalent to Option B). EHR vendor would generate robust C-CDA or perhaps they can use services of some value added HISPs to generate these C-CDA. The downside of this approach is that the EHR vendor has to collaborate with the HISP on Direct user management however the upside its that with a standard interface (XDR/XDM) they are not tied to one HISP solution vendor. However, for certification EHR vendor do need to work with a HISP to show that they can satisfy meaningful use measures but during deployment, they can pick any HISP which provides the API capability.


There is even a third option (not discussed by EHRA) where the EHR vendors can have a custom interface with the HISP or perhaps just so a secure SMTP to the HISP and certify together with the HISP for meaningful use. This is a bit unfavorable for the EHR vendors as they locked in the HISP partnership but it also allows them time to build substantial technologies like XDR/XDM interfaces or being able to generate first-class C-CDA documents.

Thoughts or comments? As usual, use the space below.


###### Resources:





	
  * EHR Vendors Association: [http://www.himssehra.org/](http://www.himssehra.org/)

	
  * Guidance on Meaning Use 2 Secure Transport from EHRA: [Link](http://www.himssehra.org/docs/EHRAStage2SecureHealthTransportCertificationandMeaningfulUse.pdf)

	
  * ONC EHR guidance: [Link](http://www.nationalehealth.org/ckfinder/userfiles/files/Helping%20Providers%20Meet%20Direct%20Requirements%20for%20Meaningful%20Use%20Stage%202.pdf)

	
  * NwHIN Exchange specifications: [http://exchange-specifications.wikispaces.com/](http://exchange-specifications.wikispaces.com/)


