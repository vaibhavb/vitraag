---
author: vitraag
comments: true
date: 2026-03-12T00:00:00Z
layout: post
slug: ai-assisted-grading-canvas-api-claude
title: "AI-Assisted Grading with Canvas API and Claude"
categories:
    - ai
    - security
    - teaching
---

*How I built a grading pipeline for a Hacker Techniques & Exploits course — and what I learned about prompting AI to give feedback like a teacher.*

---

Grading is one of the hardest parts of teaching. Not because it's intellectually difficult, but because it compounds: 30 students, 5 labs, each submission a PDF or Word doc, each deserving real written feedback. By the time you get to the 25th submission you've read about nmap that week, the feedback starts to blur.

I wanted to fix that — or at least make it less draining. Here's what I built and how it works.

---

## The Setup: Canvas Already Has an API

Most instructors don't know this, but Canvas — one of the most widely deployed LMS platforms — exposes a full REST API, and instructors can access it with a personal token generated directly from their account settings (Account → Settings → New Access Token). No admin privileges needed.

That one fact unlocked everything. From the API I can:

- List all assignments and their submission types
- Pull every student's submitted files with download URLs
- Post grades and written comments back to SpeedGrader

The course I'm teaching — CIS-55, Hacker Techniques & Exploits at Peralta College — has 36 students and 5 labs covering penetration testing tools, OSINT, and incident response. All submitted as file uploads: PDFs, Word docs, screenshots, even scanned handwritten pages.

---

## The Pipeline

The system has four stages, each a standalone script that hands off to the next:

```
Discover → Download → AI Grade → Human Review → Upload
```

**Discover** queries Canvas for all assignments with `online_upload` submission types and shows you who has submitted and who hasn't, at a glance.

**Download** fetches every attachment for every student into a local directory tree organized by lab and student name. It skips files already present, so re-runs are fast.

**AI Grade** is the core: for each submission, it extracts text (or renders scanned PDFs to images), builds a prompt around a rubric YAML file, sends it to Claude, and gets back a structured JSON response with per-criterion scores, a total, a written comment, and a flag if something looks off.

**Upload** reads the reviewed CSV and posts each grade and comment back to Canvas via the API — the same way SpeedGrader does it manually.

The whole thing is wrapped in a single `make lab LAB="Lab 5"` command that walks you through the steps interactively.

---

## The Rubric: YAML as the Source of Truth

The key design decision was to encode rubrics as YAML files rather than hardcoding them into prompts. Each lab has its own file:

```yaml
assignment_id: 1643223
assignment_name: "Lab 3 - nmap, metasploit, sqlmap"
total_points: 100

criteria:
  - name: "Nmap Scanning"
    points: 30
    description: >
      Correct nmap scans performed — host discovery, port scan,
      service/version detection. Commands and output shown.

  - name: "Metasploit Usage"
    points: 30
    description: >
      Module selected, options configured, exploit executed.
      Evidence of successful or attempted exploitation shown.

  - name: "SQLMap"
    points: 25
    description: >
      SQLMap used against a vulnerable target. Command, target URL,
      and output documented.

  - name: "Bonus - LLMs or Nessus"
    points: 15
    description: >
      Used an LLM to assist with exploitation OR ran a Nessus scan.

extra_instructions: |
  For nmap: look for -sV, -sC, -O flags showing competence beyond basic ping.
  For Metasploit: use/exploit/show options/run sequence expected.
```

This separation matters. When a rubric changes, you update the YAML — the code and prompt stay the same. And the rubric file becomes a precise specification of what you're actually measuring, forcing you to think it through before grading begins.

---

## The Prompt: Teaching Claude to Sound Like a Teacher

The most important part of this project wasn't the API integration — it was the system prompt. Early drafts produced feedback that sounded like a rubric being recited back. Technically accurate, but cold.

The breakthrough was two constraints added to the system prompt:

**First-person instructor voice.** Instead of "The student demonstrated..." the feedback reads "I can see you put real effort into this section..." Small shift, completely different feel. Students respond to feedback that sounds like it came from a person who read their work.

**Per-criterion breakdown.** Each comment must include one sentence per rubric criterion explaining the score: "For Nmap Scanning I'm giving you 25/30 because you ran -sV and -sC correctly but didn't include output showing the open ports." This turns a number into a teaching moment.

The full system prompt:

```
You are grading lab submissions for a Hacker Techniques & Exploits course.
Write ALL feedback in first person as the instructor speaking directly to
the student. Use "I" for yourself and "you" for the student.
Be warm, encouraging, and specific.

For EACH rubric criterion, include one sentence explaining what score you
gave and why: "For [Criterion] I'm giving you X/Y points because..."
Then add 1-2 overall sentences of encouragement or guidance.

Return valid JSON: { scores, total, comment, flag, confidence }
```

The `flag` field does real work: Claude returns `AI_GENERATED_SUSPECTED`, `REVIEW_NEEDED`, or `INCOMPLETE` when something warrants a second look. On Lab 5, 13 of 22 submissions were flagged — mostly for AI-generated content or thin evidence. That's not Claude being trigger-happy; that's a useful signal that those submissions need human eyes before the grade is final.

---

## Handling the Messy Reality of Student Submissions

Student submissions are not clean. In a single lab I encountered:

- Text-layer PDFs (easy)
- Word documents (easy)
- Scanned image-based PDFs with no extractable text (fixed by rendering pages to PNG and sending them through Claude's vision API)
- Screenshots only, no write-up (flagged as INCOMPLETE)
- HTML files exported from Notion
- Multiple files in a single submission

The extractor layer handles all of these. If `PyMuPDF` returns fewer than 50 characters from a PDF, it falls back to rendering each page as a 144dpi image and passing them to Claude as base64 vision inputs. That caught a beautifully written incident report on the 23andMe breach that would otherwise have been invisible.

---

## Human Always in the Loop

The pipeline produces a CSV after AI grading, not a final grade. The CSV has a `skip` column — set it to `true` for any student you want to handle manually. Every flagged submission shows up sorted to the top.

The workflow is:

1. Run the script — takes a few minutes for 22 students
2. Review the CSV — fix anything that looks wrong, soften or sharpen comments
3. Confirm the upload — the script asks "Post 22 grades to Canvas? [y/N]" and waits

The AI handles the first draft. The instructor handles the judgment calls.

There's also a minimum score floor (80 in my course) applied before saving the CSV — any submitted work earns at least that, regardless of quality. That's a policy decision encoded as a single line of Python, not baked into the prompt.

---

## Built with Claude Code

The entire system was built in a single session using Claude Code — Anthropic's CLI for agentic coding. I described the problem, Claude Code called the Canvas API live to inspect the course data, and we iterated on the design together.

The workflow I followed: describe the goal, explore the API, sketch the architecture, write the code, run the tests, fix the bugs that appear in real data. Claude Code handled the Canvas API calls, wrote the pytest test suite, debugged the scanned PDF issue when a real submission broke the extractor, and suggested the rubric-as-YAML design that made the whole thing composable.

What stood out was the speed of the feedback loop. Instead of reading API docs and writing curl commands separately, I could say "check what Lab 5 submissions look like" and get back real data from my actual course within seconds. That tight loop between intention and result is what made a project like this tractable in an afternoon.

---

## Where It Mattered Most: The Capstone

The most valuable use of the system turned out to be the final capstone project — and it's worth describing separately because the stakes and complexity were higher than the weekly labs.

The capstone gave students three different paths to choose from, each testing a different depth of skill. Submissions were largely written reports paired with in-class verbal presentations. That combination — a document you read before class and a live presentation you sit through — is exactly where grading fatigue compounds fastest. You're evaluating the same student twice, across two different media, against a rubric that has to flex across three distinct project types.

The AI tool helped on three specific dimensions:

**AI-assisted writing detection.** With 36 students submitting written work, spotting AI-generated content by eye alone is unreliable and exhausting. The `AI_GENERATED_SUSPECTED` flag gave me a structured signal to check — not a verdict, but a prompt to look harder. Cross-referencing the written submission against what the student said aloud in their presentation made the assessment much more grounded.

**Rubric adherence across three tracks.** Because students chose different project types, the rubric had to be applied differently depending on which path they took. Encoding each track as its own YAML rubric meant Claude evaluated submissions against the right criteria automatically, rather than me mentally context-switching between rubrics for every other student.

**Depth of evidence.** The written sections varied enormously in specificity — some students showed every command, every screenshot, every step; others described what they did in general terms. The AI feedback reliably flagged thin evidence with `REVIEW_NEEDED`, which surfaced the submissions that needed a harder look before the presentation.

I still reviewed every submission and heard every student present in class. The presentations are irreplaceable — you learn things in five minutes of live Q&A that a written report would never reveal. But walking into those presentations having already read AI-generated first-pass feedback meant I arrived with specific questions, not a blank slate. That made the conversations sharper.

---

## What I'd Do Differently

**Grade calibration.** The AI scores are internally consistent but not necessarily calibrated to how I grade. A few more examples of "this is a 90 in my class" in the rubric's `extra_instructions` would help anchor the scoring.

**Caching AI responses.** Right now every re-run calls the API again. Storing responses keyed by submission file hash would make iteration much cheaper.

**Side-by-side review UI.** The CSV review step works, but it would be better to see the submission and the proposed feedback side by side before approving. A simple local web UI would do it.

---

## The Code

The full pipeline — Canvas client, extractor, grader, uploader, rubric YAMLs, tests, Docker setup, and Makefile — is available at **[cyberdefendersprogram/canvas-ai-assisted-grader](https://github.com/cyberdefendersprogram/canvas-ai-assisted-grader)**.

If you're a Canvas instructor and you've read this far: your personal API token is waiting in Account → Settings → New Access Token. The activation energy is lower than you think.

---

* Vaibhav teaches CIS-55 Hacker Techniques & Exploits (among other courses) at Merritt College (Peralta System). He is also a security practitioner and AI tinkerer.*
