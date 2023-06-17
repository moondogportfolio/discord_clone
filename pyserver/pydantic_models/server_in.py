from pydantic import BaseModel, Field
from typing import List, Optional
from pydantic_models.universal import ObjectIdFactory

class BaseServerRoom(BaseModel):
    name: str = Field(..., example="Room 1")


class ChannelBase(BaseModel):
    name: str = Field(..., example="Channel 1")
    rooms: List[BaseServerRoom]
    id = ObjectIdFactory()


class ServerIn(BaseModel):
    name: str = Field(..., example="Test Server")
    channels: Optional[List[ChannelBase]]

