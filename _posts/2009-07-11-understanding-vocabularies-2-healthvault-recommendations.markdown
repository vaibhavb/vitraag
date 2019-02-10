---
author: vitraag
comments: true
date: 2009-07-11 01:46:50+00:00
layout: post
link: https://vitraagblog.wordpress.com/2009/07/10/understanding-vocabularies-2-healthvault-recommendations/
slug: understanding-vocabularies-2-healthvault-recommendations
title: 'Understanding Vocabularies #2 – HealthVault Recommendations'
wordpress_id: 132
categories:
- HealthVault
- Vocabularies
---

In my [last article](http://healthblog.vitraag.com/2009/04/understanding-vocabularies-wait-what-did-you-say/) in the vocabulary category, I described the need for semantically enabled data and how different categories of health data have different standard vocabulary / ontology associated with them. In the following table I attempt to summarize the recommended vocabularies for different HealthVault types. 

 

**Disclaimer:** Please note this is not a definitive or complete list, and I will update the table as I discover inconsistencies. The definitive source are the XSDs associated with [HealthVault data types](http://developer.healthvault.com/types/types.aspx).

 <table cellpadding="1" cellspacing="0" border="1" width="843" ><tbody >     <tr >       
<td width="157" valign="top" >**HealthVault Type**
</td>        
<td width="310" valign="top" >**Type Schema**
</td>        
<td width="194" valign="top" >**HV Recommended vocabulary related to this type**
</td>        
<td width="180" valign="top" >**Comments**
</td>     </tr>      <tr >       
<td width="158" valign="top" >Advance Directive
</td>        
<td width="310" valign="top" >[822a5e5a-14f1-4d06-b92f-8f3f1b05218f](http://developer.healthvault.com/types/type.aspx?id=822a5e5a-14f1-4d06-b92f-8f3f1b05218f)
</td>        
<td width="194" valign="top" >None
</td>        
<td width="180" valign="top" >         

Examples include living wills and [power of attorney](http://en.wikipedia.org/wiki/Power_of_attorney) for healthcare.

      
</td>     </tr>      <tr >       
<td width="159" valign="top" >Allergy
</td>        
<td width="310" valign="top" >[52bf9104-2c5e-4f1f-a66d-552ebcc53df7](http://developer.healthvault.com/types/type.aspx?id=52bf9104-2c5e-4f1f-a66d-552ebcc53df7)
</td>        
<td width="194" valign="top" >[icd9cm](http://developer.healthvault.com/types/vocab.aspx?name=icd9cm&family=icd&version=1.0), [icd9cm-reactions](http://developer.healthvault.com/types/vocab.aspx?name=icd9cm-reactions&family=icd&version=1.0)
</td>        
<td width="180" valign="top" >Details on [ICD-9 Codes](http://en.wikipedia.org/wiki/List_of_ICD-9_codes)
</td>     </tr>      <tr >       
<td width="160" valign="top" >Basic Demographic Information
</td>        
<td width="310" valign="top" >[bf516a61-5252-4c28-a979-27f45f62f78d](http://developer.healthvault.com/types/type.aspx?id=bf516a61-5252-4c28-a979-27f45f62f78d)
</td>        
<td width="194" valign="top" >[ISO-3166](http://developer.healthvault.com/types/vocab.aspx?name=iso3166&family=iso&version=1.0)
</td>        
<td width="180" valign="top" >Country of residence
</td>     </tr>      <tr >       
<td width="161" valign="top" >Blood Glucose Measurement
</td>        
<td width="310" valign="top" >         

[879e7c04-4e8a-4707-9ad3-b054df467ce4](http://developer.healthvault.com/types/type.aspx?id=879e7c04-4e8a-4707-9ad3-b054df467ce4)

      
</td>        
<td width="194" valign="top" >glucose-measurement-type
</td>        
<td width="180" valign="top" >
</td>     </tr>      <tr >       
<td width="161" valign="top" >Blood Oxygen Saturation
</td>        
<td width="310" valign="top" >         

[3a54f95f-03d8-4f62-815f-f691fc94a500](http://developer.healthvault.com/types/type.aspx?id=3a54f95f-03d8-4f62-815f-f691fc94a500)

      
</td>        
<td width="194" valign="top" >blood-oxygen-saturation-measurement-method
</td>        
<td width="180" valign="top" >
</td>     </tr>      <tr >       
<td width="161" valign="top" >Body Composition
</td>        
<td width="310" valign="top" >         

[18adc276-5144-4e7e-bf6c-e56d8250adf8](http://developer.healthvault.com/types/type.aspx?id=18adc276-5144-4e7e-bf6c-e56d8250adf8)

      
</td>        
<td width="194" valign="top" >body-composition-measurement-methods
</td>        
<td width="180" valign="top" >
</td>     </tr>      <tr >       
<td width="161" valign="top" >Body Dimension
</td>        
<td width="310" valign="top" >[dd710b31-2b6f-45bd-9552-253562b9a7c1](http://developer.healthvault.com/types/type.aspx?id=dd710b31-2b6f-45bd-9552-253562b9a7c1)
</td>        
<td width="194" valign="top" >body-dimension-measurement-names, body-dimension-measurement-names-pediatric
</td>        
<td width="180" valign="top" >
</td>     </tr>      <tr >       
<td width="161" valign="top" >Calorie Guideline
</td>        
<td width="310" valign="top" >         

[d3170d30-a41b-4bde-a116-87698c8a001a](http://developer.healthvault.com/types/type.aspx?id=d3170d30-a41b-4bde-a116-87698c8a001a)

      
</td>        
<td width="194" valign="top" >calorie-guideline-names
</td>        
<td width="180" valign="top" >
</td>     </tr>      <tr >       
<td width="161" valign="top" >Concern
</td>        
<td width="310" valign="top" >[aea2e8f2-11dd-4a7d-ab43-1d58764ebc19](http://developer.healthvault.com/types/type.aspx?id=aea2e8f2-11dd-4a7d-ab43-1d58764ebc19)
</td>        
<td width="194" valign="top" >concern-description
</td>        
<td width="180" valign="top" >Concerns are more general than conditions
</td>     </tr>      <tr >       
<td width="161" valign="top" >Condition
</td>        
<td width="310" valign="top" >[7ea7a1f9-880b-4bd4-b593-f5660f20eda8](http://developer.healthvault.com/types/type.aspx?id=7ea7a1f9-880b-4bd4-b593-f5660f20eda8)
</td>        
<td width="194" valign="top" >
</td>        
<td width="180" valign="top" >
</td>     </tr>      <tr >       
<td width="161" valign="top" >Continuity of Care Document ([CCD](http://en.wikipedia.org/wiki/Charge-coupled_device))
</td>        
<td width="310" valign="top" >         

[9c48a2b8-952c-4f5a-935d-f3292326bf54](http://developer.healthvault.com/types/type.aspx?id=9c48a2b8-952c-4f5a-935d-f3292326bf54)

      
</td>        
<td width="194" valign="top" >
</td>        
<td width="180" valign="top" >
</td>     </tr>      <tr >       
<td width="161" valign="top" >Continuity of Care Record ([CCR](http://en.wikipedia.org/wiki/Continuity_of_Care_Record))
</td>        
<td width="310" valign="top" >         

[1e1ccbfc-a55d-4d91-8940-fa2fbf73c195](http://developer.healthvault.com/types/type.aspx?id=1e1ccbfc-a55d-4d91-8940-fa2fbf73c195)

      
</td>        
<td width="194" valign="top" >
</td>        
<td width="180" valign="top" >[http://www.ccrstandard.com/](http://www.ccrstandard.com/)
</td>     </tr>      <tr >       
<td width="161" valign="top" >Daily Medication Usage
</td>        
<td width="310" valign="top" >[a9a76456-0357-493e-b840-598bbb9483fd](http://developer.healthvault.com/types/type.aspx?id=a9a76456-0357-493e-b840-598bbb9483fd)
</td>        
<td width="194" valign="top" >dose-purpose, usage-schedule, [x12-de-1330](http://developer.healthvault.com/types/vocab.aspx?name=x12-de-1330&family=x12-de&version=1.0), prescription-type, [x12-d3-355](http://developer.healthvault.com/types/vocab.aspx?name=x12-de-355&family=x12-de&version=1.0), 
</td>        
<td width="180" valign="top" >
</td>     </tr>      <tr >       
<td width="161" valign="top" >Diabetes Insulin Injection Use
</td>        
<td width="310" valign="top" >         

[184166be-8adb-4d9c-8162-c403040e31ad](http://developer.healthvault.com/types/type.aspx?id=184166be-8adb-4d9c-8162-c403040e31ad)

      
</td>        
<td width="194" valign="top" >insulin-types, 
</td>        
<td width="180" valign="top" >
</td>     </tr>      <tr >       
<td width="161" valign="top" >Discharge Summary
</td>        
<td width="310" valign="top" >         

[02ef57a2-a620-425a-8e92-a301542cca54](http://developer.healthvault.com/types/type.aspx?id=02ef57a2-a620-425a-8e92-a301542cca54)

      
</td>        
<td width="194" valign="top" >icd9cm
</td>        
<td width="180" valign="top" >
</td>     </tr>      <tr >       
<td width="161" valign="top" >HbA1C Measurement
</td>        
<td width="310" valign="top" >         

[227f55fb-1001-4d4e-9f6a-8d893e07b451](http://developer.healthvault.com/types/type.aspx?id=227f55fb-1001-4d4e-9f6a-8d893e07b451)

      
</td>        
<td width="194" valign="top" >HbA1C-assay-method
</td>        
<td width="180" valign="top" >
</td>     </tr>      <tr >       
<td width="161" valign="top" >Health Assessment
</td>        
<td width="310" valign="top" >         

[58fd8ac4-6c47-41a3-94b2-478401f0e26c](http://developer.healthvault.com/types/type.aspx?id=58fd8ac4-6c47-41a3-94b2-478401f0e26c)

      
</td>        
<td width="194" valign="top" >health-assessment-name, health-assessment-value-sets, health-assessment-groups, health-assessment-category
</td>        
<td width="180" valign="top" >
</td>     </tr>      <tr >       
<td width="161" valign="top" >Heart Rate
</td>        
<td width="310" valign="top" >[b81eb4a6-6eac-4292-ae93-3872d6870994](http://developer.healthvault.com/types/type.aspx?id=b81eb4a6-6eac-4292-ae93-3872d6870994)
</td>        
<td width="194" valign="top" >heart-rate-measurement-conditions
</td>        
<td width="180" valign="top" >
</td>     </tr>      <tr >       
<td width="161" valign="top" >HL7 Clinical Document Architecture, Release 2
</td>        
<td width="310" valign="top" >         

[1ed1cba6-9530-44a3-b7b5-e8219690ebcf](http://developer.healthvault.com/types/type.aspx?id=1ed1cba6-9530-44a3-b7b5-e8219690ebcf)

      
</td>        
<td width="194" valign="top" >
</td>        
<td width="180" valign="top" >
</td>     </tr>      <tr >       
<td width="161" valign="top" >Immunization
</td>        
<td width="310" valign="top" >         

[cd3587b5-b6e1-4565-ab3b-1c3ad45eb04f](http://developer.healthvault.com/types/type.aspx?id=cd3587b5-b6e1-4565-ab3b-1c3ad45eb04f)

      
</td>        
<td width="194" valign="top" >[vaccines-cvx](http://developer.healthvault.com/types/vocab.aspx?name=vaccines-cvx&family=HL7&version=2.3%2009_2008), vaccine-manufacturers-mvx, medication-routes, 
</td>        
<td width="180" valign="top" >
</td>     </tr>      <tr >       
<td width="161" valign="top" >Insulin Injection
</td>        
<td width="310" valign="top" >         

[3b3c053b-b1fe-4e11-9e22-d4b480de74e8](http://developer.healthvault.com/types/type.aspx?id=3b3c053b-b1fe-4e11-9e22-d4b480de74e8)

      
</td>        
<td width="194" valign="top" >insulin-types
</td>        
<td width="180" valign="top" >
</td>     </tr>      <tr >       
<td width="161" valign="top" >Insurance Plan
</td>        
<td width="310" valign="top" >         

[9366440c-ec81-4b89-b231-308a4c4d70ed](http://developer.healthvault.com/types/type.aspx?id=9366440c-ec81-4b89-b231-308a4c4d70ed)

      
</td>        
<td width="194" valign="top" >coverage-types
</td>        
<td width="180" valign="top" >
</td>     </tr>      <tr >       
<td width="161" valign="top" >Lab Test Results
</td>        
<td width="310" valign="top" >         

[f57746af-9631-49dc-944e-2c92bee0d1e9](http://developer.healthvault.com/types/type.aspx?id=f57746af-9631-49dc-944e-2c92bee0d1e9)

      
</td>        
<td width="194" valign="top" >[LOINC](http://developer.healthvault.com/types/vocab.aspx?name=LOINC&family=regenstrief&version=2.26), lab-status, lab-results-flag, 
</td>        
<td width="180" valign="top" >More on LOINC [here](http://en.wikipedia.org/wiki/LOINC).
</td>     </tr>      <tr >       
<td width="161" valign="top" >Medication
</td>        
<td width="310" valign="top" >[30cafccc-047d-4288-94ef-643571f7919d](http://developer.healthvault.com/types/type.aspx?id=30cafccc-047d-4288-94ef-643571f7919d)
</td>        
<td width="194" valign="top" >[Rxnorm](http://developer.healthvault.com/types/vocab.aspx?name=RxNorm%20Active%20Ingredients&family=RxNorm&version=07AC_080303F), NDC, medication-prescribed
</td>        
<td width="180" valign="top" >
</td>     </tr>      <tr >       
<td width="161" valign="top" >Medication Fill
</td>        
<td width="310" valign="top" >         

[167ecf6b-bb54-43f9-a473-507b334907e0](http://developer.healthvault.com/types/type.aspx?id=167ecf6b-bb54-43f9-a473-507b334907e0)

      
</td>        
<td width="194" valign="top" >[Rxnorm](http://developer.healthvault.com/types/vocab.aspx?name=RxNorm%20Active%20Ingredients&family=RxNorm&version=07AC_080303F), NDC
</td>        
<td width="180" valign="top" >
</td>     </tr>      <tr >       
<td width="161" valign="top" >Personal Demographic Information
</td>        
<td width="310" valign="top" >         

[92ba621e-66b3-4a01-bd73-74844aed4f5b](http://developer.healthvault.com/types/type.aspx?id=92ba621e-66b3-4a01-bd73-74844aed4f5b)

      
</td>        
<td width="194" valign="top" >blood-types, ethnicity, marital-status, religion, education-level, 
</td>        
<td width="180" valign="top" >
</td>     </tr>      <tr >       
<td width="161" valign="top" >Pregnancy
</td>        
<td width="310" valign="top" >[46d485cf-2b84-429d-9159-83152ba801f4](http://developer.healthvault.com/types/type.aspx?id=46d485cf-2b84-429d-9159-83152ba801f4)
</td>        
<td width="194" valign="top" >delivery-complications, anesthesia-methods, delivery-methods, pregnancy-outcomes, gender-types, conception-methods, 
</td>        
<td width="180" valign="top" >
</td>     </tr>      <tr >       
<td width="161" valign="top" >Question Answer
</td>        
<td width="310" valign="top" >[55d33791-58de-4cae-8c78-819e12ba5059](http://developer.healthvault.com/types/type.aspx?id=55d33791-58de-4cae-8c78-819e12ba5059)
</td>        
<td width="194" valign="top" >question-sets, answer-choice-sets
</td>        
<td width="180" valign="top" >
</td>     </tr>      <tr >       
<td width="161" valign="top" >Sleep Related Activity
</td>        
<td width="310" valign="top" >         

[031f5706-7f1a-11db-ad56-7bd355d89593](http://developer.healthvault.com/types/type.aspx?id=031f5706-7f1a-11db-ad56-7bd355d89593)

      
</td>        
<td width="194" valign="top" >
</td>        
<td width="180" valign="top" >         

November 2005, "Your Guide to Healthy Sleep", ISBN 1-933236-05-1

      
</td>     </tr>      <tr >       
<td width="161" valign="top" >Sleep Session
</td>        
<td width="310" valign="top" >         

[11c52484-7f1a-11db-aeac-87d355d89593](http://developer.healthvault.com/types/type.aspx?id=11c52484-7f1a-11db-aeac-87d355d89593)

      
</td>        
<td width="194" valign="top" >
</td>        
<td width="180" valign="top" >         

November 2005, "Your Guide to Healthy Sleep", ISBN 1-933236-05-1

      
</td>     </tr>      <tr >       
<td width="161" valign="top" >Vital Signs
</td>        
<td width="310" valign="top" >         

[73822612-c15f-4b49-9e65-6af369e55c65](http://developer.healthvault.com/types/type.aspx?id=73822612-c15f-4b49-9e65-6af369e55c65)

      
</td>        
<td width="194" valign="top" >lab-results-units, lab-results-flag, 
</td>        
<td width="180" valign="top" >
</td>     </tr>   </tbody></table>  

 

As you can notice above we recommend ICD-9, RxNorm, LOINC, NDC. x12-de-1130, x12-de-335. We do prefer [SNOMED-CT](http://en.wikipedia.org/wiki/SNOMED_CT) as well, however the application using it need to have license for it.

 

 

Having written the above I would like to match that with what Dr. Halamka recommends in his [post](http://geekdoctor.blogspot.com/2009/04/data-elements-of-ehr.html). Note that I mention content column for completeness, however its not useful for comparison.

 <table cellpadding="2" cellspacing="0" border="1" width="718" ><tbody >     <tr >       
<td width="236" valign="top" >** Data **
</td>        
<td width="231" valign="top" >** Content**
</td>        
<td width="249" valign="top" >** Vocabulary**
</td>     </tr>      <tr >       
<td width="236" valign="top" >Demographics
</td>        
<td width="231" valign="top" >HL7 2.x for messaging, CCD for document summaries
</td>        
<td width="249" valign="top" >HITSP Harmonized code sets for gender, marital status
</td>     </tr>      <tr >       
<td width="236" valign="top" >Problem List
</td>        
<td width="231" valign="top" >HL7 2.x for messaging, CCD for document summaries
</td>        
<td width="249" valign="top" >[SNOMED-CT](http://www.nlm.nih.gov/research/umls/Snomed/snomed_main.html)
</td>     </tr>      <tr >       
<td width="236" valign="top" >Medications 
</td>        
<td width="231" valign="top" >[NCPDP](http://www.ncpdp.org/) script for messaging, CCD for document summaries
</td>        
<td width="249" valign="top" >RxNorm and Structured SIG
</td>     </tr>      <tr >       
<td width="236" valign="top" >Allergies
</td>        
<td width="231" valign="top" >HL7 2.x for messaging, CCD for document summaries
</td>        
<td width="249" valign="top" >[UNII](http://www.fda.gov/ForIndustry/DataStandards/SubstanceRegistrationSystem-UniqueIngredientIdentifierUNII/ucm127839.htm) for foods and substances, NDF-RT for medication class, RxNorm for Medications
</td>     </tr>      <tr >       
<td width="236" valign="top" >Progress Notes and Other Narrative Documents (History and Physical, Operative Notes, Discharge Summary)
</td>        
<td width="231" valign="top" >HL7 2.x for messaging, CCD for document summaries
</td>        
<td width="249" valign="top" >CDA Templates (interesting [note](http://www.openehr.org/wiki/display/stds/openEHR+Archetypes+for+HL7+CDA+Documents))
</td>     </tr>      <tr >       
<td width="236" valign="top" >Departmental Reports (Pathology/Cytology, GI, Pulmonary, Cardiology etc.)
</td>        
<td width="231" valign="top" >HL7 2.x for messaging, CCD for document summaries
</td>        
<td width="249" valign="top" >SNOMED-CT
</td>     </tr>      <tr >       
<td width="236" valign="top" >Laboratory Results
</td>        
<td width="231" valign="top" >HL7 2.x for messaging, CCD for document summaries
</td>        
<td width="249" valign="top" >LOINC for lab name, [UCUM](http://unitsofmeasure.org/) for units of measure, SNOMED-CT for test ordering reason
</td>     </tr>      <tr >       
<td width="236" valign="top" >Microbiology
</td>        
<td width="231" valign="top" >HL7 2.x for messaging, CCD for document summaries
</td>        
<td width="249" valign="top" >LOINC for lab name/observation
</td>     </tr>      <tr >       
<td width="236" valign="top" >Images
</td>        
<td width="231" valign="top" >DICOM
</td>        
<td width="249" valign="top" >
</td>     </tr>      <tr >       
<td width="236" valign="top" >Administrative Transactions (Benefits/Eligibility, Referral/Authorization, Claims/Remittance)
</td>        
<td width="231" valign="top" >X12
</td>        
<td width="249" valign="top" >[X12](http://www.x12.org/), [CAQH](http://www.caqh.org/) CORE
</td>     </tr>   </tbody></table>  

****

 

**Next Time: **I’ll try to update the above tables with more details and try to come with recommendations of which clinical type (in the Data column above) would potentially match with which HealthVault type.

 

As usual leave your suggestions in the comments.
