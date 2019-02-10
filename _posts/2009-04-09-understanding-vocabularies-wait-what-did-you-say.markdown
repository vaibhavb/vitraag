---
author: vitraag
comments: true
date: 2009-04-09 19:22:14+00:00
layout: post
link: https://vitraagblog.wordpress.com/2009/04/09/understanding-vocabularies-wait-what-did-you-say/
slug: understanding-vocabularies-wait-what-did-you-say
title: Understanding Vocabularies. Wait! What did you say?
wordpress_id: 84
categories:
- HealthIT
- HealthVault
- Ideas
- Vocabularies
tags:
- Semantic Web
---

Any data system the semantic meaning of data is as important as the strucutre of the data. In [HealthVault](http://www.healthvault.com/) we expose a very [structured data](http://en.wikipedia.org/wiki/Data_model) set in form of various [data types ](http://developer.healthvault.com/types/types.aspx)and the semantic meaning of the content in those data sets is dictated by [vocabularies](http://developer.healthvault.com/types/vocabs.aspx).

 

[HealthVault Vocabulary](http://developer.healthvault.com/types/vocabs.aspx) is a big area so I'm going to attempt to break this down in separate series of posts. In this post i'm primarily going to focus on vocabularies in general.

 

Many of you might have heard of the term - [Semantic Web](http://en.wikipedia.org/wiki/Semantic_Web) or Web 3.0. So whats this buzz about? Well Web 1.0 was for humans to connect, [Web 2.0](http://en.wikipedia.org/wiki/Web_2.0) was for systems to connect to humans via rich internet applications. Web 3.0 promises a web for systems - a web where programs can communicate and link to each other. So what this implies is for Semantic Web to be successful - the data being put on the semantic internet need not only be structured but also the content be in such a way that **computer programs **can understand the meaning of it. This is only possible if everyone has a shared Vocabulary or Ontology, or a mechanism to relate to a new Vocabulary.

 

To solve the [ontology](http://en.wikipedia.org/wiki/Ontology_%28information_science%29) problem we can just sit down and invent a vocabulary which everyone will use henceforth and be done with it, right! First, we won't agree to single vocabulary and second we can't plan for future vocabularies. And the most important challenge is that the system which powers this vocabulary needs to agree with the architecture of the web i.e must be decentralized and open!

 

The semantic web community is using a very powerful way to achieve this. They are using the same mechanism which powers resource discovery (for example - URL linking) to discover and understand vocabularies. Two candidates which make this possible are [RDF](http://en.wikipedia.org/wiki/Resource_Description_Framework) (resource description format) and [OWL](http://en.wikipedia.org/wiki/Web_Ontology_Language) (Web [Ontology Language](http://en.wikipedia.org/wiki/Ontology_%28information_science%29)). I won't describe these technologies in details here but keep it for some other day. However the point of this note is to surface example ontologies or vocabularies this community has successfully used/developed so far:

 

  
  * [FOAF](http://en.wikipedia.org/wiki/FOAF_%28software%29) - [http://en.wikipedia.org/wiki/FOAF_(software)](http://en.wikipedia.org/wiki/FOAF_(software)) : This ontology describes a persons social network 
   
  * FAO - [http://en.wikipedia.org/wiki/Geopolitical_ontology](http://en.wikipedia.org/wiki/Geopolitical_ontology): This ontology describes a geopolitical unit. 
 

So how does this fit in the HealthCare? John Hamalka outlines the elements of vocabulary whicn an [EHR](http://en.wikipedia.org/wiki/Electronic_health_record) can use in his post - [http://geekdoctor.blogspot.com/2009/04/data-elements-of-ehr.html](http://geekdoctor.blogspot.com/2009/04/data-elements-of-ehr.html). He mentions preferred vocabularies and transports for some of important EHR elements. In the following posts i will try to go deeper in this area.

 

So how does this fit with HealthVault? Well HealthVault exposes all the vocabularies it uses - [http://developer.healthvault.com/types/vocabs.aspx](http://developer.healthvault.com/types/vocabs.aspx). We let people also annotate their data with any vocabulary they like. However this leds to an interesting interoperability problem, so on the [XSD](http://en.wikipedia.org/wiki/XML_Schema_%28W3C%29) schemas of our data types ([http://developer.healthvault.com/types/types.aspx](http://developer.healthvault.com/types/types.aspx)) we specify preferred vocabularies for some data elements. In the following posts i will provide more details with regards to this.

 

As you can from John's post their is no dearth of language systems for various medical or healthcare terms. However their is a big gap on best practices on how one can denormalize various vocabularies for implementeting systems which can interoperate with other systems using different vocabularies. I tend to think that there are some lessons to be learned in this area from semantic web efforts and also a need for a more structured effort to surface best practices. May be I'll dig deeper in this area in one of the future posts.

 

Next post: Recommended Vocabularies for Various Data Contexts.

 

###### Related articles by Zemanta

 

  
  * [Semantic Web Glossary](http://semanticalley.com/2009/02/12/semantic-web-glossary/) (semanticalley.com) 
   
  * [Semantic web - The foundations](http://www.digital-constructions.com/blog/2009/02/semantic-web-foundations.html) (digital-constructions.com) 
   
  * [A conference comes of age: a review of the 7th International Semantic Web Conference (ISWC2008)](http://blogs.talis.com/nodalities/2009/01/a-conference-comes-of-age-a-review-of-the-7th-international-semantic-web-conference-iswc2008.php) (blogs.talis.com) 
 

[![Reblog this post [with Zemanta]](http://img.zemanta.com/reblog_e.png?x-id=85daab76-ae3f-4d76-a5dc-84166fb6ddd7)](http://reblog.zemanta.com/zemified/85daab76-ae3f-4d76-a5dc-84166fb6ddd7/)
