from pydantic import BaseSettings
from functools import lru_cache

class APISettings(BaseSettings):
    host: str
    port: str

    class Config:
        env_file = ".env"

class AppSettings(BaseSettings):
    public_paths: list[str] = ["/","/hello"] 

appsettings = AppSettings()

@lru_cache
def init_settings():
    mysettings = APISettings()
    return mysettings
