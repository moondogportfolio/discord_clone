from pydantic_models.resource import *
from fastapi import APIRouter, Path, Depends
from security import get_current_user
from typing import List, Dict
from mongo_cons import query_id, set_attr, remove_attr, query_ids

from pydantic_models.universal import ObjectIdStr
from pydantic_models.resource import Resource
from processors.mongo_update import workspaces, users, data_update

from bson.objectid import ObjectId

from devtools import debug

router = APIRouter(
    prefix="/workspace",
    tags=["workspace_resource"],
    # dependencies=[Depends(get_token_header)],
)

WORKSPACE_EX = '6129fe3bbef29db420a30ec3'
BOARD_EX = '6129fe58ffb50fb57a849a6f'
TASK_EX = '612c76009f5aed17aff0397e'
RESOURCE_EX = '613fab0a367cddaa1b9130fd'
RESOURCE_CONT_EXT = '613fa6d37cd534aec98d0a59'
MEMBER_EX = '61355552389a7e7a1d45dec7'



@router.post("/{workspace_id}/resource_container", response_model=ObjectIdStr)
async def _create_workspace_resource_cont(
    workspace_id: ObjectIdStr = Path(..., example=WORKSPACE_EX)
    ):
    resource_id = str(ObjectId())
    workspaces.update_one(
        query_id(workspace_id),
        set_attr(
            attr_dict={f'resource_container.{resource_id}': {'task': {}, 'resource': {}, 'entity': {}}}
        )
    )

@router.post("/{workspace_id}/resource_container/{container_id}/task/{task_id}", response_model=ObjectIdStr)
async def _create_task_alloc(
    alloc_obj: Allocation,
    container_id: ObjectIdStr = Path(..., example=RESOURCE_CONT_EXT),
    task_id: ObjectIdStr = Path(..., example=TASK_EX),
    workspace_id: ObjectIdStr = Path(..., example=WORKSPACE_EX)
    ):
    allocation_id = str(ObjectId())
    workspaces.update_one(
        query_id(workspace_id),
        set_attr(
            attr_dict={f'resource_container.{container_id}.task.{task_id}.{allocation_id}':
            alloc_obj.dict(exclude_unset=True)}
        )
    )


@router.post("/{workspace_id}/resource_container/{container_id}/resource/{resource_id}", response_model=ObjectIdStr)
async def _create_resource_in_cont(
    resource_obj: ResourceDetails,
    container_id: ObjectIdStr = Path(..., example=RESOURCE_CONT_EXT),
    resource_id: ObjectIdStr = Path(..., example=RESOURCE_EX),
    workspace_id: ObjectIdStr = Path(..., example=WORKSPACE_EX)
    ):
    workspaces.update_one(
        query_id(workspace_id),
        set_attr(
            attr_dict={f'resource_container.{container_id}.resource.{resource_id}':
            resource_obj.dict(exclude_unset=True)}
        )
    )
@router.post("/{workspace_id}/resource_container/{container_id}/entity/{entity_id}", response_model=ObjectIdStr)
async def _create_floating_alloc(
    floating_alloc_obj: FloatingAllocation,
    container_id: ObjectIdStr = Path(..., example=RESOURCE_CONT_EXT),
    entity_id: ObjectIdStr = Path(..., example=MEMBER_EX),
    workspace_id: ObjectIdStr = Path(..., example=WORKSPACE_EX)
    ):
    workspaces.update_one(
        query_id(workspace_id),
        set_attr(
            attr_dict={f'resource_container.{container_id}.entity.{entity_id}':
            floating_alloc_obj.dict(exclude_unset=True)}
        )
    )


@router.post("/{workspace_id}/resource", response_model=ObjectIdStr)
async def _create_workspace_resource(
    resource_obj: Resource,
    workspace_id: ObjectIdStr = Path(..., example=WORKSPACE_EX)
    ):
    resource_id = str(ObjectId())
    workspaces.update_one(
        query_id(workspace_id),
        set_attr(
            attr_dict={f'resource.{resource_id}': resource_obj.dict(exclude_none=True)}
        )
    )
    return resource_id

@router.patch("/{workspace_id}/resource")
async def _modify_workspace_resource(
    resource_obj: Resource,
    workspace_id: ObjectIdStr = Path(..., example=WORKSPACE_EX)
    ):
    workspaces.update_one(
        query_id(workspace_id),
        set_attr(
            attr_dict={f'resource.{k}':v for k,v in resource_obj.dict(exclude_none=True).items()}
        )
    )


@router.post("/{workspace_id}/resource/{resource_id}/allocation/{entity_id}")
async def _create_allocation(
    alloc_obj: Allocation,
    entity_id: ObjectIdStr = Path(..., example=MEMBER_EX),
    resource_id: ObjectIdStr = Path(..., example=RESOURCE_EX),
    workspace_id: ObjectIdStr = Path(..., example=WORKSPACE_EX)
    ):
    workspaces.update_one(
        query_id(workspace_id),
        set_attr(
            attr_dict={f'resource.{resource_id}.allocation.{entity_id}': alloc_obj.dict(exclude_none=True)}
        )
    )

