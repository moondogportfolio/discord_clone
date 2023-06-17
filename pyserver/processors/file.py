from PIL import Image
from io import BytesIO
from typing import Tuple

from pydantic_models.files import RequestImageFile, GraphicsDescriptionIn
from pydantic_models.universal import ObjectIdStr

from processors.mongo_update import servers, users
from mongo_cons import query_id


def upload_file(byte_file, description: GraphicsDescriptionIn) -> ObjectIdStr:
    mongo_file = description.dict()
    mongo_file.update({'data': byte_file})
    return str(files.insert_one(mongo_file).inserted_id)


def convert_mongo_image_bytes(image_obj: GraphicsDescriptionIn, image_request: RequestImageFile) -> Tuple[bytes, str]:
    '''
    1.  Fetch image data and open.  
    2.  Process image (resize, convert)
    3.  Create byte-obj then return.
    '''
    #1
    image_request.native_extension = image_obj.extension
    pil_img = Image.open(BytesIO(image_obj.data))
    #2
    buffer = BytesIO()
    image_format = image_request.desired_extension if image_request.desired_extension else image_request.native_extension
    if (image_request.desired_extension
        and image_request.desired_extension != image_request.native_extension
        and pil_img.mode != 'RGB'):
        pil_img = pil_img.convert('RGB')
    pil_img.save(buffer, image_format)
    buffer.seek(0)
    return buffer, image_format


def get_file_emoji(server_id: ObjectIdStr,image_obj: RequestImageFile):
    image = servers.find_one(
        query_id(server_id),
        {'file': f'$emoji.{image_obj.filename}.file', '_id': False}
    )
    if not image:
        return None
    return convert_mongo_image_bytes(
        GraphicsDescriptionIn.construct(**image['file']),
        image_obj)


def get_server_icon(server_id: ObjectIdStr):
    image = servers.find_one(
        query_id(server_id),
        {'icon': 1, '_id': False}
    )
    if not image:
        return None
    return convert_mongo_image_bytes(
        GraphicsDescriptionIn.construct(**image['icon']),
        RequestImageFile.construct())


def get_user_icon(user_id: ObjectIdStr):
    image = users.find_one(
        query_id(user_id),
        {'icon': 1, '_id': False}
    )
    if not image:
        return None
    return convert_mongo_image_bytes(
        GraphicsDescriptionIn.construct(**image['icon']),
        RequestImageFile.construct())


async def img_filelike_to_bytes(file) -> Tuple[bytes, str, bool]:
    img = Image.open(file)
    imgByteArr = BytesIO()
    img.save(imgByteArr, format=img.format)
    return imgByteArr.getvalue(), img.format, getattr(img, "is_animated", False) 
