---
author: vitraag
comments: true
date: 2024-11-22T00:18:18Z
layout: post
slug: starting-with-ai-security 
title: Starting with AI Security
categories:
    - security
---
<script src="https://cdnjs.cloudflare.com/ajax/libs/mermaid/10.4.0/mermaid.min.js"></script>
<script>
  document.addEventListener("DOMContentLoaded", function () {
    // Select all code blocks with the 'language-mermaid' class
    document.querySelectorAll("pre > code.language-mermaid").forEach((block) => {
      const parent = block.parentElement;
      const mermaidCode = block.textContent;

      // Replace the <pre> block with a Mermaid-renderable <div>
      const mermaidDiv = document.createElement("div");
      mermaidDiv.classList.add("mermaid");
      mermaidDiv.textContent = mermaidCode;

      parent.replaceWith(mermaidDiv);
    });

    // Initialize Mermaid.js
    mermaid.initialize({ startOnLoad: true });
  });
</script>
<style>
.mermaid {
  display: block;
  border: 1px solid red;
  max-width: 100%;
  margin: 0 auto;
  overflow-x: auto;
}
</style>
{%raw%}
```mermaid
graph TD
    A[End Users] --> B[Application Services]
    B --> C[LLM Application]
    C --> D[LLM Production Services]
    D --> E[LLM Automation Agents]
    D --> F[LLM Modes]
    F --> G[Training Dataset and Processing]
    G --> H[Fine-Tuning Data]
    G --> I[Training Data]
    I --> J[External Data Sources]
    H --> J
    D --> K[Plugins or Extensions]
    K --> L[Downstream Services]
    L --> M[Database]
    L --> N[Websites]
    L --> O[Services]
```
{%endraw%}

- Prompt Injection
- Jailbreak e.g DAN (Do/Say Anything Now, )
- Defense -- Guardrails / AI Firewalls / -- Garak scanner for AI

- [Red Team Strategy - Johann's Blog](https://embracethered.com/blog/)
- [OWASP Top 10 for LLM Applications](https://genai.owasp.org)
- [Getting Started with AI CTFs](https://www.youtube.com/watch?v=hnNZoHoyYpE)
- [Real-world Attacks on LLM Applications](https://www.youtube.com/watch?v=_4Q980G4ZXI)
- [ChatGPT for Red Teams](https://github.com/NetsecExplained/chatgpt-your-red-team-ally)
- [Attacking and Defending Generative AI](https://github.com/NetsecExplained/Attacking-and-Defending-Generative-AI)
- [AI Vulnerability Database](https://avidml.org)
- 
