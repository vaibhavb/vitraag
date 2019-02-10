---
author: vitraag
comments: true
date: 2008-04-18 07:02:28+00:00
layout: post
link: https://vitraagblog.wordpress.com/2008/04/18/long-tail-tale-getting-an-auth-token-sure-openhealthvault-can/
slug: long-tail-tale-getting-an-auth-token-sure-openhealthvault-can
title: Long Tail Tale - Getting an Auth Token, sure OpenHealthVault can!
wordpress_id: 29
categories:
- Open Source
- RubyOnRails
---

Alrite finally i got the OpenSSL Crypto to work HealthVault. It took some Ninja hacking and quite a lot of debugging to figure out what was going wrong with signing of a xml for getting an authentication token from HealthVault. Turns out that my signing code was dead on but HealthVault didn't quite like the white space in the "content" section. I wont belabor you more but the short of the long is that now OpenHealthVault can talk to HealthVault and get itself authenticated. As usual the code is at [http://svn.vitraag.com/openhealthvault](http://svn.vitraag.com/openhealthvault) and the application in action is at [http://openhealthvault.vitraag.com](http://openhealthvault.vitraag.com). Well now its time to get a user to be authenticated with HealthVault Shell and the Rails goodies, I expect these to flow rather smoothly.

Next part : [ Doing User Authentication ](http://healthblog.vitraag.com/2008/06/doing-user-authentication-with-healthvault/)
