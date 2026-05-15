from fastapi import FastAPI

from app.database import Base
from app.database import engine

from app.models.birthday_client import BirthdayClient
from app.models.sent_birthday import SentBirthday

from app.routes.sync import router as sync_router
from app.routes.birthdays import router as birthdays_router
from app.routes.send import router as send_router


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Birthday API"
)

app.include_router(sync_router)
app.include_router(birthdays_router)
app.include_router(send_router)

@app.get("/")
def home():

    return {
        "status": "online"
    }