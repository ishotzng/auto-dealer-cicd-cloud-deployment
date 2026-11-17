def sample_booking(**overrides):
    booking = {
        "vehicle_id": "TOYOTA-001",
        "customer_name": "John Doe",
        "vehicle_make": "Toyota",
        "vehicle_model": "Camry",
        "service_type": "Engine Oil Change"
    }

    booking.update(overrides)
    return booking


def test_home(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["status"] == "running"


def test_health_check(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_create_booking(client):
    response = client.post(
        "/bookings",
        json=sample_booking()
    )

    assert response.status_code == 201
    assert response.json()["vehicle_id"] == "TOYOTA-001"
    assert response.json()["customer_name"] == "John Doe"
    assert response.json()["status"] == "pending"


def test_get_all_bookings(client):
    client.post("/bookings", json=sample_booking())

    response = client.get("/bookings")

    assert response.status_code == 200
    assert len(response.json()) == 1


def test_get_booking_by_id(client):
    created = client.post(
        "/bookings",
        json=sample_booking()
    )

    booking_id = created.json()["id"]

    response = client.get(f"/bookings/{booking_id}")

    assert response.status_code == 200
    assert response.json()["id"] == booking_id


def test_get_nonexistent_booking(client):
    response = client.get("/bookings/999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Booking not found"


def test_get_vehicle_history(client):
    client.post("/bookings", json=sample_booking())

    client.post(
        "/bookings",
        json=sample_booking(
            vehicle_id="HONDA-001",
            vehicle_make="Honda",
            vehicle_model="Accord"
        )
    )

    response = client.get("/vehicles/TOYOTA-001/history")

    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["vehicle_id"] == "TOYOTA-001"
