from fastapi import APIRouter, Depends, Response

from pydantic_models.servers import InviteIn
from pydantic_models.users import User
from pydantic_models.universal import ObjectIdStr

from processors.users import add_relationship, confirm_relationship, deny_relationship

from security import get_current_user

router = APIRouter(
    prefix="/users",
    tags=["user"],
    # dependencies=[Depends(get_token_header)],
    responses={412: {'description': 'Already a friend.'}}
)



@router.put("/@me/relationships/{user_id}")
async def _add_relationship(
    user_id: ObjectIdStr,
    current_user: User = Depends(get_current_user)
    ):
    if user_id in current_user.relationships:
        return Response(status_code=412)
    await add_relationship(current_user.id, user_id)


@router.patch("/@me/relationships/{user_id}")
async def _confirm_relationship(
    user_id: ObjectIdStr,
    current_user: User = Depends(get_current_user)
    ):
    if user_id in current_user.relationships:
        return Response(status_code=412)
    await confirm_relationship(current_user.id, user_id)


@router.delete("/@me/relationships/{user_id}")
async def _deny_relationship(
    user_id: ObjectIdStr,
    current_user: User = Depends(get_current_user)
    ):
    try:
        if current_user.relationships[user_id] == 'friends':
            return Response(status_code=412)
        deny_relationship(current_user.id, user_id)
    except:
        deny_relationship(current_user.id, user_id)
