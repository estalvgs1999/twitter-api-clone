# Python
from datetime import date
from typing import Optional
from uuid import UUID

# Pydantic
from pydantic import BaseModel
from pydantic.fields import Field
from pydantic.networks import EmailStr


class UserBase(BaseModel):
    user_id: UUID = Field(...)
    email: EmailStr = Field(..., example="johnwick@yourmail.com")


class User(UserBase):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        example="John"
    )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        example="Wick"
    )
    birth_date: Optional[date] = Field(default=None, example="20/11/2021")
    

class UserLoginDto(UserBase):
    password: str = Field(
        ...,
        min_length=8,
        max_length=20,
        example="Y0uR-Pa55wor6$"
    )
