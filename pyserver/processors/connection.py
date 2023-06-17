from processors.mongo_update import users, data_update
from pydantic_models.update import UpdateObject
from pydantic_models.universal import ObjectIdStr
from pydantic_models.users import User


from socketio.exceptions import ConnectionRefusedError

from mongo_cons import query_id, query_ids

from init_objects import sio, session

from devtools import debug

from security import get_current_user

async def modify_user_connection(user_id: ObjectIdStr, connection,  user_obj: User = None):
    await data_update(
        UpdateObject(
            collection = 'users',
            filter = query_id(user_id),
            attr_val = {'state.connection': connection}),
        announce = False
        )

    # TODO, CACHE
    subscribers = users.find_one(
        query_id(user_id),
        {'servers': 1, '_id': 0}
    )
    subscribers = list(subscribers['servers'].keys())

    await data_update(
        UpdateObject(
            collection = 'servers',
            filter = query_ids(subscribers),
            attr_val = {f'members.{user_id}.connection': connection}),
        'MEMBER_PRESENCE_DELTA',
        subscribers = subscribers


    )



@sio.event
async def connect(sid, environ, auth=None):
    debug('SOCKET ATTEMPT CONNECTION.')
    if auth['token']:
        try:
            user = await get_current_user(auth['token'].replace('Bearer ', ''))
            session.add_user(sid, user.id)
            [sio.enter_room(sid, server) for server in user.servers.keys()]
            debug(sio.manager.get_rooms(sid, namespace='/'))
            await sio.emit('socket_init', sid)
            debug(session.get_state())
        except Exception as e:
            debug(e)
            raise ConnectionRefusedError('Authentication failed.')
    else:
        raise ConnectionRefusedError('Authentication failed.') 
        

    # debug('connect ', sid, auth, environ)
    # heartbeat_interval = {
    #     'heartbeat_interval': 1000
    # }
    # await sio.emit('SERVER_HELLO', heartbeat_interval, to=sid)
    # print('DONE')

@sio.event
async def disconnect(sid):
    debug(f'SOCKET DISCONNECT {sid}, {session.get_user_id(sid)}')
    await modify_user_connection(session.get_user_id(sid), 'offline')
    session.remove_user(sid)
    debug(session.get_state())
