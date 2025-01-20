import base64
import secrets
from typing import List

from pydantic import AnyHttpUrl
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Project settings
    PROJECT_NAME: str = "AskDB"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"

    # Database settings
    DATABASE_URL: str

    # CORS settings
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = ["*"]

    # Token settings
    TOKEN_TYPE: str = "Bearer"

    # Security settings
    SECRET_KEY: str = secrets.token_urlsafe(32)
    FERNET_KEY: str = base64.urlsafe_b64encode(secrets.token_bytes(32)).decode()
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_TIME_IN_MINUTES: int = 10080  # 7 days (7 * 24 * 60)

    MEDIA_PATH: str = "media"

    # Password settings
    MINIMUM_PASSWORD_LENGTH: int = 8
    PASSWORD_RESET_TOKEN_EXPIRE_MINUTES: int = 60

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
