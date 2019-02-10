---
author: vitraag
comments: true
date: 2017-07-22 00:50:19+00:00
layout: post
link: https://vitraagblog.wordpress.com/2017/07/21/how-secure-are-your-health-apps/
slug: how-secure-are-your-health-apps
title: How Secure Are Your Health Apps ?
wordpress_id: 1559
categories:
- ramblings
tags:
- Appsec
- Cybersecurity
- Healthcare
- Mobile Security
- Team Healthsec
---





![](https://cdn-images-1.medium.com/max/800/0*S9R-ksZ-9WEDwTvY.)

The False Promise of HIPPA for Health Security (Source: healthsecurity.com)

**Editor’s Note: **This article describes the project HealthSec to explore software vulternabilites in healthcare mobile apps, its Michael Navarro and Shishir Paudel for DHXLabs & [Lib13 Inc](http://www.lib13.com) in collaboration with Appthority, as part of the Cyber Defenders 2017 Program.




### **Hello!**




Greetings from Team HealthSec! We are Michael Navarro and Shishir Paudel from the 2017 Cyber Defenders program. Our group is interested in the software vulnerability domain of cybersecurity and our project focuses on the security vulnerabilities of mobile applications for healthcare. Our team has been partnered with Appthority, an infosec company that provides security software and consultation for mobile devices at the enterprise-level. DHX Labs, in conjunction with Appthority, asked us to help them develop and enhance an application security report and elaborate its operational characteristics with a focus on healthcare and fitness apps. We were curious — why health care? Well after some research, we learned that the healthcare industry is woefully behind the times in their implementation of cyber security.




### **Healthcare Security Is SubStandard**




The unfortunate state of cybersecurity in healthcare is the result of healthcare organizations failing to prioritize it. Cybersecurity has historically been a low priority because healthcare computer systems don’t store monetary assets or trade secrets. However, as current events attest, if hospitals and healthcare organizations don’t create secure networks, hackers can easily shut away vital information; information that doctors need to help their patients.




Healthcare is becoming more and more popular for cybercriminals to target. The medical records of a patient include their **social security number, date of birth, name, address, email, and occupation**. At one point, medical records were sold on the darkweb for upwards of $500 per record. In 2017, it is so easy to steal medical records that the supply of records have far outweighed the demand, resulting in a price of less than one cent per medical record when bought in bulk. Health Care needs to step up their cybersecurity game unless it wants to continue to be a cyber goldmine.




Perhaps the most driving reason for a hospital, which is a business, to improve their cybersecurity is to avoid violating the HIPAA (Health Insurance Portability and Accountability Act of 1996). As more and more cyber criminals target healthcare systems to make money, it is becoming more and more apparent that most hospitals and healthcare systems are not up to par with HIPAA regulations. Breached hospitals are paying upwards of $5.5 million in settlements. Hospitals should start prioritizing investing in their cybersecurity, so they can avoid lawsuits and protect their patients’ private information. An ounce of prevention is worth a pound of cure.




### **Healthcare Hacks**




#### **Anthem — $115 million**




On February 05, 2015 , Anthem released a press release regarding a cyber attack against them describing the breach as a very sophisticated attack to gain unauthorized access to one of their parent company’s IT systems. The hackers obtained personal information relating to consumers and Anthem employees who are currently covered, or who have received coverage in the past. The information accessed includes names, birthdays, social security numbers, street addresses, email addresses and employment information including income data. Anthem says no credit card information was compromised. So far this is the largest cyberattack in the world directed specifically at healthcare.




The hackers stole around 80 million detailed medical records also known as “fullz” on the darkweb because they contain enough information to create a new line of credit. These fullz are more valuable than credit card information because they can be used in any sort of fraudulent criminal activity.




In 2017, two years after the attack, Anthem has announced that it will be paying $115 million in settlements, the largest settlement ever paid for a data breach.




#### **MyQuest**




On November 2016, a cyber attack hit Quest Diagnostics, a New Jersey based clinical laboratory services company. Hackers gained access through the company’s mobile app, MyQuest by Care360. Quest Diagnostics operates forensic toxicology laboratories across the United States that perform workplace drug testing. The company announced its internet application was breached by an unauthorized third party and 34,000 patients were affected by the attack. However, officials stated Social Security numbers, credit card information, insurance cards and financial information wasn’t included in the stolen data. This incident highlights the necessity for healthcare systems to not only protect their backends, but also secure their mobile apps. As the Internet of Things continues to grow, we must be careful to secure all entry points to a network, and any device or software that communicates sensitive information.




#### **WannaCry — Ransomware!**




On May 12th, 2017 the world witnessed the largest global ransomware attack in history. The ransomware infected 300,000 computers in 150 countries, including Britain, Ukraine, Russia, India and Taiwan. Many organizations were severely hindered, including FedEx and Britain’s National Health Service. Hospitals across the Britain were forced to turn away surgery patients and cancel appointments after the cyber attacks crippled their system. This ransomware went beyond extorting money; it obstructed doctors from saving lives. The WannaCry ransomware was spread by using an exploit created by NSA that was leaked called EternalBlue, which exploits a vulnerability in Microsoft’s implementation of the Server Message Block protocol (SMB). The ironic part is that Microsoft created an update that fixed this issue a month beforehand — much of this destruction could have been prevented if people would just update Windows.




### **Our Approach — Peer-review and ideas please!**




At the outset of the summer, Appthority sent us examples of their security analysis reports that they generate for mobile apps. These reports check apps for basic security vulnerabilities and risky behaviors, and then they generate a score that represents the security level of these apps.




Initially, we wrote a report methodically examining Appthority’s security analysis, and we studied the history of healthcare cybersecurity to identify what security vulnerabilities should be screened for when performing analysis of healthcare apps.




We then generated a report analyzing instances of healthcare cybersecurity breaches and we are generating a template for healthcare app security analysis incorporating vulnerability areas unique to healthcare information. **Do you have more ideas on what app characteristics we can check for?**




Moving forward we will be implementing the code necessary to some test vulnerabilities identified in our analysis template and devise techniques to judge the operational characteristics for deploying them.




Right now, we are thinking of following areas and might love your input and feedback:






  1. What should an easy to read healthcare focussed software vulnerability report for mobile applications look like — SSL usage, Minimal app permissioning, HIPAA compliance..what else?


  2. What **operational characteristics** which should test for running these reports on 100s of applications on a regular basis? Number of hours need to do first set of testing of the applications and then how frequently should we check the applications for vulnerabilities.


  3. We are thinking of addressing **privacy preserving data layer **— for e.g. why should a healthcare application share its exact location when approximate user location is sufficient. As a stretch goal we want implement a helper functions to enable that.



