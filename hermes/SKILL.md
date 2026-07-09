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

Load this skill when the user says:
- "Evaluate my project honestly"
- "Tell me if this project has a future"
- "Is this worth pursuing?"
- "Rate my project"
- "Be brutally honest about my project"
- "Does this have commercial potential?"
- "I need a reality check"

**Do NOT use when:**
- The user is clearly emotionally fragile or going through a difficult time
- The user needs encouragement, not honesty
- The project is a clearly stated learning exercise (not a commercial endeavor)
- The user explicitly asks for positive feedback only

## How to Use

### Step 1: Collect Project Information

Ask the user for:
1. Project name and path (local or GitHub URL)
2. Brief description (1-3 sentences)
3. Target market / intended users
4. Business model (if commercial)
5. Team size
6. Current traction (users? revenue?)
7. Any known competitors
8. Any unique advantages (patents, data, relationships, experience)

Ask ONE question at a time. Do not dump all 8.

### Step 2: Run Technical Assessment

Use the `core` evaluation engine or run manually:

```bash
# If the Python package is installed:
python -m core.evaluator --project /path/to/project
```

Or use the agent's own tools to assess the project:
- Read the source code
- Check for tests, CI, documentation
- Scan for security issues and code smells
- Evaluate architecture quality

### Step 3: Run Commercial Assessment

Based on user-provided information + web research:
- Search for competitors (GitHub stars, funding, market position)
- Evaluate market reality
- Assess differentiation and moat

### Step 4: Generate Strategic Options

Analyze every plausible strategic path:
- Open Core + Enterprise
- Consulting/Services
- Acquisition
- Pivot to new market
- Keep building (more features)
- Aggressive marketing
- Abandonment (the most rational option for many projects)

### Step 5: Deliver The Final Blow

Close with:
1. The fundamental question: "What do you have that others don't?"
2. Assessment of their unique advantages (if any)
3. Final verdict: Viable / Conditionally Viable / Not Viable
4. Confidence score
5. The uncomfortable truth
6. What to actually do

### Step 6: Follow-up

After delivering the evaluation:
- If "Not Viable": Offer no false hope. Recommend what they should actually do.
- If "Conditionally Viable": Identify the SINGLE risk that could kill it.
- If "Viable": Still remind them that 80% of viable projects fail anyway.

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
3. Is every strategic option I'm recommending actually easier than the current path?
4. If a friend told me they were pursuing this, would I try to stop them?
5. Am I writing detailed implementation steps for something with <10% chance?

## Verification Checklist

- [ ] All 8 project information items collected
- [ ] Technical assessment run (code scan, test check, CI check)
- [ ] Commercial assessment with competitor research
- [ ] Strategic options evaluated with realistic probabilities
- [ ] "Same Difficulty Trap" checked for each option
- [ ] Final blow delivered with uncomfortable truth
- [ ] Confidence score honestly assigned
- [ ] No false hope given
- [ ] Concrete "what to actually do" provided
