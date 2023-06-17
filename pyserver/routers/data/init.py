from fastapi import APIRouter, Depends
from security import get_current_user
from pydantic_models.users import User
from pydantic_models.init_data import InitData

from processors.init_data import fetch_init_data
from processors.connection import modify_user_connection


router = APIRouter(
    # prefix="/server",
    tags=["data"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)



@router.get("/init_data", response_model=InitData, tags=["user"], response_model_exclude_none=True)
async def read_users_me(current_user: User = Depends(get_current_user)):
    await modify_user_connection(current_user.id, 'online')
    init_data = fetch_init_data(current_user)
    return init_data

