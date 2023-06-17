from bson.objectid import ObjectId
from bson.errors import InvalidId
from typing import Optional
from pydantic import BaseModel



def ObjectIdFactory():
    return str(ObjectId())


class ObjectIdStr(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate


    @classmethod
    def validate(cls, v):
        if not isinstance(v, str):
            raise ValueError("Not a valid ObjectId string.")
        if len(v) != 24:
            raise ValueError("Not a valid ObjectId string.")
        return v

class ObjectId_Model(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate


    @classmethod
    def validate(cls, v):
        try:
            ObjectId(str(v))
        except InvalidId:
            raise ValueError("Not a valid ObjectId")
        return str(v)


class PermissionBitflag(int):
    @classmethod
    def __get_validators__(self):
        yield self.validate

    @classmethod
    def validate(self, v):
        if not isinstance(v, int):
            raise TypeError('Int required.')
        if v > 4294967296: #2^32
            raise ValueError('Invalid value.')
        return self(v)

    def __repr__(self):
        return f'PermissionBitflag({super().__repr__()})'


class Permission(BaseModel):
    allow: Optional[PermissionBitflag] = PermissionBitflag(64)
    deny:  Optional[PermissionBitflag] = PermissionBitflag(64)
