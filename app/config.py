from dotenv import load_dotenv
import os

load_dotenv()

class Settings:

    CRM_API_URL = os.getenv("CRM_API_URL")

    CRM_API_TOKEN = os.getenv("CRM_API_TOKEN")
    CRM_IDENTIFICADOR = os.getenv("CRM_IDENTIFICADOR")

    CRM_STORE_CODES = os.getenv("CRM_STORE_CODES", "").split(",")

    DATABASE_URL = os.getenv("DATABASE_URL")

    WABA_API_URL = os.getenv("WABA_API_URL")

    WABA_TOKEN = os.getenv("WABA_TOKEN")

    DEBUG = os.getenv("DEBUG", "false").lower() == "true"

settings = Settings()