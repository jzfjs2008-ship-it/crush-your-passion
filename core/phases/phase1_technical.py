"""
Phase 1: Technical Assessment

Comprehensive multi-language project analysis covering:
- Code security and quality (Python, JS/TS, Rust, Go, Java)
- Infrastructure maturity (CI/CD, Docker, configs)
- Dependency health
- Documentation completeness
- Project structure and modularization
- Git health
- Architecture depth
"""

import ast
import re
import json
from pathlib import Path
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class TechnicalFinding:
    category: str   # security, code-quality, dependency, docs, infra, structure, testing, maintainability
    severity: str   # critical, major, minor, info
    title: str
    description: str
    line_ref: Optional[str] = None


@dataclass
class TechnicalReport:
    findings: List[TechnicalFinding] = field(default_factory=list)
    security_score: int = 0          # 0-100
    quality_score: int = 0           # 0-100
    depth_score: int = 0             # 0-100
    infra_score: int = 0             # 0-100
    docs_score: int = 0              # 0-100
    testing_score: int = 0           # 0-100
    debt_estimate_rounds: int = 0
    production_readiness: str = "Not Ready"
    fatal_flaw: Optional[str] = None
    project_language: str = "Unknown"
    total_files: int = 0
    total_lines: int = 0
    has_tests: bool = False
    has_ci: bool = False
    has_docker: bool = False
    has_readme: bool = False
    has_license: bool = False
    has_changelog: bool = False
    has_contributing: bool = False

    def grade(self) -> str:
        scores = [self.security_score, self.quality_score, self.depth_score,
                  self.infra_score, self.docs_score, self.testing_score]
        avg = sum(scores) / len(scores)
        if avg >= 90: return "A"
        if avg >= 75: return "B"
        if avg >= 60: return "C"
        if avg >= 40: return "D"
        return "F"

    def breakdown(self) -> str:
        return (
            f"  Security:      {self.security_score}/100\n"
            f"  Code Quality:  {self.quality_score}/100\n"
            f"  Depth:         {self.depth_score}/100\n"
            f"  Infrastructure:{self.infra_score}/100\n"
            f"  Documentation: {self.docs_score}/100\n"
            f"  Testing:       {self.testing_score}/100"
        )

    def summary(self) -> str:
        return (
            f"Technical Grade: {self.grade()}\n"
            f"Language: {self.project_language} · "
            f"{self.total_files} files · {self.total_lines} LoC\n"
            f"{self.breakdown()}\n"
            f"Production Readiness: {self.production_readiness}\n"
            f"Audit Rounds Needed: {self.debt_estimate_rounds}\n"
            f"Findings: {len(self.findings)} "
            f"({sum(1 for f in self.findings if f.severity == 'critical')} critical, "
            f"{sum(1 for f in self.findings if f.severity == 'major')} major, "
            f"{sum(1 for f in self.findings if f.severity == 'minor')} minor, "
            f"{sum(1 for f in self.findings if f.severity == 'info')} info)"
        )


# ── Security patterns ──────────────────────────────────────────────

SECURITY_PATTERNS = [
    (r'(?:sk|pk)_[a-fA-F0-9]{32,}|ghp_[a-zA-Z0-9]{36}|gho_[a-zA-Z0-9]{36}',
     'exposed_credential', 'Hardcoded API key or token', 'critical'),
    (r'password\s*[=:]\s*["\'`][^"\'\n]+["\'`]',
     'hardcoded_password', 'Hardcoded password', 'critical'),
    (r'(?i)secret\s*[=:]\s*["\'`][^"\'\n]{8,}["\'`]',
     'hardcoded_secret', 'Hardcoded secret', 'critical'),
    (r'exec\s*\(', 'dangerous_exec', 'Use of exec() — arbitrary code execution risk', 'critical'),
    (r'eval\s*\(', 'dangerous_eval', 'Use of eval() — code injection risk', 'critical'),
    (r'(?i)os\.system\s*\(', 'os_command_injection', 'os.system() — shell injection vector', 'critical'),
    (r'subprocess\s*\.\s*(?:call|Popen|run)\s*\(.*shell\s*=\s*True',
     'shell_injection', 'subprocess with shell=True — command injection risk', 'critical'),
    (r'pickle\.loads?', 'unsafe_deserialize', 'pickle deserialization — arbitrary code execution', 'critical'),
    (r'(?:SELECT|INSERT|UPDATE|DELETE)\s+.+\+\s+', 'sql_injection_risk', 'String concatenation in SQL — SQL injection vector', 'critical'),
    (r'(?i)raw_input\b', 'unsafe_input_py2', 'Python 2 raw_input — dangerous', 'critical'),
]

SMELL_PATTERNS = [
    (r'except\s*:\s*(?:pass|#|$)',
     'bare_except_pass', 'Bare except with pass — silently swallows all errors', 'major'),
    (r'except\s*:', 'bare_except', 'Bare except — catches absolutely everything', 'major'),
    (r'\#\s*TODO', 'todo_unresolved', 'Unresolved TODO in code', 'minor'),
    (r'\#\s*FIXME', 'fixme_unresolved', 'Unresolved FIXME — known bug deferred', 'major'),
    (r'\#\s*HACK', 'hack_in_code', 'Hack/workaround in production code', 'major'),
    (r'\#\s*XXX', 'xxx_marker', 'XXX marker — code that needs attention', 'minor'),
    (r'(?i)\.decode\(|\.encode\(', 'encoding_hack', 'Manual encode/decode — likely encoding workaround', 'minor'),
    (r'try\s*:\s*\n\s+(?:pass|#)', 'empty_try_block', 'Empty try block — no error handling', 'major'),
    (r'if\s+False\s*:', 'dead_code', 'Dead code (if False block)', 'minor'),
    (r'print\s*\(', 'stray_print', 'Stray print() in production code', 'minor'),
    (r'console\.log\s*\(', 'stray_console_log', 'Stray console.log() in JS/TS code', 'minor'),
    (r'debugger\s*;', 'stray_debugger', 'Stray debugger statement in JS', 'major'),
    (r'(?i)fprintf\(stderr', 'debug_fprintf', 'Debug fprintf to stderr', 'minor'),
]

# ── Language detection ─────────────────────────────────────────────

LANGUAGE_SIGNATURES = [
    ("Python",         ["*.py"],     ["requirements.txt", "setup.py", "pyproject.toml", "Pipfile", "setup.cfg"]),
    ("JavaScript",     ["*.js"],     ["package.json"]),
    ("TypeScript",     ["*.ts", "*.tsx"], ["tsconfig.json", "package.json"]),
    ("Rust",           ["*.rs"],     ["Cargo.toml"]),
    ("Go",             ["*.go"],     ["go.mod"]),
    ("Java",           ["*.java"],   ["pom.xml", "build.gradle", "build.gradle.kts"]),
    ("Kotlin",         ["*.kt", "*.kts"], ["build.gradle.kts", "pom.xml"]),
    ("Ruby",           ["*.rb"],     ["Gemfile"]),
    ("PHP",            ["*.php"],    ["composer.json"]),
    ("C/C++",          ["*.c", "*.cpp", "*.h", "*.hpp"], ["CMakeLists.txt", "Makefile"]),
    ("C#",             ["*.cs"],     ["*.csproj", "*.sln"]),
    ("Swift",          ["*.swift"],  ["Package.swift"]),
    ("Shell",          ["*.sh", "*.bash"], []),
    ("Dockerfile",     ["Dockerfile", "Dockerfile.*"], []),
]


class Phase1Technical:

    def __init__(self, project_path: str, project_name: str):
        self.project_path = Path(project_path)
        self.project_name = project_name

    def evaluate(self) -> TechnicalReport:
        report = TechnicalReport()
        if not self.project_path.exists():
            report.fatal_flaw = f"Project path does not exist: {self.project_path}"
            return report

        # ── Gather all files ──
        all_files = list(self.project_path.rglob("*"))
        source_files = [f for f in all_files if f.is_file() and not self._is_excluded(f)]

        report.total_files = len(source_files)
        report.total_lines = sum(len(f.read_text(encoding="utf-8", errors="ignore").splitlines())
                                  for f in source_files)

        # ── Detect language ──
        report.project_language = self._detect_language(source_files)

        # ── Run scans ──
        self._scan_security(source_files, report)
        self._scan_code_smells(source_files, report)
        self._scan_infrastructure(all_files, report)
        self._scan_documentation(all_files, report)
        self._scan_testing(all_files, report)
        self._scan_dependencies(source_files, all_files, report)
        self._assess_depth(source_files, all_files, report)
        self._assess_structure(source_files, report)
        self._rate(report)

        return report

    # ── Helpers ──────────────────────────────────────────────────────

    def _is_excluded(self, path: Path) -> bool:
        excluded_dirs = {".git", "__pycache__", "node_modules", ".venv", "venv",
                         "env", ".tox", ".eggs", "dist", "build", ".next",
                         "target", "vendor", ".bundle", ".gradle", "bin", "obj"}
        return any(part in excluded_dirs for part in path.parts)

    def _detect_language(self, files: List[Path]) -> str:
        exts = {f.suffix for f in files}
        names = {f.name for f in files}
        for lang, extensions, config_files in LANGUAGE_SIGNATURES:
            if any(suffix in exts for suffix in extensions):
                return lang
            if any(cf in names for cf in config_files if cf.startswith("*") or "." in cf):
                return lang
        # Check for config files that indicate language even without source files
        all_names = {f.name for f in files}
        for lang, _, config_files in LANGUAGE_SIGNATURES:
            if config_files and any(cf in all_names for cf in config_files):
                return lang
        return "Unknown"

    def _scan_file(self, pattern: str, content: str, f: Path, findings: List[TechnicalFinding],
                   patterns_list: list):
        for pat, fid, desc, sev in patterns_list:
            for m in re.finditer(pat, content):
                line_num = content[:m.start()].count('\n') + 1
                findings.append(TechnicalFinding(
                    category="security" if sev == "critical" else "code-quality",
                    severity=sev, title=desc,
                    description=f"In {f.name}:{line_num} — {m.group()[:80]}",
                    line_ref=f"{f.name}:{line_num}",
                ))

    # ── Scan dimensions ──────────────────────────────────────────────

    def _scan_security(self, files: List[Path], report: TechnicalReport):
        for f in files:
            try:
                content = f.read_text(encoding="utf-8", errors="ignore")
            except (IOError, UnicodeDecodeError):
                continue
            self._scan_file(None, content, f, report.findings, SECURITY_PATTERNS)
        # Deduplicate by line_ref
        seen = set()
        unique = []
        for f in report.findings:
            key = (f.category, f.severity, f.line_ref or f.title)
            if key not in seen:
                seen.add(key)
                unique.append(f)
        report.findings[:] = unique

    def _scan_code_smells(self, files: List[Path], report: TechnicalReport):
        for f in files:
            try:
                content = f.read_text(encoding="utf-8", errors="ignore")
            except (IOError, UnicodeDecodeError):
                continue
            self._scan_file(None, content, f, report.findings, SMELL_PATTERNS)

    def _scan_infrastructure(self, all_files: List[Path], report: TechnicalReport):
        names = {f.name for f in all_files}
        paths = {str(f.relative_to(self.project_path)) for f in all_files}

        # CI/CD
        ci_indicators = [
            ".github/workflows", ".gitlab-ci.yml", "Jenkinsfile", ".circleci",
            "azure-pipelines.yml", ".drone.yml", ".woodpecker.yml",
        ]
        report.has_ci = any(p in paths or any(p in str(p_) for p_ in paths) for p in ci_indicators)

        # Docker
        report.has_docker = "Dockerfile" in names or "docker-compose.yml" in names or \
                            any(f.name.startswith("Dockerfile.") for f in all_files)

        # Config files
        has_editor_config = ".editorconfig" in names
        has_prettier = ".prettierrc" in names or ".prettierrc.json" in names
        has_eslint = ".eslintrc" in names or ".eslintrc.json" in names
        has_ruff = "ruff.toml" in names or ".ruff.toml" in names
        has_mypy = "mypy.ini" in names or ".mypy.ini" in names
        has_env = ".env.example" in names

        infra_findings = []
        if not report.has_ci:
            infra_findings.append(TechnicalFinding("infra", "major", "No CI/CD pipeline",
                "No CI configuration found. Every change is manually deployed — high risk of regression."))
        if not report.has_docker:
            infra_findings.append(TechnicalFinding("infra", "minor", "No Docker support",
                "No Dockerfile or docker-compose.yml. Not containerized."))
        if not has_editor_config:
            infra_findings.append(TechnicalFinding("infra", "minor", "No .editorconfig",
                "Missing .editorconfig — inconsistent coding styles across contributors."))
        if not has_env:
            infra_findings.append(TechnicalFinding("infra", "minor", "No .env.example",
                "Missing env template — onboarding new developers is harder."))
        report.findings.extend(infra_findings)

    def _scan_documentation(self, all_files: List[Path], report: TechnicalReport):
        names = {f.name for f in all_files}
        report.has_readme = "README.md" in names or "README.rst" in names or "README" in names
        report.has_license = "LICENSE" in names or "LICENSE.txt" in names or "LICENSE.md" in names
        report.has_changelog = "CHANGELOG.md" in names or "HISTORY.md" in names
        report.has_contributing = "CONTRIBUTING.md" in names or "CONTRIBUTING.rst" in names

        docs_findings = []
        if not report.has_readme:
            docs_findings.append(TechnicalFinding("docs", "critical", "No README",
                "Zero discoverability. New users and contributors have no entry point."))
        elif report.has_readme:
            readme_path = self.project_path / "README.md"
            if readme_path.exists():
                content = readme_path.read_text(encoding="utf-8", errors="ignore")
                if len(content) < 200:
                    docs_findings.append(TechnicalFinding("docs", "major", "README is too short",
                        f"README is only {len(content)} chars. A good README should explain what, why, and how."))
                if not re.search(r'##\s+(install|usage|example|getting started)', content, re.I):
                    docs_findings.append(TechnicalFinding("docs", "minor", "README missing setup instructions",
                        "No Install/Usage sections. Users must guess how to set it up."))

        if not report.has_license:
            docs_findings.append(TechnicalFinding("docs", "major", "No license",
                "No LICENSE file. Other developers cannot legally use or contribute to this project."))
        if not report.has_changelog:
            docs_findings.append(TechnicalFinding("docs", "minor", "No CHANGELOG",
                "No changelog — hard to track what changed between versions."))
        if not report.has_contributing:
            docs_findings.append(TechnicalFinding("docs", "info", "No CONTRIBUTING guide",
                "No contribution guidelines — may deter potential contributors."))

        report.findings.extend(docs_findings)

    def _scan_testing(self, all_files: List[Path], report: TechnicalReport):
        names = {f.name for f in all_files}
        paths_str = " ".join(str(p) for p in all_files)

        # Test framework indicators
        test_files = [f for f in all_files if f.is_file() and (
            f.name.startswith("test_") or f.name.endswith("_test.py") or
            f.name.endswith("_test.go") or f.name.endswith("_test.rs") or
            f.name.endswith(".test.js") or f.name.endswith(".test.ts") or
            f.name.endswith(".spec.js") or f.name.endswith(".spec.ts") or
            "test" in f.name.lower()
        )]
        test_framework = None
        if any(f.name == "pytest.ini" for f in all_files) or "pytest" in paths_str:
            test_framework = "pytest"
        elif "jest" in paths_str:
            test_framework = "Jest"
        elif "mocha" in paths_str:
            test_framework = "Mocha"
        elif "vitest" in paths_str:
            test_framework = "Vitest"
        elif any(f.name.endswith("_test.go") for f in all_files):
            test_framework = "Go test"
        elif any(f.name.endswith("_test.rs") for f in all_files):
            test_framework = "cargo test"

        report.has_tests = len(test_files) > 0

        testing_findings = []
        if not report.has_tests:
            testing_findings.append(TechnicalFinding("testing", "critical", "No test files found",
                "Zero tests. Untested code is not production code by any standard."))
        else:
            if test_framework:
                testing_findings.append(TechnicalFinding("testing", "info", f"Uses {test_framework}",
                    f"Test framework detected: {test_framework}  ({len(test_files)} test files)"))
            else:
                testing_findings.append(TechnicalFinding("testing", "info", "Test files found",
                    f"{len(test_files)} test files exist (framework not detected)"))

            # Check if tests actually assert something meaningful
            test_content = ""
            for tf in test_files[:5]:
                try:
                    test_content += tf.read_text(encoding="utf-8", errors="ignore")
                except Exception:
                    pass
            if test_content and "assert" not in test_content and "expect" not in test_content:
                testing_findings.append(TechnicalFinding("testing", "major", "Tests lack assertions",
                    "Test files exist but contain no assert/expect statements — they may not actually validate anything."))

        report.findings.extend(testing_findings)

    def _scan_dependencies(self, source_files: List[Path], all_files: List[Path], report: TechnicalReport):
        names = {f.name for f in all_files}

        dep_indicators = {
            "requirements.txt": "Python",
            "pyproject.toml": "Python",
            "Pipfile": "Python",
            "Cargo.toml": "Rust",
            "go.mod": "Go",
            "package.json": "Node.js",
            "Gemfile": "Ruby",
            "composer.json": "PHP",
            "pom.xml": "Java/Maven",
            "build.gradle": "Java/Gradle",
        }

        found_deps = [name for name in names if name in dep_indicators]

        # Check for outdated patterns
        if "requirements.txt" in names:
            req_path = self.project_path / "requirements.txt"
            if req_path.exists():
                content = req_path.read_text(encoding="utf-8", errors="ignore")
                unpinned = [line for line in content.splitlines()
                           if line.strip() and not line.startswith("#") and "==" not in line and ">=" not in line]
                if unpinned:
                    report.findings.append(TechnicalFinding("dependency", "major",
                        f"{len(unpinned)} unpinned Python deps",
                        "Dependencies without pinned versions — builds are non-reproducible."))

        # Check package.json for scripts
        if "package.json" in names:
            pkg_path = self.project_path / "package.json"
            if pkg_path.exists():
                try:
                    pkg = json.loads(pkg_path.read_text(encoding="utf-8", errors="ignore"))
                    if "scripts" in pkg and not any(s in str(pkg.get("scripts", {})) for s in ["test", "build", "lint"]):
                        report.findings.append(TechnicalFinding("dependency", "minor",
                            "package.json has no standard scripts",
                            "No test/build/lint scripts in package.json."))
                except json.JSONDecodeError:
                    pass

        if not found_deps:
            report.findings.append(TechnicalFinding("dependency", "major",
                "No dependency manifests found",
                "Cannot determine project dependencies or build requirements."))
        else:
            report.findings.append(TechnicalFinding("dependency", "info",
                f"Dep manifests: {', '.join(found_deps)}",
                f"Detected {len(found_deps)} dependency configuration files."))

    def _assess_depth(self, source_files: List[Path], all_files: List[Path], report: TechnicalReport):
        """Evaluate technical depth and architecture complexity."""
        names = {f.name for f in all_files}

        # Look for indicators of real engineering depth
        depth_signals = {
            "Dockerfile": 5,
            "docker-compose.yml": 3,
            "Makefile": 3,
            "migrations": 8,
            "alembic.ini": 5,
            "protobuf": 10,
            ".proto": 10,
            "grpc": 8,
            "graphql": 6,
            "kubernetes": 8,
            "terraform": 6,
            "ci/cd": 3,
        }

        score = 50  # baseline
        for signal, points in depth_signals.items():
            if signal in names:
                score += points
            elif any(signal in str(f).lower() for f in all_files):
                score += points // 2

        # Deduct for red flags
        has_entry_point = any(f.name in ("main.py", "index.js", "main.ts", "main.go", "main.rs", "cmd/", "app.py")
                              for f in source_files)
        if not has_entry_point:
            score -= 10

        report.depth_score = max(0, min(100, score))

    def _assess_structure(self, files: List[Path], report: TechnicalReport):
        """Evaluate project organization and modularization."""
        root_files = [f for f in files if f.parent == self.project_path]

        # Count top-level directories as module indicators
        top_dirs = {f.parent.name for f in files if f.parent != self.project_path and
                    f.parent.parent == self.project_path}
        root_dir_count = len(top_dirs)

        # Check for standard project structure
        has_src = (self.project_path / "src").exists()
        has_lib = (self.project_path / "lib").exists()
        has_tests_dir = (self.project_path / "tests").exists() or (self.project_path / "test").exists()

        structure_findings = []

        if root_dir_count == 0 and report.total_files > 1:
            structure_findings.append(TechnicalFinding("structure", "major", "Flat project structure",
                "All files at root level. No modular organization."))
        elif root_dir_count == 1 and report.total_files > 5:
            structure_findings.append(TechnicalFinding("structure", "minor", "Minimal project structure",
                f"Only {root_dir_count} top-level directories for {report.total_files} files."))

        if not has_src and not has_lib and root_dir_count > 0:
            structure_findings.append(TechnicalFinding("structure", "info", "No src/ or lib/ directory",
                "Consider moving source code under a src/ or lib/ directory for clarity."))

        if len(root_files) > 10:
            structure_findings.append(TechnicalFinding("structure", "minor", "Many root-level files",
                f"{len(root_files)} files at project root — consider organizing into subdirectories."))

        report.findings.extend(structure_findings)

    def _rate(self, report: TechnicalReport):
        """Calculate all scores from findings and signals."""
        sec_crit = sum(1 for f in report.findings if f.severity == "critical" and f.category == "security")
        sec_major = sum(1 for f in report.findings if f.severity == "major" and f.category == "security")
        quality_major = sum(1 for f in report.findings if f.severity == "major" and f.category == "code-quality")
        quality_minor = sum(1 for f in report.findings if f.severity == "minor" and f.category == "code-quality")
        infra_major = sum(1 for f in report.findings if f.severity == "major" and f.category == "infra")
        docs_crit = sum(1 for f in report.findings if f.severity == "critical" and f.category == "docs")
        test_crit = sum(1 for f in report.findings if f.severity == "critical" and f.category == "testing")
        test_major = sum(1 for f in report.findings if f.severity == "major" and f.category == "testing")

        report.security_score = max(0, 100 - sec_crit * 20 - sec_major * 10)
        report.quality_score = max(0, 100 - quality_major * 8 - quality_minor * 3)
        report.infra_score = max(0, 100 - infra_major * 15)
        report.docs_score = max(0, 100 - docs_crit * 30 - (1 if not report.has_license else 0) * 20)
        report.testing_score = max(0, 100 - test_crit * 30 - test_major * 10)

        # Production readiness
        if sec_crit > 0:
            report.production_readiness = "Not Ready (security vulnerabilities)"
        elif test_crit > 0 and sec_major > 0:
            report.production_readiness = "Not Ready (no tests + security issues)"
        elif not report.has_ci and not report.has_docker:
            report.production_readiness = "Conditional — manual deployment only"
        elif report.grade() in ("D", "F"):
            report.production_readiness = "Needs Significant Work"
        elif report.grade() == "C":
            report.production_readiness = "Conditional — Needs X weeks"
        else:
            report.production_readiness = "Ready"

        # Debt estimate
        report.debt_estimate_rounds = (
            sec_crit * 2 + sec_major * 1 +
            quality_major // 2 +
            (3 if not report.has_tests else 0) +
            (2 if not report.has_ci else 0) +
            docs_crit * 2 +
            1  # baseline — nobody's perfect
        )
