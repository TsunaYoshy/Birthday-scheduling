import requests

from app.config import settings


def get_birthday_clients(store_code: str):

    headers = {
        "Authorization": (
            f"Bearer {settings.CRM_API_TOKEN}"
        ),
        "Identificador": (
            settings.CRM_IDENTIFICADOR
        ),
        "Content-Type": "application/json"
    }

    payload = {
        "codLoja": store_code
    }

    response = requests.post(
        settings.CRM_API_URL,
        headers=headers,
        json=payload,
        timeout=30
    )

    response.raise_for_status()

    data = response.json()

    return data.get("aniversario", [])