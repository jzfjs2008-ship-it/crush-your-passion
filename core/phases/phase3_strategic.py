"""
Phase 3: Strategic Options Analysis

Evaluates every possible path and explains why it won't work.
The most painful phase — every option examined and found wanting.
"""

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class StrategicOption:
    name: str
    surface_appeal: str
    actual_problems: str
    hidden_assumptions: str
    assumption_validity: str
    real_probability: int  # 0-100
    what_it_actually_requires: str
    is_harder_than_original: bool = False
    is_viable: bool = False


@dataclass
class StrategicReport:
    options: List[StrategicOption] = field(default_factory=list)
    all_options_fail: bool = False
    highest_probability: int = 0
    recommendation: Optional[str] = None

    def summary(self) -> str:
        viable = [o for o in self.options if o.is_viable]
        header = (
            f"Strategic Options Analyzed: {len(self.options)}\n"
            f"Viable Paths: {len(viable)}\n"
            f"Highest Probability: {self.highest_probability}%\n"
        )
        if self.all_options_fail:
            header += "Verdict: NO VIABLE STRATEGIC PATH FOUND\n"
        return header


class Phase3Strategic:
    """Brutal strategic options analysis.

    Evaluates every option honestly, including the uncomfortable
    truth that most pivots are harder than the original project.
    """

    # Common strategic options that almost never work
    COMMON_DELUSIONS = [
        {
            "name": "Pivot to Open Core with Enterprise",
            "when_applicable": lambda desc, market, biz: True,
            "surface_appeal": "Give away the basic version, charge enterprises for advanced features.",
            "actual_problems": (
                "Enterprise sales cycles are 9-18 months. You need enterprise relationships, "
                "compliance certifications (SOC2, HIPAA), dedicated sales staff, and a product "
                "that actually solves enterprise-grade problems. If your free version is useful "
                "enough to attract users, it probably solves 90% of the problem — leaving no "
                "reason to pay."
            ),
            "hidden_assumptions": (
                "That enterprises are willing to pay for what you built, that you can reach "
                "enterprise decision-makers, that your product meets enterprise compliance requirements."
            ),
            "assumption_validity": "Low. Enterprise sales requires relationships you almost certainly don't have.",
            "real_probability": 5,
            "requires": "Enterprise sales team, compliance certifications, 18+ months runway",
            "harder": True,
        },
        {
            "name": "Add Consulting / Services Arm",
            "when_applicable": lambda desc, market, biz: True,
            "surface_appeal": "Make money doing custom implementations and support.",
            "actual_problems": (
                "Consulting doesn't scale. You trade time for money. Every consulting engagement "
                "pulls you away from product development. Consulting is a different business — "
                "you need sales, project management, delivery processes, and industry credentials."
            ),
            "hidden_assumptions": (
                "That people will pay for your consulting, that you have the expertise to deliver, "
                "that consulting revenue will fund rather than cannibalize product development."
            ),
            "assumption_validity": "Very low. Consulting requires industry relationships and credentials you likely lack.",
            "real_probability": 3,
            "requires": "Industry credentials, consulting sales pipeline, project management capability",
            "harder": True,
        },
        {
            "name": "Acquisition Exit",
            "when_applicable": lambda desc, market, biz: True,
            "surface_appeal": "Build it, get acquired by a big company.",
            "actual_problems": (
                "Acquisitions require one of: (1) users — millions of active users, "
                "(2) revenue — meaningful recurring revenue, (3) unique technology — patented "
                "or hard-to-replicate IP. Without at least one of these, acquisition probability "
                "is effectively zero. Most startups fail to achieve any of the three."
            ),
            "hidden_assumptions": (
                "That someone wants to acquire you, that your technology is unique enough "
                "to be worth acquiring rather than building in-house."
            ),
            "assumption_validity": "Near zero without users, revenue, or unique IP.",
            "real_probability": 1,
            "requires": "Millions of users OR significant revenue OR patented technology",
            "harder": True,
        },
        {
            "name": "Pivot to a Different Market",
            "when_applicable": lambda desc, market, biz: True,
            "surface_appeal": "The current market isn't working — try a different one.",
            "actual_problems": (
                "Pivoting to a new market means starting from zero: new customer discovery, "
                "new competitors, new messaging, potentially new technology. The probability "
                "that the new market is easier than the current one is low — most markets "
                "are hard for the same reasons (no contacts, no reputation, no distribution)."
            ),
            "hidden_assumptions": (
                "That the new market is easier to enter, that your skills transfer, "
                "that the new market has paying customers."
            ),
            "assumption_validity": "Unknown, but the pivot itself resets all progress.",
            "real_probability": 8,
            "requires": "New customer research, new product-market fit search, starting from zero",
            "harder": True,
        },
        {
            "name": "Keep Building — Just Ship More Features",
            "when_applicable": lambda desc, market, biz: True,
            "surface_appeal": "The product just needs more features to gain traction.",
            "actual_problems": (
                "Feature accretion is the most common death spiral. If you don't have users "
                "now, more features won't fix it. The problem is not feature deficiency — "
                "it's that no one cares about the category you're building in. More features "
                "increase maintenance burden and technical debt without solving the adoption problem."
            ),
            "hidden_assumptions": (
                "That lack of features is the reason for no traction, when the real problem "
                "is almost certainly distribution, positioning, or market need."
            ),
            "assumption_validity": "Almost always false. Feature count and adoption are uncorrelated.",
            "real_probability": 10,
            "requires": "A fundamentally different strategy, not more code",
            "harder": False,
        },
        {
            "name": "Aggressive Marketing / Growth Hacking",
            "when_applicable": lambda desc, market, biz: True,
            "surface_appeal": "The product is good, it just needs distribution.",
            "actual_problems": (
                "Marketing can't fix a product that solves a non-existent problem. If your "
                "product has no differentiation (see Phase 2), aggressive marketing just "
                "accelerates the discovery that your product is a commodity. Paid acquisition "
                "without a proven unit-economy model burns cash on unprofitable users."
            ),
            "hidden_assumptions": (
                "That the product has product-market fit and just needs awareness. "
                "If you don't have organic traction, marketing won't fix it."
            ),
            "assumption_validity": "Low. Products with real PMF grow organically before paid marketing.",
            "real_probability": 15,
            "requires": "Marketing budget, growth expertise, and a product worth distributing",
            "harder": True,
        },
    ]

    def evaluate(
        self,
        project_name: str,
        project_description: str,
        target_market: str,
        business_model: str,
        technical_grade: str,
        commercial_grade: str,
    ) -> StrategicReport:
        report = StrategicReport()

        for option in self.COMMON_DELUSIONS:
            if not option["when_applicable"](project_description, target_market, business_model):
                continue

            is_viable = option["real_probability"] >= 20

            # Apply the "Same Difficulty Trap": if the surface appeal sounds good
            # but the option is harder than the original, flag it
            option_obj = StrategicOption(
                name=option["name"],
                surface_appeal=option["surface_appeal"],
                actual_problems=option["actual_problems"],
                hidden_assumptions=option["hidden_assumptions"],
                assumption_validity=option["assumption_validity"],
                real_probability=option["real_probability"],
                what_it_actually_requires=option["requires"],
                is_harder_than_original=option.get("harder", True),
                is_viable=is_viable,
            )
            report.options.append(option_obj)

        # Add context-specific option: if technical grade is F, the path is obvious
        if technical_grade == "F" or commercial_grade == "F":
            report.options.append(StrategicOption(
                name="Abandon / Walk Away",
                surface_appeal="Stop investing time and money into something that won't work.",
                actual_problems=(
                    "Sunk cost fallacy makes this the hardest option to accept. But "
                    "it's often the most rational. Every hour spent on a project with "
                    "no viable path is an hour stolen from something that could work."
                ),
                hidden_assumptions="That there's a better use of your time. There almost certainly is.",
                assumption_validity="Very high — your time is finite and valuable.",
                real_probability=85,
                what_it_actually_requires="Acceptance, moving on, learning from the failure",
                is_harder_than_original=False,
                is_viable=True,
            ))

        if not report.options:
            report.options.append(StrategicOption(
                name="No Clear Path Forward",
                surface_appeal="…",
                actual_problems="Insufficient data to generate meaningful strategic options.",
                hidden_assumptions="That the project has enough substance to evaluate.",
                assumption_validity="Not applicable — project lacks sufficient definition.",
                real_probability=0,
                what_it_actually_requires="A complete rethink from fundamentals.",
                is_viable=False,
            ))

        # Determine if all options fail
        viable = [o for o in report.options if o.is_viable]
        report.all_options_fail = len(viable) == 0
        report.highest_probability = max(o.real_probability for o in report.options)

        # Generate harsh recommendation
        if report.all_options_fail:
            report.recommendation = (
                "None of the available strategic options have a meaningful probability of success. "
                "The most rational course of action — which you will probably ignore — "
                "is to stop investing in this project and redirect your energy elsewhere."
            )
        else:
            best = max(viable, key=lambda o: o.real_probability)
            report.recommendation = (
                f"The most viable path is '{best.name}' at {best.real_probability}%, "
                f"but even this has significant limitations. Be honest about whether you "
                f"have the resources and conviction to pursue it."
            )

        return report
