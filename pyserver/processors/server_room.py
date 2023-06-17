from bson.objectid import ObjectId
from pydantic_models.universal import ObjectIdStr
from pydantic_models.update import UpdateObject
from pydantic_models.rooms import ServerRoom
from pydantic_models.servers import RoomChannelPartial, Channel
from processors.mongo_update import rooms, data_update, servers
from processors.room import delete_room

from mongo_cons import query_id, set_attr

def get_server_room(room_id: ObjectIdStr):
    return rooms.find_one(query_id(room_id))



def get_list_of_server_rooms(server_id):
    '''
    TODO
    '''
    result = rooms.find({'server': server_id})
    if result:
        return list(result)
    return result



def delete_server_room(room_id: ObjectIdStr):
    result = delete_room(room_id)
    return result

async def create_server_channel(server_id: ObjectIdStr, name: str):
    await data_update(UpdateObject.construct(
        filter = query_id(server_id),
        collection = 'servers',
        attr_val = {
            f'channels.{str(ObjectId())}': Channel(name = name).dict()
        },
        operation = 'set'),
        'SERVER_CHANNEL_CREATED'
    )

def create_server_room(server_id: ObjectIdStr, channel_id: ObjectIdStr, name: str):
    new_server_room_obj = ServerRoom(
        name = name,
        server = server_id,
        channel = channel_id
        )
    new_room_id = rooms.insert_one(
        new_server_room_obj.dict(),
        ).inserted_id
    new_room_id = str(new_room_id)
    if new_room_id:
        servers.update_one(
            query_id(server_id),
            set_attr(
                f'channels.{channel_id}.rooms.{new_room_id}',
                RoomChannelPartial.construct(
                    position= 'TODO',
                    name= name
                ).dict()
            ))
    return new_room_id
    # data_update(UpdateObject.construct(
    #     filter = query_id(server_id),
    #     collection = 'servers',
    #     attr_val = {
    #         f'channels.{channel_id}.rooms.{new_room_id}':
    #         RoomChannelPartial.construct(position= 69, name= name).dict()
    #     },
    #     operation = 'set'),
    #     'SERVER_ROOM_CREATED',
    #     announce= False
    # )
    # return new_room_id