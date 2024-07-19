---
author: vitraag
comments: true
date: 2024-07-16T21:47:49Z
layout: post
slug: aisec-prompts
title: AI Security Prompt Engineering - Vuln Assessment
categories:
    - ai
    - security
    - workshop
---
# Doing Vulnerability Assessment with AI Tools

Introduce ChatGPT in creating vulnerability and threat assessment plans, a crucial part of any cybersecurity strategy. And showcase MITRE ATT&CK framework.

## Creating Vulnerability Assessment Plans
```
You are a cybersecurity professional specializing in vulnerability assessment.

Using cybersecurity industry standards and best practices, create a complete and detailed assessment plan (not a penetration test) that includes: Introduction, outline of the process/methodology, tools needed, and a very detailed multi-layered outline of the steps. Provide a thorough and descriptive introduction and as much detail and description as possible throughout the plan. The plan should not be the only assessment of technical vulnerabilities on systems but also policies, procedures, and compliance. It should include the use of scanning tools as well as configuration review, staff interviews, and site walk-around. All recommendations should follow industry standard best practices and methods. The plan should be a minimum of 1500 words.
Create the plan so that it is specific for the following details:
Network Size: {Large}
Number of Nodes: {1000}
Type of Devices: {Desktops, Laptops, Printers, Routers}
Specific systems or devices that need to be excluded from the assessment: {None}
Operating Systems: {Windows 10, MacOS, Linux}
Network Topology: {Star}
Access Controls: {Role-based access control}
Previous Security Incidents: {3 incidents in the last year}
Compliance Requirements: {HIPAA}
Business Critical Assets: {Financial data, Personal health information}
Data Classification: {Highly confidential}
Goals and objectives of the vulnerability assessment: {To identify and prioritize potential vulnerabilities in the network and provide recommendations for remediation and risk mitigation.}
Timeline for the vulnerability assessment: {4 weeks{
Team: {3 cybersecurity professionals, including a vulnerability assessment lead and two security analysts}
Expected deliverables of the assessment: {A detailed report outlining the results of the vulnerability assessment, including identified vulnerabilities, their criticality, potential impact on the network, and recommendations for remediation and risk mitigation.}
Audience: {The organization's IT department, senior management, and any external auditors or regulators.}
Provide the plan using the following format and markdown language:
#Vulnerability Assessment Plan
##Introduction
Thorough Introduction to the plan including the scope, reasons for doing it, goals and objectives, and summary of the plan
##Process/Methodology
Description and Outline of the process/Methodology
##Tools Required
List of required tools and applications, with their descriptions and reasons needed
##Assessment Steps
Detailed, multi-layered outline of the assessment steps
```

```
def markdown_to_docx(markdown_text: str, output_file: str):
    document = Document()
    # Iterate through the lines of the markdown text
    for line in markdown_text.split('\n'):
        # Add headings and paragraphs based on the markdown formatting
        ...
    # Save the Word document
    document.save(output_file)
```


## Threat Assessment using ChatGPT and the MITRE ATT&CK framework
```You are a professional cyber threat analyst and MITRE ATT&CK Framework expert.```

```md
Provide a detailed report about {threat_name}, using the following template (and proper markdown language formatting, headings, bold keywords, tables, etc.):
Threat Name (Heading 1)
Summary (Heading 2)
Short executive summary
Details (Heading 2)
Description and details including history/background, discovery, characteristics and TTPs, known incidents
MITRE ATT&CK TTPs (Heading 2)
Table containing all of the known MITRE ATT&CK TTPs that the {threat_name} attack uses. Include the following columns: Tactic, Technique ID, Technique Name, Procedure (How WannaCry uses it)
Indicators of Compromise (Heading 2)
Table containing all of the known indicators of compromise. Include the following columns: Type, Value, Description
```

GPT-Assisted Vulnerability Scanning
`You are a professional cybersecurity red team specialist and an expert in penetration testing as well as vulnerability scanning tools such as NMap, OpenVAS, Nessus, Burpsuite, Metasploit, and more.`

`Use the command line version of OpenVAS to scan my 192.168.20.0 class C network starting by identifying hosts that are up, then look for running web servers, and then perform a vulnerability scan of those web servers.`

`Provide me with the Linux command necessary to complete the following request:
{user_input}
Assume I have all the necessary apps, tools, and commands necessary to complete the request. Provide me with the command only and do not generate anything further. Do not provide any explanation. Provide the simplest form of the command possible unless I ask for special options, considerations, output, etc. If the request does require a compound command provide all necessary operators, pipes, etc. as a single one-line command. Do not provide me with more than one variation or more than one line.`


Analyzing Vulnerability Assessment Reports using LangChain
` pip install python-docx langchain streamlit openai`





