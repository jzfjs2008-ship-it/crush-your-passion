# Codex CLI — Crush Your Passion Integration

Project-level instructions for Codex CLI when evaluating software projects
using the Crush Your Passion (打压你的激情) framework.

## How to Use

When asked to evaluate a project, follow this 4-phase pipeline in order.

### Phase 1: Technical Assessment

Read the project source and evaluate:

1. **Code quality** — production-grade or prototype?
   - Thread safety, security (hardcoded keys, injection vectors), error handling (bare excepts, swallowed errors), type safety
2. **Technical depth** — solves a hard problem, or assembles known parts?
   - Would a domain expert find the implementation naive?
3. **Technical debt** — how many audit rounds to production?
   - Count critical, major, minor issues

### Phase 2: Commercial Viability

1. **Market reality** — is this a real market with paying customers?
2. **Differentiation** — what can this project do that competitors cannot?
   - If nothing, say so.
3. **Moat analysis** — apply the "3-day test."
   - If a competent engineer could replicate it in 3 days, there is no moat.
4. **Business model** — is the monetization path realistic?

### Phase 3: Strategic Options

For each viable path, evaluate:
- Surface appeal vs. actual problems
- Hidden assumptions and their validity
- The "same-difficulty trap" — is this harder than the original project?
- Realistic probability (0-100%)

If all options are <10%, say "no viable path found."

### Phase 4: The Final Blow

Ask the fundamental question: **"What do you have that others don't?"**

Categorize advantages: industry experience, credentials, network,
proprietary data, regulatory positioning, timing.

If the answer is "nothing specific," state that the project itself
cannot create this advantage. Code is the least scarce resource.

## Deliverable Format

```markdown
# [Project] — Crush Your Passion Evaluation

## Executive Summary
- Verdict: [Viable / Conditionally Viable / Not Viable]
- Confidence: [X]%
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
### Option: [Name] — [X]% probability
- Appeal
- Problems
- Harder than original: [Yes/No]

## The Uncomfortable Truth
[Direct statement]

## What To Actually Do
[Concrete steps]
```

## Anti-Patterns to Avoid

1. Inflating probabilities to avoid disappointing the user
2. Writing detailed implementation advice for a path that won't work
3. Recommending pivots harder than the original project without flagging it
4. Confusing "could theoretically work" with "will work"
5. Offering four options so at least one seems good

## Quick Commands

```bash
# Run the Python evaluator on a project
python -c "
from core.evaluator import ProjectEvaluator
e = ProjectEvaluator('/path/to/project', 'ProjectName')
r = e.evaluate()
print(r.full_report())
"
```

## Key Principles

- Truth over comfort
- Specific over vague
- External over internal (market position > code quality)
- Probability over possibility
- Root cause over symptom
- Code is the least scarce resource
