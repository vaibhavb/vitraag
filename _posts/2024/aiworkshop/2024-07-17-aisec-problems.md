---
author: vitraag
comments: true
date: 2024-07-16T21:47:49Z
layout: post
slug: ai-security-problems
title: AI Security Problems
categories:
    - ai
    - security
    - workshop
---
# AI and Security Problems
This post covers some interesting problem areas at the intersection of AI and Security. These could be worked on in an hackathon format.

## Foundational AI and Data Analysis
- Learn about nitty gritty of AI with in-depth [LLM101](https://github.com/karpathy/LLM101n) from Andrej Karpathy and create your own version of AI Story Teller or a Security Game!
- Solve popular problems from Kaggle like [Titanic Bias Analysis](https://www.kaggle.com/competitions/titanic). Answers questions like what is AI good for?

## Science of AI, and AI of Science
- ** Deduce Physical Laws with AI **
  Use [pySR](https://github.com/MilesCranmer/PySR) to learn and find popular symbolic equations. Try to tackle the problem of can we create science with AI?

## Enhancing foundation models with RAGs and Finetuning
- ** Use an existing LLM model to optimize it for security use case **
  Use one of the open weights models from [huggingface](https://huggingface.co/) to create finetuned model for security or enable retrieval augmented generation (RAG) on it. You can do RAG on generative model with APIs as well.

## AI Devices enhancing Security
- ** Use ESP32S3 to create a voice bot **
  Make an voice bot inspired by [this](https://wiki.seeedstudio.com/xiao_esp32s3_speech2chatgpt/).
- ** Use ESP32S3 to create a camera detection system with ChatGPT **
  Continuosly take photos of a server enclosure area and detect if there was an intrusion. You can use inspiration and code from [friend][https://github.com/BasedHardware/Friend)
- ** Deploy models on ESP32S3 **
  Make your own AI system to detect an object (like recycleable or not) and train it. Samples are available on [seedstudio](https://wiki.seeedstudio.com/xiao_esp32s3_sscma/)

## Generative AI Applications in Cyber Security
- **AI-Powered Intrusion Detection System**
  Develop an AI-assisted intrusion detection system that can analyze network traffic patterns and system logs to identify potential security breaches in real-time.

- **Smart IoT Security Camera for Server Racks**
  Create an AI-powered IoT security camera system that monitors server racks, detects unauthorized access or equipment removal, and sends instant alerts to security personnel.

- **AI-Enhanced Red Team Automation**
  Design an AI system that can automate various aspects of red team operations, including vulnerability scanning, exploitation, and reporting, to improve the efficiency of penetration testing.

- **Automated Security Code Review**
  Develop an AI tool that can automatically review code for security vulnerabilities, suggesting fixes and best practices to developers in real-time.

- **AI-Driven Project Planning and Threat Modeling**
  Create an AI assistant that can help project managers and security professionals in identifying potential threats, conducting risk assessments, and developing comprehensive security plans for software projects.

## Advanced Security Applications with Generative AI.
- **AI-Enhanced pfSense Firewall**
  Integrate AI capabilities into the open-source pfSense firewall to improve threat detection, automate rule creation, and enhance overall network security.

- **AI-Powered Phishing Detection and Prevention**
  Develop an AI system that can analyze emails, links, and attachments to identify and prevent sophisticated phishing attempts in real-time.

- **Automated Incident Response Orchestration**
  Create an AI-driven incident response system that can automatically detect security incidents, prioritize them, and orchestrate appropriate response actions across multiple security tools.

- **AI-Based Malware Behavior Analysis**
  Design an AI system that can analyze the behavior of unknown files and processes to detect and classify new or evolving malware threats.

## Security of *AI*
- [Prompt Engineering]()
- **Secure AI Model Development and Deployment**
  Develop a framework and set of tools to ensure the secure development, testing, and deployment of AI models, protecting against adversarial attacks and data poisoning.

## What's next?
To assist with the Merritt Secure AI Hackathon we will be doing a pre-hackathon introduction to AI and Security webinar on Friday July 19th from 3-4pm. This webinar will also be recorded.

Use the following [zoom link](https://peralta-edu.zoom.us/j/9402327279) to join on Friday, July 19th 3-4pm:
https://peralta-edu.zoom.us/j/9402327279
Topic: Getting Started with AI and Cyber Security

Update:
Recording is available [here](https://peralta-edu.zoom.us/rec/share/nGaiCnwbLRNJaYdJhziyJwyS_HtXqauRT2UeNCbKnm_ZJ8cEvezP6pBj_k3iH2qY.ARDQf4ocKOosO-vr)

## References

- Buchanan, B., Caporale, C., Cunningham, J., & Frye, J. (2023). *ChatGPT for Cybersecurity Cookbook*. Packt Publishing.
  - GitHub Repository: [https://github.com/PacktPublishing/ChatGPT-for-Cybersecurity-Cookbook](https://github.com/PacktPublishing/ChatGPT-for-Cybersecurity-Cookbook)

- Diogenes, Y., & Ozkaya, E. (2019). *Cybersecurity – Attack and Defense Strategies: Infrastructure security with Red Team and Blue Team tactics*. Packt Publishing.
  - O'Reilly Learning Link: [https://learning.oreilly.com/library/view/-/9781789804027/](https://learning.oreilly.com/library/view/-/9781789804027/)

- Netgate. (n.d.). *About pfSense Software*. pfSense.
  - Website: [https://www.pfsense.org/about-pfsense/](https://www.pfsense.org/about-pfsense/)
