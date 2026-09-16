import pytest


def test_create_payment_success(client):
    """Test successful payment creation via POST /payments."""
    payload = {
        "customer_id": "cust_101",
        "amount": 150.50,
        "currency": "USD"
    }
    response = client.post("/payments", json=payload)
    assert response.status_code == 201

    data = response.json()
    assert data["payment_id"].startswith("pay_")
    assert data["customer_id"] == "cust_101"
    assert data["amount"] == 150.50
    assert data["currency"] == "USD"
    assert data["status"] == "completed"
    assert "created_at" in data
    assert data["processing_time_ms"] > 0


def test_get_payment_by_id_success(client):
    """Test retrieving a created payment via GET /payments/{payment_id}."""
    create_payload = {
        "customer_id": "cust_102",
        "amount": 49.99,
        "currency": "EUR"
    }
    create_res = client.post("/payments", json=create_payload)
    payment_id = create_res.json()["payment_id"]

    get_res = client.get(f"/payments/{payment_id}")
    assert get_res.status_code == 200
    data = get_res.json()
    assert data["payment_id"] == payment_id
    assert data["customer_id"] == "cust_102"
    assert data["amount"] == 49.99
    assert data["currency"] == "EUR"


def test_list_payments(client):
    """Test listing all stored payments via GET /payments."""
    client.post("/payments", json={"customer_id": "cust_A", "amount": 10.0, "currency": "USD"})
    client.post("/payments", json={"customer_id": "cust_B", "amount": 20.0, "currency": "GBP"})

    response = client.get("/payments")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    customer_ids = [p["customer_id"] for p in data]
    assert "cust_A" in customer_ids
    assert "cust_B" in customer_ids


def test_create_payment_invalid_amount(client):
    """Test payment creation fails with 422 for non-positive amounts."""
    payload = {
        "customer_id": "cust_103",
        "amount": -50.00,
        "currency": "USD"
    }
    response = client.post("/payments", json=payload)
    assert response.status_code == 422


def test_create_payment_invalid_currency(client):
    """Test payment creation fails with 422 for invalid currency codes."""
    payload = {
        "customer_id": "cust_104",
        "amount": 100.00,
        "currency": "INVALID_CODE"
    }
    response = client.post("/payments", json=payload)
    assert response.status_code == 422


def test_get_payment_not_found(client):
    """Test fetching non-existent payment_id returns 404 Not Found."""
    response = client.get("/payments/pay_doesnotexist999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Payment with ID 'pay_doesnotexist999' was not found"}
