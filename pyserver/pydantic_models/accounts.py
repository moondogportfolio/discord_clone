from pydantic import BaseModel, validator
from typing import Optional

class RegistrationForm(BaseModel):
    username: str
    password: str
    email: str
    password_hash: Optional[str]

    @validator('username')
    def _verify_username(cls, v):
        if len(v) < 1 and len(v) > 15:
            raise ValueError('Username must be between 1 to 15 characters in length, inclusive.')
        return v

    class Config:
        schema_extra = {
            "example": {
                "username": "jaja",
                "password": "jaja",
                "email": "jaja@jaja.com"
            }
        }


class Account(BaseModel):
    username: str
    password: str
