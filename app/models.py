from datetime import UTC, datetime

from sqlalchemy import Column, DateTime, Integer, String

from app.database import Base


class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    vehicle_id = Column(String(50), nullable=False, index=True)
    customer_name = Column(String(100), nullable=False)
    vehicle_make = Column(String(50), nullable=False)
    vehicle_model = Column(String(50), nullable=False)
    service_type = Column(String(100), nullable=False)
    booking_date = Column(
        DateTime,
        default=lambda: datetime.now(UTC),
        nullable=False
    )
    status = Column(String(30), default="pending", nullable=False)
