from fastapi import APIRouter

from app.database import SessionLocal

from app.models.birthday_client import BirthdayClient

router = APIRouter()


@router.get("/birthdays")
def get_birthdays():
    
    print("Buscando aniversariantes...")
    db = SessionLocal()

    try:

        clients = db.query(BirthdayClient).all()

        response = []

        for client in clients:

            response.append({
                "id": client.id,
                "name": client.first_name,
                "last_name": client.last_name,
                "phone": client.phone
            })
    
        return response

    finally:
        db.close()
        print("Aniversariantes encontrados.")