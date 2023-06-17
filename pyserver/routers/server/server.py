from fastapi import APIRouter, Depends, UploadFile, File
from fastapi.param_functions import Path, Query

from pydantic_models.universal import ObjectIdStr
from pydantic_models.users import User
from security import get_current_user
from typing import Optional, List
from devtools import debug

from processors.server_room import create_server_channel
from processors.file import img_filelike_to_bytes

from processors.server import ServerDiscoveryPartial, get_server, discover_servers, GraphicsDescriptionIn, add_server_emoji, edit_server_icon, create_server,delete_server, ServerIn, Server


router = APIRouter(
    prefix="/server",
    tags=["server"],
    responses={404: {"description": "Not found"}},
)

@router.get("/discover", 
        response_model=List[ServerDiscoveryPartial]
        )
async def _discover_servers():
    return discover_servers()


    

@router.post("/{server_id}/emojis")
async def _create_emoji(
    server_id: ObjectIdStr, 
    name: str = Query(..., min_length=2, max_length=100),
    file: UploadFile = File(...) ):
    data, extension, animated = await img_filelike_to_bytes(file.file)
    mongo_file = GraphicsDescriptionIn.construct(
            category = 'emoji',
            extension = extension,
            data = data,
            animated = animated
        )
    return add_server_emoji(server_id, name, mongo_file)


@router.post("/{server_id}/icon")
async def _edit_server_icon(
    server_id: ObjectIdStr, 
    file: UploadFile = File(...) ):
    data, extension, animated = await img_filelike_to_bytes(file.file)
    mongo_file = GraphicsDescriptionIn.construct(
            category = 'server_icon',
            extension = extension,
            data = data,
            animated = animated
        )
    return edit_server_icon(server_id, mongo_file)


# @router.post("/server/{server_id}/rooms", tags=["server"])


@router.post("")
async def _create_server(
    server_obj: ServerIn,
    icon: Optional[str] = None,
    current_user: User = Depends(get_current_user)
    ):
    '''
    ✔ - Create new server.
    '''
    return create_server(server_obj, icon, current_user.id)
    

@router.delete("/{server_id}",
        status_code=204,
        response_description="No content. Server has been deleted.",
        responses={404: {'description': 'Server not found.'}},
        tags = ["server"]
        )
async def _delete_server(
    server_id: ObjectIdStr = Path(..., example = "60fbabedc30a2589720f09a4"),
    ):
    '''
    Delete server.
    '''
    debug(server_id)
    return delete_server(server_id)




# @router.patch("/server/{server_id}",
#         tags = ["server"]
#         )
# async def _modify_server(
#     server_obj: BaseServer,
#     server_id: ObjectIdStr = Path(..., example = "60fbabedc30a2589720f09a4"),
#     ):
#     '''
#     Modify server.
#     '''
#     return modify_server(server_id, server_obj)


@router.get("/{serverid}",  response_model=Server)
async def _get_server(
    server_id: ObjectIdStr
    ):
    '''
    ✔ - Get server.
    '''
    return get_server(server_id)



@router.post("/{server_id}/channel"
        )
async def _create_server_channel(
    server_id: ObjectIdStr,
    name: str
    ):
    '''
    ✔ - Create server channel.
    '''
    await create_server_channel(server_id, name)


