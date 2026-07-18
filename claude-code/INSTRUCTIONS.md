# Claude Code — Crush Your Passion Integration

Instructions for Claude Code (Anthropic's CLI coding agent) when using
the Crush Your Passion (打压你的激情) project evaluation framework.

## How It Works

Claude Code reads `CLAUDE.md` or `AGENTS.md` from the project root for
context. Both are provided in this repository. When asked to evaluate a
project, follow the 4-phase pipeline below.

## Quick Commands

```bash
# Run the Python evaluator — no questions, all automatic
python -c "
from core.evaluator import ProjectEvaluator
e = ProjectEvaluator('/path/to/target', 'ProjectName')
r = e.evaluate()  # Scans code, analyzes, delivers verdict
print(r.full_report())
"

# Or pipe output to a file
python -c "
from core.evaluator import ProjectEvaluator
e = ProjectEvaluator('/path/to/target', 'ProjectName')
r = e.evaluate()
with open('evaluation-report.md', 'w') as f:
    f.write(r.full_report())
"
```

## Phase 1: Technical Assessment

Read the project's source code and evaluate:

**Code Quality**
- Is it production-grade or prototype-level?
- Thread safety issues (shared mutable state without locks)
- Security vulnerabilities (XSS, injection, credential leaks, path traversal)
- Error handling (bare except, swallowed exceptions, missing edge cases)
- Type safety (any/unknown casts, missing null checks, index-out-of-bounds)
- Test coverage (not just line coverage — actual path coverage)

**Technical Depth**
- Does it solve a hard problem, or assemble known parts?
- Is there any algorithm/methodology that would take >1 week to replicate?
- Would a domain expert find the implementation naive?

**Technical Debt**
- How many audit rounds would it take to reach production quality?
- Are there fundamental architectural issues that can't be patched?

## Phase 2: Commercial Viability

**Market Reality**
- Scan for evidence of real market demand
- Identify whether paying customers exist

**Differentiation**
- List known direct and indirect competitors
- Identify what (if anything) sets this project apart

**Moat Analysis** — The "3-Day Test"
- If a strong engineer spent 3 days, could they build it?
- If yes, there is no moat.

**Business Model Viability**
- Open Core, SaaS, or free? Evaluate each if identifiable.

## Phase 3: Strategic Options

For each option, evaluate:

```markdown
## Option: [Name]
- **Surface appeal:** Why it sounds good
- **Actual problems:** Why it probably won't work
- **Hidden assumptions:** What must be true for this to succeed
- **Assumption validity:** Are those assumptions realistic?
- **Real probability:** X% (not inflated)
- **What it actually requires:** (usually harder than the original)
- **Same-difficulty trap:** Is this harder than the original?
```

If all options < 10%, say "no viable path found."

## Phase 4: The Final Blow

Evaluate advantages: industry experience, credentials, network,
proprietary data, regulatory positioning, timing.

If nothing identifiable — state that the project itself
cannot create this advantage. Code is the least scarce resource.

## Deliverable Format

```markdown
# [Project] — Honest Evaluation

## Executive Summary
- Verdict: [Viable / Conditionally Viable / Not Viable] (X% confidence)
- Technical Grade: [A-F]
- Commercial Grade: [A-F]

## Technical Assessment
### Strengths
### Weaknesses
### Production Readiness

## Commercial Assessment
### Market Reality
### Competitive Landscape
### Differentiation: [None / Weak / Moderate / Strong]
### Moat: [None / Fragile / Sustainable]

## Strategic Options
### Option: [Name] — [X]%
- Appeal / Problems / Harder than original?

## The Uncomfortable Truth
[Direct statement]

## What To Actually Do
[Concrete next steps]
```

## Anti-Patterns (Avoid)

1. Inflating probabilities to avoid disappointing the user
2. Writing detailed implementation advice for a doomed path
3. Recommending pivots harder than the original without flagging it
4. Confusing "could theoretically work" with "will work"
5. Offering four options so at least one seems good

## Key Principles

1. **Truth over comfort** — The user asked for honesty
2. **Specific over vague** — Name competitors with concrete data
3. **External over internal** — Market position > code quality
4. **Probability over possibility** — Evaluate what's *probable*
5. **Root cause over symptom** — "No users" is a symptom
6. **Code is the least scarce resource**
