from fastapi import APIRouter
from sqlalchemy.orm import Session

from app.database import SessionLocal

from app.models.birthday_client import BirthdayClient

from app.services.crm_service import get_birthday_clients

router = APIRouter()


@router.post("/sync-birthdays")
def sync_birthdays():

    db: Session = SessionLocal()

    try:

        clients = get_birthday_clients()

        inserted = []

        for client in clients:

            full_phone = (
                f"55"
                f"{client['DDD']}"
                f"{client['NumeroCelular']}"
            )

            exists = db.query(BirthdayClient).filter(
                BirthdayClient.phone == full_phone
            ).first()

            if exists:
                continue

            new_client = BirthdayClient(
                phone=full_phone,
                ddd=client["DDD"],
                first_name=client["Nome"],
                last_name=client["Sobrenome"],
                cpf=client.get("CPF"),
                value=client.get("Valor")
            )

            db.add(new_client)

            inserted.append(full_phone)

        db.commit()

        return {
            "message": "Sincronização concluída",
            "total_inserted": len(inserted),
            "phones": inserted
        }

    finally:
        db.close()