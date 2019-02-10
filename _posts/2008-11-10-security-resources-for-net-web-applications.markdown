---
author: vitraag
comments: true
date: 2008-11-10 22:43:57+00:00
layout: post
link: https://vitraagblog.wordpress.com/2008/11/10/security-resources-for-net-web-applications/
slug: security-resources-for-net-web-applications
title: Security Resources for .NET Web Applications
wordpress_id: 48
categories:
- ASP.NET
- Programming
- Web development
---

Web applications have a class of security vulnerabilities, at times much widespread and trivial than the infamous [buffer overflow](http://en.wikipedia.org/wiki/Buffer_overflow).

![.NET Web Application Security]({{site.images}}/2008/11/aa302415_fa2sn01en-usmsdn_10.gif)

Here are some interesting Security resources on .NET Web Application:

  * [.NET Security at MSDN](http://msdn.microsoft.com/en-us/library/aa286519.aspx) - I specially like [Improving Web Application Security ](http://msdn.microsoft.com/en-us/library/ms994921.aspx)white paper.
  * [AntiXSS Library ](http://msdn.microsoft.com/en-us/library/aa973813.aspx)- Microsoft Anti-[Cross Site Scripting](http://en.wikipedia.org/wiki/Cross-site_scripting) library to protect web apps from XSS.
  * [FxCop ](http://msdn.microsoft.com/en-us/library/bb429476(vs.80).aspx)- A tools which analyses managed code assemblies
  * [Guidance Explorer](http://www.codeplex.com/guidanceExplorer) - Developer guidance (a 15000 foot view though)
  * .NET Security Blogs: [Shawnfa](http://blogs.msdn.com/shawnfa/), [Michael Howard](http://blogs.msdn.com/michael_howard/), [CLRSecurity](http://blogs.msdn.com/CLRSecurity/)
  * [MSDN Security Developer Center ](http://msdn.microsoft.com/en-us/security/default.aspx)- General guidance on writing secure code. The featured video on [exporting and importing certificates ](http://http://msdn.microsoft.com/en-us/security/cc424865.aspx)would be helpful for doing certificate management as a [HealthVault](http://en.wikipedia.org/wiki/Microsoft_HealthVault) application.
  * **Update** - [Threat modeling web applications ](http://msdn.microsoft.com/en-us/library/ms978516.aspx)is a great read. The SDL [Threat modeling tool](http://download.microsoft.com/download/E/5/3/E5318D25-7AEF-4A66-A147-81BBA727F2C1/SDLTM.msi) and [forum](http://social.msdn.microsoft.com/Forums/en-US/sdlthreatmodeling/threads/) are of great utility as well.

Please leave a comment if you know of any valuable security resources.
