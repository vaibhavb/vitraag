---
author: vitraag
comments: true
date: 2011-10-28 18:14:03+00:00
layout: post
link: https://vitraagblog.wordpress.com/2011/10/28/implementing-method_missing-in-c/
slug: implementing-method_missing-in-c
title: Implementing Method_Missing in C#
wordpress_id: 363
categories:
- meta-programming
- Programming
- RubyOnRails
---

Heart of the _ruby on rails_ magic in creating a very expressive and eloquent web development framework is the use of ruby’s [method_missing](http://ruby-doc.org/docs/ProgrammingRuby/html/ref_c_object.html#Object.method_missing).

Following is an example of method_missing in action :

    
    class Roman
      def romanToInt(str)
        # ...
      end
      def <span style="color:#ff0000;"><strong>method_missing</strong></span>(methId)
        str = methId.id2name
        romanToInt(str)
      end
    end


**<!-- more -->Results:**

    
    <strong>r = Roman.new
    r.iv
    »
    4
    r.xxiii
    »
    23
    r.mm</strong>




Following is a C# 4.0 equivalent using the **dynamic** keyword.

    
    <span class="kwrd">using</span> System;
    <span class="kwrd">using</span> System.Dynamic;
    <span class="kwrd">namespace</span> Vitraag.MetaProgramming
    {
        <span class="kwrd">class</span> Program
        {
            <span class="kwrd">static</span> <span class="kwrd">void</span> Main(<span class="kwrd">string</span>[] args)
            {
                <span style="color:#ff0000;">dynamic</span> Caesar = <span class="kwrd">new</span> Roman();
                Console.WriteLine(Caesar.IV);
                Console.ReadKey();
            }
        }
    
        <span class="kwrd">class</span> Roman: <strong><span style="color:#ff0000;">DynamicObject</span></strong>
        {
            <span class="kwrd">int</span> StringToRoman(<span class="kwrd">string</span> s)
            {
                <span class="rem">// Simple logic needs a better function</span>
                <span class="kwrd">switch</span> (s)
                {
                    <span class="kwrd">case</span> <span class="str">"I"</span> : <span class="kwrd">return</span> 1;
                    <span class="kwrd">case</span> <span class="str">"IV"</span>: <span class="kwrd">return</span> 4;
                    <span class="rem">// Should add more cases</span>
                    <span class="kwrd">default</span>: <span class="kwrd">return</span> 0;
                }
            }
    
            <span class="kwrd">public</span> <span class="kwrd">override</span> <span class="kwrd">bool</span> <strong><span style="color:#ff0000;">TryGetMember</span></strong>(GetMemberBinder binder,
                 <span class="kwrd">out</span> <span class="kwrd">object</span> result)
            {
                result = StringToRoman(binder.Name);
                <span class="rem">// This logic could be improved</span>
                <span class="kwrd">if</span> ((<span class="kwrd">int</span>)result != 0)
                {
                    <span class="kwrd">return</span> <span class="kwrd">true</span>;
                }
                <span class="kwrd">return</span> <span class="kwrd">false</span>;
            }
        }
    }




Running the above code gives us the result as: **4**

I’ll be adding more thoughts in coming weeks around meta-programming and having an extensible type and formatting system. Please feel free to share your best reads or comments on the topic below!
