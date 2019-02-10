---
author: vitraag
comments: true
date: 2008-02-21 08:58:00+00:00
layout: post
link: https://vitraagblog.wordpress.com/2008/02/21/linq-to-healthvault/
slug: linq-to-healthvault
title: LINQ to HealthVault
wordpress_id: 19
categories:
- HealthVault
- Programming
---

I'm not sure how much value it add, but may we it will be interesting to have a LINQ to HealthVault, something like  
  
var query = from Person  
                     where Person.Name.Contains("Katie")  
                     select Record  
  
Charlie has a great post on expression tree [basics](http://blogs.msdn.com/charlie/archive/2008/01/31/expression-tree-basics.aspx), and this examples details how to implement a [LINQ to Terraserver](http://msdn2.microsoft.com/en-us/library/bb546158.aspx) provider.  
  
However, at this point I'm not entirely sure about the utility of such a feature for HealthVault as the system is less where clause dependant and the SDK already does a decent job of giving out data-types.
