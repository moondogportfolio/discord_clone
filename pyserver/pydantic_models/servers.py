from typing import Optional, List, Dict
from datetime import datetime

from bson.objectid import ObjectId
from pydantic import BaseModel, Field, validator

from pydantic_models.files import GraphicsDescriptionOut, GraphicsDescriptionIn
from pydantic_models.universal import Permission, PermissionBitflag, ObjectIdStr, ObjectId_Model, ObjectIdFactory


class Emoji(BaseModel):
    file : GraphicsDescriptionOut
    role: Optional[List[ObjectIdStr]] = []
    available: bool = True
    name: str


class ServerPartialSidebar(BaseModel):
    id: Optional[ObjectId_Model] = Field(None, alias='_id')
    name: str
    icon: Optional[GraphicsDescriptionOut]
    emoji: Dict[ObjectIdStr, Emoji]

    @validator('id', pre=True)
    def _init_sidebar_server(cls, v):
        if type(v) is ObjectId:
            return str(v)
        return v

    class Config:
        allow_population_by_field_name = True
        

class SidebarIndicator(BaseModel):
    id: Optional[ObjectId_Model] = Field(None, alias='_id')
    name: str
    icon: Optional[ObjectIdStr]

    @validator('id', pre=True)
    def _init_sidebar_server(cls, v):
        if type(v) is ObjectId:
            return str(v)
        return v

    class Config:
        allow_population_by_field_name = True

class RoomChannelPartial(BaseModel):
    # position: int
    name: str

class Channel(BaseModel):
    name: str
    rooms: Dict[ObjectIdStr, RoomChannelPartial] = {}
    permissions: Optional[Permission] = Permission()
    permissions_role: Optional[Dict[str, Permission]] = None
    permissions_member: Optional[Dict[str, Permission]] = None


class Role(BaseModel):
    name: Optional[str] = 'Test Role'
    color: Optional[str] = 'green'
    hoist: Optional[bool] = True
    position: Optional[int] = 0
    permissions: Optional[PermissionBitflag] = PermissionBitflag(64)
    mentionable: Optional[bool] = True



class ServerSettings(BaseModel):
    afk_timeout: Optional[int] = 3600
    verification_level: Optional[int] = 0
    notification_level: Optional[int] = 0
    afk_room_id: Optional[ObjectIdStr]
    max_members: Optional[int] = Field(50, lt=100, gt=0)
    permissions: Optional[PermissionBitflag] = PermissionBitflag(64)


class ServerStatistics(BaseModel):
    member_count: Optional[int] = 1
    presence_count: Optional[int] = 0
    created_at: Optional[datetime] = datetime.now()
    features: Optional[List[str]] = []


class UserServerPartial(BaseModel):
    nick: Optional[str]
    roles: List[ObjectIdStr] = []
    joined_at: datetime = datetime.utcnow()
    connection: str = 'offline'
    activity: Optional[str]
    icon = 'a'

class ServerMemberOps(BaseModel):
    add: List[ObjectIdStr] = Field(None, example=[ObjectIdFactory()])
    remove: List[ObjectIdStr] = Field(None, example=[ObjectIdFactory()])

class ServerMemberIn(BaseModel):
    nick: Optional[str] = Field(None, example="Test User Nick 2")
    roles: Optional[List[ServerMemberOps]]


class TimeExpiry(BaseModel):
    days: int = 0
    seconds: int = 0
    hours: int = 0
    weeks: int = 0

class InviteIn(BaseModel):
    server: ObjectIdStr
    room: ObjectIdStr
    inviter: ObjectIdStr
    max_uses: int = 0
    max_age: Optional[TimeExpiry] = None
    temporary: bool = False

class Invite(InviteIn):
    expires_at: Optional[datetime]
    uses: int = 0
    created_at: datetime = datetime.utcnow()


class BaseServer(BaseModel):
    id: Optional[ObjectId_Model] = Field(None, alias='_id')
    name: str
    description: Optional[str] = None
    splash: Optional[ObjectIdStr] = None
    vanity_url: Optional[str] = None
    owner_id: ObjectIdStr
    default_channel: str
    default_room: str
    default_role: str = None
    #performative
    settings: ServerSettings = ServerSettings()

    class Config:
        allow_population_by_field_name = True


class BaseServerIn(BaseServer):
    icon: Optional[GraphicsDescriptionIn] = {}


class Server(BaseServer):
    #OBJECTS
    id: Optional[ObjectId_Model] = Field(None, alias='_id')
    channels: Dict[ObjectIdStr, Channel] = {}
    emoji: Dict[ObjectIdStr, Emoji] = {}
    icon: Optional[GraphicsDescriptionOut] = {
        'extension': None,
        'category': None,
        'animated': None,
        'data': None
    }
    members: Dict[ObjectIdStr, UserServerPartial] = {}
    roles: Dict[ObjectIdStr, Role] = Field({}, example=Role())
    banned_members: List[ObjectIdStr] = []
    statistics: Optional[ServerStatistics] = ServerStatistics()
    invites: Dict[ObjectIdStr, Invite] = {}

    class Config:
        allow_population_by_field_name = True



class ServerDiscoveryPartial(BaseModel):
    id: Optional[ObjectId_Model] = Field(None, alias='_id')
    name: Optional[str] = None
    description: Optional[str] = None
    icon: Optional[GraphicsDescriptionOut]
    splash: Optional[ObjectIdStr] = None
    
    class Config:
        allow_population_by_field_name = True


class Modifier(BaseModel):
    add_key: Optional[List[Dict]] = None
    remove_key: Optional[List[Dict]] = None
    push_array: Optional[List] = None
    pull_array: Optional[List] = None
    set: Optional[List[Dict]] = None
