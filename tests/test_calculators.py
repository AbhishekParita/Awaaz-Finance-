import math

import pytest

from app.services.calculators import emi, fixed_deposit, savings, sip

def test_savings_example():
    result = savings(500, 12)
    assert result["total_saved"] == 6000
    assert result["currency"] == "INR"
    assert "Interest and returns are excluded" in result["assumptions"]

def test_fd_quarterly_example():
    result = fixed_deposit(10000, 6, 12)
    assert result["maturity_value"] == pytest.approx(10613.64, abs=0.01)
    assert fixed_deposit(10000, 0, 12)["maturity_value"] == 10000

def test_emi_example_and_zero_rate():
    result = emi(5000, 10, 12)
    assert result["monthly_emi"] == pytest.approx(439.58, abs=0.01)
    assert result["total_payment"] == pytest.approx(5274.95, abs=0.02)
    assert emi(12000, 0, 12)["monthly_emi"] == 1000

def test_sip_example_and_zero_rate():
    result = sip(500, 12, 12)
    assert result["estimated_value"] == pytest.approx(6341.25, abs=0.01)
    assert sip(500, 0, 12)["estimated_value"] == 6000
    assert "not guaranteed" in result["assumptions"][-1]

@pytest.mark.parametrize("function,args", [
    (savings, (0, 12)), (savings, (500, 0)), (emi, (-1, 5, 12)),
    (emi, (1000, -1, 12)), (emi, (1000, 1, 0)),
    (fixed_deposit, (1000, 101, 12)), (sip, (float("nan"), 10, 12)),
    (sip, (500, 10, 601)),
    (emi, (1000, 5, 1.5)),
    (savings, (True, 12)),
    (fixed_deposit, ("10000", 6, 12)),
])
def test_invalid_calculator_inputs(function, args):
    with pytest.raises((ValueError, OverflowError)):
        function(*args)
