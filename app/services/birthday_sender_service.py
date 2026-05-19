import time

from datetime import datetime

from sqlalchemy.orm import Session

from app.models.birthday_client import BirthdayClient
from app.models.sent_birthday import SentBirthday

from app.services.whatsapp_service import (
    send_template_message
)


def execute_birthday_sending(db: Session):

    current_year = datetime.now().year

    clients = db.query(BirthdayClient).all()

    sent = 0
    skipped = 0
    failed = 0

    print(
        f"Iniciando envio para "
        f"{len(clients)} clientes..."
    )

    for client in clients:

        try:

            already_sent = db.query(
                SentBirthday
            ).filter(
                SentBirthday.phone == client.phone,
                SentBirthday.sent_year == current_year
            ).first()

            if already_sent:

                skipped += 1

                print(
                    f"[SKIP] "
                    f"{client.phone} "
                    f"já recebeu em {current_year}"
                )

                continue

            print(
                f"[SEND] "
                f"Enviando para "
                f"{client.phone}"
            )

            response = send_template_message(
                client.phone
            )

            new_sent = SentBirthday(
                phone=client.phone,
                first_name=client.first_name,
                sent_year=current_year
            )

            db.add(new_sent)

            db.commit()

            sent += 1

            print(
                f"[OK] "
                f"{client.phone} "
                f"enviado com sucesso"
            )

            time.sleep(2)

        except Exception as error:

            failed += 1

            print(
                f"[ERROR] "
                f"{client.phone} "
                f"erro: {error}"
            )

            continue

    print("Processo finalizado.")

    return {
        "sent": sent,
        "skipped": skipped,
        "failed": failed
    }