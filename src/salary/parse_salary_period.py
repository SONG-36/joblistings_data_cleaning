# scripts/parse_salary_period.py

"""
Salary period and currency extraction.

This module ONLY extracts explicitly stated information.
No inference, no normalization, no conversion.
"""

import re
from typing import Tuple, Optional


def extract_salary_period(text: str) -> str:
    """
    Extract salary period from raw salary text.

    Returns:
        monthly | yearly | hourly | unknown
    """
    t = text.lower()

    if "per month" in t or "monthly" in t:
        return "monthly"

    if "per year" in t or "yearly" in t or "annual" in t:
        return "yearly"

    if "per hour" in t or "hourly" in t:
        return "hourly"

    return "unknown"


def extract_currency(text: str) -> Optional[str]:
    """
    Extract currency symbol or code from raw salary text.

    Returns:
        RM | MYR | USD | None
    """
    t = text.upper()

    if "RM" in t:
        return "RM"

    if "MYR" in t:
        return "MYR"

    if "USD" in t or "$" in t:
        return "USD"

    return None
