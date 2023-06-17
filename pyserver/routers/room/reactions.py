from fastapi import APIRouter, Path

from pydantic_models.universal import ObjectIdStr

from processors.reaction import *

router = APIRouter(
    prefix="/room",
    tags=["room_reactions"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

from constants import ROOM_EX, EMOJI_EX, SPECIFIC_MSG_EX


#save timestamp of last post to user
@router.put("/{room_id}/message/{message_id}/reaction/{emoji_id}/@me")
async def _add_reaction(
    room_id: ObjectIdStr = Path(..., example=ROOM_EX),
    message_id: ObjectIdStr = Path(..., example=SPECIFIC_MSG_EX),
    emoji_id: str = Path(..., example=EMOJI_EX)
    ):
    '''
    ✔ - ADD REACTION.
    '''
    await add_reaction(room_id, message_id, emoji_id)


@router.delete("/{room_id}/message/{message_id}/reaction/{emoji_id}/@me")
async def _delete_reaction(
    room_id: ObjectIdStr = Path(..., example=ROOM_EX),
    message_id: ObjectIdStr = Path(..., example=SPECIFIC_MSG_EX),
    emoji_id: str = Path(..., example=EMOJI_EX)
    ):
    '''
    ✔ - REMOVE REACTION.
    '''
    return delete_reaction(room_id, message_id, emoji_id)
