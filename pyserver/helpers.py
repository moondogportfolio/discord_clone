from typing import Tuple
from bson.objectid import ObjectId
from datetime import datetime
from types import GeneratorType
from pydantic.json import pydantic_encoder
from models import ObjectId as ObjectId_Model

from PIL import Image
from io import BytesIO


def parse(obj):
    def walker(parent, index, tracked):
        if type(tracked) is dict:
            for k, v in tracked.items():
                walker(tracked, k, v)
        elif type(tracked) is list:
            for i, v in enumerate(tracked):
                walker(tracked, i, v)
        elif type(tracked) is ObjectId:
            parent[index] = str(tracked)
        elif type(tracked) is ObjectId:
            parent[index] = str(tracked)
        elif type(tracked) is datetime:
            parent[index] = str(tracked)
    walker(obj, obj, obj)
    return obj


def jsonable_encoder(obj):
    if isinstance(obj, (str, int, float, type(None))):
        return obj
    if isinstance(obj, dict):
        return {jsonable_encoder(key): jsonable_encoder(value) for key, value in obj.items()}
    if isinstance(obj, (list, set, frozenset, GeneratorType, tuple)):
        return [jsonable_encoder(item) for item in obj]
    if isinstance(obj, ObjectId_Model):
        return str(obj)
    return pydantic_encoder(obj)


async def img_filelike_to_bytes(file) -> Tuple[bytes, str, bool]:
    img = Image.open(file)
    imgByteArr = BytesIO()
    img.save(imgByteArr, format=img.format)
    return imgByteArr.getvalue(), img.format, getattr(img, "is_animated", False) 


def dispatcher(top_object, operation, attribute, value):
    if top_object == 'server':
        top_object = 'serverdata.selected_serverdata'
    return {
        operation: {
            f'{top_object}.{attribute}': value
        }
    }