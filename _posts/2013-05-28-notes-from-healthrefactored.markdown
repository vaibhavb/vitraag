---
author: vitraag
comments: true
date: 2013-05-28 21:08:23+00:00
layout: post
link: https://vitraagblog.wordpress.com/2013/05/28/notes-from-healthrefactored/
slug: notes-from-healthrefactored
title: Notes from Health:Refactored
wordpress_id: 404
categories:
- HealthIT
---

From May 13-14, I spent some time at [Health:Refactored](http://www.health2con.com/events/conferences/health-refactored/). Apart from catching up with colleagues and kindred spirits, the event was a good learning venue for healthcare IT developers and designers.

I’m going to broadly capture my notes under data, data analysis (big data), Health UI, and Health API platforms.


### <!-- more -->Data


Bryan Sivak did a keynote highlighting various [Health Data](http://www.hhs.gov/open/initiatives/hdi/index.html) and [entrepreneurship](http://www.hhs.gov/open/initiatives/entrepreneurs/index.html) programs available at HHS. Among the various [data sets](http://hub.healthdata.gov/), the ones which he highlighted in the talk is [NPPES](https://npiregistry.cms.hhs.gov/NPPESRegistry/NPIRegistryHome.do) provider database. The update frequency of pillbox data sets was questioned by the audience. By the way, health data consortium maintains a ranked repository of 50 top health related data sets - [http://www.healthdataconsortium.org/data-sources](http://www.healthdataconsortium.org/data-sources) and Socrata ([http://dev.socrata.com/](http://dev.socrata.com/)) offers API access to public data sets. A good place to know more about the HHS lead datasets and initiatives is an upcoming conference – [HealthDataPalooza](http://healthdatapalooza.org/)!   More on HealthDataPalooza soon, but the conference is doing a half-day data analysis workshop and providing attendees with a license to Archimedes population explorer ([videos](http://www.youtube.com/user/ArchimedesModel/videos)) and the CMS [claims data set](http://www.cms.gov/Research-Statistics-Data-and-Systems/Statistics-Trends-and-Reports/SynPUFs/DE_Syn_PUF.html) (CMS DE-SynPUF). By the way, you should check out the winners of Data design diabetes innovation competition at - [http://www.redesigningdata.com/](http://www.redesigningdata.com/).

In addition to “data” discussion there was talk about “trust data”. Its important to have appropriate data in order to establish a distributed trust ecosystem. A few folks talked about National Strategy for Trusted Identities in Cyberspace ([NSTIC](http://ahier.blogspot.com/2012/09/national-strategy-for-trusted.html)) pilots.


### Data Analysis (Big Data)


Various data scientist stressed on the need to get started with data analysis with minimalism (you can’t hire quality data scientists – as most of them already work at Facebook, LinkedIn etc.). Following set of tools might be useful:



	
  * Motardata – ([http://app.mortardata.com](http://app.mortardata.com)) a “heroku” for deploying and developing Apache Hadoop.

	
  * Spark ([http://spark-project.org/](http://spark-project.org/)) and Shark ([http://shark.cs.berkeley.edu/](http://shark.cs.berkeley.edu/)) – these are upcoming faster technologies which are compatible with Hadoop

	
  * R - [http://www.r-project.org/](http://www.r-project.org/)

	
  * NLTK (Python) - [http://nltk.org/](http://nltk.org/), a natural language processing toolkit which provides easy interface with Wordnet.

	
  * Big Data platforms – Metascale, Teradata, Netezza, Greenplum etc.




### Health UI


Healthcare IT user interfaces and customer interactions need to evolve. The term which stuck with me from the conference was – “lead with love”. Compassion should show through user interface but more so the interface should be enable users to personalize, share, celebrate, and should provide value and voice – according to one of the panelists. I met with folks from various design companies including ideo, madpow etc. It was good to see familiar faces.

The UI in healthcare is still stagnant and needs a major impetus. Perhaps someday we will see a major open source toolkit (perhaps like bootstrap, YUI etc.) which helps with this. Microsoft did an attempt with Microsoft Health Common User Interface ([http://www.mscui.net/](http://www.mscui.net/)), perhaps we need something more javascript. Why should difference application user different “unpleasing” ways and icons to let us interface with allergies, medications, problems etc.


### Health API Platforms


A personal favorite of mine! A number of strong folks showed APIs at the conference, following are pointers to a few which caught my eye:



	
  * Walgreens API – Announced recently - [https://developer.walgreens.com/](https://developer.walgreens.com/) (Prescriptions and Rewards API)

	
  * NYeC – A statewide health API - [http://nyehealth.org/what-we-do/api-innovation/](http://nyehealth.org/what-we-do/api-innovation/)

	
  * athenahealth – AthenaHealth Marketplace (announced recently): [http://www.athenahealth.com/marketplace/](http://www.athenahealth.com/marketplace/)

	
  * allscripts – ADP - [http://www.allscripts.com/en/company/partners/adp-faq.html](http://www.allscripts.com/en/company/partners/adp-faq.html)

	
  * aetna carepass - [https://developer.carepass.com/](https://developer.carepass.com/) ([Zipongo](https://www.zipongo.com/) announced their carepass connection)


A more detailed analysis of various go to market approaches of various health API platforms would be a candidate for another post. A quick look at above list might leave the reader pondering how are various health care participants like retail/pharmacy (walgreens), government/states (NYeC), electronic medical records (athenahealth, allscripts) and payers (Aetna) extending their markets with data or rewards or “buzz word value” plays using an application programming interface!

More soon..
