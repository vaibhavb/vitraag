---
author: vitraag
comments: true
date: 2009-12-03 03:30:21+00:00
layout: post
link: https://vitraagblog.wordpress.com/2009/12/02/memoization/
slug: memoization
title: Memoization
wordpress_id: 226
categories:
- Programming
---

I have been meaning to write short posts about interesting programming concepts and alternative programming movements (like [alt.net](http://altdotnet.org/)). Topic of this post is an interesting programming concept called Memoization and its implementation in C# as a method attribute. 

 

[Memoization](http://en.wikipedia.org/wiki/Memoization) is an optimization technique which speeds up a program by remembering the values returned by function calls for specific input values, its also known as tabling.

 

Many of the new languages (Ruby, Python, C#) provide a very neat way to implement Memoization and many functional languages (Lisp, OCaml) have it as a first class construct for the runtime. Here is a my cheap implementation showing how one can use an integer based **Memo **attribute in C#

 
    
    <span style="color:blue;"><font size="2">class </font></span><font size="2"><span style="color:#2b91af;">Test
    </span>{   [<span style="color:#2b91af;">Memo</span>]
        <span style="color:blue;">public int </span>DoSomething(<span style="color:blue;">int </span>i)
        {
            <span style="color:blue;">for </span>(<span style="color:blue;">int </span>k = 0; k < 10000; k++)
            {
                <span style="color:blue;">int </span>j = 0;
                j = j + 500;
            }
            <span style="color:#2b91af;">Console</span>.WriteLine(<span style="color:#a31515;">"DoSomething " </span>+ i);
            <span style="color:blue;">return </span>i + 5;
        }
    }</font>


[](http://11011.net/software/vspaste)



Here is a simple driver which implements the Memoization :




    
    <font size="2"><span style="color:blue;">static void </span>Main(<span style="color:blue;">string</span>[] args)
     {
         <span style="color:#2b91af;">Debug</span>.WriteLine(<span style="color:#a31515;">"Invoking Memoizable Code"</span>);
         
         <span style="color:#2b91af;">Type </span>t = <span style="color:blue;">typeof</span>(<span style="color:#2b91af;">Test</span>);
         <span style="color:#2b91af;">Test </span>objT = <span style="color:blue;">new </span><span style="color:#2b91af;">Test</span>();
    
         </font><font size="2"><span style="color:green;">// Implement Memoization
         </span><span style="color:#2b91af;">Dictionary</span><<span style="color:blue;">int</span>, <span style="color:blue;">int</span>> <a href="http://en.wikipedia.org/wiki/Memoization" class="zem_slink" rel="wikipedia" title="Memoization">memoize</a> = <span style="color:blue;">new </span><span style="color:#2b91af;">Dictionary</span><<span style="color:blue;">int</span>, <span style="color:blue;">int</span>>();
         <span style="color:#2b91af;">MethodInfo</span>[] mi = t.GetMethods();
         <span style="color:blue;">foreach </span>(<span style="color:#2b91af;">MethodInfo </span>m <span style="color:blue;">in </span>mi)
         {
             <span style="color:blue;">foreach </span>(<span style="color:#2b91af;">Attribute </span>a <span style="color:blue;">in </span>m.GetCustomAttributes(<span style="color:blue;">false</span>))
             {
                 <span style="color:blue;">if </span>(a <span style="color:blue;">is </span><span style="color:#2b91af;">MemoAttribute</span>)
                 {
                     <span style="color:blue;">for </span>(<span style="color:blue;">int </span>i = 0; i < 2; i++)
                     {
                         <span style="color:blue;">int </span>j;
                         <span style="color:blue;">if </span>(memoize.TryGetValue(i, <span style="color:blue;">out </span>j))
                         {
                             <span style="color:#2b91af;">Debug</span>.WriteLine(<span style="color:#a31515;">"Remembered " </span>+ i);
                             <span style="color:blue;">continue</span>;
                         }
                         </font><font size="2"><span style="color:blue;">else
                         </span>{
                             j = (<span style="color:blue;">int</span>) m.Invoke(objT, <span style="color:blue;">new object</span>[]{i});
                             memoize[i] = j;
                             <span style="color:#2b91af;">Debug</span>.WriteLine(<span style="color:#a31515;">"Memorized " </span>+ i);
                         }
                     }
                 }
             }
         }
         <span style="color:#2b91af;">Console</span>.ReadLine();
     }</font>


[](http://11011.net/software/vspaste)
  

May be in comments you can suggest ways to implement a more generic Memo attribute (similar to Python’s @memo).
