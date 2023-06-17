from pydantic_models.rooms import DmRoomIn, UserPartialDmRoom, DmRoom
from pydantic_models.universal import ObjectIdStr
from pydantic_models.update import UpdateObject
from pydantic_models.users import DmRoomUserState

from processors.mongo_update import users, rooms, data_update

from mongo_cons import query_ids, query_id, set_attr

async def create_dm_room(dmroom_in: DmRoomIn, owner_id: ObjectIdStr):
    '''
    1.  Create room object and update database.
    2.  Update each participant.
    3.  Return updated data.
    '''
    #1
    participants = users.find(
        query_ids(dmroom_in.participants),
        {
            'username': 1,
            'connection': '$state.connection',
            'activity': '$state.activity',
            'icon': 1,
        },
        )
    participants = [
        UserPartialDmRoom.construct(
            participant,
            id = str(participant['_id']),
            nick = participant['username']
        )
        for participant in participants
    ]
    create_result = rooms.insert_one(
        DmRoom(
            name = dmroom_in.name,
            participants = participants,
            owner_id = owner_id
            ).dict()
        )
    await data_update(
        UpdateObject.construct(
        filter = query_ids(dmroom_in.participants),
        collection = 'users',
        mongo_ops = 'update_many',
        attr_val = {
            f'dm_rooms.{str(create_result.inserted_id)}':  DmRoomUserState.construct().dict()
        }
    )
    )
    return str(create_result.inserted_id)


def get_dm_room(dm_room_id: ObjectIdStr):
    '''
    1.  Fetch db data and return.
    '''
    #1
    return rooms.find_one(query_id(dm_room_id))


async def delete_dm_room(requesting_id: ObjectIdStr, dm_room_id: ObjectIdStr, method: str, reasons: str = None):
    '''
    1.  Attempt deleting room.
    2.  Attempt unlinking room from User 'dm_rooms' attr.
    3.  Log.
    4.  Return result.
    Behavior:
    Room database entry is not deleted. 
    '''
    #1
    if method == 'obliterate':
        result = rooms.find_one_and_delete(query_id(dm_room_id))
        deleted_room = DmRoom.construct(**result)
        if not result:
            return
        await data_update(
            UpdateObject.construct(
                filter = query_ids(map(lambda x: x['id'], deleted_room.participants)),
                attr_val = {'dm_rooms': dm_room_id},
                operation = 'pull',
                collection = 'users',
                mongo_ops = 'update_many'
            ),
            announce=False
            )
        # if result < 1:
        #     changes = AuditLogChange(
        #         new_val = None,
        #         old_val= dm_room_id,
        #         key = 'rooms')
        #     entry = AuditLogEntry(
        #         id = str(ObjectId()),
        #         actuator_id = user_id,
        #         target_id = None,
        #         changes = changes,
        #         action_type = AuditEnumEvents.ROOM_DELETE.value,
        #         options = {
        #             'members_removed': user_id
        #         },
        #         reasons = reasons
        #     )
        #     #3
        #     audit_log.insert_one(entry.dict())
        #     #4
        #     return 'No such room.'
        # else:
        #     return True
    #2
    if method == 'unlink':
        await data_update(
            UpdateObject.construct(
                filter = query_id(requesting_id),
                attr_val = {'dm_rooms': dm_room_id},
                operation = 'pull',
                collection = 'users'
            ),
            announce=False
            )
        

def modify_dm_room(dm_room_id, icon, name):
    if icon:
        rooms.update_one(query_id(dm_room_id), set_attr('icon', icon))
    if name:
        rooms.update_one(query_id(dm_room_id), set_attr('name', name))
