from fastapi import APIRouter

from sqlalchemy.orm import Session

from app.database import SessionLocal

from app.services.birthday_sender_service import (
    execute_birthday_sending
)

router = APIRouter()


@router.post("/send-birthdays")
def send_birthdays():

    db: Session = SessionLocal()

    try:

        return execute_birthday_sending(db)

    finally:

        db.close()