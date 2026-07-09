# Crush Your Passion · 打压你的激情

> A brutally honest, multi-phase project evaluation tool that systematically
> dismantles developer enthusiasm by exposing every technical flaw, commercial
> weakness, and strategic dead-end.

**The purpose is not cruelty — it's clarity.** If your passion for a project
survives this evaluation, it's probably real. If it doesn't, you saved yourself
years of wasted effort.

---

## Why This Exists

Every developer has had a passion project. Most of those projects should never
have been started, and very few should be continued. This tool exists to give
you the uncomfortable truth *before* you invest years of your life.

It is inspired by:

- The harsh reality that **90%+ of software projects fail commercially**
- The observation that **code is the least scarce resource** — what matters is
  market position, relationships, and timing
- The uncomfortable truth that **most pivots are harder than the original project**

## The Four Phases

| Phase | Name | What It Evaluates |
|-------|------|-------------------|
| 1 | Technical Assessment | Code quality, security vulnerabilities, technical depth, tech debt |
| 2 | Commercial Viability | Market reality, differentiation, moat analysis, business model |
| 3 | Strategic Options | Every pivot/exit strategy — and why most won't work |
| 4 | The Final Blow | The uncomfortable truth and what to actually do |

## Platforms

This project supports four agent platforms:

| Platform | Integration | How to Use |
|----------|-------------|------------|
| **Hermes Agent** | `hermes/SKILL.md` | `hermes skills install ./hermes/SKILL.md` |
| **OpenClaw** | `openclaw/SKILL.md` | `cp -r openclaw ~/.openclaw/skills/crush-your-passion/` |
| **Codex CLI** | `codex/INSTRUCTIONS.md` | Read instructions, run evaluation inline |
| **Claude Code** | `claude-code/INSTRUCTIONS.md` + `CLAUDE.md` | Auto-reads `CLAUDE.md` at project root |

All platforms also read `AGENTS.md` at project root for cross-platform context.

## Quick Start

### Hermes Agent

```bash
# Install the skill
hermes skills install ./hermes/SKILL.md

# Load in session
/skill crush-your-passion

# Then say:
# "Evaluate my project brutally honestly"
# "Is my project worth pursuing?"
```

### OpenClaw

```bash
# Copy the skill
cp -r openclaw ~/.openclaw/skills/crush-your-passion

# Enable the hooks
openclaw hooks enable crush-your-passion
```

### Codex CLI

```bash
# Codex loads AGENTS.md at project root automatically.
# To evaluate a project, run:
codex exec "Evaluate this project using the Crush Your Passion framework: run the 4-phase assessment, deliver a full report."
```

### Claude Code

```bash
# Claude Code auto-loads CLAUDE.md or AGENTS.md from the project root.
# Start a session:
claude

# Or run a one-shot evaluation:
claude -p "Run the Crush Your Passion evaluator on the project at /path/to/target and deliver a full 4-phase report."
```


```bash
pip install -e .

# Use as a library
python -c "
from core.evaluator import ProjectEvaluator
evaluator = ProjectEvaluator('/path/to/project', 'My Project')
report = evaluator.evaluate()
print(report.full_report())
"
```

## Project Structure

```
crush-your-passion/
├── core/
│   ├── __init__.py
│   ├── evaluator.py              # Main orchestrator
│   └── phases/
│       ├── phase1_technical.py   # Code quality & security scan
│       ├── phase2_commercial.py  # Market & competitor analysis
│       ├── phase3_strategic.py   # Strategic options
│       └── phase4_final_blow.py  # The uncomfortable truth
├── hermes/
│   └── SKILL.md                  # Hermes Agent skill
├── openclaw/
│   └── SKILL.md                  # OpenClaw skill
├── codex/
│   └── INSTRUCTIONS.md           # Codex CLI instructions
├── claude-code/
│   └── INSTRUCTIONS.md           # Claude Code instructions
├── tests/
│   └── test_evaluator.py         # Test suite
├── pyproject.toml
├── README.md
└── LICENSE
```

## The Philosophy

This tool operates on six core principles:

1. **Truth over comfort** — The user asked for honesty. Anything less is disrespect.
2. **Specific over vague** — Name concrete issues with file and line references.
3. **External over internal** — A project's fate is determined by market position
   and founder advantages, not code quality or feature count.
4. **Probability over possibility** — Everything is *possible*. Evaluate what's *probable*.
5. **Root cause over symptom** — "No users" is a symptom. "No differentiation"
   is the root cause.
6. **Code is the least scarce resource** — If a project can be replicated in days,
   it has no defensible value.

## License

MIT — Use it. Abuse it. Let it crush your enthusiasm for projects that
don't deserve your time.
