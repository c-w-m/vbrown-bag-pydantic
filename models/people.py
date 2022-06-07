""" Pydantic model for data.json.

data.json
{
    "first_name": "Michael",
    "last_name": "Kennedy",
    "address": {
        "street": "123 Main St.",
        "country": "USA",
        "zipcode": "97201"
    },
    "favorite_numbers": []
}
"""
from typing import Optional, List

from pydantic import BaseModel

#class Address:
class Address(BaseModel):
    street: str
    country: str = "USA"
    zipcode: str


#class Person:
class Person(BaseModel):
    first_name: str
    last_name: Optional[str]
    address: Optional[Address]
    favorite_numbers: Optional[List[int]]

    class Config:
        """ Stuff goes here to set behavior of class. """
