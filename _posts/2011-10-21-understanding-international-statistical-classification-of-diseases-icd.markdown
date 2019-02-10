---
author: vitraag
comments: true
date: 2011-10-21 17:29:18+00:00
layout: post
link: https://vitraagblog.wordpress.com/2011/10/21/understanding-international-statistical-classification-of-diseases-icd/
slug: understanding-international-statistical-classification-of-diseases-icd
title: Understanding International Statistical Classification of Diseases (ICD)
wordpress_id: 361
categories:
- Vocabularies
---

This a next installment of the Understanding terminologies [series](http://healthblog.vitraag.com/topics/vocabularies/).

I’ll try to keep this post short, give a general overview of International Statistical classification of Disease (ICD), talk a little about ICD-9 & ICD-10 and leave your folks will links to practical advise on converting from ICD-9 to ICD-10, and SNOMED-CT to ICD-10.

**<!-- more -->What is ICD?**

Attempts to classify diseases started in 17th century. The prime driver of this classification was to gather statistics around cause of death could across countries. Over 19th century the list of international diseases rapidly versioned, the sixth version was published in 1946, ninth in 1975 and 10th in 1990! The revision 9th and 10th are most common and referred as ICD-9 and ICD-10 respectively.

Overtime many countries started using ICD codes for insurance re-imbursements with a slight modification (clinical modification - CM), and that is a prime reason why these code have become so prominent in the Health-IT industry.

The ICD code is an alpha-numeric code which tracks a diagnosis, symptoms and cause of death.

**So what’s ICD-9-CM, ICD-10-CM?**

**ICD-9-CM **stands for the 9th revision of ICD with clinical modifications. This is most prevalent code used in the US healthcare industry for insurance re-imbursements. Following are few examples of how this code looks -
<table cellpadding="2" cellspacing="0" border="1" width="686" >
<tbody >
<tr >

<td width="133" valign="top" >**Code**
</td>

<td width="284" valign="top" >**Long Description**
</td>

<td width="267" valign="top" >**Short Desc**
</td>
</tr>
<tr >

<td width="133" valign="top" >_001.0_
</td>

<td width="284" valign="top" >Cholera; due to Vibrio cholerae
</td>

<td width="267" valign="top" >CHOLERA D/T VIB CHOLERAE
</td>
</tr>
<tr >

<td width="133" valign="top" >_01.15_
</td>

<td width="284" valign="top" >Biopsy of skull__
</td>

<td width="267" valign="top" >Skull biopsy
</td>
</tr>
</tbody>
</table>
Fig 1. ICD-9-CM codes

Note the format. **AAA.BB**. AAA stands for category and BB stands for etiology, anatomical site or manifestation.

**ICD-10-CM **is the 10th revision of ICD with clinical manifestation. All the US hospitals are mandated to use these code, starting 2013 only these codes will be re-imbursed by the payers / insurance providers. Following are few examples of how this code looks -
<table cellpadding="2" cellspacing="0" border="1" width="686" >
<tbody >
<tr >

<td width="133" valign="top" >**Code**
</td>

<td width="284" valign="top" >**Long Description**
</td>

<td width="267" valign="top" >**Short Desc**
</td>
</tr>
<tr >

<td width="133" valign="top" >_A00.0_
</td>

<td width="284" valign="top" >Cholera; due to Vibrio cholerae
</td>

<td width="267" valign="top" >CHOLERA D/T VIB CHOLERAE
</td>
</tr>
<tr >

<td width="133" valign="top" >_S61.011A_
</td>

<td width="284" valign="top" >Laceration without FB, Right__
</td>

<td width="267" valign="top" >Laceration w/o FB, Rt
</td>
</tr>
</tbody>
</table>
Fig 2. ICD-10-CM codes

Note ICD-10 is of the format – **ZAA.BBBC**

Z is supposed to Alphabetic. AA are numeric. Together ZAA make the category.
BBB is alpha-numeric and together they make etiology, anatomical site or manifestation
C is stands for code revision or extension

**How do I convert from ICD-9 to ICD-10? **

Shahid has a very good [blog-post](http://www.healthcareguy.com/2011/10/17/guest-article-actionable-advice-on-how-to-make-tangible-progress-in-icd-9-to-icd-10-migration/?utm_source=feedburner&utm_medium=feed&utm_campaign=Feed%3A+HealthcareGuy+%28The+Healthcare+IT+Guy%29) on practical advise for converting ICD-9 to ICD-10.

Following are interesting tools for the conversion -

1. ICD-9 data converter - [http://www.icd10data.com/Convert](http://www.icd10data.com/Convert)
2. Who online training - [http://apps.who.int/classifications/apps/icd/ICD10Training/](http://apps.who.int/classifications/apps/icd/ICD10Training/)

**And what about mapping ICD-10 to SNOMED-CT?**

As you have noticed ICD is more simplistic than SNOMED, rightfully since its original intent was to help with cause of death statistics. Overtime the ICD codes have been used in billing and increasing they have gotten specialized that they need to represent the diseases accurately. Naturally they have moving closer towards [SNOMED-CT](http://healthblog.vitraag.com/2009/10/understanding-snomed-ct/).

WHO has a [preview release](http://www.who.int/classifications/icd/snomedCTToICD10Maps/en/index.html) mapping some SNOMED-CT codes to ICD-10-CM.
