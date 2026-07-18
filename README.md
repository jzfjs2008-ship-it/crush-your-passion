# Crush Your Passion · 打压你的激情

> **EN:** A brutally honest, multi-phase project evaluation tool. Give it a project path — it scans every file, grades your code on 6 dimensions, kills false hope, and delivers the uncomfortable truth. No questions asked.
>
> **ZH:** 一个极度诚实的多阶段项目评估工具。只需给它一个项目路径——它就会扫描每一个文件，从六个维度给你的代码打分，扼杀不切实际的幻想，然后给出那个让人不舒服的真相。不问任何问题。

---

## Quick Start / 快速开始

```python
pip install -e .

from core.evaluator import ProjectEvaluator

# Give a path. Get crushed. / 给路径，挨打击。
e = ProjectEvaluator('/path/to/project', 'MyProject')
r = e.evaluate()   # No questions / 不提问题
print(r.full_report())
```

That's it. 就这点事。

---

## What It Does / 它能做什么

**EN:** Crush Your Passion runs a **4-phase pipeline** on your project. You give it a path. It scans your code. It grades you. It tells you things you don't want to hear.

**ZH:** 打压你的激情在你的项目上执行 **4 阶段管道分析**。你给它一个路径。它扫描你的代码。它给你打分。它告诉你那些你不想听到的话。

| Phase / 阶段 | EN | ZH |
|-------------|----|------|
| 1 | **Technical Assessment** — security, code quality, infra, docs, testing, depth | **技术评估** — 安全、代码质量、基础设施、文档、测试、技术深度 |
| 2 | **Commercial Viability** — market, differentiation, moat, business model | **商业评估** — 市场、差异化、护城河、商业模式 |
| 3 | **Strategic Options** — every pivot, and why most won't work | **战略分析** — 每一条路，以及为什么大部分走不通 |
| 4 | **The Final Blow** — the uncomfortable truth + what to actually do | **致命一击** — 那个不舒服的真相 + 你到底该怎么做 |

The result is a full report with **6 technical dimensions**, commercial grades, strategic probabilities, and a final verdict.

最终你得到一份完整的报告，包含 **6 个技术维度评分**、商业评级、战略概率分析，以及最终结论。

---

## The 6 Technical Dimensions / 六个技术维度

**EN:** The scan evaluates your project across six independent axes, each scored 0–100:

**ZH:** 扫描从六个独立维度评估你的项目，每个维度 0–100 分：

| Dimension / 维度 | EN | ZH |
|------------------|-----|------|
| **Security** | Hardcoded credentials, eval/exec, SQLi, XSS, pickle, shell injection | 硬编码凭据、eval/exec、SQL 注入、XSS、反序列化、shell 注入 |
| **Code Quality** | Bare excepts, TODOs, FIXMEs, dead code, stray debug prints | 裸 except、TODOs、FIXMEs、死代码、遗留调试输出 |
| **Depth** | Docker, protobuf, gRPC, k8s, migrations, CI/CD complexity | Docker、protobuf、gRPC、k8s、数据库迁移、CI/CD 复杂度 |
| **Infrastructure** | CI/CD pipeline, Dockerfile, editorconfig, env example | CI/CD 流水线、Dockerfile、editorconfig、环境变量模板 |
| **Documentation** | README quality + length, LICENSE, CHANGELOG, CONTRIBUTING | README 质量与长度、许可证、变更日志、贡献指南 |
| **Testing** | Test files, framework detection (pytest/Jest/Go/Rust), assertion validation | 测试文件、框架检测（pytest/Jest/Go/Rust）、断言验证 |

Language auto-detection: Python, JavaScript, TypeScript, Rust, Go, Java, Kotlin, Ruby, PHP, C/C++, C#, Swift, Shell, Dockerfile.

自动检测语言：Python、JavaScript、TypeScript、Rust、Go、Java、Kotlin、Ruby、PHP、C/C++、C#、Swift、Shell、Dockerfile。

---

## Platform Integrations / 平台集成

**EN:** Plug it into your agent of choice. All integrations are zero-interaction — path in, report out.

**ZH:** 插到你喜欢的 Agent 里。所有集成都是零交互——给路径，出报告。

| Platform / 平台 | File / 文件 | Install / 安装 |
|----------------|-------------|----------------|
| **Hermes Agent** | `hermes/SKILL.md` | `hermes skills install ./hermes/SKILL.md` |
| **OpenClaw** | `openclaw/SKILL.md` | `cp -r openclaw ~/.openclaw/skills/crush-your-passion/` |
| **Codex CLI** | `codex/INSTRUCTIONS.md` | Reads `AGENTS.md` automatically |
| **Claude Code** | `claude-code/INSTRUCTIONS.md` + `CLAUDE.md` | Reads `CLAUDE.md` / `AGENTS.md` automatically |

---

## Bilingual Output / 双语输出

**EN:** The report auto-detects your locale from:
1. Chinese characters in your project description → Chinese output
2. `LC_ALL` / `LANG` environment variables
3. Windows system language
4. Falls back to English

**ZH:** 报告自动检测你的语言环境，检测顺序：
1. 项目描述含中文字符 → 中文输出
2. `LC_ALL` / `LANG` 环境变量
3. Windows 系统语言
4. 都不匹配则使用英文

Explicit override / 手动指定：

```python
r_en = e.evaluate(locale='en')
r_zh = e.evaluate(locale='zh')
```

---

## Project Structure / 项目结构

```
crush-your-passion/
├── core/
│   ├── evaluator.py              # Orchestrator / 主调度器
│   └── phases/
│       ├── phase1_technical.py   # 6-dimension code scan / 六维代码扫描
│       ├── phase2_commercial.py  # Market analysis / 市场分析
│       ├── phase3_strategic.py   # Strategic options / 战略选项
│       └── phase4_final_blow.py  # The verdict / 最终判决
├── hermes/SKILL.md               # Hermes Agent integration
├── openclaw/SKILL.md             # OpenClaw integration
├── codex/INSTRUCTIONS.md         # Codex CLI instructions
├── claude-code/INSTRUCTIONS.md   # Claude Code instructions
├── AGENTS.md                     # Cross-platform context / 跨平台上下文
├── CLAUDE.md                     # Claude Code context
├── tests/test_evaluator.py       # 9-test suite / 9 个测试
├── pyproject.toml
├── README.md
└── LICENSE
```

---

## Philosophy / 理念

**EN:** Six rules this tool lives by:

**ZH:** 这个工具遵循六条规则：

1. **Truth over comfort** — Honesty is respect. / **真相优先于安慰** — 诚实就是尊重。
2. **Specific over vague** — Name files, lines, flaws. / **具体优先于模糊** — 指出文件、行号、缺陷。
3. **External over internal** — Market position > code quality. / **外部优先于内部** — 市场地位 > 代码质量。
4. **Probability over possibility** — What's *probable*, not what's *possible*. / **概率优先于可能性** — 评估*大概率*，不是*有可能*。
5. **Root cause over symptom** — "No users" is a symptom. / **根因优先于表象** — "没有用户"只是表象。
6. **Code is the least scarce resource** — If it can be copied in 3 days, it has no moat. / **代码是最不稀缺的资源** — 三天就能抄走的项目没有护城河。

---

## License / 许可证

MIT — Use it. Abuse it. Let it crush your enthusiasm for projects that don't deserve your time.

MIT — 用它，滥用它。让它扼杀你对那些不值得浪费时间项目的热情。
