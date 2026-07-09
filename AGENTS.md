# Crush Your Passion · 打压你的激情

Agent context file — read by Codex CLI, Hermes Agent, Claude Code, and OpenClaw.

## Overview

This project is a **brutally honest project evaluation tool**. It runs a
4-phase pipeline to assess software projects:

1. **Technical** — code quality, security, depth, debt
2. **Commercial** — market reality, differentiation, moat, business model
3. **Strategic** — every pivot analyzed, most found wanting
4. **The Final Blow** — the uncomfortable truth + what to actually do

## Using This Repo

### As a Library

```python
from core.evaluator import ProjectEvaluator
e = ProjectEvaluator('/path/to/target-project', 'Target')
r = e.evaluate(project_description="...", target_market="...")
print(r.full_report())
```

### Platform Integrations

| Platform | File | How |
|----------|------|-----|
| Hermes Agent | `hermes/SKILL.md` | `hermes skills install ./hermes/SKILL.md` |
| OpenClaw | `openclaw/SKILL.md` | `cp -r openclaw ~/.openclaw/skills/crush-your-passion/` |
| Codex CLI | `codex/INSTRUCTIONS.md` | Read instructions, then execute evaluation |
| Claude Code | `codex/INSTRUCTIONS.md` | Same — cross-platform compatible |

### Run the Evaluator Directly

```bash
pip install -e .
python -c "
from core.evaluator import ProjectEvaluator
e = ProjectEvaluator('/some/project', 'MyProject')
r = e.evaluate(
    project_description='A cool new tool',
    target_market='developers',
    business_model='free',
)
print(r.full_report())
"
```

### Run Tests

```bash
python tests/test_evaluator.py
```

## Evaluation Principles

1. **Truth over comfort.** The user asked for honesty. Anything less is disrespect.
2. **Specific over vague.** Name competitors with concrete data (stars, funding).
3. **External over internal.** A project's fate is determined by market position,
   not code quality.
4. **Probability over possibility.** Everything is *possible*. Evaluate *probable*.
5. **Root cause over symptom.** "No users" is a symptom. "No differentiation" is
   the root cause.
6. **Code is the least scarce resource.** If it can be replicated in 3 days,
   it has no defensible value.

## Project Structure

```
crush-your-passion/
├── core/                          # Python evaluation engine
│   ├── evaluator.py               # Orchestrator
│   └── phases/                    # 4-phase pipeline
│       ├── phase1_technical.py
│       ├── phase2_commercial.py
│       ├── phase3_strategic.py
│       └── phase4_final_blow.py
├── hermes/SKILL.md                # Hermes Agent integration
├── openclaw/SKILL.md              # OpenClaw integration
├── codex/INSTRUCTIONS.md          # Codex CLI instructions
├── tests/test_evaluator.py        # Test suite (9 tests)
├── pyproject.toml
└── README.md
```
