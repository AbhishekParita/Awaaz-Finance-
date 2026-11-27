"""Pure deterministic financial illustrations with explicit assumptions."""

import math

MAX_RATE = 100.0
MAX_MONTHS = 600

def _validate_amount(amount: float, name: str) -> float:
    if isinstance(amount, bool) or not isinstance(amount, (int, float)):
        raise ValueError(f"{name} must be a number.")
    value = float(amount)
    if not math.isfinite(value) or value <= 0:
        raise ValueError(f"{name} must be a finite amount greater than zero.")
    if value > 1_000_000_000_000:
        raise ValueError(f"{name} is above the supported limit.")
    return value

def _validate_rate(rate: float) -> float:
    if isinstance(rate, bool) or not isinstance(rate, (int, float)):
        raise ValueError("Annual rate must be a number.")
    value = float(rate)
    if not math.isfinite(value) or value < 0 or value > MAX_RATE:
        raise ValueError("Annual rate must be between 0% and 100%.")
    return value

def _validate_months(months: int) -> int:
    if isinstance(months, bool) or int(months) != months or not 1 <= int(months) <= MAX_MONTHS:
        raise ValueError(f"Tenure must be a whole number of months from 1 to {MAX_MONTHS}.")
    return int(months)

def _money(value: float) -> float:
    return round(value + 1e-10, 2)

def savings(monthly_amount: float, months: int) -> dict:
    """Sum regular contributions; excludes interest and returns."""
    payment = _validate_amount(monthly_amount, "Monthly amount")
    count = _validate_months(months)
    return {"calculator": "savings", "monthly_amount": _money(payment), "months": count,
            "total_saved": _money(payment * count), "total_contribution": _money(payment * count),
            "currency": "INR", "assumptions": ["Contributions are made once per month", "Interest and returns are excluded"]}

def fixed_deposit(principal: float, annual_rate_percent: float, months: int) -> dict:
    """Estimate a fixed deposit with quarterly compounding."""
    amount = _validate_amount(principal, "Principal")
    rate = _validate_rate(annual_rate_percent)
    count = _validate_months(months)
    maturity = amount * (1 + rate / 400) ** (4 * count / 12)
    return {"calculator": "fd", "principal": _money(amount), "annual_rate_percent": rate,
            "months": count, "maturity_value": _money(maturity), "interest_earned": _money(maturity - amount),
            "currency": "INR", "assumptions": ["Quarterly compounding", "Rate treated as constant for the full tenure", "Illustration only; actual bank terms may differ"]}

def emi(principal: float, annual_rate_percent: float, months: int) -> dict:
    """Calculate a reducing-balance monthly instalment."""
    amount = _validate_amount(principal, "Principal")
    rate = _validate_rate(annual_rate_percent)
    count = _validate_months(months)
    monthly_rate = rate / 1200
    payment = amount / count if monthly_rate == 0 else amount * monthly_rate * (1 + monthly_rate) ** count / ((1 + monthly_rate) ** count - 1)
    total = payment * count
    return {"calculator": "emi", "principal": _money(amount), "annual_rate_percent": rate,
            "months": count, "monthly_emi": _money(payment), "total_payment": _money(total),
            "total_interest": _money(total - amount), "currency": "INR",
            "assumptions": ["Reducing-balance EMI", "Annual rate divided into monthly periods", "Fees and rate changes excluded"]}

def sip(monthly_amount: float, annual_assumed_rate_percent: float, months: int) -> dict:
    """Illustrate monthly end-of-period contributions at a nominal annual rate."""
    payment = _validate_amount(monthly_amount, "Monthly amount")
    rate = _validate_rate(annual_assumed_rate_percent)
    count = _validate_months(months)
    monthly_rate = rate / 1200
    future_value = payment * count if monthly_rate == 0 else payment * (((1 + monthly_rate) ** count - 1) / monthly_rate)
    contributions = payment * count
    return {"calculator": "sip", "monthly_amount": _money(payment), "annual_assumed_rate_percent": rate,
            "months": count, "estimated_value": _money(future_value), "total_contribution": _money(contributions),
            "estimated_growth": _money(future_value - contributions), "currency": "INR",
            "assumptions": ["Contributions made at each month's end", "Nominal annual rate divided into monthly periods", "Illustrative estimate only; market returns are not guaranteed"]}

CALCULATORS = {"savings": savings, "fd": fixed_deposit, "emi": emi, "sip": sip}
