from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field, field_validator


class PaymentStatus(str, Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    FAILED = "failed"


class CreatePaymentRequest(BaseModel):
    """Schema for validating payment creation payload."""
    customer_id: str = Field(..., min_length=1, description="Unique identifier for the customer", examples=["cust_12345"])
    amount: float = Field(..., gt=0, description="Payment amount, must be positive (> 0)", examples=[99.99])
    currency: str = Field(..., min_length=3, max_length=3, description="3-letter uppercase ISO currency code", examples=["USD"])

    @field_validator("currency")
    @classmethod
    def validate_currency(cls, v: str) -> str:
        v_upper = v.upper()
        if not v_upper.isalpha() or len(v_upper) != 3:
            raise ValueError("Currency must be a 3-letter alphabetic currency code (e.g., USD, EUR)")
        return v_upper


class PaymentResponse(BaseModel):
    """Schema for returning payment details to API clients."""
    payment_id: str
    customer_id: str
    amount: float
    currency: str
    status: PaymentStatus
    created_at: datetime
    processing_time_ms: float

    model_config = {
        "from_attributes": True
    }
