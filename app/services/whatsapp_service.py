import requests

from app.config import settings


def send_template_message(phone: str):

    headers = {
        "Authorization": f"Bearer {settings.WABA_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "channel_id": settings.CHANNEL_ID,
        "bot_id": settings.BOT_ID,
        "message": {
            "to": phone
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