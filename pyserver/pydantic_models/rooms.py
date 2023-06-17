from pydantic import BaseModel, Field, validator
from typing import Any, Optional, List, Dict, Union
from datetime import datetime
from enum import IntEnum, auto, Enum
from pydantic_models.universal import ObjectIdStr, ObjectId_Model, Permission
# from universal import ObjectIdStr


class RoomTypesEnum(IntEnum):
    SERVER_ROOM = auto()
    DM_ROOM = auto()
    GROUP_DM_ROOM = auto()
    THREAD_ROOM = auto()
    


class PostIn(BaseModel):
    author: Optional[ObjectIdStr] = None
    content: str
    message_reference: Optional[ObjectIdStr] = None
    pinned: Optional[bool] = False


class PostEdit(PostIn):
    edited_timestamp: datetime = datetime.utcnow()


class Post(PostIn):
    #timestamp
    timestamp: Optional[datetime] = Field(datetime.utcnow(), example=datetime.utcnow())
    nonce: Optional[str]
    type: Optional[int]
    reactions: Dict[ObjectIdStr, List[ObjectIdStr]] = {} #emoji_id: user_id
    thread: Optional[ObjectIdStr]


class RoomIn(BaseModel):
    name: str = 'Test Room 2'
    posts: Optional[Dict[ObjectIdStr, Post]] = {}


class BaseRoom(RoomIn):
    '''
    id, type, posts, <name>
    '''
    id: Optional[ObjectId_Model]

    class Config:
        fields = {'id': '_id'}
        allow_population_by_field_name = True


class ServerRoomSettings(BaseModel):
    cooldown: Optional[int] = 60


class RoomStatistics(BaseModel):
    last_message_id: ObjectIdStr = None


class ServerRoomStatistics(RoomStatistics):
    last_pin_timestamp: Optional[datetime] = None




class ServerRoom(BaseRoom):
    channel: ObjectIdStr #parent_id
    type = RoomTypesEnum.SERVER_ROOM
    permissions: Optional[Permission] = Permission(allow= 69, deny= 69)
    permissions_role: Optional[Dict[str, Permission]] = Field(None, example={'60eb61dd10c8b129dccb07fe': Permission()})
    permissions_member: Optional[Dict[str, Permission]] = Field(None, example={'60eb61dd10c8b129dccb07fe': Permission()})
    settings: ServerRoomSettings = ServerRoomSettings()
    server: ObjectIdStr
    position: int = 0
    statistics: ServerRoomStatistics = ServerRoomStatistics()



class ThreadSettingsIn(BaseModel):
    auto_archive_duration: int = 60

class ThreadSettings(ThreadSettingsIn):
    archived: bool = False
    archive_timestamp: datetime = datetime.utcnow()
    locked: bool = False


class ThreadMember(BaseModel):
    join_timestamp: datetime = datetime.utcnow()

class ThreadRoomIn(BaseModel):
    server: ObjectIdStr
    room: ObjectIdStr #parent_id
    init_post: ObjectIdStr
    settings: Optional[ThreadSettingsIn] = ThreadSettingsIn()


class ThreadRoom(ThreadRoomIn, BaseRoom):
    members: Dict[ObjectIdStr, ThreadMember]
    type = RoomTypesEnum.THREAD_ROOM
    settings: ThreadSettings = ThreadSettings()
    owner_id: ObjectIdStr



class ThreadData(BaseModel):
    selected_threaddata: ThreadRoom


class DmRoomIn(BaseModel):
    participants: Optional[List[ObjectIdStr]]
    name: str

    @validator('participants')
    def _validate_dm_participants(cls, v):
        if len(v) < 2:
            raise ValueError('Invalid amount of participants.')
        return v


class UserPartialDmRoom(BaseModel):
    nick: Optional[str]
    joined_at: datetime = datetime.utcnow()
    connection: str = 'offline'
    activity: Optional[str]
    id: Optional[ObjectIdStr] = Field(..., alias="_id")

    class Config:
        allow_population_by_field_name = True


class DmRoom(BaseRoom):
    type = RoomTypesEnum.DM_ROOM
    participants: Optional[List[UserPartialDmRoom]]
    owner_id: ObjectIdStr
    name: str


class RoomData(BaseModel):
    selected_roomdata: Union[ServerRoom, DmRoom]
    room_permissions: Optional[int]
