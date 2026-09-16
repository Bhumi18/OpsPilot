import logging
from typing import List, Optional
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from app.models.payment import Payment

logger = logging.getLogger(__name__)


class PaymentRepository:
    """PostgreSQL-backed repository for managing payment data via SQLAlchemy 2.x."""

    def __init__(self, db: Session) -> None:
        self.db = db

    def create(self, payment: Payment) -> Payment:
        """Persists a new Payment ORM instance into PostgreSQL."""
        try:
            self.db.add(payment)
            self.db.commit()
            self.db.refresh(payment)
            return payment
        except SQLAlchemyError as e:
            self.db.rollback()
            logger.error(f"Database error while creating payment '{payment.payment_id}': {e}")
            raise

    def get_by_id(self, payment_id: str) -> Optional[Payment]:
        """Retrieves a single Payment record by payment_id."""
        try:
            return self.db.get(Payment, payment_id)
        except SQLAlchemyError as e:
            logger.error(f"Database error while fetching payment '{payment_id}': {e}")
            raise

    def get_all(self) -> List[Payment]:
        """Retrieves all stored Payment records ordered by creation timestamp."""
        try:
            statement = select(Payment).order_by(Payment.created_at.desc())
            return list(self.db.scalars(statement).all())
        except SQLAlchemyError as e:
            logger.error(f"Database error while retrieving all payments: {e}")
            raise
