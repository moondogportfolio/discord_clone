from typing import Optional, Dict, List
from pydantic import BaseModel

class Operation(BaseModel):
    attr_val: Optional[Dict] = None
    operation: Optional[str] = 'set'

class UpdateObject(Operation):
    filter: Dict
    operation_list: Optional[List[Operation]] = None
    collection: str
    mongo_ops: str = 'update'
    upsert: bool = False
    array_filters: List = None



class BulkUpdateObject(BaseModel):
    collection: str
    update_items: List[UpdateObject]