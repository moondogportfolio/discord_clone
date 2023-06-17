from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from typing import Optional

from pydantic_models.users import User, UserIn
from pydantic_models.universal import ObjectIdStr

from processors.users import get_user, modify_user
from processors.file import img_filelike_to_bytes
from processors.server import edit_user_icon, GraphicsDescriptionIn

from security import get_current_user, get_password_hash

from devtools import debug

router = APIRouter(
    prefix="/users",
    tags=["user"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


@router.post("/{user_id}/icon")
async def _edit_user_icon(
    user_id: ObjectIdStr, 
    file: UploadFile = File(...) ):
    data, extension, animated = await img_filelike_to_bytes(file.file)
    mongo_file = GraphicsDescriptionIn.construct(
            category = 'server_icon',
            extension = extension,
            data = data,
            animated = animated
        )
    edit_user_icon(user_id, mongo_file)



@router.get("/{user_id}",
        response_model=User, 
        responses={404: {"description": "Item not found"}}
        )
async def _get_user(user_id: ObjectIdStr):
    result = get_user(user_id)
    if not result:
        raise HTTPException(status_code=404, detail="No such user.")
    return result



@router.get("/@me", response_model=User)
async def _get_current_user(current_user: User = Depends(get_current_user)):
    return current_user


@router.patch("/@me", response_model=User)
async def _modify_current_user(
        user_obj: Optional[UserIn],
        current_user: User = Depends(get_current_user),
        ):

    await modify_user(current_user.id, user_obj)
    # debug(user_obj)
    # if not avatar and not username:
    #     raise HTTPException(status_code=400)
    # img_bytes = await img_filelike_to_bytes(avatar.file) if avatar else None
    # if not modify_user(current_user.id, username, img_bytes):
    #     raise HTTPException(status_code=401)
    # return FileResponse("image.png", media_type="image/png")

