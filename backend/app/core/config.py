from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Sentinelcore"
    database_url: str = "sqlite:///./sentinel.db"
    secret_key: str = "replace-me"
    class Config:
        env_file = ".env"

settings = Settings()
