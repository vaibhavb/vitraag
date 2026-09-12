---
author: vitraag
comments: true
date: 2026-09-11T00:00:00Z
layout: post
slug: jain-magic-squares-a-meditation-on-thirty-four
title: "Jain Magic Squares: A Meditation on Thirty-Four"
categories:
    - jainism
tags:
    - jainism
    - paryushan
    - shyamapana
---

[![The Khajuraho Jain magic square](/assets/images/2026/2026-khajuraho-jain-magic-square.png)](/assets/images/2026/2026-khajuraho-jain-magic-square.png)

Over the last few years, I have used Paryushan, a holy period in Jainism culminating in Samvatsari in the Shwetambar tradition, to pause and reflect. I usually spend some of this time with philosophical readings, particularly readings about Jainism ([more on that here]({% post_url 2024/2024-09-07-jain-links %})). This year, I am trying something a little different. Alongside the philosophy, I am adding some Jain mathematics and art.

One thing that caught my attention is the magic square inscribed at the Parshvanath Jain temple in Khajuraho. The temple is believed to have originally been dedicated to Adinath. There is something fascinating about finding a mathematical object in a place like this: carved in stone, surrounded by art, in a space meant for contemplation. ([Temple history](https://en.wikipedia.org/wiki/Parshvanatha_temple,_Khajuraho))

Manjul Bhargava, one of my favorite number theorists, recently explored this square in his ICM 2026 public lecture, [Magic Squares, Cubes, and Hypercubes: From Ancient Origins to Recent Advances](https://www.youtube.com/watch?v=of8Maaq1Fsg). What drew me in was how he moved from this old inscription to a much larger mathematical idea.

The square contains every number from **1 to 16**, each appearing once:

| 7 | 12 | 1 | 14 |
|:---:|:---:|:---:|:---:|
| 2 | 13 | 8 | 11 |
| 16 | 3 | 10 | 5 |
| 9 | 6 | 15 | 4 |

It is called the **Chautisa Yantra**, roughly, the "thirty-four machine." Every row, every column, and both main diagonals add up to **34**. But that is only the beginning.

Take the four corners: **7 + 14 + 9 + 4 = 34**. Take the four numbers in the center: **13 + 8 + 3 + 10 = 34**. Move a little two-by-two window around the square, and its four numbers still add up to 34.

It even works across the edges. Imagine the right edge joining the left, and the bottom joining the top. A small block straddling the right and left edges gives **14 + 7 + 11 + 2 = 34**. Follow a diagonal that continues across an edge, and you can find **12 + 8 + 5 + 9 = 34**.

Of course, this does not mean that any four numbers you pick will add up to 34. It is the arrangement that matters. The more carefully you look, the more relationships you find.

[![Chautisa Yantra explained](/assets/images/2026/2026-chautisa-yantra-explained.png)](/assets/images/2026/2026-chautisa-yantra-explained.png)

This is where Bhargava's graph picture helped me. Think of each number as a dot, with lines connecting neighboring dots. Then connect opposite edges, so that the graph wraps around in both directions. Every loop of four edges through four distinct dots has the same sum: 34. Some of those loops look like ordinary little squares. Others travel around the joined edges. Even a whole row becomes a four-edge loop.

The surprising next step is that this graph has the same connections as the vertices and edges of a four-dimensional cube. There are 16 vertices, just as there are 16 numbers here. Each square face has four vertices, and the labels on those vertices add up to 34. The flat inscription gives us a way to look at a structure that is much harder to picture directly.

The theorem in his slides takes this further: magic-faced cubes of order two exist in every dimension, with a uniqueness statement under a particular family of natural transformations. Here, "order two" means two positions along each dimension. "Unique" does not mean there is only one way to write the numbers on the page; it means the solutions are equivalent under those transformations. For the four-dimensional case, the counting formula shown in the lecture gives **2⁴ × 5! = 1,920** labelings.

I do not need to hold the whole theorem in my head to enjoy this. I can start with four numbers, check their sum, and follow another path. There is something very meditative about that. My attention slows down. A square that looked simple begins to reveal more depth.

For me, that makes this more than a mathematical experience. It becomes a spiritual experience too. I am not claiming that this was the inscription's original purpose. It is simply how I experience it: a small invitation to look closely, stay with something, and notice what I missed the first time.

This Paryushan, alongside the philosophical readings, I am spending a little time with these sixteen numbers. Mathematics, art, and reflection meet here in a way I want to keep exploring.

*Michhami Dukkadam.*

---

*Illustration caption: The Chautisa Yantra at Khajuraho, rewritten in modern numerals. Rows, columns, diagonals, and every four-cycle of its wrap-around grid graph sum to 34. Diagram and theorem explanation adapted from the supplied slides of Manjul Bhargava's ICM 2026 public lecture.*
