---
author: vitraag
comments: true
date: 2011-11-24 07:59:13+00:00
layout: post
link: https://vitraagblog.wordpress.com/2011/11/24/dynamic-attributes/
slug: dynamic-attributes
title: Dynamic Attributes
wordpress_id: 371
categories:
- meta-programming
---

Domain Specific Languages in ruby are easily possible owing to the ability to add attribute methods on the Module class.

You might have seen :

    
    class Module
      def attribute(*attribs)
        attribs.each do |a|
          define_method(a) { instance_variable_get("@#{a}") }
          define_method("#{a}=") { |val| instance_variable_set("@#{a}", val) }
        end
      end
    end
    
    class Person
      attribute :name, :email
    end
    
    person = Person.new
    person.name = "Gregory Brown"
    
    p person.name #=<span class="kwrd">></span> "Gregory Brown"



