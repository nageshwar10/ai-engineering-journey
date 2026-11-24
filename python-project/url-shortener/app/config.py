
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

    mysql_host: str
    mysql_port: int
    mysql_database: str
    mysql_user: str
    mysql_password: str

    database_url: str
    base_url: str
    code_length: int


settings = Settings()
