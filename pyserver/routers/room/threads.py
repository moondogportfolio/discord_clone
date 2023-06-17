from fastapi import APIRouter, Depends
from fastapi.param_functions import Path
from pydantic_models.universal import ObjectIdStr
from pydantic_models.rooms import ThreadRoomIn, ThreadRoom
from pydantic_models.users import User
from security import get_current_user

from processors.threads import *
from devtools import debug


THREAD_EX = '611e3254ec337b6f27450b19'

router = APIRouter(
    prefix="/thread",
    tags=["threads"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)



@router.post("",
        response_model=ThreadData
        )
async def _create_thread(
    thread_in: ThreadRoomIn,
    current_user: User = Depends(get_current_user)
    ):
    '''
    Create thread.
    '''
    return create_thread(thread_in, current_user.id)


@router.get("/{thread_id}",
        response_model=ThreadData
        )
async def _get_thread(
    thread_id: ObjectIdStr = Path(..., example=THREAD_EX),
    current_user: User = Depends(get_current_user)
    ):
    '''
    Get thread.
    '''
    return enter_thread(thread_id, current_user.id)


# @router.put("/{thread_id}/member/@me")
# async def _add_thread_member_self(
#     thread_id: ObjectIdStr
#     ):
#     '''
#     Add self to thread members.
#     '''


# @router.put("/{thread_id}/member/{user_id}")
# async def _add_thread_member(
#     thread_id: ObjectIdStr,
#     user_id: ObjectIdStr,
#     ):
#     '''
#     Add user to thread members.
#     '''



# @router.delete("/{thread_id}/member/@me")
# async def _delete_thread_member_self(
#     thread_id: ObjectIdStr
#     ):
#     '''
#     Remove self from thread members.
#     '''


# @router.delete("/{thread_id}/member/{user_id}")
# async def _delete_thread_member(
#     thread_id: ObjectIdStr,
#     user_id: ObjectIdStr,
#     ):
#     '''
#     Remove user from thread members.
#     '''

