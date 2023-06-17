from fastapi import APIRouter, Path, Depends
from security import get_current_user
from typing import List, Dict
from mongo_cons import query_id, set_attr, remove_attr, query_ids

from pydantic_models.universal import ObjectIdStr, ObjectIdFactory
from pydantic_models.tasks import *
from pydantic_models.users import User, UserTask, UserWorkspace
from pydantic_models.update import UpdateObject, Operation
from pydantic_models.resource import Transaction
from pydantic_models.organization import EntityGroup

from processors.mongo_update import workspaces, users, data_update

from bson.objectid import ObjectId

from devtools import debug

router = APIRouter(
    prefix="/workspace",
    tags=["workspace"],
    # dependencies=[Depends(get_token_header)],
)

WORKSPACE_EX = '6129fe3bbef29db420a30ec3'
BOARD_EX = '6129fe58ffb50fb57a849a6f'
TASK_EX = '612c76009f5aed17aff0397e'

@router.post("")
async def _create_workspace(
    workspace: WorkspaceIn,
    current_user: User = Depends(get_current_user),
    ):
    inserted_id = workspaces.insert_one(workspace.dict()).inserted_id
    users.update_one(
        query_id(current_user.id),
        set_attr(f'workspaces.{str(inserted_id)}', {})
        )

@router.get("/{workspace_id}",
        response_model=Workspace
)
async def _get_workspace(
    workspace_id: ObjectIdStr = Path(..., example=WORKSPACE_EX)
):
    return workspaces.find_one(query_id(workspace_id))



@router.post("/{workspace_id}/field")
async def _create_workspace_field(
    workspace_field: WorkspaceFields,
    workspace_id: ObjectIdStr = Path(..., example=WORKSPACE_EX)
    ):
    debug(workspace_field)
    workspaces.update_one(
        query_id(workspace_id),
        set_attr(
            attr_dict={f'field.{k}':v for k,v in workspace_field.dict(exclude_none=True).items()}
        )
    )


@router.post("/{workspace_id}/member")
async def _create_workspace_member(
    member_obj: MemberIn,
    workspace_id: ObjectIdStr = Path(..., example=WORKSPACE_EX)
    ):
    workspaces.update_one(
        query_id(workspace_id),
        set_attr(
            attr_dict={f'member.{str(ObjectId())}': member_obj.dict(exclude_none=True)}
        )
    )

@router.patch("/{workspace_id}/member/{member_id}")
async def _modify_workspace_member(
    member_obj: MemberIn,
    member_id: ObjectIdStr,
    workspace_id: ObjectIdStr = Path(..., example=WORKSPACE_EX)
    ):
    update = {
        'set': {},
        'addToSet': {}
    }
    for k,v in member_obj.dict(exclude_unset=True).items():
        if type(v) == list:
            update['addToSet'][f'member.{member_id}.{k}'] = {'$each': v}
        else:
            update['set'][f'member.{member_id}.{k}'] = v
    debug(update)
    await data_update(
       UpdateObject.construct(
            filter = query_id(workspace_id),
            collection = 'workspaces',
            operation_list = [Operation(
                attr_val = v,
                operation = k
            ) for k,v in update.items()]
            ),
        announce=False    
    )


@router.patch("/{workspace_id}/field/{field_name}")
async def _modify_workspace_field(
    field_name: str,
    field_obj: Dict,
    workspace_id: ObjectIdStr = Path(..., example=WORKSPACE_EX)
    ):
    field_dict = {
        'status': StatusField.construct,
        'group': GroupField.construct,
        'granularity': GranularityField.construct,
        'involved': InvolvedField.construct,
        'tag': TagField.construct,
		}
    field_obj = field_dict[field_name](**field_obj)
    await data_update(
       UpdateObject.construct(
            filter = query_id(workspace_id),
            collection = 'workspaces',
            attr_val = {f'field.{field_name}.{k}':v for k,v in field_obj.dict(exclude_unset=True).items() if type(v)!=list}
            ),
        announce=False    
    )

@router.patch("/{workspace_id}/field/{field_name}/{field_attribute}")
async def _modify_workspace_field(
    field_name: str,
    field_attribute: str,
    field_attr_obj: Union[list, str],
    operation: str,
    workspace_id: ObjectIdStr = Path(..., example=WORKSPACE_EX)
    ):
    debug(field_attr_obj)
    if(type(field_attr_obj)==list):
        field_attr_obj = {'$each': field_attr_obj} if operation == 'addToSet' else {'$in': field_attr_obj}
    await data_update(
       UpdateObject.construct(
            filter = query_id(workspace_id),
            collection = 'workspaces',
            attr_val = {f'field.{field_name}.{field_attribute}': field_attr_obj},
            operation = operation
            ),
        announce=False    
    )

@router.post("/{workspace_id}/board")
async def _create_board(
    board: BoardIn,
    workspace_id: ObjectIdStr = Path(..., example=WORKSPACE_EX)
    ):
    workspaces.update_one(
        query_id(workspace_id),
        set_attr(
            f'board.{ObjectIdFactory()}',
            board.dict()
        )
        )

@router.post("/{workspace_id}/transaction", response_model=ObjectIdStr)
async def _create_workspace_tx(
    tx_obj: Transaction,
    workspace_id: ObjectIdStr = Path(..., example=WORKSPACE_EX)
    ):
    tx_id = str(ObjectId())
    workspaces.update_one(
        query_id(workspace_id),
        set_attr(
            attr_dict={f'transaction.{tx_id}': tx_obj.dict(exclude_none=True)}
        )
    )
    return tx_id

@router.post("/{workspace_id}/transaction", response_model=ObjectIdStr)
async def _create_workspace_tx(
    tx_obj: Transaction,
    workspace_id: ObjectIdStr = Path(..., example=WORKSPACE_EX)
    ):
    tx_id = str(ObjectId())
    workspaces.update_one(
        query_id(workspace_id),
        set_attr(
            attr_dict={f'transaction.{tx_id}': tx_obj.dict(exclude_none=True)}
        )
    )
    return tx_id


@router.post("/{workspace_id}/group", response_model=ObjectIdStr)
async def _create_workspace_group(
    group_obj: EntityGroup,
    workspace_id: ObjectIdStr = Path(..., example=WORKSPACE_EX)
    ):
    group_id = str(ObjectId())
    workspaces.update_one(
        query_id(workspace_id),
        set_attr(
            attr_dict={f'group.{group_id}': group_obj.dict(exclude_none=True)}
        )
    )
    return group_id

'''
possible sideeffect of deleting field:
    task has values for nonexisting field
resolution:
    upon removal of field, update tasks as well
'''


'''
update subscribers
'''