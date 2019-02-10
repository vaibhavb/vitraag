---
author: vitraag
comments: true
date: 2017-07-25 01:39:43+00:00
layout: post
link: https://vitraagblog.wordpress.com/2017/07/24/setting-up-an-introductory-cybersecurity-lab-strategies-and-struggles/
slug: setting-up-an-introductory-cybersecurity-lab-strategies-and-struggles
title: Setting Up an Introductory CyberSecurity Lab — Strategies and Struggles
wordpress_id: 1560
categories:
- ramblings
tags:
- Cybersecurity
- Laboratory
---





**Editor’s Note:** It’s hard to put together an introductory cyber security lab, this post by Greg Moore details our efforts in this direction. Please provide feedback and links on what you think will be great tools and resources for students learning the art and craft of cyber defense!




![](https://vitraagblog.files.wordpress.com/2017/07/84662-14a-smmtbqfhnxjzbmzfejq.png)

A Prototype Cyber Security Lab (Source: ARL — US Army)

At Cyber Defenders, our mission is to bring students with little to no background in cybersecurity up to a knowledge level that allows them to work on meaningful research projects. The inaugural Cyber Defenders program has four project teams, each partnering with a different industry leader to work on a project in a growing and critical area of cyber security. The project topics for this year’s cohort are malware analysis ([GotMalware](https://medium.com/cyberdefenders/got-malware-meet-us-e725711a4fc1)), consumer data protection ([Pensieve](https://medium.com/cyberdefenders/our-secure-future-can-be-built-on-blockchains-introducing-pensieve-345668171532)), mobile healthcare application vulnerabilities ([HealthSec](https://medium.com/cyberdefenders/how-secure-are-your-health-apps-73043311d74)), and network security ([Raspi](https://medium.com/cyberdefenders/baking-a-raspberry-pi-to-capture-data-from-the-network-e5c89fb195ad)).




As most students entering the program have little to no background in cybersecurity, prior to beginning our project work we provide a general introduction to the field of cybersecurity via lab exercises, tutorials, and suggested reading. Below we enumerate the steps we have taken to provide that general introduction and background. We invite you, dear reader, to contribute any suggestions about learning aids or content structure that will help us improve our cybersecurity lab!




### **Labs**






  1. 
**CIA triad  
**We begin our introduction to cybersecurity with a discussion of the CIA triad (Confidentiality, Integrity, and Availability). This helps students conceptualize the ways that cybersecurity can be compromised and provides a useful starting point to introduce the various domains of cybersecurity that attempt to address these threat categories. As an exercise several types of attacks are presented (such as DDOS, password cracking, replay, etc) and students are asked to identify which letter(s) in the triad apply. CIA [tutorials](http://resources.infosecinstitute.com/category/certifications-training/cissp/domains/security-and-risk-management/the-security-cia-triad/#gref) and [videos](https://www.youtube.com/watch?v=szcmb-lcYV4).


  2. 
**Cryptography-  
**Cryptography is presented as the cybersecurity domain that attempts to guarantee confidentiality and integrity for electronic information. We begin the cryptography lesson by covering the concepts of encryption and hashing. This provides an opportunity to review some foundational math concepts like changing bases and performing logic operations such as AND, OR, XOR, etc. To help students visualize what occurs during encryption, we have the student download CrypTool and walk through an animated tutorial covering the steps involved in AES encryption (CrypTool>Individ. Procedures>Visualization of Algorithms>AES>Rijndael Animation). We then introduce the concepts of salting and nonces, and we explore the differences between symmetric and asymmetric cryptography. As an exercise, we go through different combinations of public key encryption, private key encryption, shared key encryption, hashing, salting, and use of nonces. Students are asked to identify whether the combinations provide assurances of Confidentiality and Integrity. We conclude the cryptography exploration with a tutorial that demonstrates password cracking using a provided Python program and rainbow table. Cryptography [Tutorials](https://www.guru99.com/how-to-make-your-data-safe-using-cryptography.html) and [Videos](https://www.youtube.com/watch?v=t8-aq_Rd5v0)



  3. 
**Network Security: **This lab provides an overview of networking and how network security strategies are deployed to address the Availability pillar of the CIA triad. The introduction to networking begins with a description of the OSI layer model. We walk through each layer and their associated protocol, protocol data unit, and keyterms (such as MAC address, IP, etc). We then examine the well-known traditional network attacks ping-of-death, DDOS, and botnet-mediated DDOS. The network security lab concludes with a wireshark exercise in which students perform packet capture and practice analyzing network traffic. Network Security [Tutorials](https://www.concise-courses.com/hacking-tools/packet-crafting-tools/wireshark/)-


  4. 
**Malware — **The malware lab begins with an overview of common types of malware and infection vectors. We cover concepts such as the reverse shell exploit, ransomware, and botnet generation. We then guide the students through installations of VirtualBox, KaliLinux, and Debian and then work through several tutorials that describe how malware can be generated using Metasploit and deployed. A favorite exercise involves walking students through infection of a pdf with a reverse callback shell in Metasploit. The students email the pdf to a dummy email account and open it on a Debian VM, and then control the Debian VM from their KaliLinux terminal. Following are some of the Malware Tutorials we use : [KaliLinux](https://www.youtube.com/user/kalinuxx), [Metasploit](https://www.offensive-security.com/metasploit-unleashed/), and [Building A BotNet](https://readwrite.com/2013/07/31/how-to-build-a-botnet-in-15-minutes/).


  5. 
**Data forensics **— The data forensics lab concludes our introduction to cyber security module. We begin with a discussion of file storage and erasure mechanisms. We then walk the students through a file recovery exercise using the forensic analysis tool Autopsy. Data Forensics [Tutorial](https://www.youtube.com/watch?v=e5O-d5M90EI).




### **Books**




We have found the following books to be extremely helpful for introducing concepts, providing background information, and serving as on-hand reference guides.






  1. Singer, Peter W., and Allan Friedman. **_Cybersecurity: What Everyone Needs to Know_**. Oxford University Press, 2014**. **[Link](https://www.amazon.com/Cybersecurity-Cyberwar-Everyone-Needs-Know/dp/0199918112/)



  2. Anderson, Ross J. **_Security engineering: a guide to building dependable distributed systems_**. John Wiley & Sons, 2010. [Link](https://www.amazon.com/Security-Engineering-Building-Dependable-Distributed/dp/0470068523/)



  3. Schneier, Bruce. **_Data and Goliath: The hidden battles to collect your data and control your world_**. WW Norton & Company, 2015. [Link](https://www.amazon.com/Data-Goliath-Battles-Collect-Control/dp/039335217X/)



  4. Regalado, Daniel, et al. **_Gray Hat Hacking the Ethical Hacker’s Handbook_. McGraw-Hill Education Group**, 2015. [Link](https://www.amazon.com/Hacking-Ethical-Hackers-Handbook-Fifth/dp/1260108414/)



  5. Anley, Chris, et al. **_The shellcoder’s handbook: discovering and exploiting security holes_**. John Wiley & Sons, 2011. [Link](https://www.amazon.com/Shellcoders-Handbook-Discovering-Exploiting-Security/dp/047008023X/)



  6. Marcella Jr, Albert J., and Frederic Guillossou. **_Cyber forensics: From data to digital evidence_**. Vol. 623. John Wiley & Sons, 2012. [Link](https://www.amazon.com/Cyber-Forensics-Data-Digital-Evidence/dp/1118273664/)





### **Suggested Hardware**






  1. Raspberry Pi: [Amazon](https://www.amazon.com/Vilros-Raspberry-Kit-Clear-Bluetooth-Connectivity/dp/B01D92SSX6/)



  2. Ethernet sniffer: [Amazon](https://www.amazon.com/midBit-Technologies-LLC-10-100/dp/B00DY77HHK/)



  3. Bluefruit (Bluetooth sniffer) at [Amazon](https://www.amazon.com/Adafruit-Bluefruit-Sniffer-Bluetooth-nRF51822/dp/B00SKWGPE0/), Ubertooth (Bluetooth sniffer) at [Amazon](https://hakshop.com/collections/wireless-gear/products/ubertooth-one)



  4. Rubber Ducky (USB keystroke injection tool) at [Hakshop](https://hakshop.com/products/usb-rubber-ducky-deluxe).


  5. Wifi Pineapple Router at [Hakshop](https://hakshop.com/products/wifi-pineapple)



  6. LAN Turtle at [Hakshop](https://hakshop.com/products/lan-turtle)





### **Suggested Software**






  1. Virtual Box : [https://www.virtualbox.org/wiki/Downloads](https://www.virtualbox.org/wiki/Downloads)



  2. Kali Linux VM: [https://www.offensive-security.com/kali-linux-vmware-virtualbox-image-download/](https://www.offensive-security.com/kali-linux-vmware-virtualbox-image-do)



  3. CrypTool: [https://www.cryptool.org/en/ct1-downloads](https://www.cryptool.org/en/ct1-downloads)



  4. Wireshark/Tshark: [https://www.wireshark.org/download.html](https://www.wireshark.org/download.html)



  5. Autopsy: [http://www.autopsy.com/download/](http://www.autopsy.com/download/)





### What else should we include? Suggestions?..



