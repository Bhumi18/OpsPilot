from datetime import datetime, timezone
from enum import Enum
from sqlalchemy import DateTime, Float, String
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class PaymentStatus(str, Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    FAILED = "failed"


class Payment(Base):
    """SQLAlchemy ORM model representing the payments database table."""
    __tablename__ = "payments"

    payment_id: Mapped[str] = mapped_column(String(50), primary_key=True, index=True)
    customer_id: Mapped[str] = mapped_column(String(100), index=True, nullable=False)
    amount: Mapped[float] = mapped_column(Float, nullable=False)
    currency: Mapped[str] = mapped_column(String(3), nullable=False)
    status: Mapped[str] = mapped_column(String(20), nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False
    )
    processing_time_ms: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
