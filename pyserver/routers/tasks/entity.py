from pydantic_models.resource import *
from fastapi import APIRouter, Path, Depends
from security import get_current_user
from typing import List, Dict
from mongo_cons import query_id, set_attr, remove_attr, query_ids, push_arr_ele, pull_arr_ele

from pydantic_models.universal import ObjectIdStr
from pydantic_models.resource import Resource
from pydantic_models.organization import *
from processors.mongo_update import workspaces, users, data_update

from bson.objectid import ObjectId

from devtools import debug

router = APIRouter(
    prefix="/workspace",
    tags=["workspace_entity"],
    # dependencies=[Depends(get_token_header)],
)



WORKSPACE_EX = '6129fe3bbef29db420a30ec3'
BOARD_EX = '6129fe58ffb50fb57a849a6f'
TASK_EX = '612c76009f5aed17aff0397e'
RESOURCE_EX = '613fab0a367cddaa1b9130fd'
RESOURCE_CONT_EXT = '613fa6d37cd534aec98d0a59'
MEMBER_EX = '61355552389a7e7a1d45dec7'
ENTITY_GROUP_ID = '6141b191972ccbfa38b9fa45'


@router.post("/{workspace_id}/entity-group", response_model=ObjectIdStr)
async def _create_entity_group(
    workspace_id: ObjectIdStr = Path(..., example=WORKSPACE_EX)
    ):
    entity_group_id = str(ObjectId())
    workspaces.update_one(
        query_id(workspace_id),
        set_attr(
            attr_dict={f'entity_group.{entity_group_id}': {}}
        )
    )


@router.post("/{workspace_id}/entity-group/{entity_group_id}/entity/{entity_id}")
async def _add_entity(
    entity_obj: EntityPartial,
    workspace_id: ObjectIdStr = Path(..., example=WORKSPACE_EX),
    entity_group_id: ObjectIdStr = Path(..., example=ENTITY_GROUP_ID),
    entity_id: ObjectIdStr = Path(..., example=MEMBER_EX)
    ):
    workspaces.update_one(
        query_id(workspace_id),
        set_attr(
            attr_dict={f'entity_group.{entity_group_id}.entity.{entity_id}': entity_obj.dict(exclude_unset=True)}
        )
    )




@router.post("/{workspace_id}/entity-group/{entity_group_id}/relationship/{entity_id}")
async def _link_entities(
    relationship: str,
    workspace_id: ObjectIdStr = Path(..., example=WORKSPACE_EX),
    entity_group_id: ObjectIdStr = Path(..., example=ENTITY_GROUP_ID),
    entity_id: ObjectIdStr = Path(..., example=MEMBER_EX)
    ):
    workspaces.update_one(
        query_id(workspace_id),
        set_attr(
            attr_dict={f'entity_group.{entity_group_id}.relationship.{entity_id}': relationship}
        )
    )



@router.post("/{workspace_id}/entity-group/{entity_group_id}/task/{task_id}/")
async def _add_task(
    task_obj: EntityTask,
    workspace_id: ObjectIdStr = Path(..., example=WORKSPACE_EX),
    entity_group_id: ObjectIdStr = Path(..., example=ENTITY_GROUP_ID),
    task_id: ObjectIdStr = Path(..., example=TASK_EX)
    ):
    workspaces.update_one(
        query_id(workspace_id),
        set_attr(
            attr_dict={f'entity_group.{entity_group_id}.task.{task_id}': task_obj.dict(exclude_unset=True)}
        )
    )


@router.post("/{workspace_id}/entity-group/{entity_group_id}/task/{task_id}/schedule")
async def _add_task_schedule(
    schedule_obj: TaskSchedule,
    workspace_id: ObjectIdStr = Path(..., example=WORKSPACE_EX),
    entity_group_id: ObjectIdStr = Path(..., example=ENTITY_GROUP_ID),
    task_id: ObjectIdStr = Path(..., example=TASK_EX)
    ):
    schedule_id = str(ObjectId())
    workspaces.update_one(
        query_id(workspace_id),
        set_attr(
            attr_dict={f'entity_group.{entity_group_id}.task.{task_id}.schedule.{schedule_id}': schedule_obj.dict(exclude_unset=True)}
        )
    )


@router.patch("/{workspace_id}/entity-group/{entity_group_id}/entity/{task_id}/schedule/{schedule_id}")
async def _modify_task_schedule(
    schedule_obj: TaskSchedule,
    workspace_id: ObjectIdStr = Path(..., example=WORKSPACE_EX),
    entity_group_id: ObjectIdStr = Path(..., example=ENTITY_GROUP_ID),
    task_id: ObjectIdStr = Path(..., example=TASK_EX)
    ):
    schedule_id = str(ObjectId())
    workspaces.update_one(
        query_id(workspace_id),
        set_attr(
            attr_dict={f'entity_group.{entity_group_id}.task.{task_id}.schedule.{schedule_id}': schedule_obj.dict(exclude_unset=True)}
        )
    )

@router.post("/{workspace_id}/entity-group/{entity_group_id}/entity/{task_id}/schedule/{schedule_id}/override")
async def _add_task_override(
    override_list: List[ObjectIdStr],
    workspace_id: ObjectIdStr = Path(..., example=WORKSPACE_EX),
    entity_group_id: ObjectIdStr = Path(..., example=ENTITY_GROUP_ID),
    task_id: ObjectIdStr = Path(..., example=TASK_EX)
    ):
    schedule_id = str(ObjectId())
    workspaces.update_one(
        query_id(workspace_id),
        add_to(
            attr_dict={f'entity_group.{entity_group_id}.task.{task_id}.schedule.{schedule_id}.override': {'$addToSet': override_list.dict(exclude_unset=True)}}
        )
    )


@router.delete("/{workspace_id}/entity-group/{entity_group_id}/entity/{task_id}/schedule/{schedule_id}/override")
async def _delete_task_override(
    override_list: List[ObjectIdStr],
    workspace_id: ObjectIdStr = Path(..., example=WORKSPACE_EX),
    entity_group_id: ObjectIdStr = Path(..., example=ENTITY_GROUP_ID),
    task_id: ObjectIdStr = Path(..., example=TASK_EX)
    ):
    schedule_id = str(ObjectId())
    workspaces.update_one(
        query_id(workspace_id),
        pull_arr_ele(
            attr_dict={f'entity_group.{entity_group_id}.task.{task_id}.schedule.{schedule_id}.override': {'$pull': override_list.dict(exclude_unset=True)}}
        )
    )


