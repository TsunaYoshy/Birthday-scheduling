from sqlalchemy.orm import Session

from app.models.birthday_client import (
    BirthdayClient
)

from app.services.crm_service import (
    get_birthday_clients
)

from app.config import settings


def sync_birthdays(db: Session):

    print("Limpando cache...")

    db.query(BirthdayClient).delete()

    db.commit()

    print("Cache limpo.")

    total_inserted = 0

    for store_code in settings.CRM_STORE_CODES:

        print(
            f"Consultando loja {store_code}..."
        )

        try:

            clients = get_birthday_clients(
                store_code
            )

            for client in clients:

                full_phone = (
                    f"55"
                    f"{client['DDD']}"
                    f"{client['NumeroCelular']}"
                )

                new_client = BirthdayClient(
                    phone=full_phone,
                    ddd=client["DDD"],
                    first_name=client["Nome"],
                    last_name=client["Sobrenome"],
                    cpf=client.get("CPF"),
                    value=client.get("Valor")
                )

                db.add(new_client)

                total_inserted += 1

            db.commit()

            print(
                f"Loja {store_code}: "
                f"{len(clients)} clientes"
            )

        except Exception as error:

            print(
                f"[ERROR] "
                f"Loja {store_code}: "
                f"{error}"
            )

            continue

    print(
        f"{total_inserted} clientes sincronizados."
    )

    return total_inserted