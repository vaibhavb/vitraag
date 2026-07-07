---
author: vitraag
comments: true
date: 2026-07-06T00:00:00Z
layout: post
slug: timelens-your-personal-historian
title: "TimeLens — Your Personal Historian (and Please, Break It)"
categories:
    - vitraagcollective
    - swiftui
    - sanfrancisco
    - feedback
---

I've walked past the Ferry Building in San Francisco more times than I can count, and for years it was basically wallpaper. A big clock tower you stop noticing the same way you stop noticing your own kitchen.

A few weeks ago I started a dumb little side project to fix that, and it turned into something I actually open now: **TimeLens**. Point your phone at a place, and it shows you what that same spot looked like decades ago — then lets you drag a slider between "then" and "now" like you're personally responsible for time itself.

---

## Why "historian," specifically

Here's the moment that actually got me hooked: standing at the Ferry Building, just looking at it, and realizing I had no idea what its story was — which bugged me way more than it should have. I like history. I like walking around cities and wondering what used to be where I'm standing. So I started digging, and it turns out there used to be an entire elevated freeway running right along the waterfront in front of the building — the Embarcadero Freeway — until it got cracked up badly enough in the 1989 earthquake that the city just tore the whole thing down instead of fixing it. I'd been standing where a highway used to be, for years, without a clue.

And then it gets better: for a long stretch of the city's history, the ground I was standing on wasn't ground at all. Most of that stretch of the Financial District behind the Ferry Building is landfill — old piers, sunken Gold Rush-era ships, decades of junk paved over. The "land" is younger than the building on it.

That's the itch TimeLens is actually scratching. Not just "here's an old photo of this spot" but "here's the actual story of the dirt under your feet" — a bridge that isn't there anymore, a bay that used to lap right up to where you're standing, a building that burned down and got rebuilt twice. I want that story available in five seconds on my phone instead of staying locked in some Wikipedia rabbit hole I never actually open. Hence: your personal historian.

## The idea

Nothing fancy, I promise. Open the app, it figures out (roughly, we're not launching satellites here) what landmark you're near, and pulls up a timeline of archival photos for that spot. Tap through the years, pick one, and slide between the old photo and today's view.

The first place I built this for is the Ferry Building, because it's a five-minute walk from my apartment and has a genuinely great photographic record — a 1901 postcard, a 1912 shot from the Panama-Pacific Exposition era (the tower already has "1915" lit up on it, which delights me disproportionately), a 1939 Bay Bridge-era postcard, a 1980 night shot, and a 2017 restored-marketplace photo.

Here's what that actually looks like:

[![TimeLens: Ferry Building timeline and then/now compare](/assets/images/2026/2026-TimeLens-Ferry-Building-Then-Now.png)](/assets/images/2026/2026-TimeLens-Ferry-Building-Then-Now.png)

Left screen: pick a year off the timeline and get a bit of context on what was going on then. Right screen: the actual reason this app exists — drag that little circle left and right and watch 1901 dissolve into today. There's something genuinely arresting about seeing the same clock tower, same proportions, 125 years apart, with your thumb doing the time traveling. I've shown this to exactly four people and all four of them stood there sliding it back and forth like it was a fidget toy. Mission accomplished, I guess.

## Why I'm building it

Mostly for me, if I'm honest. I like history, I like walking around cities, and I wanted something that turns "huh, I wonder what this looked like before" from a whole research rabbit hole into a five-second glance. No login, no feed, no algorithm trying to keep you engaged — just a camera and a slider. The lowest-stakes app I could think to build.

Right now it really only knows the Ferry Building well. A few other SF landmarks — Coit Tower, Palace of Fine Arts, Mission Dolores, Sutro Baths — are stubbed in but photo-less, like a house with the frame up and no drywall yet. The plan is to keep curating more spots over time, mostly pulling from Library of Congress and Wikimedia Commons archives, with proper licensing and attribution baked in rather than bolted on later in a panic.

## What I actually want from you

Here's the real reason for this post: I want to know if this is interesting to anyone besides me, and I want to know before I sink another month into landmark #2.

- Would you actually use something like this on a walk?
- Is "then/now slider" the fun part, or is the context blurb the fun part?
- What's the second landmark I should chase down archival photos for?

Tell me I'm wrong, tell me it's neat, tell me the slider is laggy — all useful.

## Want to try it?

I just moved the app over to a proper Apple Developer account, so I can finally hand out TestFlight builds instead of just showing people my phone. If you're in the Bay Area (or just curious enough to poke at it remotely), **send me a note** and I'll add you as a tester — no App Store review to wait around for, just an invite and the TestFlight app.

Reply here, DM me, or email me — whatever's easiest — and let me know you want in.

---

*Built with SwiftUI, currently SF-only, more landmarks coming as I find archival photos worth featuring.*
