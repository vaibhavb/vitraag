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

*Day 1 notes from [AI Engineer](https://www.ai.engineer/), where I went in expecting a model beauty pageant and left thinking about plumbing instead.*

---

I spent Day 1 of the conference bracing for the usual sport: which model wins this month's leaderboard, whose benchmark chart has the steepest line, who gets to say "SOTA" the most times per keynote. That's not what happened.

Almost every talk that stuck with me was about the boring, unglamorous stuff *around* the model — orchestration, evals, retrieval, human review, cost control, debugging. Turns out agents are quietly becoming real software systems, and real software systems need the things software has always needed: interfaces, contracts, tests, and someone willing to say "no, you can't just YOLO this into prod."

Here's what I want to go build with, roughly in the order I'd reach for the coffee to start.

---

## 1. [BAML](https://boundaryml.com/) for structured AI workflows

BAML's whole pitch is treating LLM calls like software interfaces instead of prompts you whisper hopefully into the void. If you've ever regex'd a model's output at 11pm because it decided today was the day to wrap JSON in a friendly little paragraph, you understand the appeal instantly.

This matters a lot when "close enough" isn't a valid grading criterion — SOC 2 evidence, HIPAA controls, vendor questionnaire answers. Free text is fine for a chatbot. It is not fine for a control mapping someone's auditor is going to read.

**Experiment to try:** a security questionnaire assistant that takes a policy doc and returns something typed and boring on purpose:

```json
{
  "control": "...",
  "evidence": "...",
  "gap": "...",
  "risk": "...",
  "needs_human_review": true
}
```

Boring is the feature.

## 2. [Agent2Agent / A2A](https://github.com/a2aproject/A2A) for multi-agent systems

Multi-agent systems have a discovery problem — right now most of them "communicate" via one enormous prompt that's basically five job descriptions duct-taped together, praying nobody drops their part.

A2A's "agent card" idea is refreshingly unfancy: each agent publishes what it does, what it accepts, and how to talk to it. A contract instead of a group chat where everyone's guessing what everyone else meant.

**Experiment to try:** a four-agent compliance chain — evidence finder, policy mapper, risk reviewer, final answer drafter — versus the equivalent single-prompt or MCP-tool-calling version. My money's on the agent cards being easier to debug at 2am, but I'd like to actually watch it fail before I say that with confidence.

## 3. [MiniMax M3](https://www.minimax.io/blog/minimax-m3) for long-context and multimodal work

Real engineering work is not just code. It's screenshots of a dashboard someone forgot to caption, an architecture diagram from 2023 that's 40% aspirational, a ticket thread, some logs, a Slack screenshot of a Slack screenshot. A model that can actually reason across that pile — instead of just the code — is doing something closer to what a senior engineer does when they inherit a mess.

**Experiment to try:** hand M3 a whole repo plus its surrounding docs and ask for an architecture map, risk areas, and refactor suggestions. Then run the same ask through Claude, Gemini, and Codex and see who actually read the diagrams versus who's confidently making it up.

## 4. [GLM-5.2](https://huggingface.co/blog/zai-org/glm-52-blog) for open-weight coding agents

Open-weight models being genuinely competitive at coding and agentic work matters for more than the bill. It's about who gets to say yes to using AI at all — teams in healthcare, security, or government where "just send it to a hosted API" is not a sentence legal will let you finish.

**Experiment to try:** run GLM-5.2 through a gauntlet — Terraform security review, Python refactors, SOC 2 control mapping, long transcript summarization, malware-analysis helper prompts. For the security-flavored tasks specifically, I'll be reading every output like it's trying to sell me a timeshare. Trust, but verify, then verify again.

## 5. [HumanLayer](https://github.com/humanlayer) and control-loop coding

This might be the most immediately useful idea from the whole day, mostly because it's not really a new idea — it's just "how good teams already work," pointed at an agent instead of a junior engineer:

1. Measure the current state.
2. Pick one small improvement.
3. Let the agent make the change.
4. Open a small PR.
5. Let a human review.
6. Repeat.

The alternative — an agent handing you an 1,800-line PR titled "fixes" — is not a workflow, it's an act of aggression.

**Experiment to try:** a daily coding-agent loop that opens exactly one small, reviewable PR a day. Fix one lint class, improve one test, bump one dependency, migrate one route, document one thing that's been undocumented since the Obama administration. Small diffs, every day, forever. Compounding interest, but for code quality.

## 6. [Agentcraft](https://www.getagentcraft.com/) for visual agent orchestration

Agentcraft's pitch is basically an RTS game for your agent fleet, and it's making fun of a real problem: past a certain number of agents, the human becomes the bottleneck, squinting at seven terminal tabs trying to figure out which one is stuck and which one just quietly finished an hour ago.

**Experiment to try:** even without Agentcraft itself, a lightweight dashboard tracking task, branch, last action, status, PR link, blocker, and "needs human approval" per agent. Nothing clever — just something that answers "which agent needs me right now" faster than tab-cycling does.

## 7. Production evals for agentic systems

Benchmarks tell you the model is smart. They don't tell you the agent didn't quietly call the wrong tool, retrieve the wrong document, or burn 40,000 tokens deciding not to ask for help when it clearly should have. For agents, the final answer is maybe a third of the story — the path matters as much as the destination.

**Experiment to try:** 20 scenario-based evals for a security or compliance agent, scored on the full trajectory, not just the final answer:

* Review this Terraform S3 bucket for security issues.
* Find whether this policy covers HIPAA breach notification.
* Answer this vendor questionnaire using only approved evidence.
* Identify whether this log contains PHI.
* Draft a risk-register entry from this incident summary.

This is the point where "AI engineering" stops sounding like a vibe and starts looking like actual engineering — the part with test plans and failure modes, not just demos.

## 8. Model routing and "AI Switzerland"

The framing from the Notion talk stuck with me: optionality is leverage. Not everything needs the frontier model, in the same way not every trip needs a helicopter. Email triage, CSV munging, deterministic SQL, formatting — a lot of that doesn't need intelligence at all, let alone the expensive kind.

**Experiment to try:** a router with tiers — cheap model for classification and formatting, strong model for real reasoning, local/open model for sensitive or low-stakes internal tasks, and "no LLM" for anything actually deterministic. The goal isn't cheapest-everywhere. It's matching intelligence to the job, the same discipline you'd apply to picking which employee handles which task.

---

## Bonus: [Effect](https://effect.website/) for making TypeScript behave

Not from the main stage, but it kept coming up in hallway-track conversations, and once someone shows you Effect you can't unsee the problem it's solving: TypeScript's type system is great at describing shapes and terrible at describing what happens when things go wrong. Untyped errors, silent async failures, retries bolted on with `try/catch` and vibes.

Effect wraps all of that — errors, dependencies, concurrency, retries — into the type system itself, so the compiler actually knows what can fail and how. For agentic pipelines specifically, where a tool call can fail in six different ways and you'd like to know which six before it happens in production, that's not a nice-to-have, it's the whole point.

**Experiment to try:** rebuild one leg of an agent pipeline — say, the tool-calling layer — in Effect and see how much of the "did this actually fail or did it just return something weird" debugging disappears. My guess is a lot of it, but I've been wrong about frameworks before.

---

## Takeaway

The theme of Day 1, if I had to compress it: AI engineering is graduating from demos to systems. The interesting work isn't prompting anymore — it's building the harness around the model:

* Typed outputs
* Multi-agent protocols
* Long-context workflows
* Human approval gates
* Small agent-generated PRs
* Production evals
* Better retrieval
* Smarter model routing

If I only get to try five of these before the novelty wears off, it's [BAML](https://boundaryml.com/), [A2A](https://github.com/a2aproject/A2A), [MiniMax M3](https://www.minimax.io/blog/minimax-m3), [GLM-5.2](https://huggingface.co/blog/zai-org/glm-52-blog), and [HumanLayer](https://github.com/humanlayer) — reliability, interoperability, model optionality, long-context reasoning, and not letting the robot merge to main unsupervised. That last one still feels like the whole ballgame.
