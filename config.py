import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    TOURNAMENT_API_URL = os.getenv("TOURNAMENT_API_URL", "https://example.com/api/tournaments")
    SCHEDULER_INTERVAL = int(os.getenv("SCHEDULER_INTERVAL", "60"))  # Интервал проверки турниров, сек
    USER_STORAGE_TYPE = os.getenv("USER_STORAGE_TYPE", "json")  # json или sqlite
    ADMINS = os.getenv("ADMINS", "").split(",") if os.getenv("ADMINS") else []

settings = Settings()
