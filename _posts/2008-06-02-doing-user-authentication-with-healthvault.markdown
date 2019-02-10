---
author: vitraag
comments: true
date: 2008-06-02 09:46:50+00:00
layout: post
link: https://vitraagblog.wordpress.com/2008/06/02/doing-user-authentication-with-healthvault/
slug: doing-user-authentication-with-healthvault
title: Doing User Authentication with HealthVault
wordpress_id: 33
categories:
- HealthVault
- Open Source
- RubyOnRails
---

My previous post with regards to writing the HealthVault Ruby Library demonstrated how one goes about authentication their application with HealthVault. Now that you have successfully gotten HealthVault to trust your application how do you make sure that the user who logs in is a valid user. In the HealthVault lingo this is called user authentication. 

To successfully do a user authentication, an application must:



	
  * Redirect the user to HealthVault shell sign-in page.

	
  * Receive a token identifying the current user on a pre-registered URL with HealthVault, and use that token to do any user related transactions with HealthVault hence onwards. This token is valid for 20 minutes.



Now, in code it looks like follows lets assume that you application has a pre-registered URL of http://localhost:3000/healthvault/redirect. When a user wants to login, you actually redirect them to HealthVault shell (http://account.healthvault-ppe.com/redirect.aspx) in the following way:

    
    
    redirect_to "https://account.healthvault-ppe.com/redirect.aspx?target=AUTH&targetqs=?appid=05a059c9-c309-46af-9b86-b06d42510550%26redirect%3dhttp%253a%252f%252flocalhost%253a3000%252fhealthvault%252fredirect"
    


Note the parameters **target, appid & redirect** in the above URL.

The above redirection once successful will send the user to the page http://localhost:3000/healthvault/redirect. On this page you should read the wctoken from the URL query-string. In ruby I do this the following way:


    
    
      def redirect
        if (request.query_parameters["target"] == "AppAuthSuccess")
          session[:wctoken] = request.query_parameters["wctoken"]
          redirect_to :controller => 'healthvault', :action => 'index'
        end
      end
    



Voila!! you have the much needed wctoken. In the next article we will what can we do with this magic wctoken!

Next time: [Putting it all together! ](http://healthblog.vitraag.com/2008/06/lighting-it-up/)
