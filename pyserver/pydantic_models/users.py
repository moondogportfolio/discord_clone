from pydantic_models.universal import ObjectIdStr, ObjectId_Model
from pydantic_models.tasks import Workspace
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Dict
from enum import IntEnum, auto, Enum



class UserStatistics(BaseModel):
    joined_servers: Optional[int] = 0


class UserState(BaseModel):
    selected_server: Optional[ObjectIdStr]
    selected_room: Optional[ObjectIdStr] #TOCULL
    selected_channel: Optional[ObjectIdStr]
    selected_thread: Optional[ObjectIdStr]
    selected_dm: Optional[str] #TOCULL
    selected_workspace: Optional[ObjectIdStr]
    pinned_rooms: Optional[List[ObjectIdStr]] = []
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
        valid = ['server', 'friends', 'dm', 'workspace']
        if v not in valid:
            raise ValueError('Invalid selected view. Must be one of', {*valid})
        return v


class Relationship(BaseModel):
    blocked: List[ObjectIdStr] = []
    friend: List[ObjectIdStr] = []
    pending_incoming: List[ObjectIdStr] = []
    pending_outgoing: List[ObjectIdStr] = []



class UserSelectedState(BaseModel):
    selected_room: str
    selected_channel: str

class DmRoomUserState(BaseModel):
    position: int = None
    # setting closing a dm room unpins it


class UserIn(BaseModel):
    username: Optional[str]
    password: Optional[str]
    email: Optional[str]
    state: Optional[UserState]

class UserTask(BaseModel):
    group: Optional[List[str]] = []

class UserBoard(BaseModel):
    task: Dict[ObjectIdStr, UserTask] = {}

class UserWorkspace(BaseModel):
    board: Dict[ObjectIdStr, UserBoard] = {}

class User(BaseModel):
    username: str
    #descriptive
    id: Optional[ObjectId_Model] = Field(None, alias='_id')
    discriminator: int
    avatar: Optional[ObjectIdStr]
    #security
    password: str
    email: str
    otp_hash: Optional[str]
    #object ids
    servers: Optional[Dict[ObjectIdStr, UserSelectedState]] = {}
    dm_rooms: Dict[ObjectIdStr, DmRoomUserState] = {}
    workspace: Optional[Dict[ObjectIdStr, UserWorkspace]] = {}
    #performative
    state: UserState
    statistics: UserStatistics
    relationships: Optional[Relationship] = Relationship()

    class Config:
        allow_population_by_field_name = True
