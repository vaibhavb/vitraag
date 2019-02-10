---
author: vitraag
comments: true
date: 2008-03-10 23:33:00+00:00
layout: post
link: https://vitraagblog.wordpress.com/2008/03/10/transforming-xsl-datetime-to-healthvault-date-time/
slug: transforming-xsl-datetime-to-healthvault-date-time
title: Transforming Xsl DateTime to HealthVault date-time
wordpress_id: 21
categories:
- HealthVault
- Xsl
---

If you are working on transforming a schema to HealthVault data-type, you will run in to issue for transforming Xsl DateTime to date-time. The reason healthvault wants its own date-time is to facilitate approximate datetime i.e date only, time only scenarios like I took Polio vaccine when i was a kid prolly 10 years ago, now how do you DateTime that ? Anyways, here is Xsl which does DateTime to date-time using a Xsl template GenerateWhenNode.

    
    
                  0">                                                                                                                                                                                                                                                                                                                                                                                                                    <s>                              </s>                                                                             0">                                                                                                                                                                                                                                                                                                                                                                                                                    <s>                              </s>                                                                    
