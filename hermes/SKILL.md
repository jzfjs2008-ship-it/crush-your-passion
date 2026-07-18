---
name: crush-your-passion
description: "A brutally honest, multi-phase project evaluation tool that systematically dismantles a developer's enthusiasm by exposing every technical flaw, commercial weakness, and strategic dead-end. Designed to test whether your passion can survive absolute honesty."
version: 1.0.0
author: jznem
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [evaluation, brutal-honesty, project-review, code-quality, commercial-viability, strategic-analysis]
    related_skills: [inspiration, spike, plan, code-audit]
---

# Crush Your Passion · 打压你的激情 — Project Evaluation Skill

## Overview

**Crush Your Passion** is a multi-phase project evaluation tool designed to give developers the most brutally honest assessment possible of their software project. It deliberately aims to suppress unwarranted enthusiasm by exposing uncomfortable truths.

The name is ironic — the tool's purpose is not cruelty, but clarity. If your passion for a project survives this evaluation, it's probably real. If it doesn't, you saved yourself years of wasted effort.

### What It Does

| Phase | Name | What It Evaluates |
|-------|------|-------------------|
| 1 | Technical Assessment | Code quality, security, technical depth, tech debt |
| 2 | Commercial Viability | Market reality, differentiation, moat, business model |
| 3 | Strategic Options | Every pivot/exit strategy — and why most won't work |
| 4 | The Final Blow | The uncomfortable truth and what to actually do |

## When to Use

Load this skill when the user asks for a project evaluation.
Deliver the report directly — no questions, no data collection.

## How to Use

### Run the Evaluation

Get the project path, then execute the 4-phase pipeline directly:

```bash
# Option A: Use Python evaluator (automated code scan)
python -c "
from core.evaluator import ProjectEvaluator
e = ProjectEvaluator('/path/to/project', 'ProjectName')
r = e.evaluate()  # No questions asked — scans code automatically
print(r.full_report())
"
```

### The 4 Phases (Run in Order)

| Phase | What It Does | How |
|-------|-------------|-----|
| 1 Technical | Scans code for security flaws, code smells, infra gaps, docs quality, testing coverage | Automated — read source + config files |
| 2 Commercial | Evaluates market reality, differentiation, moat | Use defaults unless user volunteers info |
| 3 Strategic | Lists every pivot — and why most won't work | Based on Phase 1+2 results |
| 4 The Final Blow | Delivers the uncomfortable truth | Automatic from previous phases |

## Output Format

```markdown
# [Project Name] — CRUSH YOUR PASSION EVALUATION

## EXECUTIVE SUMMARY
- Verdict: [Viable / Conditionally Viable / Not Viable]
- Confidence: [X]%
- Technical Grade: [A-F]
- Commercial Grade: [A-F]

## TECHNICAL ASSESSMENT
[Findings, scores, fatal flaws]

## COMMERCIAL ASSESSMENT
[Market reality, competitors, moat]

## STRATEGIC OPTIONS
[Each option with realistic probability]

## THE FINAL BLOW
[The uncomfortable truth + what to actually do]
```

## Key Principles

1. **Truth over comfort.** The user asked for honesty. Anything less is disrespect.
2. **Specific over vague.** Name concrete issues with line numbers when possible.
3. **External over internal.** A project's fate is determined by market position and founder advantages, not code quality.
4. **Probability over possibility.** Everything is *possible*. Evaluate what's *probable*.
5. **Root cause over symptom.** "No users" is a symptom. "No differentiation in a crowded market" is the root cause.
6. **Code is the least scarce resource.** If a project's value can be replicated in days, the project has no defensible value.
7. **Every pivot is harder than the original.** If you recommend pivoting, acknowledge it.

## Anti-Patterns (MUST AVOID)

1. **Inflating probabilities.** Don't say 15% when you mean 3%.
2. **Detailed advice for doomed paths.** Don't write 2000 words on a consulting pivot when the user has no industry connections.
3. **Recommending harder pivots without labeling them.** Always flag "this is harder than your current approach."
4. **Multiple options so one seems good.** If all options are <10%, say so.
5. **Confusing "could work" with "will work."** Everything could work. Very little does.

## Self-Check Before Delivering

1. Would I invest my own money in this? If no, why am I suggesting it could work?
2. Am I inflating probabilities to avoid disappointing the user?
3. If a friend told me they were pursuing this, would I try to stop them?

## Verification

- [ ] Phase 1 technical scan completed
- [ ] Phase 2-4 run with available data
- [ ] Final blow delivered — no false hope
