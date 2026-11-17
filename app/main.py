from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from app import models, schemas
from app.database import Base, engine, get_db

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Auto Dealer Service API",
    description="Vehicle service booking and history tracker",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to Auto Dealer Service API",
        "status": "running"
    }


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.post("/bookings", response_model=schemas.BookingResponse, status_code=201)
def create_booking(
    booking: schemas.BookingCreate,
    db: Session = Depends(get_db)
):
    new_booking = models.Booking(**booking.model_dump())

    db.add(new_booking)
    db.commit()
    db.refresh(new_booking)

    return new_booking


@app.get("/bookings", response_model=list[schemas.BookingResponse])
def get_bookings(db: Session = Depends(get_db)):
    return db.query(models.Booking).all()


@app.get("/bookings/{booking_id}", response_model=schemas.BookingResponse)
def get_booking(booking_id: int, db: Session = Depends(get_db)):
    booking = db.query(models.Booking).filter(
        models.Booking.id == booking_id
    ).first()

    if booking is None:
        raise HTTPException(status_code=404, detail="Booking not found")

    return booking


@app.get(
    "/vehicles/{vehicle_id}/history",
    response_model=list[schemas.BookingResponse]
)
def get_vehicle_history(vehicle_id: str, db: Session = Depends(get_db)):
    return db.query(models.Booking).filter(
        models.Booking.vehicle_id == vehicle_id
    ).all()
