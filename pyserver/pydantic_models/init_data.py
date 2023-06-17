
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Union
from pydantic_models.universal import ObjectId_Model, ObjectIdStr, PermissionBitflag
from pydantic_models.users import User
from pydantic_models.rooms import RoomData, ThreadData, DmRoom, ServerRoom
from pydantic_models.servers import ServerPartialSidebar, SidebarIndicator, Server
from pydantic_models.tasks import Workspace
from applications import AppCommand





class ServerData(BaseModel):
    selected_serverdata: Server
    base_permissions: PermissionBitflag
    user_roles: List[str]


class ChannelData(BaseModel):
    name: str
    channel_permissions: int


class UserMessagingPartial(BaseModel):
    id: ObjectId_Model = Field(None, alias='_id')
    avatar: Optional[ObjectIdStr]
    username: str
    connection: str

    class Config:
        allow_population_by_field_name = True



class WorkspacePartialSidebar(BaseModel):
    id: Optional[ObjectId_Model] = Field(None, alias='_id')
    name: str
    position: Optional[int]

    class Config:
        allow_population_by_field_name = True


class EnterServer_InitData(BaseModel):
    serverdata: Optional[ServerData]
    channeldata: Optional[ChannelData]
    threaddata: Optional[ThreadData]
    roomdata: Dict[ObjectIdStr, ServerRoom] = {}

class EnterWorkspaceData(BaseModel):
    workspacedata: Dict[ObjectIdStr, Workspace] = {}
    workspacelist: List[WorkspacePartialSidebar]


class InitData(EnterServer_InitData, EnterWorkspaceData):
    userdata: User
    serverlist: List[ServerPartialSidebar] = []
    applist: List[AppCommand]
    friendlist: List[UserMessagingPartial] = []
    # roomdata: Dict[ObjectIdStr, Union[ServerRoom, DmRoom]] = {}

'''
Q.  why is roomdata for server a single value while for dms its a list?
A.  dms has preview while server rooms has not.
'''