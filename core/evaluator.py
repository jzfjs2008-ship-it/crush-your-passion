"""
ProjectEvaluation Engine — the main orchestrator.

Runs all 4 phases in sequence:
Phase 1: Technical Assessment
Phase 2: Commercial Viability
Phase 3: Strategic Options
Phase 4: The Final Blow

Bilingual (en/zh) — auto-detects from user input or env.
"""

from dataclasses import dataclass, field
from typing import List, Optional

from .locale import detect_locale, _t
from .phases.phase1_technical import Phase1Technical, TechnicalReport
from .phases.phase2_commercial import Phase2Commercial, CommercialReport, Competitor
from .phases.phase3_strategic import Phase3Strategic, StrategicReport
from .phases.phase4_final_blow import Phase4FinalBlow, FinalBlowReport


@dataclass
class EvaluationReport:
    project_name: str
    locale: str = "en"
    technical: TechnicalReport = field(default_factory=TechnicalReport)
    commercial: CommercialReport = field(default_factory=CommercialReport)
    strategic: StrategicReport = field(default_factory=StrategicReport)
    final_blow: FinalBlowReport = field(default_factory=FinalBlowReport)

    @property
    def overall_verdict(self) -> str:
        return self.final_blow.verdict_type

    @property
    def overall_confidence(self) -> int:
        return self.final_blow.confidence

    def full_report(self) -> str:
        t = lambda en, zh: _t(en, zh, self.locale)
        lines = []
        lines.append("# " + "=" * 60)
        lines.append(f"# {self.project_name} — {t('CRUSH YOUR PASSION EVALUATION', '打压你的激情 · 项目评估报告')}")
        lines.append("# " + "=" * 60)
        lines.append("")

        lines.append(f"## {t('EXECUTIVE SUMMARY', '执行摘要')}")
        lines.append(f"{t('Verdict', '结论')}: {self.overall_verdict}")
        lines.append(f"{t('Confidence', '置信度')}: {self.overall_confidence}%")
        lines.append(f"{t('Technical Grade', '技术评级')}: {self.technical.grade()}")
        lines.append(f"{t('Commercial Grade', '商业评级')}: {self.commercial.grade()}")
        lines.append("")

        lines.append(f"## {t('TECHNICAL ASSESSMENT', '技术评估')}")
        lines.append(self.technical.summary())
        if self.technical.findings:
            lines.append("")
            lines.append(f"### {t('Key Findings', '主要发现')}")
            for f in self.technical.findings[:10]:
                lines.append(f"- [{f.severity.upper()}] {f.title}: {f.description}")
            if len(self.technical.findings) > 10:
                lines.append(f"- {t('... and', '...以及')} {len(self.technical.findings) - 10} {t('more findings', '条更多发现')}")
        lines.append("")

        lines.append(f"## {t('COMMERCIAL ASSESSMENT', '商业评估')}")
        lines.append(self.commercial.summary())
        if self.commercial.competitors:
            lines.append("")
            lines.append(f"### {t('Competitive Landscape', '竞争格局')}")
            for c in self.commercial.competitors[:5]:
                lines.append(f"- {c.name} ({c.type}): {c.stars_or_funding} — {c.overlap_pct}% {t('overlap', '重叠度')}")
        lines.append("")

        lines.append(f"## {t('STRATEGIC OPTIONS', '战略选项')}")
        lines.append(self.strategic.summary())
        for opt in self.strategic.options:
            lines.append("")
            lines.append(f"### {opt.name} — {opt.real_probability}% {t('probability', '概率')}")
            lines.append(f"- {t('Appeal', '表面吸引力')}: {opt.surface_appeal}")
            lines.append(f"- {t('Problems', '实际问题')}: {opt.actual_problems}")
            lines.append(f"- {t('Harder than original', '比原方案更难')}: {t('YES', '是') if opt.is_harder_than_original else t('No', '否')}")
            lines.append(f"- {t('Viable', '可行')}: {t('YES', '是') if opt.is_viable else t('NO', '否')}")
        if self.strategic.recommendation:
            lines.append("")
            lines.append(f"**{t('Recommendation', '建议')}:** {self.strategic.recommendation}")
        lines.append("")

        lines.append(f"## {t('THE FINAL BLOW', '致命一击')}")
        lines.append(self.final_blow.summary())
        lines.append("")
        lines.append(self.final_blow.fundamental_question)
        lines.append("")

        lines.append("---")
        lines.append(t(
            "*This evaluation is designed to test whether your passion survives\nbrutal honesty. If it didn't — that's the point.*",
            "*这份评估的目的是测试你的热情能否经得起残酷的诚实。\n如果不能——那正是意义所在。*"
        ))

        return "\n".join(lines)

    def short_verdict(self) -> str:
        t = lambda en, zh: _t(en, zh, self.locale)
        return (
            f"=== {self.project_name}: {self.overall_verdict} ({self.overall_confidence}%) ===\n"
            f"{t('Tech', '技术')}: {self.technical.grade()} | {t('Comm', '商业')}: {self.commercial.grade()} | "
            f"{t('Best Strat', '最佳策略')}: {self.strategic.highest_probability}%\n"
            f"{self.final_blow.the_uncomfortable_truth[:200]}..."
        )


class ProjectEvaluator:
    """Main evaluation orchestrator — runs all 4 phases."""

    def __init__(self, project_path: str, project_name: str):
        self.project_path = project_path
        self.project_name = project_name
        self.phase1 = Phase1Technical(project_path, project_name)
        self.phase2 = Phase2Commercial()
        self.phase3 = Phase3Strategic()
        self.phase4 = Phase4FinalBlow()

    def evaluate(
        self,
        project_description: str = "",
        target_market: str = "",
        business_model: str = "",
        team_size: int = 1,
        has_users: bool = False,
        has_revenue: bool = False,
        competitors: Optional[List[Competitor]] = None,
        unique_advantages: Optional[List[str]] = None,
        locale: Optional[str] = None,
    ) -> EvaluationReport:
        if locale is None:
            locale = detect_locale(project_description + target_market + business_model)
        report = EvaluationReport(project_name=self.project_name, locale=locale)

        # Phase 1: Technical
        report.technical = self.phase1.evaluate()

        # Phase 2: Commercial
        report.commercial = self.phase2.evaluate(
            project_name=self.project_name,
            project_description=project_description,
            target_market=target_market,
            business_model=business_model,
            team_size=team_size,
            has_users=has_users,
            has_revenue=has_revenue,
            competitors=competitors,
        )

        # Phase 3: Strategic
        report.strategic = self.phase3.evaluate(
            project_name=self.project_name,
            project_description=project_description,
            target_market=target_market,
            business_model=business_model,
            technical_grade=report.technical.grade(),
            commercial_grade=report.commercial.grade(),
        )

        # Phase 4: The Final Blow
        report.final_blow = self.phase4.evaluate(
            technical_grade=report.technical.grade(),
            commercial_grade=report.commercial.grade(),
            strategic_report_summary=report.strategic.summary(),
            unique_advantages=unique_advantages,
        )

        return report
