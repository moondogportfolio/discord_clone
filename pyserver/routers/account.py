from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from pydantic_models.users import User

from processors.accounts import *

from security import get_current_user, get_password_hash

router = APIRouter(
    # prefix="/server",
    tags=["account_management"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

@router.post("/register")
async def _register_account(reg_form: RegistrationForm):
    # email = False
    # if email:
    #     # to = RegistrationForm.email
    #     to = 'mccndcg@gmail.com'
    #     subject = 'Account registration.'
    #     body = 'Click me.'
    #     html = '127.0.0.1/8000/OK'
    #     yag.send(to = to, subject = subject, contents = [body, html])
    reg_form.password_hash = get_password_hash(reg_form.password)
    register_account(reg_form)


@router.get("/register/{email_code}")
async def _validate_email(email_code, current_user: User = Depends(get_current_user)):
    if (email_code == 'OK'
        and not current_user.state.verified
        and validate_email(current_user.id)
        ):
        return {'response': 'EMAIL VALIDATED'}
    else:
        return JSONResponse(status_code=406, content='EMAIL VALIDATION UNSUCCESSFUL.')
    
