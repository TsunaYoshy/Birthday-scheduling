import requests

from app.config import settings


def send_template_message(phone: str):

    headers = {
        "Authorization": f"Bearer {settings.WABA_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": phone,
        "type": "template",
        "template": {
            "name": "aniversariante_do_dia",
            "language": {
                "code": "pt_BR"
            }
        }
    }

    response = requests.post(
        settings.WABA_API_URL,
        headers=headers,
        json=payload,
        timeout=30
    )

    response.raise_for_status()

    return response.json()