# scripts/parse_salary.py

"""
Salary parsing core dispatcher.

This module converts raw salary text into structured components
according to frozen rules defined in:
- docs/salary_cleaning_rules.md

Scope:
- No currency conversion
- No salary normalization across periods
- No inference beyond explicit text
"""

import re
import pandas as pd
from typing import Optional, Dict


def parse_salary(salary_raw: Optional[str]) -> Dict:
    """
    Parse a single salary_raw value into structured fields.

    Parameters
    ----------
    salary_raw : str or NaN
        Original salary text from raw dataset.

    Returns
    -------
    dict with keys:
        - salary_type
        - salary_min
        - salary_max
        - salary_period
        - currency
    """

    # ---------- Rule 1: Missing salary ----------
    if salary_raw is None or pd.isna(salary_raw) or str(salary_raw).strip() == "":
        return _handle_missing()

    text = str(salary_raw).strip()

    # ---------- Rule 2: Negotiable ----------
    if _is_negotiable(text):
        return _handle_negotiable()

    # ---------- Rule 7: Unparseable (semantic only) ----------
    if _is_unparseable(text):
        return _handle_unparseable(text)

    # ---------- Rule 6: Directional salary ----------
    if _is_directional(text):
        return _handle_directional(text)

    # ---------- Rule 5: Salary range ----------
    if _is_range(text):
        return _handle_range(text)

    # ---------- Rule 4: Single value ----------
    if _is_single_value(text):
        return _handle_fixed(text)

    # ---------- Fallback ----------
    return _handle_unparseable(text)


# =========================
# Rule handlers (stubs)
# =========================

def _handle_missing() -> Dict:
    return {
        "salary_type": "missing",
        "salary_min": None,
        "salary_max": None,
        "salary_period": "unknown",
        "currency": None,
    }


def _handle_negotiable() -> Dict:
    return {
        "salary_type": "negotiable",
        "salary_min": None,
        "salary_max": None,
        "salary_period": "unknown",
        "currency": None,
    }


def _handle_unparseable(text: str) -> Dict:
    return {
        "salary_type": "unparseable",
        "salary_min": None,
        "salary_max": None,
        "salary_period": "unknown",
        "currency": None,
    }


def _handle_directional(text: str) -> Dict:
    return {
        "salary_type": "directional",
        "salary_min": None,
        "salary_max": None,
        "salary_period": "unknown",
        "currency": _extract_currency(text),
    }


def _handle_range(text: str) -> Dict:
    return {
        "salary_type": "range",
        "salary_min": None,
        "salary_max": None,
        "salary_period": "unknown",
        "currency": _extract_currency(text),
    }


def _handle_fixed(text: str) -> Dict:
    return {
        "salary_type": "fixed",
        "salary_min": None,
        "salary_max": None,
        "salary_period": "unknown",
        "currency": _extract_currency(text),
    }



# =========================
# Pattern detectors (stubs)
# =========================

def _is_negotiable(text: str) -> bool:
    keywords = ["negotiable", "面议"]
    return any(k.lower() in text.lower() for k in keywords)


def _is_unparseable(text: str) -> bool:
    keywords = [
        "depends on experience",
        "market rate",
        "competitive"
    ]
    return any(k.lower() in text.lower() for k in keywords)


def _is_directional(text: str) -> bool:
    keywords = ["up to", "from", "above"]
    return any(k.lower() in text.lower() for k in keywords)


def _is_range(text: str) -> bool:
    # examples: "RM 2,800 – RM 3,200", "3000 - 4000"
    return bool(re.search(r"\d+.*[-–].*\d+", text))


def _is_single_value(text: str) -> bool:
    # one numeric value, no range separator
    numbers = re.findall(r"\d+", text)
    return len(numbers) == 1


def _extract_currency(text: str) -> Optional[str]:
    text_upper = text.upper()
    if "RM" in text_upper:
        return "RM"
    return None
