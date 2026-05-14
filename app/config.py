from dotenv import load_dotenv
import os

load_dotenv()

class Settings:

    CRM_API_URL = os.getenv("CRM_API_URL")

    CRM_API_TOKEN = os.getenv("CRM_API_TOKEN")
    CRM_IDENTIFICADOR = os.getenv("CRM_IDENTIFICADOR")

    CRM_STORE_CODE = os.getenv("CRM_STORE_CODE")

    DATABASE_URL = os.getenv("DATABASE_URL")

settings = Settings()