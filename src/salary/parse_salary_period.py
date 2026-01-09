"""
Salary period and currency extraction.

This module ONLY extracts explicitly stated information.
No inference, no normalization, no conversion.
"""

from typing import Optional, Dict


def extract_salary_period(text: Optional[str]) -> Dict:
    """
    Extract salary period from raw salary text.

    Defensive design:
    - Handles None / NaN / non-string values safely

    Returns:
        {
            salary_period: monthly | yearly | hourly | unknown
            salary_period_source: explicit | missing
            salary_period_confidence: float
        }
    """
    # Handle NaN, None, and non-string values
    if not isinstance(text, str) or not text.strip():
        return {
            "salary_period": "unknown",
            "salary_period_source": "missing",
            "salary_period_confidence": 0.0,
        }

    t = text.lower()

    if "per month" in t or "monthly" in t:
        return {
            "salary_period": "monthly",
            "salary_period_source": "explicit",
            "salary_period_confidence": 1.0,
        }

    if "per year" in t or "yearly" in t or "annual" in t:
        return {
            "salary_period": "yearly",
            "salary_period_source": "explicit",
            "salary_period_confidence": 1.0,
        }

    if "per hour" in t or "hourly" in t:
        return {
            "salary_period": "hourly",
            "salary_period_source": "explicit",
            "salary_period_confidence": 1.0,
        }

    return {
        "salary_period": "unknown",
        "salary_period_source": "missing",
        "salary_period_confidence": 0.0,
    }


def extract_currency(text: Optional[str]) -> Dict:
    """
    Extract currency symbol or code from raw salary text.

    Defensive design:
    - Handles None / NaN / non-string values safely

    Returns:
        {
            currency: RM | MYR | USD | None
            currency_source: explicit | missing
        }
    """
    # Handle NaN, None, and non-string values
    if not isinstance(text, str) or not text.strip():
        return {
            "currency": None,
            "currency_source": "missing",
        }

    t = text.upper()

    if "MYR" in t:
        return {"currency": "MYR", "currency_source": "explicit"}

    if "RM" in t:
        return {"currency": "RM", "currency_source": "explicit"}

    if "USD" in t or "$" in t:
        return {"currency": "USD", "currency_source": "explicit"}

    return {
        "currency": None,
        "currency_source": "missing",
    }
