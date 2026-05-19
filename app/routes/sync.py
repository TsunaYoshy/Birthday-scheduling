from fastapi import APIRouter
from sqlalchemy.orm import Session

from app.database import SessionLocal

from app.services.crm_sync_service import (
    sync_birthdays
)

router = APIRouter()


@router.post("/sync-birthdays")
def sync_birthdays_route():

    db: Session = SessionLocal()

    try:

        inserted = sync_birthdays(db)

        return {
            "message": "Sincronização concluída",
            "inserted": inserted
        }

    finally:

        db.close()