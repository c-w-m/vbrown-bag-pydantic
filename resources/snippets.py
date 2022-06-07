"""snippets"""
from typing import Optional, List
from pydantic import BaseModel, BaseSettings


# Person models ##################################

class Address(BaseModel):
    street: str
    country: str = "USA"
    zipcode: Optional[str] = None


class Person(BaseModel):
    first_name: str
    last_name: Optional[str]
    address: Optional[Address]
    favorite_numbers: List[int] = []


# Some people in Python ##########################
some_people = [
    Person(first_name='Michael',
           last_name='Kennedy',
           address={
               street='123 Main St.',
               zipcode='97201'
               },
           favorite_numbers=[]
    ),
    Person(first_name='Chris',
           last_name='Williams',
           address={
               street='47400 SE Wood ln',
               country='USA',
               zipcode='01834'
        },
        favorite_numbers=[1, "7", 11, 97]
    ),
    Person(first_name='Sara',
           last_name='Jackson'
    )
]

###################################################

# Config / Settings ###############################

class DbConfig(BaseSettings):
    name: str = ''
    ip_address: str = ''
    user: str = ''
    password: str = ''


class ServerConfig(BaseSettings):
    api_key: Optional[str] = None
    version: Optional[int] = None
    db_settings: DbConfig = DbConfig(
        _env_file='../environment/db.env',
        _env_file_encoding='utf-8'
    )

settings = ServerConfig(
    _env_file='../environment/server.env',
    _env_file_encoding='utf-8'
)

settings.db_settings = DbConfig(
    _env_file='../environment/db.env',
    _env_file_encoding='utf-8'
)
