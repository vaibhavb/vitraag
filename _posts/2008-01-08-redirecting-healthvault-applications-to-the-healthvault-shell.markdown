---
author: vitraag
comments: true
date: 2008-01-08 21:54:00+00:00
layout: post
link: https://vitraagblog.wordpress.com/2008/01/08/redirecting-healthvault-applications-to-the-healthvault-shell/
slug: redirecting-healthvault-applications-to-the-healthvault-shell
title: Redirecting HealthVault Applications to the HealthVault Shell
wordpress_id: 14
categories:
- HealthVault
---

One can redirect HealthVault applications to the HealthVault Shell for various reasons.

For example if you want to redirect a user to list of frequently asked questions, the url is [this ](https://www.microsofthealthbeta.com/help.aspx?topicid=faq)but one programmatically generate it as the code below :

    
        
            using Microsoft.Health.Web; 
    /// <summary> 
    /// Redirect the user to HealthVault frequently asked questions    
    /// </summary>   
    public void RedirectToHealthVaultFaq()    
    {        
    RedirectToShellUrl(ShellRedirect.To.Help, ShellRedirect.Help.FAQ);    
    }
    
    /// <summary>
    /// Template class for HealthVaultShellRedirects    
    /// NOTE: Does not include all possible redirections   
    /// </summary>  
    public static class HealthVaultShellRedirect
    {
        public static class To
        {
            public const string Help = "help";
            public const string AppAuth = "appauth";
            public const string CreateAccount = "createaccount";
        }
    
        public static class Help
        {
            public const string FAQ = "topicid=faq";
        }
        public static class AppAuth
        {
            public const string AppId = "appid="; public const string Redirect = "redirect=";
        }
        public static class CreateAccount
        {
            public const string AppId = "appid="; public const string IsMRA = "ismra="; public const string PersistWCToken = "persistwctoken=";
        }
    }
    


For complicated targets one can use the string builder class to build the query string.

For example if one wants to redirect a user to healthvault for account creation. (HealthVaultShellRedirect, class is defined in first sample)
:

    
     
    /// <summary></summary>    
    /// Redirect a user to create a new healthvault account    
    ///     
    public void RedirectForAccountCreation()    
    {        
        StringBuilder query = new StringBuilder(128);
        query.Append(HealthVaultShellRedirect.CreateAccount.AppId);
        query.Append(WebApplicationConfiguration.AppId);
        // We are doing this for only one record
        query.Append("&" + HealthVaultShellRedirect.CreateAccount.IsMRA + "false"); 
        // We dont need a persistent token, it might be useful for managing campaigns 
        query.Append("&" + HealthVaultShellRedirect.CreateAccount.PersistWCToken + " ");
        RedirectToShellUrl(HealthVaultShellRedirect.To.CreateAccount,            query.ToString());
    }
    
    
    /// <summary>
    ///    
    /// Redirect to HealthVaultShell for application authentication    
    /// </summary> 
    public void RedirectToAppAuthPage()
    {        
        StringBuilder query = new StringBuilder(128);
        query.Append(HealthVaultShellRedirect.AppAuth.AppId);
        query.Append(WebApplicationConfiguration.AppId);
        query.Append("&" + HealthVaultShellRedirect.AppAuth.Redirect);
        query.Append(HttpUtility.UrlEncode(Request.Url.AbsoluteUri));
        RedirectToShellUrl(HealthVaultShellRedirect.To.AppAuth, query.ToString());    
    }
    
    


A complete list of possible To targets and their parameters is detailed in this HealthVault forums [post](http://forums.microsoft.com/MSDN/ShowPost.aspx?PostID=2623122&SiteID=1). Please be advised that lot of the functionality there is advanced and serves as a good reference.
