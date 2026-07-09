"""
Phase 2: Commercial Viability Assessment

Evaluates market reality, differentiation, moat, and business model.
This phase is where ambition meets the market's indifference.
"""

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Competitor:
    name: str
    type: str  # direct, indirect, platform, vertical
    stars_or_funding: str
    core_feature: str
    overlap_pct: int


@dataclass
class CommercialReport:
    market_reality_score: int = 0           # 0-100
    differentiation_score: int = 0          # 0-100
    moat_score: int = 0                     # 0-100
    business_model_score: int = 0           # 0-100
    competitors: List[Competitor] = field(default_factory=list)
    fatal_flaw: Optional[str] = None

    def grade(self) -> str:
        avg = (self.market_reality_score + self.differentiation_score +
               self.moat_score + self.business_model_score) / 4
        if avg >= 90: return "A"
        if avg >= 75: return "B"
        if avg >= 60: return "C"
        if avg >= 40: return "D"
        return "F"

    def summary(self) -> str:
        return (
            f"Commercial Grade: {self.grade()}\n"
            f"Market Reality: {self.market_reality_score}/100\n"
            f"Differentiation: {self.differentiation_score}/100\n"
            f"Moat: {self.moat_score}/100\n"
            f"Business Model: {self.business_model_score}/100\n"
            f"Competitors Identified: {len(self.competitors)}"
        )


class Phase2Commercial:
    """Brutal commercial viability evaluation."""

    def evaluate(
        self,
        project_name: str,
        project_description: str,
        target_market: str,
        business_model: str,
        team_size: int,
        has_users: bool,
        has_revenue: bool,
        competitors: Optional[List[Competitor]] = None,
    ) -> CommercialReport:
        report = CommercialReport()

        if competitors:
            report.competitors = competitors

        # Market reality assessment
        # The harshest filter: does a real market exist?
        score_market = 50  # Start at neutral (most projects overestimate their market)
        adjustments = []

        if not target_market or target_market in ("everyone", "all developers", "general"):
            score_market -= 30
            adjustments.append("Vague target market — 'everyone' means no one")
        elif len(target_market) < 15:
            score_market -= 10
            adjustments.append("Market description too generic")

        if not has_users:
            score_market -= 20
            adjustments.append("Zero users — no validation of market need")
            if not has_revenue:
                score_market -= 15
                adjustments.append("Zero revenue AND zero users — project is entirely unvalidated")

        if team_size == 1:
            score_market += 5  # Solo founder is normal
        elif team_size > 10 and not has_revenue:
            score_market -= 20
            adjustments.append("Large team with no revenue — burning cash with no traction")

        # Check for common market delusions
        market_keywords_lower = target_market.lower()
        if "billion" in market_keywords_lower or "trillion" in market_keywords_lower:
            score_market -= 10
            adjustments.append("Citing TAM in billions/trillions — TAM is not a strategy")

        report.market_reality_score = max(0, min(100, score_market))

        # Differentiation assessment
        score_diff = 70
        if not competitors or len(competitors) == 0:
            # "No competitors" usually means "haven't looked"
            score_diff -= 20
            adjustments.append("No competitors listed — likely means market doesn't exist or research wasn't done")
            report.fatal_flaw = "No known competitors. Either the market is imaginary or the creator hasn't done basic research."

        direct_overlaps = [c for c in (competitors or []) if c.type == "direct"]
        if direct_overlaps:
            high_overlap = [c for c in direct_overlaps if c.overlap_pct > 70]
            if high_overlap:
                score_diff -= 30
                adjustments.append(f"High overlap with {len(high_overlap)} direct competitors — what's actually different?")

        # Check for genuine uniqueness claims
        if not any(phrase in project_description.lower() for phrase in
                   ["patent", "proprietary", "exclusive", "unique algorithm",
                    "novel approach", "first to", "only product"]):
            score_diff -= 10
            adjustments.append("No claimed unique advantage — undifferentiated me-too product")

        report.differentiation_score = max(0, min(100, score_diff))

        # Moat assessment (The 3-Day Test)
        score_moat = 30  # Default: weak — most projects have no moat
        moat_signals = {
            "patented": 40,
            "proprietary data": 35,
            "network effect": 25,
            "regulatory": 30,
            "platform lock-in": 20,
            "exclusive partnership": 20,
            "brand": 10,
        }
        desc_lower = project_description.lower()
        found_moat = False
        for signal, points in moat_signals.items():
            if signal in desc_lower:
                score_moat += points
                found_moat = True
                adjustments.append(f"Moat signal detected: {signal} (+{points})")

        if not found_moat:
            adjustments.append("No moat — a competent engineer could replicate this in <3 days")
            if report.fatal_flaw is None:
                report.fatal_flaw = "No defensible moat. Any success will be immediately competed away."

        report.moat_score = max(0, min(100, score_moat))

        # Business model viability
        score_biz = 50
        biz_lower = business_model.lower()
        if not business_model:
            score_biz -= 30
            adjustments.append("No business model defined")
        elif "free" in biz_lower and "premium" not in biz_lower:
            score_biz -= 10
            adjustments.append("Free-only with no monetization path")
        elif "ads" in biz_lower:
            score_biz -= 15
            adjustments.append("Ad-based model — requires massive scale to be viable")
        elif "open source" in biz_lower and "enterprise" not in biz_lower:
            score_biz -= 10
            adjustments.append("Open source with no enterprise tier — community edition solves 90% of the problem, leaving no reason to pay")

        if "saas" in biz_lower or "subscription" in biz_lower:
            score_biz += 10
        if "enterprise" in biz_lower:
            score_biz += 10
        if "consulting" in biz_lower or "services" in biz_lower:
            score_biz -= 5
            adjustments.append("Consulting/services model — not scalable, requires personal involvement")

        report.business_model_score = max(0, min(100, score_biz))

        return report
