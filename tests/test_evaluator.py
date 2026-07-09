"""
Tests for Crush Your Passion evaluation engine.
"""

import sys
import tempfile
import os
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from core.evaluator import ProjectEvaluator
from core.phases.phase2_commercial import Competitor


def test_phase1_technical_with_valid_project():
    """Test technical evaluation on a real Python project (self-test)."""
    evaluator = ProjectEvaluator(
        project_path=str(Path(__file__).parent.parent),
        project_name="crush-your-passion"
    )
    report = evaluator.evaluate()
    assert report.technical is not None
    assert report.technical.code_quality_score >= 0
    assert report.technical.technical_depth_score >= 0
    assert report.technical.grade() in ("A", "B", "C", "D", "F")
    print(f"Technical grade: {report.technical.grade()}")
    print(report.technical.summary())


def test_phase1_technical_empty_project():
    """Test technical evaluation on a non-existent project."""
    evaluator = ProjectEvaluator("/nonexistent/path", "ghost-project")
    report = evaluator.evaluate()
    assert report.technical.fatal_flaw is not None
    assert "does not exist" in report.technical.fatal_flaw


def test_phase1_technical_new_project():
    """Test with a project that has minimal files."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create a minimal project with intentional flaws
        (Path(tmpdir) / "main.py").write_text(
            "import os\n\ndef run(cmd):\n    os.system(cmd)\n\ntry:\n    pass\nexcept:\n    pass\n"
        )
        (Path(tmpdir) / "config.py").write_text('password = "supersecret123"\nAPI_KEY = "sk_test_abcdefghijklmnopqrstuvwxyz123456"\n')

        evaluator = ProjectEvaluator(tmpdir, "bad-project")
        report = evaluator.evaluate()

        # Should find at least a critical security issue (hardcoded key + password)
        critical_count = sum(1 for f in report.technical.findings if f.severity == "critical")
        assert critical_count >= 1, f"Expected critical findings, got: {[f.title for f in report.technical.findings]}"
        assert report.technical.code_quality_score < 80  # Should be penalized
        print(f"Findings: {len(report.technical.findings)}")
        print(f"Critical: {critical_count}")
        print(report.technical.summary())


def test_phase2_commercial_no_competitors():
    """Test commercial assessment with no competitors listed."""
    evaluator = ProjectEvaluator("/tmp", "test-project")
    report = evaluator.evaluate(
        project_description="A cool new app",
        target_market="everyone",
        business_model="free",
        team_size=1,
        has_users=False,
        has_revenue=False,
    )
    assert report.commercial.market_reality_score <= 30
    assert report.commercial.differentiation_score <= 50
    assert report.commercial.moat_score <= 30
    print(report.commercial.summary())


def test_phase2_commercial_strong_position():
    """Test commercial assessment with strong market position."""
    evaluator = ProjectEvaluator("/tmp", "strong-project")
    report = evaluator.evaluate(
        project_description="Patented algorithm for enterprise data processing with proprietary data access",
        target_market="Enterprise SaaS for data engineering teams at Fortune 500 companies",
        business_model="Enterprise SaaS with subscription pricing",
        team_size=5,
        has_users=True,
        has_revenue=True,
        competitors=[
            Competitor("LegacyCorp", "indirect", "$50M funding", "Old approach", 30),
        ],
    )
    assert report.commercial.market_reality_score > 30
    assert report.commercial.moat_score > 50  # Patent mention should boost
    print(report.commercial.summary())


def test_phase3_strategic_abandon_most_viable():
    """Test strategic options — abandon/walk away should be most viable for failing projects."""
    evaluator = ProjectEvaluator("/tmp", "failing-project")
    report = evaluator.evaluate(
        project_description="Another todo app",
        target_market="everyone",
        business_model="free",
    )
    # Abandon/walk away should be the highest-probability option
    assert report.strategic.highest_probability >= 80
    print(report.strategic.summary())
    for opt in report.strategic.options:
        print(f"  - {opt.name}: {opt.real_probability}% (viable: {opt.is_viable})")


def test_phase4_final_blow_not_viable():
    """Test the final blow delivers the crushing verdict."""
    evaluator = ProjectEvaluator("/tmp", "dead-project")
    report = evaluator.evaluate(
        project_description="Yet another social media app for pets",
        target_market="everyone",
        business_model="free with ads",
    )
    assert report.final_blow.verdict_type == "Not Viable"
    assert report.final_blow.confidence >= 70
    print(report.final_blow.summary())


def test_full_report_output():
    """Test the full report generation."""
    evaluator = ProjectEvaluator("/tmp", "demo-project")
    report = evaluator.evaluate(
        project_description="An AI-powered todo list",
        target_market="productivity enthusiasts",
        business_model="freemium SaaS",
        team_size=1,
        has_users=False,
        has_revenue=False,
    )
    full = report.full_report()
    assert "EXECUTIVE SUMMARY" in full
    assert "TECHNICAL ASSESSMENT" in full
    assert "COMMERCIAL ASSESSMENT" in full
    assert "STRATEGIC OPTIONS" in full
    assert "THE FINAL BLOW" in full
    print(full[:500])


def test_short_verdict():
    """Test the short verdict format."""
    evaluator = ProjectEvaluator("/tmp", "test-project")
    report = evaluator.evaluate()
    verdict = report.short_verdict()
    assert "test-project:" in verdict
    assert len(verdict) < 500


if __name__ == "__main__":
    print("=" * 60)
    print("RUNNING CRUSH YOUR PASSION TEST SUITE")
    print("=" * 60)
    
    tests = [
        ("Valid project          ", test_phase1_technical_with_valid_project),
        ("Non-existent project   ", test_phase1_technical_empty_project),
        ("New project with flaws ", test_phase1_technical_new_project),
        ("No competitors         ", test_phase2_commercial_no_competitors),
        ("Strong position        ", test_phase2_commercial_strong_position),
        ("Abandon most viable    ", test_phase3_strategic_abandon_most_viable),
        ("Final blow             ", test_phase4_final_blow_not_viable),
        ("Full report            ", test_full_report_output),
        ("Short verdict          ", test_short_verdict),
    ]
    
    passed = 0
    failed = 0
    for name, fn in tests:
        try:
            fn()
            print(f"  \u2713 {name}")
            passed += 1
        except Exception as e:
            print(f"  \u2717 {name}: {e}")
            failed += 1
    
    print(f"\n{passed}/{passed + failed} passed")
    if failed:
        print(f"FAILURES: {failed}")
    else:
        print("ALL TESTS PASSED")
