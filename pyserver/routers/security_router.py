from security import verify_otp, get_current_user, create_otp_secretkey, Token, login_access_token_fetch
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse
from pydantic_models.users import User
from pydantic_models.exceptions import DatabaseException
from fastapi import Depends, Query, APIRouter
from typing import Optional

from processors.accounts import create_otp_secret




router = APIRouter(
    # prefix="/server",
    tags=["security"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

@router.post("/token", response_model=Token)
async def token(form_data: OAuth2PasswordRequestForm = Depends()):
    return login_access_token_fetch(form_data)


#https://github.com/pyauth/pyotp
@router.get("/otp_protected")
async def _otp_protected(current_user: User = Depends(get_current_user), otp: Optional[int] = Query(None, ge=100000, le=999999)):
    secret = current_user.otp_hash
    print(current_user)
    if not verify_otp(secret, otp):
        return JSONResponse(status_code=401, content={"message": "Wrong OTP."})
    #PROCEED


@router.get("/otp")
async def _get_otp_secret(current_user: User = Depends(get_current_user)):
    otp_secret = create_otp_secretkey()
    if not create_otp_secret(current_user.id, otp_secret):
        raise DatabaseException(name='MongoDB')
    return {'otp_secret': otp_secret}

