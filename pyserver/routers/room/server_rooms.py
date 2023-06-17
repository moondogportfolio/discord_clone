from fastapi import APIRouter, Path, Query
from typing import List

from pydantic_models.universal import ObjectIdStr

from processors.server_room import *
from processors.dm_room import *

from constants import SERVER_EX, CHANNEL_EX, ROOM_EX

router = APIRouter(
    # prefix="/server_room",
    tags=["server_room"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)



@router.post("server/{server_id}/rooms")
async def _create_server_room(
    name: str = Query(..., example='Test Room'),
    server_id: ObjectIdStr = Path(..., example=SERVER_EX),
    channel_id: ObjectIdStr = Query(..., example=CHANNEL_EX)
    ):
    '''
    ✔ - Create new server room.
    '''
    return create_server_room(server_id, channel_id, name)
    


@router.get("server/{server_id}/rooms",
        response_model=List[ServerRoom],
        responses={404: {'description': 'Server not found.'}}
        )
async def _get_server_rooms(
    server_id: ObjectIdStr = Path(..., example=SERVER_EX),
    ):
    '''
    ✔ - Get server rooms. 
    '''
    return get_list_of_server_rooms(server_id)



@router.get("server_room/{room_id}", 
        response_model=ServerRoom,
        responses={404: {'description': 'Room not found.'}}
        )
async def _get_server_room(room_id: ObjectIdStr = Path(..., example=ROOM_EX)):
    '''
    ✔ - Get server room. 
    '''
    return get_server_room(room_id)



@router.patch("server_room/{room_id}",
        response_model=ServerRoom
        )
async def modify_server_room(server_room_id: ObjectIdStr):
    '''
    Modify server room.  TODO
    '''
    return modify_server_room(server_room_id)



@router.delete("server_room/{room_id}",
        status_code=204,
        response_description="No content. Room has been deleted.",
        responses={404: {'description': 'Server room not found.'}}
        )
async def _delete_server_room(server_room_id: ObjectIdStr):
    '''
    ✔ - Delete server room. 
    '''
    return delete_server_room(server_room_id)

