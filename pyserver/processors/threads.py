from pydantic_models.rooms import ThreadRoomIn, ThreadRoom, ThreadData, ThreadMember
from mongo_cons import query_id, set_attr
from pydantic_models.universal import ObjectIdStr
from init_objects import emitter
from processors.mongo_update import rooms
from devtools import debug




def enter_thread(thread_id: ObjectIdStr, current_user: ObjectIdStr) -> ThreadData:
    '''
    1.  Fetch room data.
    2.  Socket operations.
    3.  Get channel overwrites.
    3.  Return fetched data.
    '''
    #1
    selected_threaddata = ThreadRoom.construct(**rooms.find_one(query_id(thread_id)))
    #2
    try:
        emitter.enter_sio_room(current_user, thread_id)
    except KeyError:
        # offline case
        pass
    #3
    return ThreadData.construct(
        selected_threaddata = selected_threaddata
        )


def create_thread(thread_in: ThreadRoomIn, user_id):
    thread_out = ThreadRoom.construct(
        **thread_in.dict(),
        owner_id = user_id,
        members = {user_id: ThreadMember.construct()}
        )
    thread_id = rooms.insert_one(thread_out.dict(exclude_none=True)).inserted_id
    thread_out.id = thread_id
    rooms.update_one(
        query_id(thread_in.room),
        set_attr(f'posts.{thread_in.init_post}.thread', str(thread_id))
    )
    return thread_out