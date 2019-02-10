---
author: vitraag
comments: true
date: 2008-03-10 21:00:00+00:00
layout: post
link: https://vitraagblog.wordpress.com/2008/03/10/testing-your-application-on-older-versions-of-ie-web-app-compat-that-is/
slug: testing-your-application-on-older-versions-of-ie-web-app-compat-that-is
title: Testing your application on older versions of IE - Web app compat that is!
wordpress_id: 20
categories:
- ASP.NET
- Web development
---

Recently I ran in a bug in our AHA application on IE 6. Coming to the terms with testing across multiple browsers is a painful realization of the evils of web development. I tried several ways by which i can install IE 6 on my Vista machine, including tricky thing like DLL redirection. But this is way too painful - however I stumbled on a sweet way of doing application compatibility tests - virtual pc!!  
  
Here is the cook-book way to get different version of IE for compatibility tests -  
1. Deploy your application on a staging server  
2. Install Virtual PC[ 2007 ](http://www.microsoft.com/windows/products/winfamily/virtualpc/default.mspx)(it works on Vista)  
3. Get the IE testing images from [here](http://www.microsoft.com/downloads/details.aspx?FamilyId=21EABB90-958F-4B64-B5F1-73D0A413C8EF&displaylang=en).  
  
One downside of this approach is that you cannot step into and debug you application because virtual pc is a painful to configure for running on your corporate LAN :(.
