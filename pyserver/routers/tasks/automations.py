from fastapi import APIRouter, Path, Depends
from security import get_current_user
from typing import List, Dict
from mongo_cons import query_id, set_attr, remove_attr, query_ids

from pydantic_models.universal import ObjectIdStr, ObjectIdFactory
from pydantic_models.tasks import *
from pydantic_models.users import User, UserTask, UserWorkspace
from pydantic_models.update import UpdateObject, Operation
from pydantic_models.automation import Automation


from processors.mongo_update import workspaces, users, data_update

from bson.objectid import ObjectId

from devtools import debug

router = APIRouter(
    prefix="/automation",
    tags=["automation"],
    # dependencies=[Depends(get_token_header)],
)

WORKSPACE_EX = ''
BOARD_EX = ''
TASK_EX = ''

@router.post("")
async def _create_automation(
    automation: Automation,
    current_user: User = Depends(get_current_user),
    ):
    users.update_one(
        query_id(current_user.id),
        set_attr(f'automation.{str(ObjectId())}', automation.dict(exclude_unset=True))
        )
