"""settings example"""
from typing import Optional

from pydantic import BaseSettings


class DbSettings(BaseSettings):
    name: str
    ip_address: str
    user: Optional[str]
    password: Optional[str]


class ServerSettings(BaseSettings):
    api_key: str
    version: int
    db_settings: Optional[DbSettings]


settings = ServerSettings(
    _env_file='environment/server.env',
    _env_file_encoding='utf-8'
)
print(settings)

db_settings = DbSettings(
    _env_file='environment/db.env',
    _env_file_encoding='utf-8'
)
print(db_settings)
