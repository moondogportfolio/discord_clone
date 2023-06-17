from fastapi import APIRouter, Depends, Path

from pydantic_models.init_data import EnterServer_InitData
from pydantic_models.users import User
from pydantic_models.universal import ObjectIdStr
from pydantic_models.servers import ServerMemberIn
from security import get_current_user

from processors.server_user import add_server_member, delete_server_member
from processors.init_data import enter_server_main
from processors.server import server_modify_member

from constants import SERVER_EX, SERVER_USER_EX


router = APIRouter(
    prefix="/server",
    tags=["server_user"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

@router.put("/{server_id}/enter", response_model=EnterServer_InitData)
async def _enter_server(
    server_id: ObjectIdStr = Path(..., example=SERVER_EX),
    current_user: User = Depends(get_current_user)
    ):
    '''
    ✔ - Enter server.
    '''
    return enter_server_main(server_id, current_user)


@router.put("/{server_id}/member/{user_id}")
async def _add_server_member(
    server_id: ObjectIdStr = Path(..., example=SERVER_EX),
    user_id: ObjectIdStr = Path(..., example=SERVER_USER_EX)
    ):
    '''
    ✔ - Add server member.
    '''
    return add_server_member(server_id, user_id)



@router.patch("/{server_id}/member/{user_id}")
async def _server_modify_member(
    modifiers: ServerMemberIn,
    server_id: ObjectIdStr = Path(..., example=SERVER_EX),
    user_id: ObjectIdStr = Path(..., example=SERVER_USER_EX)
    ):
    '''
    ✔ - Modify server member.
    '''
    return server_modify_member(server_id, user_id, modifiers)


@router.delete("/{server_id}/member/{user_id}",
        status_code=204,
        response_description="No content. Room has been deleted.",
        responses={404: {'description': 'Server room not found.'}},
        tags = ["server_user"]
        )
async def _delete_server_member(
    server_id: ObjectIdStr = Path(..., example=SERVER_EX),
    user_id: ObjectIdStr = Path(..., example=SERVER_USER_EX)
    ):
    '''
    ✔ - Kick server member.
    '''
    return delete_server_member(server_id, user_id)

# 