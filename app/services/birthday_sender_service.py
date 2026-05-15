from datetime import datetime

from sqlalchemy.orm import Session

from app.models.birthday_client import BirthdayClient
from app.models.sent_birthday import SentBirthday

from app.services.whatsapp_service import send_template_message


def execute_birthday_sending(db: Session):

    current_year = datetime.now().year

    clients = db.query(BirthdayClient).all()

    sent = []
    skipped = []

    for client in clients:

        already_sent = db.query(SentBirthday).filter(
            SentBirthday.phone == client.phone,
            SentBirthday.sent_year == current_year
        ).first()

        if already_sent:

            skipped.append(client.phone)

            continue

        response = send_template_message(
            client.phone
        )

        new_sent = SentBirthday(
            phone=client.phone,
            first_name=client.first_name,
            sent_year=current_year
        )

        db.add(new_sent)

        sent.append({
            "phone": client.phone,
            "response": response
        })

    db.commit()

    return {
        "sent": sent,
        "skipped": skipped
    }