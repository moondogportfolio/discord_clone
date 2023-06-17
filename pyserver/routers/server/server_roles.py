from fastapi import APIRouter, Path

from pydantic_models.universal import ObjectIdStr
from pydantic_models.servers import Role, ServerMemberIn

from processors.server import create_server_role


SERVER_EX = ''
SERVER_USER_EX = ''


router = APIRouter(
    prefix="/server",
    tags=["server_role"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

@router.post("/{server_id}/role", response_model=Role)
async def _create_server_role(
    server_id: ObjectIdStr
    ):
    return create_server_role(server_id)


@router.get("/{server_id}/role/{role_id}")
async def _get_server_role(
    server_id: ObjectIdStr = Path(..., example=SERVER_EX),
    role_id: ObjectIdStr = Path(..., example=SERVER_USER_EX)
    ):
    return get_server_role(server_id, role_id)


@router.patch("/{server_id}/role/{role_id}")
async def _modify_server_role(
    modifiers: ServerMemberIn,
    server_id: ObjectIdStr = Path(..., example=SERVER_EX),
    role_id: ObjectIdStr = Path(..., example=SERVER_USER_EX)
    ):
    '''
    ✔ - Modify server member.
    '''
    return modify_server_role(server_id, role_id, modifiers)


@router.delete("/{server_id}/role/{role_id}",
        status_code=204,
        response_description="No content. Room has been deleted.",
        responses={404: {'description': 'Server room not found.'}}
        )
async def _delete_server_role(
    server_id: ObjectIdStr = Path(..., example=SERVER_EX),
    role_id: ObjectIdStr = Path(..., example=SERVER_USER_EX)
    ):
    return delete_server_role(server_id, role_id)

