from pydantic_models.universal import ObjectIdStr
from pydantic_models.accounts import RegistrationForm
from pydantic_models.users import UserState, User, UserStatistics
from mongo_cons import query_id, set_attr

from processors.mongo_update import users

def register_account(reg_form: RegistrationForm):
    user_obj = User(
        discriminator = 5,
        username = reg_form.username,
        password = reg_form.password_hash,
        email = reg_form.email,
        state = UserState(),
        statistics = UserStatistics()
    )
    users.insert_one(user_obj.dict())


def validate_email(user_id: ObjectIdStr):
    if users.update_one(query_id(user_id), set_attr('state.verified', True)).modified_count > 0:
        return True


def create_otp_secret(user_id, secret):
    if (users.update_one(query_id(user_id), set_attr('otp_hash', secret)).modified_count > 0):
        return True

