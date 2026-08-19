from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "SentinelCore"
    app_version: str = "1.0.0"
    environment: str = "development"

    database_url: str

    jwt_secret: str
    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    redis_url: str = "redis://redis:6379/0"

    log_level: str = "INFO"

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
        extra="ignore",
    )


settings = Settings()
