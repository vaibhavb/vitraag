---
author: vitraag
comments: true
date: 2011-10-13 06:38:00+00:00
layout: post
link: https://vitraagblog.wordpress.com/2011/10/12/healthvault-powershell-module-the-beginnings/
slug: healthvault-powershell-module-the-beginnings
title: HealthVault PowerShell Module - The beginnings.
wordpress_id: 358
categories:
- HealthVault
- hvposh
- Open Source
- PowerShell
---

Let me show you some awesomeness, and then I’ll explain what’s going on!<!-- more -->

PS C:UsersvaibhavbDesktop> **Import-Module HvPosh**
PS C:UsersvaibhavbDesktop> **Grant-HVaccess**

Is auth done?
Is Auth done - (Y)?
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help
(default is "Y"):y

PS C:UsersvaibhavbDesktop>** Get-Things weight | Format-Table**

When        Value       Key         TypeId      TypeName    EffectiveDa       State       Flags  IsPersonal IsDownVersi
te                                                     oned
----        -----       ---         ------      --------    -----------       -----       -----  ---------- -----------
10/12/2011  175 pounds  f7931e43... 3d34d87e... Weight M... 10/12/20...      Active        None       False       False
10/12/2011  385         d4b2e3ab... 3d34d87e... Weight M... 10/12/20...      Active        None       False       False
8/5/2011... 160         382e9e1f... 3d34d87e... Weight M... 8/5/2011...      Active        None       False       False
7/7/2010... 250 pounds  1a76d859... 3d34d87e... Weight M... 7/7/2010...      Active        None       False       False
…

PS C:UsersvaibhavbDesktop> **Add-Things weight 170
**PS C:UsersvaibhavbDesktop> **Get-Things weight | Format-Table**

When        Value       Key         TypeId      TypeName    EffectiveDa       State       Flags  IsPersonal IsDownVersi
te                                                     oned
----        -----       ---         ------      --------    -----------       -----       -----  ---------- -----------
10/13/2011  170 pounds  45abc16d... 3d34d87e... Weight M... 10/13/20...      Active        None       False       False
10/12/2011  175 pounds  f7931e43... 3d34d87e... Weight M... 10/12/20...      Active        None       False       False
10/12/2011  385         d4b2e3ab... 3d34d87e... Weight M... 10/12/20...      Active        None       False       False
8/5/2011... 160         382e9e1f... 3d34d87e... Weight M... 8/5/2011...      Active        None       False       False

So what is the cool thing going on above? Well in **five commands** we are able to authenticate, get and put weight readings in to HealthVault!

This is all possible owing to the magic of [powershell](http://en.wikipedia.org/wiki/Windows_PowerShell), and a powershell HealthVault module ([HvPosh](https://github.com/vaibhavb/HvPosh)). This is just a start, there all kinds of nerd scenarios this HealthVault command line shell can do! Think about command line automation for getting in all that data in to HealthVault, working with test data, understanding the healthvault xml, and doing all sorts of quantization on your personal health data!! The possibilities are limit-less, well at least for the command line nerds :).

**So what is HvPosh?**

HvPosh is a HealthVault powershell module currently running as a desktop client application. The source for this module is up on [github](https://github.com/vaibhavb/HvPosh) and you are welcome to contribute more functions, cmdlets, test data or infact various analysis modules!

Take HvPosh for a spin, and yep! this is right out of oven so be gentle!

[![image]({{site.images}}/2011/10/image_thumb.png)]({{site.images}}/2011/10/image.png)

Fig 1. HvPosh On [GitHub](https://github.com/vaibhavb/HvPosh).
