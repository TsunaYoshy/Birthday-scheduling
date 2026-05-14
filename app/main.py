from fastapi import FastAPI

from app.database import Base
from app.database import engine

from app.routes.sync import router as sync_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Birthday API"
)

app.include_router(sync_router)


@app.get("/")
def home():

    return {
        "status": "online"
    }