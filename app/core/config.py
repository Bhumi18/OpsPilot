from typing import Optional
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables or defaults."""
    APP_NAME: str = "OpsPilot"
    ENVIRONMENT: str = "development"
    LOG_LEVEL: str = "INFO"

    # PostgreSQL Database Settings
    POSTGRES_USER: str = "opspilot_user"
    POSTGRES_PASSWORD: str = "opspilot_password"
    POSTGRES_DB: str = "opspilot"
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: int = 5432
    DATABASE_URL: Optional[str] = None

    @property
    def sync_database_url(self) -> str:
        """Construct database connection URL if DATABASE_URL is not explicitly set."""
        if self.DATABASE_URL:
            return self.DATABASE_URL
        return f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )


settings = Settings()
