# Crush Your Passion — Core Evaluation Engine
# A deliberately brutal project evaluation tool.

from .evaluator import ProjectEvaluator, EvaluationReport, evaluate_from_url
from .locale import detect_locale, _t
from .phases import (
    Phase1Technical,
    Phase2Commercial,
    Phase3Strategic,
    Phase4FinalBlow,
)

__all__ = [
    "ProjectEvaluator",
    "EvaluationReport",
    "detect_locale",
    "_t",
    "Phase1Technical",
    "Phase2Commercial",
    "Phase3Strategic",
    "Phase4FinalBlow",
]
