"""
Phase 4: The Final Blow — The Uncomfortable Truth

The closing phase. Confronts the developer with the fundamental
question they've been avoiding, then delivers the final verdict.
This is the phase that crushes passion.
"""

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class FinalBlowReport:
    fundamental_question: str = ""
    unique_advantages: List[str] = field(default_factory=list)
    unique_advantage_found: bool = False
    verdict: str = ""
    verdict_type: str = ""  # Viable, Conditionally Viable, Not Viable
    confidence: int = 0     # 0-100
    the_uncomfortable_truth: str = ""
    what_to_actually_do: str = ""

    def summary(self) -> str:
        return (
            f"Verdict: {self.verdict_type}\n"
            f"Confidence: {self.confidence}%\n"
            f"Unique Advantage: {'Yes' if self.unique_advantage_found else 'No'}\n\n"
            f"The Uncomfortable Truth:\n{self.the_uncomfortable_truth}\n\n"
            f"What To Actually Do:\n{self.what_to_actually_do}"
        )


class Phase4FinalBlow:
    """The closing phase that delivers the final demoralizing truth.

    This phase asks the question everyone avoids and provides
    an answer that strips away all remaining optimism.
    """

    # Categories of potential unique advantages
    ADVANTAGE_CATEGORIES = {
        "Industry Experience": "10+ years in a specific domain doing real work, not just consulting",
        "Academic Credentials": "Top-tier publications at respected conferences/journals",
        "Network": "Direct relationships with 5+ potential paying customers who have budget authority",
        "Proprietary Data": "Legal, exclusive access to a dataset competitors cannot obtain",
        "Regulatory Positioning": "Certifications, licenses, or compliance expertise others lack",
        "Timing": "Early entry into a market that is DEFINITELY about to grow (not 'might grow')",
        "Technical Breakthrough": "A genuine algorithmic or engineering advance that would take >6 months to replicate",
        "Brand / Reputation": "Personal recognition in the community that makes people trust your product",
    }

    def evaluate(
        self,
        technical_grade: str,
        commercial_grade: str,
        strategic_report_summary: str,
        unique_advantages: Optional[List[str]] = None,
    ) -> FinalBlowReport:
        report = FinalBlowReport()

        # The fundamental question
        report.fundamental_question = (
            "What do you have that others don't?\n\n"
            "Code is the least scarce resource in the world. "
            "A project's fate is determined by external advantages — "
            "market position, relationships, timing, proprietary data — "
            "not by how clean the code is or how many features it has."
        )

        # Assess unique advantages
        report.unique_advantages = unique_advantages or []
        genuine_advantages = []

        if unique_advantages:
            for adv in unique_advantages:
                for category, description in self.ADVANTAGE_CATEGORIES.items():
                    if category.lower() in adv.lower():
                        genuine_advantages.append(adv)
                        break

        # Determine if any advantage is genuinely valuable
        key_advantages = [
            a for a in genuine_advantages
            if any(kw in a.lower() for kw in [
                "10+ years", "20+ years", "decade",
                "patent", "phd", "professor",
                "exclusive", "proprietary access",
                "regulatory", "fda", "certified",
                "published", "citation",
            ])
        ]

        report.unique_advantage_found = len(key_advantages) > 0
        report.unique_advantages = genuine_advantages

        # Determine verdict type and confidence
        if report.unique_advantage_found and technical_grade in ("A", "B"):
            report.verdict_type = "Viable"
            report.confidence = min(80, 50 + len(key_advantages) * 10)
            # Still punch them in the gut
            report.the_uncomfortable_truth = (
                f"You have {len(key_advantages)} genuine advantages, which puts you ahead of 95% of projects. "
                f"But advantages erode. Your competitors are working on closing the gap right now. "
                f"The question isn't whether you can succeed — it's whether you can sustain the "
                f"effort long enough to convert those advantages into market position before they expire."
            )
        elif technical_grade in ("A", "B") and commercial_grade in ("A", "B"):
            report.verdict_type = "Conditionally Viable"
            report.confidence = 45
            report.the_uncomfortable_truth = (
                "Your project is technically competent and in a real market. But 'competent' and "
                "'in a real market' are table stakes, not winning strategies. Without a unique "
                "personal advantage (industry experience, relationships, proprietary data), you're "
                "entering a race where everyone else has the same tools and you have no head start. "
                "You can build this product. The question is whether you can build it faster, "
                "cheaper, or better than the dozen other teams also building it — and you probably can't."
            )
        elif commercial_grade == "F":
            report.verdict_type = "Not Viable"
            report.confidence = 85
            report.the_uncomfortable_truth = (
                "This project is not commercially viable. The market doesn't exist, or the "
                "competition is insurmountable, or the business model is fantasy. You asked for "
                "an honest evaluation, and the honest answer is: this project should not be "
                "pursued commercially. No amount of refactoring, feature additions, or pivots "
                "will fix the fundamental market problem. The only thing additional effort "
                "achieves is deeper sunk cost."
            )
        else:
            report.verdict_type = "Not Viable"
            report.confidence = 70
            report.the_uncomfortable_truth = (
                "This project has no sustainable path to success. The combination of mediocre "
                "technical execution and weak commercial positioning creates a situation where "
                "even heroic effort has negligible probability of changing the outcome. You are "
                "fighting gravity. Gravity always wins."
            )

        # "What to actually do" — the final nail
        if report.verdict_type == "Not Viable":
            report.what_to_actually_do = (
                "1. Accept that this project, as designed, cannot succeed.\n"
                "2. Extract what you learned and apply it to a different problem.\n"
                "3. Consider whether the real skill you built was coding, or learning "
                "to evaluate projects honestly. If the latter, that skill is valuable — "
                "use it on your next idea.\n"
                "4. Do not keep iterating 'just a little more.' That path leads to years "
                "of wasted effort. You have been warned.\n"
                "5. The most successful developers don't persist on failing projects. "
                "They recognize failure early, learn, and move on. Be that developer."
            )
        elif report.verdict_type == "Conditionally Viable":
            report.what_to_actually_do = (
                "1. Identify the ONE risk that would kill the project and validate it first.\n"
                "2. Stop building features. Start finding paying customers.\n"
                "3. Set a 90-day deadline. If no meaningful traction by then, walk away.\n"
                "4. Do not quit your day job.\n"
                "5. The conditional viability means you have a narrow window. Use it wisely."
            )
        else:
            report.what_to_actually_do = (
                "1. Execute. Stop second-guessing and build.\n"
                "2. Your advantages are real but perishable — move with urgency.\n"
                "3. Set clear milestones with kill criteria.\n"
                "4. Remember that even viable projects fail 80% of the time.\n"
                "5. Your passion will not save you. Execution will."
            )

        return report
