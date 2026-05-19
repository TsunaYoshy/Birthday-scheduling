from app.database import SessionLocal

from app.services.crm_sync_service import (
    sync_birthdays
)

from app.services.birthday_sender_service import (
    execute_birthday_sending
)


def run():

    db = SessionLocal()

    try:

        print("Iniciando JOB diário...")

        sync_birthdays(db)

        result = execute_birthday_sending(db)

        print(result)

        print("JOB finalizado.")

    finally:

        db.close()


if __name__ == "__main__":

    run()