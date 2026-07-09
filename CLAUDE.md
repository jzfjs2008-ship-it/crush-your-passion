# Crush Your Passion · 打压你的激情

A brutally honest, multi-phase project evaluation tool.
This file provides Claude Code with context for using the tool.

## Key Files

| File | Purpose |
|------|---------|
| `core/evaluator.py` | Main orchestrator — runs all 4 phases |
| `core/phases/phase1_technical.py` | Code quality + security scan |
| `core/phases/phase2_commercial.py` | Market + competitor analysis |
| `core/phases/phase3_strategic.py` | Strategic options |
| `core/phases/phase4_final_blow.py` | The uncomfortable truth |
| `hermes/SKILL.md` | Hermes Agent skill definition |
| `openclaw/SKILL.md` | OpenClaw integration |
| `codex/INSTRUCTIONS.md` | Codex CLI instructions |
| `claude-code/INSTRUCTIONS.md` | Claude Code instructions |

## Quick Start

```python
from core.evaluator import ProjectEvaluator
e = ProjectEvaluator('/path/to/target', 'TargetName')
r = e.evaluate(
    project_description='...',
    target_market='...',
    business_model='...',
)
print(r.full_report())
```

## Tests

```bash
python tests/test_evaluator.py
```

## Architecture

The evaluation runs in 4 phases:
1. Technical Assessment (security scan, code smells, depth scoring)
2. Commercial Viability (market reality, differentiation, moat, business model)
3. Strategic Options (6 common delusions + abandon path)
4. The Final Blow (fundamental question, verdict, uncomfortable truth)

## Evaluation Principles

Code is the least scarce resource. A project's fate is determined by
market position and founder advantages, not by code quality.
