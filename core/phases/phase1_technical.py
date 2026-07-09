"""
Phase 1: Technical Assessment

Evaluates code quality, technical depth, and technical debt.
Designed to find every flaw — this phase is the first crack
in the developer's confidence.
"""

import ast
import re
from pathlib import Path
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class TechnicalFinding:
    category: str  # code-quality, security, depth, debt
    severity: str  # critical, major, minor
    title: str
    description: str
    line_ref: Optional[str] = None


@dataclass
class TechnicalReport:
    findings: List[TechnicalFinding] = field(default_factory=list)
    code_quality_score: int = 0       # 0-100
    technical_depth_score: int = 0    # 0-100
    debt_estimate_rounds: int = 0
    production_readiness: str = "Not Ready"
    fatal_flaw: Optional[str] = None

    def grade(self) -> str:
        avg = (self.code_quality_score + self.technical_depth_score) / 2
        if avg >= 90: return "A"
        if avg >= 75: return "B"
        if avg >= 60: return "C"
        if avg >= 40: return "D"
        return "F"

    def summary(self) -> str:
        return (
            f"Technical Grade: {self.grade()}\n"
            f"Code Quality: {self.code_quality_score}/100\n"
            f"Technical Depth: {self.technical_depth_score}/100\n"
            f"Production Readiness: {self.production_readiness}\n"
            f"Estimated Audit Rounds to Production: {self.debt_estimate_rounds}\n"
            f"Findings: {len(self.findings)} ({sum(1 for f in self.findings if f.severity == 'critical')} critical, "
            f"{sum(1 for f in self.findings if f.severity == 'major')} major, "
            f"{sum(1 for f in self.findings if f.severity == 'minor')} minor)"
        )


class Phase1Technical:
    """Brutal technical evaluation of a project."""

    SECURITY_PATTERNS = [
        (r'(?:sk|pk)_[a-fA-F0-9]{32,}', 'exposed_api_key', 'Hardcoded API key found'),
        (r'password\s*=\s*["\'][^"\']+["\']', 'hardcoded_password', 'Hardcoded credential'),
        (r'exec\s*\(', 'dangerous_exec', 'Use of exec() — code injection risk'),
        (r'eval\s*\(', 'dangerous_eval', 'Use of eval() — code injection risk'),
        (r'raw_input', 'python2_unsafe_input', 'Python 2 raw_input — dangerous'),
        (r'(?:SELECT|INSERT|UPDATE|DELETE).*\+', 'sql_injection_risk', 'String concatenation in SQL — SQL injection vector'),
        (r'<script[^>]*>', 'xss_risk', 'Inline script tag — XSS vector'),
        (r'pickle\.loads?', 'unsafe_deserialize', 'pickle deserialization — arbitrary code execution'),
        (r'os\.system\(', 'os_command_injection', 'os.system() — shell injection risk'),
        (r'subprocess\.call\(.*shell=True', 'shell_injection', 'subprocess with shell=True — command injection'),
    ]

    CODE_SMELL_PATTERNS = [
        (r'except\s*:\s*pass', 'bare_except_pass', 'Bare except with pass — silently swallows errors'),
        (r'except\s*:', 'bare_except', 'Bare except — catches all exceptions'),
        (r'\#\s*TODO', 'todo_left', 'Unresolved TODO in code'),
        (r'\#\s*FIXME', 'fixme_left', 'Unresolved FIXME in code'),
        (r'(?:print|printf?)\s*\(', 'debug_print', 'Stray print/debug statement in production code'),
        (r'\.decode\(|\.encode\(', 'encoding_hack', 'Manual encode/decode — likely encoding workaround'),
        (r'try\s*:\s*\n\s+pass', 'empty_try', 'Empty try block'),
        (r'if\s+False', 'dead_code', 'Dead code (if False block)'),
        (r'__author__', 'stale_header', 'Stale module header metadata'),
    ]

    def __init__(self, project_path: str, project_name: str):
        self.project_path = Path(project_path)
        self.project_name = project_name

    def evaluate(self) -> TechnicalReport:
        report = TechnicalReport()

        if not self.project_path.exists():
            report.fatal_flaw = f"Project path does not exist: {self.project_path}"
            report.production_readiness = "Not Ready"
            report.code_quality_score = 0
            report.technical_depth_score = 0
            report.debt_estimate_rounds = 999
            return report

        python_files = list(self.project_path.rglob("*.py"))
        other_source = (
            list(self.project_path.rglob("*.js")) +
            list(self.project_path.rglob("*.ts")) +
            list(self.project_path.rglob("*.rs")) +
            list(self.project_path.rglob("*.go")) +
            list(self.project_path.rglob("*.java"))
        )

        # Code quality: scan for patterns
        security_hits = 0
        smell_hits = 0
        total_lines = 0
        total_files = len(python_files) + len(other_source)

        for f in python_files + other_source:
            try:
                content = f.read_text(encoding="utf-8", errors="ignore")
                lines = content.splitlines()
                total_lines += len(lines)

                # Security scan
                for pattern, finding_id, desc in self.SECURITY_PATTERNS:
                    matches = re.finditer(pattern, content, re.IGNORECASE)
                    for m in matches:
                        line_num = content[:m.start()].count('\n') + 1
                        report.findings.append(TechnicalFinding(
                            category="security",
                            severity="critical",
                            title=desc,
                            description=f"In {f.name}:{line_num} — {m.group()[:60]}",
                            line_ref=f"{f.name}:{line_num}",
                        ))
                        security_hits += 1

                # Code smell scan
                for pattern, finding_id, desc in self.CODE_SMELL_PATTERNS:
                    matches = re.finditer(pattern, content, re.IGNORECASE)
                    for m in matches:
                        line_num = content[:m.start()].count('\n') + 1
                        severity = "major" if finding_id in ("bare_except_pass", "bare_except") else "minor"
                        report.findings.append(TechnicalFinding(
                            category="code-quality",
                            severity=severity,
                            title=desc,
                            description=f"In {f.name}:{line_num}",
                            line_ref=f"{f.name}:{line_num}",
                        ))
                        smell_hits += 1

            except (IOError, UnicodeDecodeError):
                report.findings.append(TechnicalFinding(
                    category="code-quality",
                    severity="minor",
                    title="Unreadable file",
                    description=f"Cannot read {f} — possibly binary or corrupted",
                ))

        # Technical depth: check for indicators of shallow work
        has_tests = len(list(self.project_path.rglob("test_*.py"))) > 0 or \
                    len(list(self.project_path.rglob("*_test.py"))) > 0
        has_docs = (self.project_path / "README.md").exists()
        has_type_hints = False
        has_ci_config = (
            (self.project_path / ".github" / "workflows").exists() or
            (self.project_path / ".gitlab-ci.yml").exists()
        )

        for f in python_files:
            try:
                content = f.read_text(encoding="utf-8", errors="ignore")
                tree = ast.parse(content)
                for node in ast.walk(tree):
                    if isinstance(node, ast.FunctionDef):
                        if node.returns or any(
                            hasattr(a, 'annotation') and a.annotation
                            for a in node.args.args
                        ):
                            has_type_hints = True
                            break
            except SyntaxError:
                continue

        # Score calculation — intentionally harsh
        score_quality = 100
        score_quality -= security_hits * 15  # -15 per security issue
        score_quality -= smell_hits * 5      # -5 per smell
        if total_files == 0:
            score_quality -= 50
        if total_lines < 50:
            score_quality -= 30
        score_quality = max(0, min(100, score_quality))

        score_depth = 100
        if not has_tests:
            score_depth -= 25
            report.findings.append(TechnicalFinding(
                category="depth", severity="major",
                title="No test suite",
                description="Zero test files found. Untested code is not production code."
            ))
        if not has_docs:
            score_depth -= 15
            report.findings.append(TechnicalFinding(
                category="depth", severity="minor",
                title="No README",
                description="Missing README.md — zero discoverability for new contributors."
            ))
        if not has_type_hints:
            score_depth -= 10
        if not has_ci_config:
            score_depth -= 15
            report.findings.append(TechnicalFinding(
                category="depth", severity="major",
                title="No CI/CD pipeline",
                description="No CI configuration found. Every change is untested and manually deployed."
            ))
        if total_files < 3:
            score_depth -= 20
        score_depth = max(0, min(100, score_depth))

        report.code_quality_score = score_quality
        report.technical_depth_score = score_depth

        # Estimate debt
        report.debt_estimate_rounds = (
            security_hits * 2 +
            smell_hits // 2 +
            (3 if not has_tests else 0) +
            (2 if not has_ci_config else 0)
        )
        if report.debt_estimate_rounds == 0:
            report.debt_estimate_rounds = 1  # nobody's perfect

        # Production readiness
        if security_hits > 0:
            report.production_readiness = "Not Ready (security vulnerabilities)"
        elif score_quality < 40 or score_depth < 40:
            report.production_readiness = "Needs Significant Work"
        elif score_quality < 70 or score_depth < 70:
            report.production_readiness = "Conditional — Needs X weeks"
        else:
            report.production_readiness = "Ready"

        return report
