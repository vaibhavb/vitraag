---
author: vitraag
comments: true
date: 2024-02-05 05:06:00+00:00
layout: post
slug: rails-on-m1-mac 
title: Rails on M1 Mac
categories:
    - rubyonrails
    - code
---
The following worked for me, you dont need to buy any tools like some definitive guides say.

``` bash
> brew install rvm
> rvm reinstall 3.3.0 --with-openssl-dir=/opt/homebrew/opt/openssl@3
> gem install rails
> rails --version
```
