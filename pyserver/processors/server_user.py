from pymongo.collection import ReturnDocument
from processors.mongo_update import servers, users
from pydantic_models.servers import UserServerPartial
from pydantic_models.users import UserSelectedState
from mongo_cons import query_id, set_attr, inc_attr, remove_attr

def add_server_member(server_id, user_id, invite_id=None):
    '''
    1.  Find user.
    2.  Update server.members.{user_id}
    3.  Update user.servers.{server_id}
    '''
    #1
    user = users.find_one(query_id(user_id),
        {'connection': '$state.connection',
        'activity': '$state.activity'}
        )
    #2
    query = query_id(server_id)
    query.update({f'members.{user_id}':{'$exists': False}})
    update = set_attr(f'members.{user_id}', UserServerPartial.construct(**user).dict())
    if invite_id: update.update(inc_attr(f'invites.{invite_id}.uses', 1))
    server_obj = servers.find_one_and_update(
        query,
        update,
        return_document = ReturnDocument.AFTER,
        projection={'default_room': 1, 'default_channel': 1,'_id':0}
    )
    #3
    query = set_attr(f'servers.{server_id}',
        UserSelectedState.construct(
            selected_room= server_obj['default_room'],
            selected_channel = server_obj['default_channel']
        ).dict()
        )
    query.update(inc_attr('statistics.joined_servers', 1))
    if server_obj:
        users.update_one(
            query_id(user_id),
            query
        )

def delete_server_member(server_id, user_id):
    result1 = servers.update_one(
        query_id(server_id),
        remove_attr(f'members.{user_id}', '')
    ).modified_count
    if result1 > 0:
        users.update_one(
            query_id(user_id),
            remove_attr(f'servers.{server_id}', '')
        )
