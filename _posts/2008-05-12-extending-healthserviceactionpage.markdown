---
author: vitraag
comments: true
date: 2008-05-12 16:04:02+00:00
layout: post
link: https://vitraagblog.wordpress.com/2008/05/12/extending-healthserviceactionpage/
slug: extending-healthserviceactionpage
title: Customizing HealthVault Redirection
wordpress_id: 30
categories:
- ASP.NET
- HealthVault
---

The HealthServiceActionPage gives you a very nice [mechanism](http://msdn.microsoft.com/en-us/healthvault/bb852205.aspx) by which you can declaratively define pages handling various HealthVault shell targets. However, folks frequently run in to situation where they need more dynamic way of redirecting and handling shell targets. A simple scenario is if you want to users to come back to the same URL they clicked after being authorized by healthvault shell, e.g. User clicks and returns to [https://www.healthapp.com/username/stats](https://www.healthapp.com/username/stats) instead of going to the default home [https://www.healthapp.com/username/](https://www.healthapp.com/username/).








Here is a code snippet which illustrates how to extend the HealthServiceActionPage:
```csharp 
    using System;
    public partial class Redirect : Microsoft.Health.Web.HealthServiceActionPage
    {
        //We don't want this page to require log on because when we sign out,
        //we still want this page to read the WCPage_ActionSignOut key in the
        protected override bool LogOnRequired
        {
            get
            {
                return false;
            }
        }
    
        public const String ActionQueryStringValue = "actionqs";
        public const String DefaultURL = "http://www.healthapp.com/username";
    
        protected override void OnActionApplicationAuthorizationSuccessful(string action, 
         string actionQueryString)
        {
            string targetLocation;
            String fullTargetLocation;
            string url = Request.QueryString[ActionQueryStringValue];
            // TODO: Validate that the URL is from home domain
            if (url != null)
            {
                targetLocation = url;
            }
            else
            {
                targetLocation = DefaultURL;
            }
            // we assume that the query string startswith '?'
            fullTargetLocation = targetLocation + actionQueryString;
            Response.Redirect(fullTargetLocation);
        }
    }
```
    
The magic is in the [OnActionApplicationAuthorizationSuccessful ](http://msdn.microsoft.com/en-us/library/cc462358.aspx)method, which allows us to override the authorization successful target. The HealthVault SDK [HealthServiceActionPage](http://msdn.microsoft.com/en-us/library/cc188454.aspx) now provides us several OnAction methods which could be use to override the particular APPAUTH targets.

You can also download this code from MSDN Code [here](http://code.msdn.microsoft.com/hvactionpage).
