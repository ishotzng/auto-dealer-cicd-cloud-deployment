from datetime import datetime

from pydantic import BaseModel, ConfigDict


class BookingCreate(BaseModel):
    vehicle_id: str
    customer_name: str
    vehicle_make: str
    vehicle_model: str
    service_type: str


class BookingResponse(BaseModel):
    id: int
    vehicle_id: str
    customer_name: str
    vehicle_make: str
    vehicle_model: str
    service_type: str
    booking_date: datetime
    status: str

    model_config = ConfigDict(from_attributes=True)
