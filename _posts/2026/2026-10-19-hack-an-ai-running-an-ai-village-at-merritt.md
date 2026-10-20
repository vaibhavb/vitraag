---
author: vitraag
comments: true
date: 2026-10-19T00:00:00Z
layout: post
slug: hack-an-ai-running-an-ai-village-at-merritt
title: "Hack an AI: Running an AI Village at Merritt"
categories:
    - ai
    - cyber security
    - education
---

[![Hack an AI table tent](/assets/images/2026/2026-aivillage-hero-table-tent.jpg)](/assets/images/2026/2026-aivillage-hero-table-tent.jpg)

*The table tent: scan, sign up, and try to hack an AI.*

Last Friday I ran an AI Village at the Merritt College Cybersecurity Job Fair & Employer Day. The pitch on the table tent was three words: hack an AI. Students scanned a QR code, signed up on their phone, and tried to talk a chatbot into giving up a secret.

## Why I wanted to do this

Every employer at the fair is putting AI into something: a chatbot, a help desk, an email assistant. Very few of the students I work with have ever tried to break one. Most AI security talks explain prompt injection. I wanted students to do it.

Prompt injection is also the one hack you can do with nothing but words. No exploit code, no tools to install. For a student who has never hacked anything, getting a chatbot to hand over its password is a real first win, and a good story for the next employer table.

So the plan was four steps: sign up, learn, hack, compete. Everyone who signed up got a month of TryHackMe Premium and a custom module of six AI security rooms. Two guided labs let them break a chatbot and hijack an AI email agent. A small prompt injection CTF with a live scoreboard was there for anyone who wanted more.

## Building it on my home lab

I didn't want an API bill, or student chats going to an AI company. So the AIs ran on a small AMD mini PC in my home lab, a Radeon 780M running Qwen3 30B on llama.cpp. It does about 36 tokens a second and four conversations at once, which is plenty for a booth. The sign-up page and CTF ran on Cloudflare, and I kept OpenRouter with the same model as a backup in case the room got busy. We never needed it.

The part I enjoyed most was the receipt printer. It's the same little thermal printer I have been using at home to print poems: Rumi, Kabir, Ghalib, verses from the Bhaktamar. It talks through an old parallel port and a USB adapter, and it kept printing garbage until I sent it the image in small strips with a pause in between. For one day it printed hacker receipts instead: a hacker number, a checklist of rooms and labs, and a box for every CTF flag.

[![The AI Village booth](/assets/images/2026/2026-aivillage-booth.jpg)](/assets/images/2026/2026-aivillage-booth.jpg)

*The booth: receipt printer, table tent, and three laptops for TryHackMe, the AI Labs and the CTF.*

## How it went

19 students signed up and got their TryHackMe invites the same day. 4 of them played the CTF and captured 8 flags. Everyone who played solved the first challenge, and nobody got past the Output Filter.

That gap taught me the most. A job fair is not a CTF. Students had a few minutes between employer tables, not fifteen. The sign-up and the free TryHackMe month fit that time. The harder challenges did not.

[![A full room for the talks](/assets/images/2026/2026-aivillage-talk.jpg)](/assets/images/2026/2026-aivillage-talk.jpg)

*A full room for the talks at the job fair.*

## What I would change

Next time I want to run short group demos on the big screen at set times. Five minutes, one chatbot, the whole crowd shouting ideas. Then point people to the labs and the CTF to keep going at home. And a small prize for the top score never hurts.

## Try it yourself

The full write-up, with all the numbers, is on the [Cyber Defenders Program site](https://www.cyberdefendersprogram.com/aivillage/). Both labs and the CTF are open source at [github.com/cyberdefendersprogram/aivillage](https://github.com/cyberdefendersprogram/aivillage). If you teach security, use them in your class, and tell me how it goes.

Only hack AI you have permission to test.
