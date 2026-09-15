from typing import List
from fastapi import APIRouter, Depends, HTTPException, status

from app.schemas.payment import CreatePaymentRequest, PaymentResponse
from app.services.payment_service import PaymentService

router = APIRouter(prefix="/payments", tags=["payments"])


def get_payment_service() -> PaymentService:
    """Dependency provider for PaymentService."""
    return PaymentService()


@router.post("", response_model=PaymentResponse, status_code=status.HTTP_201_CREATED)
def create_payment(
    payload: CreatePaymentRequest,
    service: PaymentService = Depends(get_payment_service)
):
    """Create and process a payment."""
    return service.create_payment(payload)


@router.get("", response_model=List[PaymentResponse])
def list_payments(
    service: PaymentService = Depends(get_payment_service)
):
    """Retrieve all recorded payments."""
    return service.list_payments()


@router.get("/{payment_id}", response_model=PaymentResponse)
def get_payment(
    payment_id: str,
    service: PaymentService = Depends(get_payment_service)
):
    """Retrieve details for a specific payment by payment_id."""
    payment = service.get_payment(payment_id)
    if not payment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Payment with ID '{payment_id}' was not found"
        )
    return payment
