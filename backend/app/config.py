from pydantic_settings import BaseSettings
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
PROJECT_ROOT = BASE_DIR.parent

class Settings(BaseSettings):

    APP_NAME: str = "Advanced AI Medical Intelligence Platform"

    VERSION: str = "1.0.0"

    MODEL_PATH: str = str(
        PROJECT_ROOT / "models" / "final_medical_ai_model.keras"
    )


    DATABASE_URL: str = "sqlite:///medical.db"

    GROQ_API_KEY: str = ""

    class Config:
        env_file = ".env"


settings = Settings()