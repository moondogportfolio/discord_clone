from pydantic import BaseModel
from typing import Union, List, Dict, Optional


# class Condition(BaseModel):
#     operation: Operation

# class Automation(BaseModel):
#     trigger: List[Condition]
#     logic: str
#     value: Union[str, int]


class Automation(BaseModel):
    rules: Dict
    data: Optional[Dict]