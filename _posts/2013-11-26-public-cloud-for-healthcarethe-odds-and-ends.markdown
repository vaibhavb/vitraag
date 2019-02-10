---
author: vitraag
comments: true
date: 2013-11-26 22:57:25+00:00
layout: post
link: https://vitraagblog.wordpress.com/2013/11/26/public-cloud-for-healthcarethe-odds-and-ends/
slug: public-cloud-for-healthcarethe-odds-and-ends
title: Public Cloud for Healthcare–The odds and ends
wordpress_id: 412
categories:
- HealthIT
---

As computing and storage becomes more ubiquitous, its natural to ask when can regulated industries utilize the quality and economies of scales. Maybe utility computing could have alleviated some aspects of healthcare.gov by flipping the switch to an alternative powergrid, if you will. However there are number if interesting challenges and nuances for public clouds to offer utility computing and storage to healthcare customers.

 

**So what are the problems?**

 

  
  * **Security & Privacy:** Unlike electricity, utility computing is too ingrained in to [processes and innovation](http://www.cioupdate.com/financial-strategies/speed-bumps-on-the-road-to-true-utility-computing-1.html) for existing businesses. 
   
  * **Compliance:** Utility companies to be able to comply with data audit policies as well as have a business structure which enables signing of business associate agreement. 
   
  * **Lock in and interoperability:** Developing a solution too ingrained in to a utility architecture can effect the core business of a company 
   
  * **Co-innovation: **In past decade most businesses have innovated by adopting IT strategically. We see a CIO as part of every organization, to continue that innovation the public computing utility needs to offers ways to co-innovate easily. 
 

**So what are the current solutions?**

 

  
  * Well most cloud-based healthcare organization keep maintain their own cloud infrastructure.             
    * The data is encrypted at REST either by Database Transparent Data Encryption (TDE). Both Oracle and SQLServer support it. 
       
    * File system encryption 
       
   
  * Healthcare organizations sign a HIPAA BAA and most data centers are certified to one of the standards – (SAS 70, ISO etc.) 
 

**What’s needed?**

 

  
  * More public cloud vendors should sign HIPAA BAAs – Microsoft [Azure](http://www.microsoft.com/health/en-us/initiatives/pages/cloud-services-for-health.aspx), [AWS](http://aws.amazon.com/compliance) and most recently Google Cloud already do. 
   
  * Co-innovate for security and compliance solutions like AWS [CloudHSM](http://aws.amazon.com/cloudhsm/)
   
  * Make encryptions at rest easy – blob store [keys](http://stackoverflow.com/questions/11428250/key-management-in-windows-azure) are a great start. 
