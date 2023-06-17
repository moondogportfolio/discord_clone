from devtools import debug
from pymongo import collection

from pydantic_models.universal import ObjectIdStr
from pydantic_models.update import UpdateObject, BulkUpdateObject, Operation
from pydantic_models.users import UserIn

from mongo_cons import query_id, set_attr    

from processors.mongo_update import data_update, users
from processors.file import upload_file

from io import BytesIO



def get_user(user_id: ObjectIdStr):
    return users.find_one(query_id(user_id))


async def modify_user(user_id: ObjectIdStr, user_obj: UserIn):
    
    
    user_obj = user_obj.dict(exclude_unset=True)
    user_obj.update(
            {f'state.{k}':v for k,v in user_obj['state'].items()}
        )
    user_obj.pop('state')
    debug(user_obj)
    await data_update(
       UpdateObject.construct(
            filter = query_id(user_id),
            attr_val = user_obj,
            collection = 'users'
            )
        )
    # avatar_id  = upload_file(avatar)
    # print(type(avatar_id))
    # attr_dict = {
    #     'username': username,
    #     'avatar': avatar_id
    # }
    # # if users.update_one(query_id(user_id), set_attr(attr_dict = attr_dict)).modified_count > 0:
    # #     return True


async def add_relationship(initiator_id, target_id):
    debug('enter')
    op1 = UpdateObject.construct(
        filter = query_id(initiator_id),
        attr_val = {'relationships.pending_outgoing': target_id},
        operation = 'push'
        )
    op2 = UpdateObject.construct(
        filter = query_id(target_id),
        attr_val = {'relationships.pending_incoming': initiator_id},
        operation = 'push'
        )
    results = await data_update(BulkUpdateObject.construct(
        collection = 'users',
        update_items = [op1, op2])
        )
    debug(results)


async def confirm_relationship(initiator_id, target_id):
    op1 = UpdateObject.construct(
        filter = query_id(initiator_id),
        operation_list = [
            Operation.construct(
                attr_val = {'relationships.friend': target_id},
                operation = 'push'
            ),
            Operation.construct(
                attr_val = {'relationships.pending_incoming': target_id},
                operation = 'pull'
            )
        ]
        )

    op2 = UpdateObject.construct(
        filter = query_id(target_id),
        operation_list = [
            Operation.construct(
                attr_val = {'relationships.friend': initiator_id},
                operation = 'push'
            ),
            Operation.construct(
                attr_val = {'relationships.pending_outgoing': initiator_id},
                operation = 'pull'
            )
        ]
        )
    await data_update(BulkUpdateObject.construct(
        collection = 'users',
        update_items = [op1, op2])
        )


def deny_relationship(initiator_id, target_id):
    op1 = UpdateObject.construct(
        filter = query_id(initiator_id),
        attr_val = {'relationships.pending_outgoing': target_id},
        operation = 'pull'
        )
    op2 = UpdateObject.construct(
        filter = query_id(target_id),
        attr_val = {'relationships.pending_incoming': initiator_id},
        operation = 'pull'
        )
    data_update(BulkUpdateObject.construct(
        collection = 'users',
        update_items = [op1, op2])
        )

