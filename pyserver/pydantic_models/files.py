from pydantic import BaseModel, validator, root_validator
from typing import Optional
import re

from pydantic_models.universal import ObjectIdStr

IMAGE_FORMATS = [
    'png',
    'jpg',
    'jpeg',
    'webp',
    'gif'    
]

class GraphicsDescriptionOut(BaseModel):
    extension: str
    category: str
    animated: Optional[bool] = False


class GraphicsDescriptionIn(GraphicsDescriptionOut):
    data: bytes

    @validator('extension')
    def _validate_gfx_extension(cls, v):
        if v not in ['JPG', 'PNG', 'JPEG', 'WEBP', 'GIF']:
            raise ValueError('Invalid graphics extension.')
        return v

    @validator('category')
    def _validate_gfx_category(cls, v):
        if v not in ['emoji', 'server_icon', 'icon']:
            raise ValueError('Invalid graphics category.')
        return v



class RequestImageFile(BaseModel):
    filename: Optional[ObjectIdStr]
    desired_extension: Optional[str]
    native_extension: Optional[str]

    @root_validator(pre=True)
    def _extract_filename(cls, values):
        match = re.compile(r"([a-zA-Z0-9]*)\.([a-zA-Z0-9_-]+)").fullmatch(values.get('filename'))
        if match:
            values['filename'] = match.group(1)
            values['desired_extension'] = match.group(2)
            return values
        return values

    @validator('desired_extension')
    def _validate_extension(cls, v):
        if v not in IMAGE_FORMATS:
            raise TypeError('Wrong format.')
        if v == 'jpg':
            return 'jpeg'
        return v
