---
author: vitraag
comments: true
date: 2011-05-27 01:45:46+00:00
layout: post
link: https://vitraagblog.wordpress.com/2011/05/26/getting-started-with-mood-tracker-2/
slug: getting-started-with-mood-tracker-2
title: 'Getting Started with Mood Tracker #2'
wordpress_id: 325
categories:
- Mobile
---

In the last post, we sort of defined what our emotion tracking application should do. Lets get started with building it. I assume you have visual studio installed with WP7 tools, if not you can get them from [here](http://create.msdn.com/en-us/home/getting_started).

[![image]({{site.images}}/2011/05/image3.png)](http://create.msdn.com/en-us/home/getting_started)

Fig 1. Windows Phone 7 SDK

Next, we go over to [codeplex](http://healthvaultwp7.codeplex.com/), and download the HealthVault library with the sample.

[![image]({{site.images}}/2011/05/image4.png)](http://healthvaultwp7.codeplex.com/)

Fig 2. HealthVault WP7 library.

I extracted the library to my desktop and the folder structure looks like following -

[![image]({{site.images}}/2011/05/image_thumb3.png)]({{site.images}}/2011/05/image5.png)

Fig 3. HealthVault WP7 library extracted.

I open the MobileSDK solution in visual studio and hit F5, the library compiles and the WeightTracker demo starts -

[![image]({{site.images}}/2011/05/image_thumb4.png)]({{site.images}}/2011/05/image6.png)

Fig 4. Compiling and running HealthVault WP7 Sample Application

Without further ado lets create our new Silverlight for Windows phone project in our solution for MoodTracker, and reference the HVMobilePhone library in that project.

[![image]({{site.images}}/2011/05/image_thumb5.png)]({{site.images}}/2011/05/image7.png)

Fig 5. Beginnings of MoodTracker

First things first, lets get the application setup to talk to HealthVault, in App.xaml.cs class we add reference to HealthVaultService & HealthVault Shell, we also need to make sure we get a unique application ID in the developer environment of HealthVault, to do that we head over to [HealthVault Application Configuration Center](http://config.healthvault-ppe.com/), and create a new application by clicking on the button --

[![image]({{site.images}}/2011/05/image_thumb6.png)]({{site.images}}/2011/05/image8.png)

Fig 6. Creating a new application in Application Configuration Center

We create an application of type SODA and pick the name Mood Tracker for it --

[![image]({{site.images}}/2011/05/image_thumb7.png)]({{site.images}}/2011/05/image9.png)

Fig 7. Creating Mood tracker as a SODA application

One the application is created we click on the app link and assign appropriate data-type for this application using the SODA-

[![image]({{site.images}}/2011/05/image_thumb8.png)]({{site.images}}/2011/05/image10.png)

Fig 8. Adding Emotional State to our Mood tracker application.

One we create the SODA application, and appropriate data type rules we are all set! Now we can configure our base page to work with HealthVault Pre-production environment. Here is my initial code for it --

    
    
        <span class="kwrd">public</span> <span class="kwrd">partial</span> <span class="kwrd">class</span> App : Application
        {
            <span class="kwrd">public</span> <span class="kwrd">static</span> HealthVaultService HealthVaultService { get; set; }
            <span class="kwrd">public</span> <span class="kwrd">static</span> <span class="kwrd">string</span> HealthVaultShellUrl { get; set; }
    
            <span class="kwrd">static</span> <span class="kwrd">string</span> platformUrl = <span class="str">@"https://platform.healthvault-ppe.com/platform/wildcat.ashx"</span>;
            <span class="kwrd">static</span> <span class="kwrd">string</span> shellUrl = <span class="str">@"https://account.healthvault-ppe.com"</span>;
            <span class="kwrd">static</span> <span class="kwrd">string</span> masterAppId = <span class="str">"83bf507d-9186-407f-a6cd-b2d65f558690"</span>;
    
            <span class="rem">// Code to execute when the application is launching (eg, from Start)</span>
            <span class="rem">// This code will not execute when the application is reactivated</span>
            <span class="kwrd">private</span> <span class="kwrd">void</span> Application_Launching(<span class="kwrd">object</span> sender, LaunchingEventArgs e)
            {
                HealthVaultService = <span class="kwrd">new</span> HealthVaultService(platformUrl, shellUrl, <span class="kwrd">new</span> Guid(masterAppId));
            }
            <span class="rem">// Code to execute when the application is activated (brought to foreground)</span>
            <span class="rem">// This code will not execute when the application is first launched</span>
            <span class="kwrd">private</span> <span class="kwrd">void</span> Application_Activated(<span class="kwrd">object</span> sender, ActivatedEventArgs e)
            {
                HealthVaultService = <span class="kwrd">new</span> HealthVaultService(platformUrl, shellUrl, <span class="kwrd">new</span> Guid(masterAppId));
            }
    
    ..




We make this project as startup project and hit F5, and get to the first page of our application!

[![image]({{site.images}}/2011/05/image_thumb9.png)]({{site.images}}/2011/05/image11.png)

Fig 9. A start with HealthVault Service configure in base page

We have lots more to do!

Next time, we will focus on authenticating this application with HealthVault Shell!
