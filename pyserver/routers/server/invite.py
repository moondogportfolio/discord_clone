from fastapi import APIRouter, Depends

from pydantic_models.servers import InviteIn
from pydantic_models.users import User

from processors.invite import *

from security import get_current_user

router = APIRouter(
    prefix="/invite",
    tags=["invites"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)



@router.post("")
async def _add_server_invite(
    invite_obj: InviteIn
    ):
    add_server_invite(invite_obj)

@router.put("/{invite_id}")
async def _use_server_invite(
    invite_id: str,
    current_user: User = Depends(get_current_user)
    ):
    return use_server_invite(invite_id, current_user)

