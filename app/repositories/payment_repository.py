from typing import Dict, List, Optional
from app.models.payment import PaymentModel


class PaymentRepository:
    """In-memory repository for managing payment data storage."""

    def __init__(self) -> None:
        self._storage: Dict[str, PaymentModel] = {}

    def create(self, payment: PaymentModel) -> PaymentModel:
        """Stores a payment record in memory."""
        self._storage[payment.payment_id] = payment
        return payment

    def get_by_id(self, payment_id: str) -> Optional[PaymentModel]:
        """Retrieves a payment record by payment_id, returning None if not found."""
        return self._storage.get(payment_id)

    def get_all(self) -> List[PaymentModel]:
        """Retrieves all payment records from memory."""
        return list(self._storage.values())

    def clear(self) -> None:
        """Clears all stored payments (useful for test resets)."""
        self._storage.clear()


# Singleton repository instance for in-memory persistence during app execution
payment_repository = PaymentRepository()
