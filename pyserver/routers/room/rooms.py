from fastapi import APIRouter, Path, Query, Body
from typing import List, Optional

from pydantic_models.universal import ObjectIdStr

from processors.room import *

router = APIRouter(
    prefix="/room",
    tags=["room"],
    # dependencies=[Depends(get_token_header)],
)

from constants import ROOM_EX, ROOM_SERVER_POST_MSG_EX, SPECIFIC_MSG_EX

'''
-----------------------
posts: Optional[List[Post]]
-----------------------
'''
@router.get("/{room_id}/message",
        response_model=List[Post]
        )
async def _get_room_messages(
    room_id: ObjectIdStr = Path(..., example=ROOM_EX),
    limit: Optional[int] = Query(None, le=100, ge=-100, description='Positive limit gets the FIRST n posts, negative limit gets the LAST n posts.')):
    '''
    GET MESSAGES FROM ROOM.
    '''
    return get_room_messages(room_id, limit)




#save timestamp of last post to user
@router.post("/{room_id}/message"
        )
async def _post_to_room(
    room_id: ObjectIdStr = Path(..., example=ROOM_EX),
    post: PostIn = Body(..., examples=ROOM_SERVER_POST_MSG_EX)
    ):
    '''
    POST MESSAGE TO ROOM.
    '''
    return await post_to_room(room_id, post)




@router.get("/{room_id}/message/{message_id}",
        response_model=Post
        )
async def _get_room_message(
    room_id: ObjectIdStr = Path(..., example=ROOM_EX),
    message_id: ObjectIdStr = Path(..., example=SPECIFIC_MSG_EX)
    ):
    '''
    GET MESSAGE FROM ROOM.
    '''
    return get_one_room_message(room_id, message_id)



@router.patch("/{room_id}/message/{post_id}",
        )
async def _edit_room_message(
    post_id: ObjectIdStr,
    room_id: ObjectIdStr = Path(..., example=ROOM_EX),
    post: PostIn = Body(..., examples=ROOM_SERVER_POST_MSG_EX)
    ):
    '''
    EDIT MESSAGE.
    '''
    await edit_room_message(room_id, post_id, post)



# @router.delete("/room/{room_id}/message",
#         tags=["room"],
#         responses={404: {'description': 'Room not found.'}}
#         )
# async def _delete_room_message(
#     room_id: ObjectIdStr = Path(..., example=ROOM_EX),
#     post: PostIn = Body(..., examples=ROOM_SERVER_POST_MSG_EX)
#     ):
#     '''
#     EDIT MESSAGE.
#     '''
#     return delete_room_message(room_id, post)

