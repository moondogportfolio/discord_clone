from devtools import debug
from bson.objectid import ObjectId
from bson.errors import InvalidId
from fastapi.param_functions import File
from pydantic import BaseModel, validator, root_validator, Field
from typing import Any, Optional, List, Dict, Union
from datetime import datetime
from applications import AppCommand


import re

from constants import IMAGE_FORMATS
from models_enum import MessageTypes, RoomTypes



'''
-----------------------------------------------------------
BASE CLASSES TRANSFEROK
-----------------------------------------------------------
'''



class GraphicsDescriptionOut(BaseModel):
    extension: str
    category: str
    animated: Optional[bool] = False


class GraphicsDescriptionIn(GraphicsDescriptionOut):
    data: bytes

    @validator('extension')
    def _validate_gfx_extension(cls, v):
        if v not in ['JPG', 'PNG', 'JPEG', 'WEBP', 'GIF']:
            raise ValueError('Invalid graphics extension.')
        return v

    @validator('category')
    def _validate_gfx_category(cls, v):
        if v not in ['emoji', 'server_icon', 'icon']:
            raise ValueError('Invalid graphics category.')
        return v


'''
-----------------------------------------------------------
BASE CLASSES transferok
-----------------------------------------------------------
'''

def ObjectIdFactory():
    return str(ObjectId())




'''
-----------------------
Permissions definition. TRANSFEROK
-----------------------
'''

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


'''
-----------------------
ObjectId definition. TRANSFEROK
-----------------------
'''

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



'''
-----------------------------------------------------------
RESPONSE MODELS
-----------------------------------------------------------
'''





class ValidationErrorMessage(BaseModel):
    errors: List

class Message(BaseModel):
    message: str



'''
-----------------------------------------------------------
FILE MODELS transferok
-----------------------------------------------------------
'''



valid_filename = re.compile(r"([a-zA-Z0-9]*)\.([a-zA-Z0-9_-]+)")


class RequestImageFile(BaseModel):
    filename: Optional[ObjectIdStr]
    desired_extension: Optional[str]
    native_extension: Optional[str]

    @root_validator(pre=True)
    def _extract_filename(cls, values):
        match = valid_filename.fullmatch(values.get('filename'))
        if match:
            values['filename'] = match.group(1)
            values['desired_extension'] = match.group(2)
            return values
        return values

    @validator('desired_extension')
    def _validate_extension(cls, v):
        if v not in IMAGE_FORMATS:
            raise TypeError('Wrong format.')
        if v == 'jpg':
            return 'jpeg'
        return v



'''
-----------------------------------------------------------
ERROR MODEL
-----------------------------------------------------------
'''

class DatabaseException(Exception):
    def __init__(self, name: str):
        self.name = name

'''
-----------------------------------------------------------
ACCOUNT MODELS transferok
-----------------------------------------------------------
'''
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



'''
Audit log definition.
'''
class PartialRole(BaseModel):
    pass

class OverWriteObject(BaseModel):
    id: ObjectIdStr #role/user id
    type: int #0 role/ 1 member
    allow: int
    deny: int


class AuditLogChange(BaseModel):
    new_value: Optional[Union[
        str, ObjectIdStr, int, bool, List[PartialRole], List[OverWriteObject]
        ]]
    old_value: Optional[Union[
        str, ObjectIdStr, int, bool, List[PartialRole], List[OverWriteObject]
        ]]
    key: str


class AuditLogEntry(BaseModel):
    id: ObjectIdStr
    user_id: ObjectIdStr
    target_id: ObjectIdStr
    changes: AuditLogChange
    action_type: int
    options: Optional[Dict]
    reasons: Optional[str]


class AuditLog(BaseModel):
    id: ObjectIdStr #server_id
    users: List[ObjectIdStr]
    audit_log_entries: List[AuditLogEntry]







'''
User definiton. TRANSFEROK
'''



class UserStatistics(BaseModel):
    joined_servers: Optional[int] = 0


class UserState(BaseModel):
    selected_server: Optional[ObjectIdStr]
    selected_room: Optional[ObjectIdStr]
    selected_channel: Optional[ObjectIdStr]
    selected_dm: Optional[str]
    selected_view: str = 'friends'
    #flags
    mfa_enabled: Optional[bool] = False
    verified: Optional[bool] = False
    flags: Optional[int] = 0
    connection: str = 'offline'
    activity: Optional[str] = None

    @validator('connection')
    def _validate_connection(cls, v):
        if v not in ['online', 'idle', 'offline', 'dnd', 'hidden']:
            #hidden to keep offline status even while connected
            raise ValueError('Not valid connection status.')
        return v

    @validator('selected_view')
    def _validate_selected_view(cls, v):
        valid = ['server', 'friends', 'dm']
        if v not in valid:
            raise ValueError('Invalid selected view. Must be one of', {*valid})
        return v


class Relationship(BaseModel):
    # stats: SNAPCHAT STYLE RELATIONSHIP STATISTICS
    blocked: List[ObjectIdStr] = []
    friend: List[ObjectIdStr] = []
    pending_incoming: List[ObjectIdStr] = []
    pending_outgoing: List[ObjectIdStr] = []



class UserSelectedState(BaseModel):
    selected_room: str
    selected_channel: str


class User(BaseModel):
    #descriptive
    id: Optional[ObjectId_Model] = Field(None, alias='_id')
    username: str
    discriminator: int
    avatar: Optional[ObjectIdStr]
    #security
    password: str
    email: str
    otp_hash: Optional[str]
    #object ids
    servers: Optional[Dict[ObjectIdStr, UserSelectedState]] = {}
    dm_rooms: Optional[List[ObjectIdStr]] = []
    #performative
    state: UserState
    statistics: UserStatistics
    relationships: Optional[Relationship] = Relationship()

    class Config:
        allow_population_by_field_name = True




'''
Server definitions. TRANSFEROK
'''



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


'''
-----------------------
Base server definition.
-----------------------
'''


class BaseServerRoom(BaseModel):
    name: str = Field(..., example="Room 1")


class ChannelBase(BaseModel):
    name: str = Field(..., example="Channel 1")
    rooms: List[BaseServerRoom]
    id = ObjectIdFactory()


class ServerBase(BaseModel):
    name: str = Field(..., example="Test Server")
    channels: Optional[List[ChannelBase]]


'''
-----------------------
Serverdata definition.
-----------------------
'''


class ServerData(BaseModel):
    selected_serverdata: Server
    base_permissions: PermissionBitflag
    user_roles: List[str]


class ChannelData(BaseModel):
    name: str
    channel_permissions: int



'''
-----------------------------------------------------------
ROOM DEFINITION
-----------------------------------------------------------
'''

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
    type = RoomTypes.SERVER_ROOM
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

class ThreadRoomIn(BaseRoom):
    server: ObjectIdStr
    channel: ObjectIdStr #parent_id
    init_post: ObjectIdStr
    members: Dict[ObjectIdStr, ThreadMember]
    settings: ThreadSettingsIn


class ThreadRoom(BaseRoom):
    type = RoomTypes.THREAD_ROOM
    settings: ThreadSettings
    owner_id: ObjectIdStr



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
    type = RoomTypes.DM_ROOM
    participants: Optional[List[UserPartialDmRoom]]
    owner_id: ObjectIdStr
    name: str


class RoomData(BaseModel):
    selected_roomdata: Union[ServerRoom, DmRoom]
    room_permissions: Optional[int]


class ThreadData(BaseModel):
    selected_threaddata: ThreadRoom

'''
-----------------------------------------------------------
INIT DATA
-----------------------------------------------------------
'''


# class UserMessagingPartial(BaseModel):
#     id: ObjectId_Model = Field(None, alias='_id')
#     avatar: Optional[ObjectIdStr]
#     username: str
#     connection: str

#     class Config:
#         allow_population_by_field_name = True


# class EnterServerInitData(BaseModel):
#     serverdata: Optional[ServerData]
#     channeldata: Optional[ChannelData]
#     threaddata: Optional[ThreadData]
#     roomdata: Optional[RoomData]



# class InitData(EnterServerInitData):
#     userdata: User
#     serverlist: List[ServerPartialSidebar] = []
#     friendlist: List[UserMessagingPartial] = []
#     dmlist: List[SidebarIndicator] = []
#     applist: List[AppCommand]


