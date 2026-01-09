"""
test_parse_salary.py

Purpose:
Manual test cases for salary parsing logic.

This file is NOT a unit test for correctness.
It is a rule-alignment test to verify:
- which salary patterns are already handled
- which rules are recognized but not yet implemented
- which cases are intentionally left unparsed

This aligns with:
- docs/salary_cleaning_rules.md
- Day 4 (B28 / B29) design stage
"""

from src.salary.parse_salary import parse_salary

test_cases = [
    # Rule 1: Missing salary
    None,
    "",

    # Rule 2: Negotiable
    "Negotiable",
    "面议",

    # Rule 4: Single fixed value (not yet implemented)
    "RM 3,000 per month",

    # Rule 5: Range salary (not yet implemented)
    "RM 2,800 – RM 3,200 per month",
    "RM 5k – RM 6k per month",

    # Rule 6: Directional salary (not yet implemented)
    "From RM 4,000",
    "Up to RM 5,000",

    # Rule 7: Unparseable semantic text
    "Market rate",
]

for s in test_cases:
    print("=" * 60)
    print("INPUT    :", repr(s))
    result = parse_salary(s)
    print("OUTPUT   :", result)

    # Expected behavior notes (by rule design, not by current implementation)
    if s in (None, ""):
        print("EXPECTED :", "Rule 1 → salary_type='missing'")
    elif s in ("Negotiable", "面议"):
        print("EXPECTED :", "Rule 2 → salary_type='negotiable'")
    elif s == "RM 3,000 per month":
        print("EXPECTED :", "Rule 4 → fixed salary (min=max=3000, period=monthly)")
    elif s in ("RM 2,800 – RM 3,200 per month", "RM 5k – RM 6k per month"):
        print("EXPECTED :", "Rule 5 → range salary (min, max)")
    elif s in ("From RM 4,000", "Up to RM 5,000"):
        print("EXPECTED :", "Rule 6 → directional bound")
    elif s == "Market rate":
        print("EXPECTED :", "Rule 7 → unparseable")
