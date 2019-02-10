---
author: vitraag
comments: true
date: 2007-12-27 04:20:00+00:00
layout: post
link: https://vitraagblog.wordpress.com/2007/12/26/querying-healthvault-with-where-clauses/
slug: querying-healthvault-with-where-clauses
title: Querying HealthVault with "Where" clauses!
wordpress_id: 11
categories:
- HealthVault
- Python
---

				

HealthVault give me all height measures greater than 1.7m  
  
One can use the XPath attribute of the filter to do the specific queries on the healthvault search items.




Here is an example, which gives you all the height items greater than 1.7 m :




    
    
    HealthRecordSearcher searcher = PersonInfo.SelectedRecord.CreateSearcher()
    HealthRecordFilter filter = new HealthRecordFilter(typeID);
    filter.XPath = "/thing/data-xml/height/value/m[.>=1.7]";
    searcher.Filters.Add(filter);
    HealthRecordItemCollection items = searcher.GetMatchingItems()[0];
    




Please note that the XPath tag doesnot support recursive XPath queries.




Easiest way to construct the queries is first find the HealthRecordItem you want to filter, identify its XML via the GetItemXml() and then use that structure to construct your XPath query. The following is the Xml for Height -



    
    
    
    a891edda-48c3-4783-83d7-c3594a514739
    
    40750a6a-89b2-455c-bd8d-b420a4cb500b
    Active  2007-12-26T19:43:14Z                              2007          12          26                          19          43          <s>14</s>              
    
            1.9405395758527                
    




Hope this helps, I'll post more on this in case there is interest.


						
**Update: ** Eric wrote a tool to help with this, more details are [here](http://blogs.msdn.com/ericgu/archive/2009/04/10/healthvault-xpath-explorer.aspx).
	
