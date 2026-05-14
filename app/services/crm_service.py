import requests

from app.config import settings


def get_birthday_clients():

    headers = {
        "Authorization": f"Bearer {settings.CRM_API_TOKEN}",
        "Identificador": settings.CRM_IDENTIFICADOR,
        "Content-Type": "application/json"
    }

    payload = {
        "codLoja": settings.CRM_STORE_CODE
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