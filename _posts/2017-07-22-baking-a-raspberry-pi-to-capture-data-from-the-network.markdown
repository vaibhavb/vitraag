---
author: vitraag
comments: true
date: 2017-07-22 01:16:29+00:00
layout: post
link: https://vitraagblog.wordpress.com/2017/07/21/baking-a-raspberry-pi-to-capture-data-from-the-network/
slug: baking-a-raspberry-pi-to-capture-data-from-the-network
title: Baking a Raspberry Pi to Capture Data from the Network
wordpress_id: 1557
categories:
- ramblings
tags:
- Network Security
- Surveillance
- Team Raspberrypi
---





![](https://cdn-images-1.medium.com/max/800/0*s3K_GbDzI9goE222.)

Its Raspberry PI Securing Your Lawns! (Source: TBA)

**Editor’s Note:** This article describes the project Network Security with IoTs to explore Network Security concepts and implement security devices, it’s been developed with help from [Lib13 Inc](http://www.lib13.com) as part of the Cyber Defenders 2017 Program.




### Introduction




We are part of the Cyber Defenders program and our project is to set up a raspberry pi as a network surveillance system and explore concepts of network security.




We are configuring raspberry pi to perform packet capture and writing a software that allows a system administrator to remotely monitor network traffic in a customized manner, the Raspberry Pi will function as a DDOS detection that will sound an alarm when detecting malicious activity. Finally, the raspberry pi will release reports to the remote user through email, providing data on the network traffic.




### Our Approach




During the first few days of the project, our team started off by learning how to setup a Raspberry Pi to open tshark to capture packets from the network traffic. This experience gave us an insight on how a microcontroller, like the raspberry pi, can be efficient and small to complete this task. Next, we were thinking about possibilities on how we wanted our raspberry pi to do after it captured packets. We thought about setting up an alarm if the raspberry pi captured an IP address that appeared on the different packets.




Then, we came up with the idea of placing a raspberry pi inside a case and place it at a location on campus, where it is hidden from public view.




In addition, we took the time to do some research and learn about other graduate students who worked on raspberry pi and doing data packet capturing projects. This helped us understand more of our project and look at some analysis that students worked on.




Each member of the group started off by researching the principles of the whole project, meaning we learned how Wireshark works and how to capture packages using tshark. After, the members decided to find three resource per person, which means we had a total of six resources. The resources helped us divide the project into sections in order to progressively accomplish the project. The resources helped us accomplish our goals because of the available information, like articles or blog posts, easily accessed online.




### Progress So Far




We started with making a simple text input to output program to use a text file that came from tshark.Then we strip off redundant information from the text file, in order to apply important information, such as the packet number, the time the packet was captured, source IP, destination IP, protocol, and length. So far, the only information that we used from this text file was the number of packets and source IP.




On Python, we’ve made a constructor for all of the information we would need from a packet. We used a for loop to scan over all of the packets; making an algorithm to search for each line on every packet. We then place that information inside an array to be analyzed for any intrusions. Everything else seemed simple enough to perform on our Python code: added a stop switch in the program (Ctrl-C), installed “pregame” to have it play a sound if there is an intrusion detected, and finally send an email on what’s happening on a server.




### Challenges — Need Help!




One of our challenges was figuring out how to grab the packet data. We’ve attempted with many output formats in shark, but most of it came out in a scrambled mess in a text format. The best format we choose was an XML format since it displays the information very organized than the other text files. The next challenge was thinking on how to retrieve the information in python. We didn’t have any knowledge about creating constructors in Python and store the output text file to the objects. Eventually, after hours going through online and learning about constructors, we found out that creating a for loop to scoop every line, was our best bet. We use the for loop to read every line that a packet contained and applying a single array to store the information. Performing this task simultaneously was difficult, however, we learned that using a 2-dimensional array to get all the information came in use. After that, everything else seemed easy to implement in Python.




### Code Review




You can review our progress and the code at our github repository: [https://github.com/cyberdefenders/NetworkSecurity](https://github.com/cyberdefenders/NetworkSecurity)



