from fastapi import APIRouter, Response, HTTPException, UploadFile, File
from devtools import debug

from pydantic_models.universal import ObjectIdStr

from processors.file import *


router = APIRouter(
    # prefix="/server",
    tags=["file upload/download"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


@router.post("/uploadfile/",
        response_model=ObjectIdStr,
         )
async def _create_upload_file(category: str, file: UploadFile = File(...)):
    if category not in ['emoji']:
        return Response(status_code=404) 
    img_bytes, extension = await img_filelike_to_bytes(file.file)
    try:
        description = GraphicsDescriptionIn(
            category=category,
            extension=extension
        )
    except Exception as e:
        debug(e, category, extension)
        return Response(status_code=404)
    return upload_file(img_bytes, description)



@router.get("/emojis/{server_id}/{request_image}", response_class=Response,
        responses={
            200: {"content": {"image/png": {}}},
            404: {"description": "Item not found"},
        }
        )
async def _get_emoji_image(
    server_id: ObjectIdStr,
    request_image: str = RequestImageFile):
    '''
    Example: 60f8e8ed6cdb71569db2fa06
    '''
    try:
        request_image = RequestImageFile(filename = request_image)       
    except Exception as e:
        debug(e)
    buffer, extension = get_file_emoji(server_id, request_image)
    if not buffer:
        raise HTTPException(status_code=404, detail="No such image.")
    return Response(content=buffer.read(), media_type=f"image/{extension}")


@router.get("/server-icon/{server_id}", response_class=Response,
        responses={
            200: {"content": {"image/png": {}}},
            404: {"description": "Item not found"},
        }
        )
async def _get_server_icon(server_id: ObjectIdStr):
    try:
        buffer, extension = get_server_icon(server_id)
    except TypeError: # cannot unpack non-iterable NoneType object
        raise HTTPException(status_code=404, detail="Server has no icon/avatar.")
    return Response(content=buffer.read(), media_type=f"image/{extension}")


@router.get("/user-icon/{user_id}", response_class=Response,
        responses={
            200: {"content": {"image/png": {}}},
            404: {"description": "Item not found"},
        }
        )
async def _get_user_icon(user_id: ObjectIdStr):
    try:
        buffer, extension = get_user_icon(user_id)
    except TypeError: # cannot unpack non-iterable NoneType object
        raise HTTPException(status_code=404, detail="User has no icon/avatar.")
    return Response(content=buffer.read(), media_type=f"image/{extension}")


    