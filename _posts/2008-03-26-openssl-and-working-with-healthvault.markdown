---
author: vitraag
comments: true
date: 2008-03-26 01:42:32+00:00
layout: post
link: https://vitraagblog.wordpress.com/2008/03/25/openssl-and-working-with-healthvault/
slug: openssl-and-working-with-healthvault
title: OpenSSL and working with HealthVault
wordpress_id: 26
categories:
- Open Source
- Python
- RubyOnRails
---

This is my first post in an N-series indulgence in trying to evaluate HealthVault to work with Ruby On Rails or Pythons DJango. As you know we HealthVault released a [Java library](http://www.codeplex.com/HealthVaultJavaLib) - and it works in a platform independant fashion on most of platforms. I will attempt to outline some of the challenges here lets starting with -

Step 1: Authentication & Authorization -



	
  * Support for Crytography - RSA and Hash Method Authenticaion Code (SHA1/ SHA256)

	
    * The Java library comes with Sun's implementation of the above [Java.Security](http://java.sun.com/javase/technologies/security/). However in LAMP/R world the only respectable alterative is [OpenSSL](http://www.openssl.org/).

	
    * While Java is everywhere but you might have to install your flavor of OpenSSL in addition to the web-framework. However having a robust framework makes rest of work easy.




	
  * Exporting the private key from Windows generated pfx certificate to be used with one of the offerings.

	
    * While in theory it should just work but their are some format issues which will need to be dealt with getting key material to be used with the above option.





I'm going to try the Step 1 with Python & OpenSSL and lets see where I go with it.

Next Part: [Talking to the public methods of healthvault platform.](http://healthblog.vitraag.com/2008/04/talking-to-the-public-methods-of-healthvault-platform/)
