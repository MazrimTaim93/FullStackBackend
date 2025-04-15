from pydantic import AnyHttpUrl
from typing import List
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_env: str
    allow_origins: List[str]
    api_gateway_token: str
    secret_key: str
    algorithm: str
    database_user: str
    database_password: str
    database_host: str
    database_port: int = 5432
    database_name: str

    @property
    def database_url(self) -> str:
        return f"postgresql://{self.database_user}:{self.database_password}@{self.database_host}:{self.database_port}/{self.database_name}"

    class Config:
        env_file = ".env"


settings = Settings()