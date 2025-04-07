from signal import strsignal
from pydantic import AnyHttpURL
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_env: str
    allow_origins: list[AnyHttpURL]
    api_gateway_token: str

    class Config:
        env_file= ".env"

settings = Settings()