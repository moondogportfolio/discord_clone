from bson.objectid import ObjectId
from devtools import debug

from mongo_cons import query_id, set_attr

from processors.mongo_update import servers, users, data_update
from processors.server_room import create_server_room
from processors.server_user import add_server_member


from pydantic_models.universal import ObjectIdStr
from pydantic_models.server_in import ServerIn, BaseServerRoom
from pydantic_models.servers import RoomChannelPartial, Server, ServerMemberIn, Emoji, ServerDiscoveryPartial, Role
from pydantic_models.files import GraphicsDescriptionIn

def create_server(server_obj: ServerIn, icon: ObjectIdStr, owner_id: ObjectIdStr):
        rooms = []
        server_id = ObjectId()
        def create_room(room: BaseServerRoom, channel_id, index):
            room_id = create_server_room(
                server_id = str(server_id),
                channel_id = channel_id,
                name = room.name
                )
            rooms.append(room_id)
            return room_id, RoomChannelPartial(position=index,name=room.name)            
        channels = {
            channel.id: {
                'rooms': dict([create_room(room, channel.id, index) for index, room in enumerate(channel.rooms)]),
                'name': channel.name
                }
            for channel in server_obj.channels
            }
        server_obj = Server(
            name = server_obj.name,
            channels = channels,
            owner_id = owner_id,
            default_room = next(iter(channels[next(iter(channels))]['rooms'])),
            default_channel = next(iter(channels))
            )
        server_obj = server_obj.dict(exclude={'id'})
        server_obj.update({'_id': server_id})
        servers.insert_one(server_obj)
        add_server_member(server_id, owner_id)
        return server_obj

    

def delete_server(server_id: ObjectIdStr) -> int:
    return servers.delete_one(query_id(server_id)).deleted_count


def get_server(server_id):
    return servers.find_one(query_id(server_id))


    
def server_modify_member(server_id, member_id, member_obj: ServerMemberIn):
    mongo_ops = {'$set': {}, '$push': {}, '$pull': {}}
    for k, v in member_obj.dict(exclude_none=True).items():
        if type(v) is list:
            for v1 in v:
                try:
                    mongo_ops['$push'].update({f'members.{member_id}.{k}': {'$each': v1['add']}})
                except:
                    pass
                try:
                    mongo_ops['$pull'].update({k: {'$each': v1['remove']}})
                except:
                    pass
        else:
            mongo_ops['$set'].update({f'members.{member_id}.{k}':v })
    debug(mongo_ops)
    return servers.update_one(query_id(server_id),mongo_ops).modified_count


def add_server_emoji(server_id: ObjectIdStr, name: str, emoji_file: GraphicsDescriptionIn):
    result = servers.update_one(
        query_id(server_id),
        set_attr(
            f'emoji.{str(ObjectId())}',
            Emoji.construct(name=name, file = emoji_file).dict()
            )
        )
    debug(result.raw_result)

def edit_server_icon(server_id: ObjectIdStr, icon_file: GraphicsDescriptionIn):
    debug(server_id)
    result = servers.update_one(
        query_id(server_id),
        set_attr('icon', icon_file.dict())
        )
    debug(result.raw_result)
    
def edit_user_icon(user_id, icon_file: GraphicsDescriptionIn):
    result = users.update_one(
        query_id(user_id),
        set_attr('icon', icon_file.dict())
        )
    debug(result.raw_result)



def discover_servers():
    return [ServerDiscoveryPartial(**x) for x in servers.find(
        projection={
        'id': 1,
        'name': 1,
        'description': 1,
        'icon': 1,
        'splash': 1
        }
    )]


def create_server_role(server_id):
    role = Role()
    data_update(
        'servers',
        query_id(server_id),
        f'roles.{str(ObjectId())}',
        role.dict(),
        operation='set'
    )
    return role


