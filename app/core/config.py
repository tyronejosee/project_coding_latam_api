"""Configs for Core Module."""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # General Settings
    PROJECT_NAME: str = "Coding Latam API"
    API_V1_STR: str = "/api/v1"
    STATIC_DIR: str = "app/static/images"

    # CORS Settings
    CORS_ORIGINS: list[str] = [
        "http://localhost",
        "http://127.0.0.1",
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://localhost:4200",
        "http://127.0.0.1:4200",
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:8080",
        "http://127.0.0.1:8080",
    ]

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"


settings = Settings()
