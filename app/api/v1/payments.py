from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from app.core.database import get_db
from app.repositories.payment_repository import PaymentRepository
from app.schemas.payment import CreatePaymentRequest, PaymentResponse
from app.services.payment_service import PaymentService

router = APIRouter(prefix="/payments", tags=["payments"])


def get_payment_repository(db: Session = Depends(get_db)) -> PaymentRepository:
    """Dependency provider for PaymentRepository using the request-scoped database session."""
    return PaymentRepository(db)


def get_payment_service(
    repo: PaymentRepository = Depends(get_payment_repository)
) -> PaymentService:
    """Dependency provider for PaymentService."""
    return PaymentService(repo)


@router.post("", response_model=PaymentResponse, status_code=status.HTTP_201_CREATED)
def create_payment(
    payload: CreatePaymentRequest,
    service: PaymentService = Depends(get_payment_service)
):
    """Create and process a payment."""
    try:
        return service.create_payment(payload)
    except SQLAlchemyError:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="A database error occurred while creating the payment."
        )


@router.get("", response_model=List[PaymentResponse])
def list_payments(
    service: PaymentService = Depends(get_payment_service)
):
    """Retrieve all recorded payments."""
    try:
        return service.list_payments()
    except SQLAlchemyError:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="A database error occurred while fetching payments."
        )


@router.get("/{payment_id}", response_model=PaymentResponse)
def get_payment(
    payment_id: str,
    service: PaymentService = Depends(get_payment_service)
):
    """Retrieve details for a specific payment by payment_id."""
    try:
        payment = service.get_payment(payment_id)
        if not payment:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Payment with ID '{payment_id}' was not found"
            )
        return payment
    except SQLAlchemyError:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="A database error occurred while fetching the payment."
        )
