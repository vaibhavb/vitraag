---
author: vitraag
comments: true
date: 2024-07-16T21:47:49Z
layout: post
slug: aisec-getting-started
title: AI Security Getting Started
categories:
    - ai
    - security
    - workshop
---
# Getting Started

## Setting up a OpenAI, Anthropic and Gemini Accounts
- OpenAI
- Anthropic
- Gemini

## Basic prompting (Application: Finding Your IP Address)
- Write a python script to find the public IP Address of a user using 'request' library

## Creating an API Key and interacting with OpenAI, Claude, Google
- OpenAI
1. **Python**: Ensure that you have Python installed on your system.
2. **OpenAI API Key**: Sign up for OpenAI and get your API key from the [OpenAI Dashboard](https://beta.openai.com/signup/).

### Step 1: Install the OpenAI Python Package
First, you need to install the OpenAI Python client library. You can do this using pip.

```sh
pip install openai
```

### Step 2: Create a Python Script
Create a new Python script file, e.g., `openai_example.py`.

### Step 3: Import Libraries and Set Up API Key
In your `openai_example.py` file, start by importing the necessary libraries and setting up your OpenAI API key.

```python
import openai
import os

def get_chatgpt_response(prompt, api_key):
    openai_client= openai.OpenAI(api_key=api_key)

    try:
        response = openai_client.chat.completions.create(
            model="gpt-3.5-turbo",  # or the appropriate model
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    api_key = os.getenv("OPENAI_API_KEY") 
    if not api_key:
        raise ValueError("No API key found. Please set the OPENAI_API_KEY environment variable.")
    
    prompt = "Write a short story about a talking cat."
    
    response = get_chatgpt_response(prompt, api_key)
    print(f"ChatGPT Response: {response}")
```

### Step 4: set openai key and run the program
```sh
export OPENAI_API_KEY='xxx'
python openai_example.py
```

## Applying ChatGPT Roles (Application: AI CISO)
- You are a cybersecurity expert with 20 years of experience. Explain the importance of multi-factor authentication (MFA) in securing online accounts, to an executive audience.
- You are a CISO with 30 years of experience. What are the top cybersecurity risks businesses should be aware of?
- You are an ethical hacker. Explain how a penetration test can help improve an organization's security posture.
- You are a network administrator. What measures do you take to secure your organization's network?
- You are a cybersecurity consultant. What additional recommendations do you have for the network administrator to further enhance network security?

## Enhancing Output with Templates (Application: Threat Report)
```md
Create an analysis report of the WannaCry Ransomware Attack as it relates to the cyber kill chain, using the following format:
# Threat Report
## Overview
- **Threat Name:**
- **Date of Occurrence:**
- **Industries Affected:**
- **Impact:**
## Cyber Kill Chain Analysis
1. **Kill chain step 1:**
2. **Kill chain step 2:**
3. …
## Mitigation Recommendations
- *Mitigation recommendation 1*
- *Mitigaiton recommendation 2*
```

## Formatting Output as a Table (Application: Security Controls Table)
- Create a table comparing five different security controls. The table should have the following columns: Control Name, Description, Implementation Cost, Maintenance Cost, Effectiveness, and Ease of Implementation.

