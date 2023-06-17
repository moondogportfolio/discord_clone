from fastapi import APIRouter, Path, Depends
from security import get_current_user
from typing import List, Dict
from mongo_cons import query_id, set_attr, remove_attr, query_ids, push_arr_ele

from pydantic_models.universal import ObjectIdStr, ObjectIdFactory
from pydantic_models.tasks import *
from pydantic_models.users import User, UserTask
from pydantic_models.update import UpdateObject, Operation

from processors.mongo_update import workspaces, users, data_update

from bson.objectid import ObjectId

from devtools import debug

router = APIRouter(
    prefix="/workspace",
    tags=["workspace_task"],
    # dependencies=[Depends(get_token_header)],
)

WORKSPACE_EX = '6129fe3bbef29db420a30ec3'
BOARD_EX = '6129fe58ffb50fb57a849a6f'
TASK_EX = '612c76009f5aed17aff0397e'
TASK_CYCLE_EX = '614618509c2fa43966e65cd7'


@router.post("/{workspace_id}/board/{board_id}/task")
async def _create_task(
    task: TaskIn,
    workspace_id: ObjectIdStr = Path(..., example=WORKSPACE_EX),
    board_id: ObjectIdStr = Path(..., example=BOARD_EX),
    current_user: User = Depends(get_current_user),
    ):
    task = task.dict(exclude_unset=True)
    task.update({
        'meta': TaskMeta.construct(
            creator=current_user.id
            ).dict(exclude_unset=True)
    })
    workspaces.update_one(
        query_id(workspace_id),
        set_attr(
            f'board.{board_id}.task.{ObjectIdFactory()}',
            task
        )
    )

@router.patch("/{workspace_id}/board/{board_id}/task/{task_id}")
async def _modify_task(
    task: TaskModify,
    task_old: TaskModify,
    workspace_id: ObjectIdStr = Path(..., example=WORKSPACE_EX),
    board_id: ObjectIdStr = Path(..., example=BOARD_EX),
    task_id: ObjectIdStr = Path(..., example=TASK_EX),
    current_user: User = Depends(get_current_user)
    ):
    update = {
        'set': {},
        'addToSet': {},
        'push': {}
    }
    for k,v in task.dict(exclude_unset=True).items():
        if k == 'involved':
            users.update_many(
                query_ids([item['entity'] for item in v]),
                set_attr(f'workspace.{workspace_id}.board.{board_id}.task.{task_id}', UserTask.construct().dict())
            )
        if k in ['group', 'involved', 'tag']:
            update['addToSet'][f'board.{board_id}.task.{task_id}.{k}'] = {'$each': v}
        else:
            update['set'][f'board.{board_id}.task.{task_id}.{k}'] = v
        
        update['push'][f'board.{board_id}.delta'] = BoardDelta.construct(
            operation= BoardDeltaOperationEnum.MODIFIED_TASK_VALUE,
            old_val= getattr(task_old, k),
            new_val= v,
            attribute=k,
            obj=BoardEntityEnum.TASK,
            obj_id=task_id
        ).dict(exclude_unset=True)
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
    
@router.post("/{workspace_id}/board/{board_id}/task/{task_id}/meta/cycle")
async def _add_task_cycle(
    cycle_obj: TaskCycle,
    workspace_id: ObjectIdStr = Path(..., example=WORKSPACE_EX),
    board_id: ObjectIdStr = Path(..., example=BOARD_EX),
    task_id: ObjectIdStr = Path(..., example=TASK_EX),
    ):
    cycle_id = str(ObjectId())
    workspaces.update_one(
        query_id(workspace_id),
        set_attr(
            attr_dict = {f'board.{board_id}.task.{task_id}.meta.cycles.{cycle_id}': cycle_obj.dict(exclude_unset=True)}
        )
    )


@router.post("/{workspace_id}/board/{board_id}/task/{task_id}/meta/cycles")
async def _set_task_cycles(
    cycle_obj: List[TaskCycle],
    workspace_id: ObjectIdStr = Path(..., example=WORKSPACE_EX),
    board_id: ObjectIdStr = Path(..., example=BOARD_EX),
    task_id: ObjectIdStr = Path(..., example=TASK_EX),
    ):
    cycle_obj = {str(ObjectId()):v.dict(exclude_unset=True) for v in cycle_obj}
    workspaces.update_one(
        query_id(workspace_id),
        set_attr(
            attr_dict = {f'board.{board_id}.task.{task_id}.meta.cycles': cycle_obj}
        )
    )
    
@router.post("/{workspace_id}/board/{board_id}/task/{task_id}/cycle-history/{cycle_id}")
async def _add_task_history_entry(
    cycle_obj: TaskCycleHistoryEntry,
    cycle_id: ObjectIdStr = Path(..., example=TASK_CYCLE_EX),
    workspace_id: ObjectIdStr = Path(..., example=WORKSPACE_EX),
    board_id: ObjectIdStr = Path(..., example=BOARD_EX),
    task_id: ObjectIdStr = Path(..., example=TASK_EX),
    ):
    debug(cycle_obj.dict())
    workspaces.update_one(
        query_id(workspace_id),
        push_arr_ele(
            f'board.{board_id}.task.{task_id}.meta.history.{cycle_id}.entries', cycle_obj.dict(exclude_unset=True)
        )
    )

    

@router.delete("/{workspace_id}/board/{board_id}/task/{task_id}")
async def _delete_task(
    workspace_id: ObjectIdStr = Path(..., example=WORKSPACE_EX),
    board_id: ObjectIdStr = Path(..., example=BOARD_EX),
    task_id: ObjectIdStr = Path(..., example=TASK_EX),
    ):
    workspaces.update_one(
        query_id(workspace_id),
        remove_attr(
            attr_dict = {f'board.{board_id}.task.{task_id}': ""}
        )
    )



@router.get("/user/tasks")
async def _get_tasks(
    current_user: User = Depends(get_current_user)
    ):
    workspace = current_user.workspaces
    filter = {}
    query = []
    for workspace_id, v in workspace.items():
        query.append(ObjectId(workspace_id))
        for board_id, v2 in v.boards.items():
            for task_id in v2.tasks.keys():
                filter.update({f'board.{board_id}.task.{task_id}': True})
    result = workspaces.find(
        query_ids(query),
        filter
    )
    debug([{str(item.pop('_id')): item} for item in result])
