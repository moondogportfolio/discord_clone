from fastapi import APIRouter, Depends
from typing import Optional
from devtools import debug
from pydantic_models.rooms import DmRoomIn, RoomData, BaseRoom
from pydantic_models.users import User
from pydantic_models.universal import ObjectIdStr

from processors.dm_room import *

from security import get_current_user

router = APIRouter(
    prefix="/dm_room",
    tags=["dm_room"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)



@router.patch("/{object_id}")
async def _modify_dm_room(dm_room_id: ObjectIdStr, icon: Optional[str] = None, name: Optional[str] = None):
    return modify_dm_room(dm_room_id, icon, name)



@router.post("",
    status_code=201
    )
async def _create_dm_room(
    dmroom: DmRoomIn,
    current_user: User = Depends(get_current_user)
    ):
    debug('enter')
    return await create_dm_room(dmroom, current_user.id)



@router.get("/{dm_room_id}",
    response_model=RoomData
    )
async def _get_dm_room(dm_room_id: ObjectIdStr):
    result = get_dm_room(dm_room_id)
    debug(result)
    return RoomData(selected_roomdata=result)



@router.delete("/{dm_room_id}",
    response_model=BaseRoom
    )
async def _delete_dm_room(user_id: ObjectIdStr, dm_room_id: ObjectIdStr, method: Optional[str] = 'obliterate'):
    '''
    DELETE ROOM.
    '''
    await delete_dm_room(user_id, dm_room_id, method)

