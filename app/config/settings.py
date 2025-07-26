from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding='utf-8',
        extra="ignore",
        # Configuración recomendada para Pydantic V2
        from_attributes=True  # Reemplaza a orm_mode
    )

    port: int
    database_url: str = Field(..., alias="DATABASE_URL")
    secret_key: str
    algorithm: str
    expires_in_minutes: int

    smtp_server: str
    smtp_port: int
    smtp_password: str
    smtp_email: str

    ms_gestion_usuarios_url: str
