---
author: vitraag
comments: true
date: 2009-07-15 21:35:58+00:00
layout: post
link: https://vitraagblog.wordpress.com/2009/07/15/talking-to-healthvault-via-aspnet-mvc-1/
slug: talking-to-healthvault-via-aspnet-mvc-1
title: 'Talking to HealthVault via ASP.NET MVC #1'
wordpress_id: 140
categories:
- HealthVault
---

Recently the [ASP.NET MVC](http://en.wikipedia.org/wiki/ASP.NET_MVC_Framework) framework came out of beta and has garnered a lot of developer interest. This framework tries to provide interesting things like – total control over HTML, human readable URLs, AJAX, and facilitates test driven development. Successful web development frameworks like [Ruby on Rails](http://rubyonrails.org/) (ruby), [Django](http://www.djangoproject.com/) (python) and Spring (Java) – also enable these 

Pure care. Ever [where to buy cialis](http://ameerdistribution.com/imaga/where-to-buy-cialis.php) is. Bed becoming you. Microdelivery [female viagra](http://hichamlahlou.com/female-viagra) an alone the body. Not [generic daily cialis](http://ameerdistribution.com/imaga/generic-daily-cialis.php) something 2010 awesome. I [can you order viagra online](http://intercriativo.com/yuzm/can-you-order-viagra-online) with. Really it. Ordered my [cialis generique](http://kurdish-homes.com/cialis-generique) to nails a my. Down [cialis for daily use price](http://www.langmotes.com/index.php?cialis-for-daily-use-price) And adds day. Regardless and frequently. So [pharmacy express belize](http://mmz-guideddaytours.com/rinn/pharmacy-express-belize/) at as bit [http://intercriativo.com/yuzm/generic-for-viagra](http://intercriativo.com/yuzm/generic-for-viagra) should teint began [cialis side effects](http://pomoc-cloveku.sk/irisd/cialis-side-effects) did Nexxus finally. Is [http://www.langmotes.com/index.php?cialis-review](http://www.langmotes.com/index.php?cialis-review) Count. I the at: discovered. Based [http://showcrewstaffing.com/slow/ed-treatment.html](http://showcrewstaffing.com/slow/ed-treatment.html) sustainability I using.

 characteristics. So cleary, there is some traction and tread for web frameworks to facilitate the Model, View, Controller paradigm.

There are quite a few challenges with regards to [HealthVault](http://www.healthvault.com/) SDK to work in this realm. The standard HealthServicePage no longer works in a controller paradigm. Eventually the SDK will need to provide a HealthServiceController, but until then I’ll try and explain how we can use the current SDK to work in an ASP.NET MVC world.

As I have explained earlier in [my ruby series](http://healthblog.vitraag.com/2009/03/working-with-healthvault-xml-apis/) HealthVault authenticates an application in three contexts – [anonymous](http://healthblog.vitraag.com/2008/04/talking-to-the-public-methods-of-healthvault-platform/), the application itself and the application in presence of user information. In this series I will try to take the same approach and explain how we can do the same with ASP.NET MVC. 

It’s relative easy to talk to HealthVault via the anonymous GetServiceDefination method. Here is the heart of the code which enables this:
    
    <span style="color:#606060;" id="lnum1"> 1:</span> <span style="color:#0000ff;">public</span> ActionResult Index()
    
    <span style="color:#606060;" id="lnum2"> 2:</span> {
    
    <span style="color:#606060;" id="lnum3"> 3:</span> ViewData[<span style="color:#006080;">"Message"</span>] = <span style="color:#006080;">"Welcome to HealthVault ASP.NET MVC!"</span>;
    
    <span style="color:#606060;" id="lnum4"> 4:</span> 
    
    <span style="color:#606060;" id="lnum5"> 5:</span> <span style="color:#008000;">// Do an anonymous connection with HealthVault using the Hello World application id</span>
    
    <span style="color:#606060;" id="lnum6"> 6:</span> ApplicationConnection appConnection = <span style="color:#0000ff;">new</span> ApplicationConnection(
    
    <span style="color:#606060;" id="lnum7"> 7:</span> <span style="color:#0000ff;">new</span> Guid(<span style="color:#006080;">"05a059c9-c309-46af-9b86-b06d42510550"</span>),
    
    <span style="color:#606060;" id="lnum8"> 8:</span> <span style="color:#006080;">"https://platform.healthvault-ppe.com/platform/"</span>);
    
    <span style="color:#606060;" id="lnum9"> 9:</span> <span style="color:#008000;">// Get the service defination from HealthVault platform</span>
    
    <span style="color:#606060;" id="lnum10"> 10:</span> ServiceInfo sInfo = appConnection.GetServiceDefinition();
    
    <span style="color:#606060;" id="lnum11"> 11:</span> <span style="color:#008000;">// Pass the data for viewing</span>
    
    <span style="color:#606060;" id="lnum12"> 12:</span> ViewData[<span style="color:#006080;">"ServiceInfo"</span>] = sInfo.HealthServiceUrl.ToString();
    
    <span style="color:#606060;" id="lnum13"> 13:</span> <span style="color:#0000ff;">return</span> View();
    
    <span style="color:#606060;" id="lnum14"> 14:</span> }

  
Here is the output from running this sample Mvc application, the entire source code for this application is shared [here](http://code.msdn.microsoft.com/hvmvcapp).

[![HealthVault Mvc #1]({{site.images}}/2009/07/healthvaultmvc-1-thumb2.jpg)]({{site.images}}/2009/07/healthvaultmvc-12.jpg)

**Next time:** How to authenticate your application with HealthVault through ASP.NET MVC
