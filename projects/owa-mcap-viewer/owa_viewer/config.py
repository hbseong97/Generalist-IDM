import os
from pathlib import Path

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    """Application settings"""

    # File storage
    EXPORT_PATH: str = os.environ.get("EXPORT_PATH", "./data")
    PUBLIC_HOSTING_MODE: bool = not bool(os.environ.get("EXPORT_PATH"))

    # Cache
    FILE_CACHE_TTL: int = int(os.environ.get("FILE_CACHE_TTL", 600))
    DEFAULT_CACHE_TTL: int = int(os.environ.get("DEFAULT_CACHE_TTL", 3600))
    CACHE_DIR: str = os.environ.get("CACHE_DIR", "./cache")

    # Server
    PORT: int = int(os.environ.get("PORT", 7860))
    HOST: str = os.environ.get("HOST", "0.0.0.0")
    LOG_LEVEL: str = os.environ.get("LOG_LEVEL", "INFO")

    # Featured datasets
    FEATURED_DATASETS: list[str] = [
        "local",
        "anonymous/example_dataset",
        "anonymous/example_dataset2",
        "anonymous/example-djmax",
        "anonymous/example-aimlab",
        "anonymous/example-pubg-battleground",
    ]

    class Config:
        env_file = ".env"


settings = Settings()
Path(settings.CACHE_DIR).mkdir(parents=True, exist_ok=True)
