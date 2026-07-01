---
author: vitraag
comments: true
date: 2026-06-30T00:00:00Z
layout: post
slug: ai-engineer-main-stage-notes
title: "AI Engineer Day 1: Tools and Ideas to Try"
categories:
    - ai
    - security
    - conference
---

*Day 1 main stage talk things to try, from [AI Engineer](https://www.ai.engineer/).*

---

The main stage on Day 1 was less about which model wins this month's leaderboard, and more about the systems around the model — orchestration, evals, retrieval, human review, cost control, debugging.

Agents are becoming real software systems. Real software systems need the things software has always needed: interfaces, contracts, tests, and review.

Here's what I want to go build with, roughly in the order I'd start.

---

## 1. [BAML](https://boundaryml.com/) for structured AI workflows

BAML treats LLM calls like software interfaces instead of loose prompts. That matters when the output needs to be reliable, not just plausible.

This matters a lot when "close enough" isn't a valid grading criterion — SOC 2 evidence, HIPAA controls, vendor questionnaire answers. Free text is fine for a chatbot. It is not fine for a control mapping someone's auditor is going to read.

**Experiment to try:** a security questionnaire assistant that takes a policy doc and returns typed, structured output:

```json
{
  "control": "...",
  "evidence": "...",
  "gap": "...",
  "risk": "...",
  "needs_human_review": true
}
```

This feels immediately useful for compliance, security reviews, and risk work.

## 2. [Agent2Agent / A2A](https://github.com/a2aproject/A2A) for multi-agent systems

Multi-agent systems need a cleaner way for agents to discover each other and communicate.

A2A's "agent card" idea is simple and useful: each agent describes what it does, what it can accept, and how other agents should interact with it. That creates a contract between agents instead of relying on one big brittle prompt.

**Experiment to try:** a four-agent compliance chain — evidence finder, policy mapper, risk reviewer, final answer drafter — versus the equivalent single-prompt or MCP-tool-calling version.

## 3. [MiniMax M3](https://www.minimax.io/blog/minimax-m3) for long-context and multimodal work

Real engineering work is not just code. It includes screenshots, architecture diagrams, tickets, docs, logs, and transcripts. A model that can reason across more of that context could be useful for debugging and architecture review.

**Experiment to try:** hand M3 a whole repo plus its surrounding docs and ask for an architecture map, risk areas, and refactor suggestions. Then compare the result with Claude, Gemini, and Codex.

## 4. [GLM-5.2](https://huggingface.co/blog/zai-org/glm-52-blog) for open-weight coding agents

Open-weight models being genuinely competitive at coding and agentic work matters for more than the bill. It's about who gets to say yes to using AI at all — teams in healthcare, security, or government where "just send it to a hosted API" is not a sentence legal will let you finish.

**Experiment to try:** benchmark GLM-5.2 on practical tasks — Terraform security review, Python refactors, SOC 2 control mapping, long transcript summarization, malware-analysis helper prompts. For the security-flavored tasks specifically, I'd still test carefully and avoid blindly trusting outputs.

## 5. [HumanLayer](https://github.com/humanlayer) and control-loop coding

The control-loop idea may be one of the most practical patterns for coding agents. Instead of asking an agent to produce a giant unreadable PR, the better loop is:

1. Measure the current state.
2. Pick one small improvement.
3. Let the agent make the change.
4. Open a small PR.
5. Let a human review.
6. Repeat.

This is much closer to how real teams work. The agent should make code easier to review, not bypass review entirely.

**Experiment to try:** a daily coding-agent loop that opens one small PR a day. Good tasks: fix one lint class, improve one test, update one dependency, migrate one API route, add one missing documentation section. Small, reviewable diffs are the key.

## 6. [Agentcraft](https://www.getagentcraft.com/) for visual agent orchestration

Agentcraft's game-inspired interface is compelling because it recognizes a real problem: humans become the bottleneck when too many agents are running at once. A visual map of agent activity makes sense — if agents are working across files, branches, tasks, and PRs, the human operator needs a way to see what's happening without reading endless logs.

**Experiment to try:** even without Agentcraft itself, a lightweight dashboard tracking task, branch, last action, status, PR link, blocker, and "needs human approval" per agent. That alone would make agent workflows easier to manage.

## 7. Production evals for agentic systems

Normal benchmarks don't tell you whether an agentic system works in production. For agents, the final answer is only part of the story. We also need to evaluate the path — did it retrieve the right context, call the right tool, recover from tool failure, ask for approval before a risky action, waste tokens, complete the task safely.

**Experiment to try:** 20 scenario-based evals for a security or compliance agent, scored on the full trajectory, not just the final answer:

* Review this Terraform S3 bucket for security issues.
* Find whether this policy covers HIPAA breach notification.
* Answer this vendor questionnaire using only approved evidence.
* Identify whether this log contains PHI.
* Draft a risk-register entry from this incident summary.

This is where AI engineering starts to look like real engineering.

## 8. Model routing and "AI Switzerland"

The Notion talk had a useful framing: optionality is leverage. Not every task needs the most expensive frontier model. Some tasks need a top model. Many do not. Email triage, CSV conversion, deterministic SQL, formatting, and simple classification can often run on cheaper models or no model at all.

**Experiment to try:** a router with tiers — cheap model for classification and formatting, strong model for complex reasoning, local/open model for sensitive or low-risk internal tasks, and no LLM for deterministic tasks. The goal is not to use the cheapest model everywhere. The goal is to use the right level of intelligence for the task.

---

## Bonus: [Effect](https://effect.website/) for making TypeScript behave

Not from the main stage, but worth adding: TypeScript's type system is good at describing shapes and weak at describing what happens when things go wrong — untyped errors, silent async failures, retries bolted on with `try/catch`.

Effect brings errors, dependencies, concurrency, and retries into the type system itself, so the compiler knows what can fail and how. For agentic pipelines, where a tool call can fail in several different ways, that's useful — you want to know the failure modes before they show up in production.

**Experiment to try:** rebuild one leg of an agent pipeline — say, the tool-calling layer — in Effect and see how much of the failure-mode debugging gets caught at compile time instead of runtime.

---

## Takeaway

My main takeaway from Day 1 is that AI engineering is moving from demos to systems. The interesting work is no longer just prompting a model. It is building the harness around the model:

* Typed outputs
* Multi-agent protocols
* Long-context workflows
* Human approval gates
* Small agent-generated PRs
* Production evals
* Better retrieval
* Smarter model routing

The tools I would try first are [BAML](https://boundaryml.com/), [A2A](https://github.com/a2aproject/A2A), [MiniMax M3](https://www.minimax.io/blog/minimax-m3), [GLM-5.2](https://huggingface.co/blog/zai-org/glm-52-blog), and [HumanLayer](https://github.com/humanlayer). Those cover the parts of the stack that seem most useful right now: reliability, interoperability, model optionality, long-context reasoning, and safe automation.
