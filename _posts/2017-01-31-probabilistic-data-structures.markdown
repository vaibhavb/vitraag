---
author: vitraag
comments: true
date: 2017-01-31 00:51:58+00:00
layout: post
link: https://vitraagblog.wordpress.com/2017/01/31/probabilistic-data-structures/
slug: probabilistic-data-structures
title: Optimal Frequency Calculation
wordpress_id: 1501
categories:
- algorithms
---

Different algorithms and structures have been used to solve rate-limiting. In this post I want to focus on use of probabilistic method & [count-min](https://en.wikipedia.org/wiki/Count%E2%80%93min_sketch) sketch in particular.



## Why



To save space or time. It approximates the result.

There is extensive research on solving the membership problem using data structures from hash tables to balanced trees and B-tree indices, and these form the backbone of systems from OSs, compilers, databases and beyond. Many of these data structures have been in widespread use for forty or more years.

Count-min consumes a stream of events and produces approximate frequency of each of the events. It can be queried for frequency of a certain event and it will return the frequency of that event with certain probability.



## Usage



Compressed sensing, Networking, Databases, NLP, Security (cryptography, finding primes), Computation Geometry (finding vertices),  Machine Learning.



## Implementation



Simple python implementation from [github](https://github.com/rafacarrascosa/countminsketch/blob/master/countminsketch.py).

[code lang=python]
def query(self, x):
"""
Return an estimation of the amount of times 
`x` has occurred. The returned value always 
overestimates the real value.
"""
return min(table[i] for table, i in zip(self.tables, 
                                           self._hash(x))
[/code]



## References






    
  * Count-Min C Implementation - https://sites.google.com/site/countminsketch/home

    
  * Count-Min Go Implementation - https://github.com/tylertreat/BoomFilters

    
  * Algorithms to live by - http://algorithmstoliveby.com/

    
  * C-Implementation - http://www.cs.rutgers.edu/∼muthu/ massdal-code-index.html


