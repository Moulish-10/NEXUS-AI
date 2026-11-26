from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    APP_NAME: str = "NEXUS AI"
    APP_ENV: str = "development"
    DEBUG: bool = True

    LLM_PROVIDER: str = "gemini"

    GOOGLE_API_KEY: str
    GEMINI_MODEL: str

    DATABASE_URL: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )


settings = Settings()