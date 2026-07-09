"""
ProjectEvaluation Engine — the main orchestrator.

Runs all 4 phases in sequence:
Phase 1: Technical Assessment
Phase 2: Commercial Viability
Phase 3: Strategic Options
Phase 4: The Final Blow
"""

from dataclasses import dataclass, field
from typing import List, Optional

from .phases.phase1_technical import Phase1Technical, TechnicalReport
from .phases.phase2_commercial import Phase2Commercial, CommercialReport, Competitor
from .phases.phase3_strategic import Phase3Strategic, StrategicReport
from .phases.phase4_final_blow import Phase4FinalBlow, FinalBlowReport


@dataclass
class EvaluationReport:
    project_name: str
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
        lines = []
        lines.append("# " + "=" * 60)
        lines.append(f"# {self.project_name} — CRUSH YOUR PASSION EVALUATION")
        lines.append("# " + "=" * 60)
        lines.append("")

        lines.append("## EXECUTIVE SUMMARY")
        lines.append(f"Verdict: {self.overall_verdict}")
        lines.append(f"Confidence: {self.overall_confidence}%")
        lines.append(f"Technical Grade: {self.technical.grade()}")
        lines.append(f"Commercial Grade: {self.commercial.grade()}")
        lines.append("")

        lines.append("## TECHNICAL ASSESSMENT")
        lines.append(self.technical.summary())
        if self.technical.findings:
            lines.append("")
            lines.append("### Key Findings")
            for f in self.technical.findings[:10]:
                lines.append(f"- [{f.severity.upper()}] {f.title}: {f.description}")
            if len(self.technical.findings) > 10:
                lines.append(f"- ... and {len(self.technical.findings) - 10} more findings")
        lines.append("")

        lines.append("## COMMERCIAL ASSESSMENT")
        lines.append(self.commercial.summary())
        if self.commercial.competitors:
            lines.append("")
            lines.append("### Competitive Landscape")
            for c in self.commercial.competitors[:5]:
                lines.append(f"- {c.name} ({c.type}): {c.stars_or_funding} — {c.overlap_pct}% overlap")
        lines.append("")

        lines.append("## STRATEGIC OPTIONS")
        lines.append(self.strategic.summary())
        for opt in self.strategic.options:
            lines.append("")
            lines.append(f"### {opt.name} — {opt.real_probability}% probability")
            lines.append(f"- Appeal: {opt.surface_appeal}")
            lines.append(f"- Problems: {opt.actual_problems}")
            lines.append(f"- Harder than original: {'YES' if opt.is_harder_than_original else 'No'}")
            lines.append(f"- Viable: {'YES' if opt.is_viable else 'NO'}")
        if self.strategic.recommendation:
            lines.append("")
            lines.append(f"**Recommendation:** {self.strategic.recommendation}")
        lines.append("")

        lines.append("## THE FINAL BLOW")
        lines.append(self.final_blow.summary())
        lines.append("")
        lines.append(self.final_blow.fundamental_question)
        lines.append("")

        lines.append("---")
        lines.append("*This evaluation is designed to test whether your passion survives\n"
                      "brutal honesty. If it didn't — that's the point.*")

        return "\n".join(lines)

    def short_verdict(self) -> str:
        return (
            f"=== {self.project_name}: {self.overall_verdict} ({self.overall_confidence}%) ===\n"
            f"Tech: {self.technical.grade()} | Comm: {self.commercial.grade()} | "
            f"Best Strat: {self.strategic.highest_probability}%\n"
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
    ) -> EvaluationReport:
        report = EvaluationReport(project_name=self.project_name)

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
