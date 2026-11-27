"""Validated API request models."""

from typing import Literal, Optional

from pydantic import BaseModel, ConfigDict, Field, field_validator

class AskRequest(BaseModel):
    message: str = Field(min_length=1, max_length=500)
    language: Literal["en", "hi"] = "en"

class CalculateRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    calculator: Literal["savings", "fd", "emi", "sip"]
    principal: Optional[float] = None
    monthly_amount: Optional[float] = None
    annual_rate_percent: Optional[float] = None
    annual_assumed_rate_percent: Optional[float] = None
    months: Optional[int] = None

    @field_validator("principal", "monthly_amount", "annual_rate_percent", "annual_assumed_rate_percent", mode="before")
    @classmethod
    def reject_boolean_numbers(cls, value):
        if value is not None and (isinstance(value, bool) or not isinstance(value, (int, float))):
            raise ValueError("A JSON number is required.")
        return value

    @field_validator("months", mode="before")
    @classmethod
    def require_whole_number_months(cls, value):
        if value is not None and (isinstance(value, bool) or not isinstance(value, int)):
            raise ValueError("Months must be a whole number.")
        return value
