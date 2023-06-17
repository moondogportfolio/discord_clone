from fastapi import APIRouter, UploadFile, File
from typing import Optional

from processors.file import img_filelike_to_bytes
from processors.utils import base64_encoder

router = APIRouter(
    # prefix="/thread",
    tags=["utils"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


@router.post("/base64encoder", response_model=str, tags=["utils"])
async def _base64_encoder(image: Optional[UploadFile] = File(...)):
    img_bytes = await img_filelike_to_bytes(image.file)
    result = base64_encoder(img_bytes)

@router.get('/taskdict')
def _taskdict():
    return taskdict