---
author: vitraag
comments: true
date: 2011-05-25 21:40:53+00:00
layout: post
link: https://vitraagblog.wordpress.com/2011/05/25/developing-healthvault-wp7-mobile-application-1/
slug: developing-healthvault-wp7-mobile-application-1
title: 'Developing HealthVault WP7 Mobile Application #1'
wordpress_id: 303
categories:
- HealthVault
- Mobile
---

Yesterday, HealthVault released [developer preview](http://blogs.msdn.com/b/healthvault/archive/2011/05/24/healthvault-1105-release.aspx) of support for mobile applications. The associated [Windows Phone 7 library](http://healthvaultwp7.codeplex.com/) is available on codeplex as well.

 

In this multi-part series, I’ll try to cover the details of building a Windows Phone 7 mobile application for HealthVault.

 

**Now, the first question is what should we build?       
**Our product management team has recently been tracking their happiness and stress level on a daily basis. I have been thinking of providing a tool which helps them to track their happiness & stress levels and of course build great products..

 

Having said above there are a [few applications](http://www.bing.com/browse?g=wp7&qpvt=windows+phone+7+apps&FORM=SGEWEB#toc=0&categories_rbid=5) in the Health & Fitness category of WP7 application store which help a user to track mood, but none of them combines happiness and stress, and stores it in HealthVault.

 

[![image]({{site.images}}/2011/05/image_thumb.png)]({{site.images}}/2011/05/image.png)      
Fig 1. [Mood swing](http://www.moodswinglife.com/) application in Windows Phone 7 Store

 

Hopefully over-time we can make the application a fun one, may be add a social game aspect to it!

 

**Well, how will the application look like?**

 

The application would allow the user to input their happiness and stress level, and perhaps look at history and may be display a social game avatar of their well-being.

 

Here is a sketch of what the app might look like --

 

[![image]({{site.images}}/2011/05/image_thumb1.png)]({{site.images}}/2011/05/image1.png)

 

Fig 2. White board wire-frame of our mood application

 

**Where to store the data?**

 

While developing a HealthVault application a relevant question is which part of the HealthVault data store the application should store data in. As we browse the [HealthVault Data Types](http://developer.healthvault.com/pages/types/types.aspx), we immediately see a relevant data type – [Emotional State](http://developer.healthvault.com/pages/types/type.aspx?id=4b7971d6-e427-427d-bf2c-2fbcf76606b3). 

 

Turn out there is also a handy tool to input sample data for this data type after clicking the “View & Edit” button next to the type -

 

[![image]({{site.images}}/2011/05/image_thumb2.png)]({{site.images}}/2011/05/image2.png)

 

Fig 3. Emotional State Data type

 

On further analysis it turns out that this type is almost perfect for our use, except the fact that we have to use a scale of 1-5 and there is an additional element – well-being, which we can ignore for now.

 

**Next Step?**

 

Now that we have defined this application, the next step would be to get our hands dirty and start working with [Windows Phone 7 tools for Visual studio](http://www.microsoft.com/downloads/en/details.aspx?FamilyID=49b9d0c5-6597-4313-912a-f0cca9c7d277) and the [HealthVault WP7 library](http://healthvaultwp7.codeplex.com/).

 

Next Post: Mood Tracker – Getting Started #2
