import logging
import time
import uuid
from typing import List, Optional

from app.models.payment import Payment, PaymentStatus
from app.repositories.payment_repository import PaymentRepository
from app.schemas.payment import CreatePaymentRequest, PaymentResponse

logger = logging.getLogger(__name__)


class PaymentService:
    """Service layer executing business logic for payment processing."""

    def __init__(self, repo: PaymentRepository) -> None:
        self.repo = repo

    def create_payment(self, request: CreatePaymentRequest) -> PaymentResponse:
        """Processes and creates a payment, determining status and computing latency."""
        start_time = time.perf_counter()

        payment_id = f"pay_{uuid.uuid4().hex[:12]}"

        # Simulate realistic payment gateway processing delay (approx. 10ms)
        time.sleep(0.01)

        # Deterministic simulation rule: amount of 999.99 triggers a failed status
        if request.amount == 999.99:
            status = PaymentStatus.FAILED
        else:
            status = PaymentStatus.COMPLETED

        end_time = time.perf_counter()
        processing_time_ms = round((end_time - start_time) * 1000, 2)

        payment = Payment(
            payment_id=payment_id,
            customer_id=request.customer_id,
            amount=request.amount,
            currency=request.currency,
            status=status.value,
            processing_time_ms=processing_time_ms
        )

        saved_payment = self.repo.create(payment)
        logger.info(
            f"Payment created: id={saved_payment.payment_id}, status={saved_payment.status}, "
            f"amount={saved_payment.amount} {saved_payment.currency}, latency={saved_payment.processing_time_ms}ms"
        )

        return PaymentResponse.model_validate(saved_payment)

    def get_payment(self, payment_id: str) -> Optional[PaymentResponse]:
        """Retrieves a single payment by ID."""
        payment = self.repo.get_by_id(payment_id)
        if not payment:
            logger.warning(f"Payment not found: payment_id={payment_id}")
            return None

        logger.info(f"Payment retrieved: id={payment_id}")
        return PaymentResponse.model_validate(payment)

    def list_payments(self) -> List[PaymentResponse]:
        """Lists all existing payments."""
        payments = self.repo.get_all()
        logger.info(f"Listing payments: count={len(payments)}")
        return [PaymentResponse.model_validate(p) for p in payments]
