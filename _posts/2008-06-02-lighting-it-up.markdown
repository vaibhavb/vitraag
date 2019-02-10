---
author: vitraag
comments: true
date: 2008-06-02 10:24:19+00:00
layout: post
link: https://vitraagblog.wordpress.com/2008/06/02/lighting-it-up/
slug: lighting-it-up
title: Lighting it up!
wordpress_id: 34
categories:
- HealthVault
- Open Source
- Python
- RubyOnRails
---

Alrite now that you have the firewood (application auth token) and the firestarter (user auth token) how can we start the fire (get details user's record).

Well first of all congratulations! most of the hard part is done!! Just a few more nitty gritty tricks though! In order to get the details about a user's health record, you need to use a method **GetPersonInfo**.

The XML for GetPersonInfo look like this:

[code lang=html]
<pre class="html">

  da9WYaQGEoseAYDOhJv2cwNIEVg=

</pre>
<header>GetPersonInfo 1 ASAAADNt1Jwbx85MgH9vkWzAINBxBWQFCtQ+osTzGw/I0Ty27OhKFCXUb83dxI5/M2mtGYymc1gKx6qwsWEtw31ZV/tyscJwmc5dNT2o2nYJcFTf1vfi/L4R5V68ckxFrd48Rz4jhU9Yg6lDhNTymCsJSDiVJCKLqKwcHcr/QSTsytRpVXBK7LpAVBicjC3OPGCEg4XE/UGwM7ZDAXlR4AR+emiHBaPOzSQD9iYMYxAyDBYZPde8N+rDv58zFw9pjDLJJIwvhXOOLahhFvX/n5DqwAb+BpdTlE19x5P/B67kKie/zDtEYWHEXHMhX+KNdvrxdm17l5pwt8JShIGimbXgAcZEFTiPVOW77mCgDxpc0U2ykcG7RVqXKTA3Gqt42OZf9aCuzq/J0wHOTLQvdx1ZYVOxo7+1TpMaW+13Fz5/jgOHR7hJZ/DPUIcKfCYdHS7phQ3r60nOReUl2qeq7rDvDmGQBWPjcCrT7CuQRSgZlyUpAav4DiFJtKh9U5DbJ5VW80dUAqcxamulklTxSR75Sb6v0X4T8B2zbfmVl+HtcupUIuz66Q== ASAAAE57vlXwS8VDupO6/FSWlMZR+OL02JQyhWvlesegc/J6f7XGgJq4xRW1WIWc7ZXufY9U1cAFeQMDF9pAvmNG1/1KGlp7FFFBdrUMk7gJLPpdTYkQeDMdp8UXcXNht+U6hJzpI7plchQKvpBMFeBj1XMOC15fLXRyfRFpD3RaIF66awgUVw== en US 2008-06-01T02:44:16.73Z 1800 0.9.1712.2902 1mWxpY+leClypXQzPvDBLFIBDpI=</header>
[/code]

So now do we go about concoting the seemingly complicated xml above. Well we already have the token and wctoken from our previous CreateAuthenticatedSession and Shell -redirect. Use the token for the auth-token in line 9 and the wctoken as user-token in line 10.

Most of the elements in the header section are straight forward. The one to comment about is hash-data (line 18). The hash in this case is SHA-1 hash of the info section. Matter of fact our info section is empty so that make sure that the SHA-1 hash is done right. In ruby i do it the following way (using OpenSSL):

[code lang=ruby]
def self.doSha1(text)
    Base64.encode64(OpenSSL::Digest::SHA1.digest(text)).chomp
end
[/code]

Now the interesting part - whats this auth on line 2? Well auth is a HMAC of header (line 5-20) section. Remember we generated the shared secret in CreateAutheticatedSession method? Now use that secret to do a HMAC digest for the header. In ruby i do it the following way:

[code lang=ruby]
def self.doHmac(secret, payload)
    key = Base64.decode64(secret)
    hashmac = OpenSSL::HMAC.digest(OpenSSL::Digest::SHA1.new(key), key, payload)
    Base64.encode64(hashmac).chomp
  end
[/code]

secret is the shared secret used for createauthenticationtoken.

Now the fun part,caveats:




    
  * Don't leave any white spaces between you xml tags. HealthVault behaves weird sometime when their is white space.

    
  * If you are getting an error saying code 3 (which implied invalid xml) and you are sure that your xml is correct, then most likely your auth section or your hash-data section are not proper. Which in turn implies that your HMAC-ing or SHA-1 hashing is a little off. The best way to actually resolve this is to first write tiny parts which make sure that the HMAC /SHA-1 is same for a known successfully call. You can get the xml for such a call from HealthVault SDK, the process is described [here](http://healthblog.vitraag.com/2008/06/curious-about-whats-under-the-healthvault-sdks-hood/). However for ease of testing i'm appending know good calls below.



**PLEASE NOTE**: Remove all the white-space between tags before testing your crypto functions to match the result seen here. I have put the white space for readability.

CreateAuthenticatedSessionToken (for SharedSecret)

[code lang=html]
<header>CreateAuthenticatedSessionToken 1 05a059c9-c309-46af-9b86-b06d42510550 en US 2008-06-01T02:44:16.21Z 1800 0.9.1712.2902</header>05a059c9-c309-46af-9b86-b06d42510550 b2uCbONZDGj8jDYhz3e5PcJfugPQTHOsOvpZ6kA9uG5XzQXV+EHtXtTDAbwHbFyNozC1uR7uZwgi44pfgw4NyQp8LO2PwI9E7pOx/Ho7+6siY41sjI5+frhq2fcj8iljpG8EK07WGDuf4JeFg5yc8IWjHHtUwabpdPVJWYLi18+Gk7AaFfCuM1iQwFbBSWWMyckCe3V48JaCZcNVcS/XuJJovFdsM9QnZ1CwrQaaBB/evf1u1YGM3fXpVeCjVWPXpHiu3WWVVsJ5aURtCzGvXJe9R7Gh10sYDSG6wC/CJvcBSJlRCpacA1qds2gcMCBwO+iDCPY3I15+FbM0E9D+Qw== 05a059c9-c309-46af-9b86-b06d42510550 RXziN4RDYIu89cu+cOp4POLhKUCSUb0sPsV9yaz8m6BfJxjpDNUBRUF5MU3OJMJ7DH0FPXg8HFuahbvSz1HxG1Q6MlahpHAmUkXNBJ0zcrKvcH3+NiS3qD26FkpLXsvzjNv/QSxwqRMpYnDhY11RkUkOvz2M2Ybg9H5aEe7RpfYCYwEAudpj05J2KEFMP2WO1Q6Kz8hjIhf2QdswgzvLueUQ2ajG8Al9DvpGWLKl4dGNqnY1/FUnJOZq/nPivTYHYOcH/qpC5euWIt7bU6hXRehAIC9IYTbHG32jLBoIxhM79Wtj2sRdn4j3SBk/QVqQNXyPrAgFIzmtR7CSaN393A==
[/code]

Successful GetPersonInfo using the above SharedSecret:

[code lang=html]
da9WYaQGEoseAYDOhJv2cwNIEVg=
<header>GetPersonInfo 1 ASAAADNt1Jwbx85MgH9vkWzAINBxBWQFCtQ+osTzGw/I0Ty27OhKFCXUb83dxI5/M2mtGYymc1gKx6qwsWEtw31ZV/tyscJwmc5dNT2o2nYJcFTf1vfi/L4R5V68ckxFrd48Rz4jhU9Yg6lDhNTymCsJSDiVJCKLqKwcHcr/QSTsytRpVXBK7LpAVBicjC3OPGCEg4XE/UGwM7ZDAXlR4AR+emiHBaPOzSQD9iYMYxAyDBYZPde8N+rDv58zFw9pjDLJJIwvhXOOLahhFvX/n5DqwAb+BpdTlE19x5P/B67kKie/zDtEYWHEXHMhX+KNdvrxdm17l5pwt8JShIGimbXgAcZEFTiPVOW77mCgDxpc0U2ykcG7RVqXKTA3Gqt42OZf9aCuzq/J0wHOTLQvdx1ZYVOxo7+1TpMaW+13Fz5/jgOHR7hJZ/DPUIcKfCYdHS7phQ3r60nOReUl2qeq7rDvDmGQBWPjcCrT7CuQRSgZlyUpAav4DiFJtKh9U5DbJ5VW80dUAqcxamulklTxSR75Sb6v0X4T8B2zbfmVl+HtcupUIuz66Q== ASAAAE57vlXwS8VDupO6/FSWlMZR+OL02JQyhWvlesegc/J6f7XGgJq4xRW1WIWc7ZXufY9U1cAFeQMDF9pAvmNG1/1KGlp7FFFBdrUMk7gJLPpdTYkQeDMdp8UXcXNht+U6hJzpI7plchQKvpBMFeBj1XMOC15fLXRyfRFpD3RaIF66awgUVw== enUS2008-06-01T02:44:16.73Z 18000.9.1712.29021mWxpY+leClypXQzPvDBLFIBDpI=</header>
[/code]

Sweet!!! you wanna check out th lighted application? Well its [live...](http://openhealthvault.vitraag.com) (Please Note: it will prompt you yo sign in with HealthVault id, its still rough around edges and doesn't deal with corner cases).

So lets see your LAMPR application lighted up soon..

Next time: [How to do offline access and use PutThings ](http://healthblog.vitraag.com/2008/08/putthings-for-offline-access/)
