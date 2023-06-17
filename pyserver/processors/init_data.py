from pydantic_models.users import User
from pydantic_models.universal import ObjectId, ObjectIdStr
from pydantic_models.rooms import ThreadData, ThreadRoom, ServerRoom, DmRoom, RoomTypesEnum
from pydantic_models.servers import Server
from pydantic_models.init_data import InitData, EnterServer_InitData, ServerData, ChannelData, RoomData, EnterWorkspaceData

from processors.mongo_update import servers, users, rooms, workspaces

from applications import generate_default_apps

from mongo_cons import query_ids, query_id, set_attr
from init_objects import emitter

from devtools import debug

def fetch_init_data(userdata: User):
    serverlist = []
    if userdata.statistics.joined_servers > 0:
        # return InitData(userdata = userdata)
        serverlist = list(servers.aggregate(
            [
                {'$match':{'_id': {"$in": list(map(lambda item: ObjectId(item), userdata.servers.keys()))}}},
                {'$project':{'name': True, 'icon': True, 'emoji': True}}
            ]
        ))
    if userdata.state.selected_view in ['friends', 'dm']:
        return InitData(
            **enter_dms(userdata),
            userdata = userdata,
            serverlist = serverlist,
            applist = generate_default_apps()
        )
    elif userdata.state.selected_view == 'workspace':
        return InitData(
            **enter_workspace( userdata.workspace.keys(), userdata.state.selected_workspace).dict(),
            userdata = userdata,
            serverlist = serverlist,
            applist = generate_default_apps()
        )
    return InitData(
        **enter_server_main(userdata.state.selected_server, userdata).dict(),
        userdata = userdata,
        serverlist = serverlist,
        applist = generate_default_apps()
    )


def enter_workspace(workspace_keys, selected_workspace):
            
    return EnterWorkspaceData(
        workspacedata = {selected_workspace: workspaces.find_one( query_id(selected_workspace))},
        workspacelist = list(
            workspaces.find(query_ids([ObjectId(item) for item in workspace_keys]),
            {'name': 1})
            )
    )


def enter_dms(userdata):
    '''
    1. Get friendlist (to show in second_panel)
    2. Get active friends (to show in third_panel) > pass
    3. If selected_dm is not 'friends_button', enter dm room.
    '''
    #1
    friendlist = list(users.find(
        query_ids([ObjectId(item) for k, v in userdata.relationships.dict().items() for item in v]),
        {'username': 1, 'avatar': 1, 'connection': '$state.connection'}
        ))
    #2
    #3

    emitter.enter_sio_room(userdata.id, list(userdata.dm_rooms.keys()))
    dmdata = {
        str(item['_id']): item for item in
        rooms.find(
        query_ids([ObjectId(item) for item in userdata.dm_rooms.keys()]),
        # {'name': 1, 'icon': 1}
        )}
    debug(friendlist, dmdata)
    # if userdata.state.selected_view == 'dm':
    #     pass
    return {
        'friendlist': friendlist,
        'roomdata': dmdata
    }
    

def enter_server_main(server_id: ObjectIdStr, userdata: User):
    users.update(query_id(userdata.id), set_attr(attr_dict=
        {
            'state.selected_server': server_id,
            'state.selected_channel': userdata.servers[server_id].selected_channel,
            'state.selected_room': userdata.servers[server_id].selected_room
        }))
    serverdata = enter_server(
        server_id,
        userdata.id
    )
    selected_channel_id = userdata.servers[server_id].selected_channel
    selected_room_id = userdata.servers[server_id].selected_room
    channeldata = enter_channel(
        serverdata.selected_serverdata.channels[selected_channel_id],
        serverdata.user_roles,
        serverdata.base_permissions,
        userdata.id
    )
    roomdata = enter_room(
        selected_room_id,
        serverdata.user_roles,
        channeldata.channel_permissions,
        userdata.id
    )
    return EnterServer_InitData.construct(
        serverdata = serverdata,
        channeldata = channeldata,
        roomdata = {selected_room_id: roomdata.selected_roomdata}
    )

def enter_server(selected_server: ObjectIdStr, user_id: ObjectIdStr) -> ServerData:
    '''
    0.  Create server entry of user (ServerMember)
    1.  Fetch server data.
    2.  Generate roomlist.
    3.  Compute base permissions.
    4.  Socket operations.
    5.  Return fetched data.
    '''
    #1
    selected_serverdata = Server(**servers.find_one(query_id(selected_server)))
    #3
    base_perms = selected_serverdata.settings.permissions
    try:
        user_roles = selected_serverdata.members[user_id].roles
        for role in user_roles:
            base_perms = base_perms | selected_serverdata.roles[role].permissions
    except KeyError:
        user_roles = None
    #4
    #new user in server
    #5
    return ServerData(
        selected_serverdata = selected_serverdata,
        base_permissions = base_perms,
        user_roles = user_roles,
    )

def enter_channel(selected_channeldata, user_roles, base_perms, id) -> ChannelData:
    '''
    1. Compute and return channel_permission.
    '''
    channel_perms = base_perms
    def inverter(num):
        return (1<<36) - 1 - num
    try:
        channel_perms &= inverter(selected_channeldata.permissions.deny)
    except:
        pass
    try:
        channel_perms |= selected_channeldata.permissions.allow
    except:
        pass
    for role in user_roles:
        try:
            channel_perms &= inverter(selected_channeldata.permissions_member.role.deny)
        except:
            pass
        try:
            channel_perms |= selected_channeldata.permissions_member.role.allow
        except:
            pass
    try:
        channel_perms &= inverter(selected_channeldata.permissions_member.id.deny)
    except:
        pass
    try:
        channel_perms |= selected_channeldata.permissions_member.id.allow
    except:
        pass
    return ChannelData(
        channel_permissions = channel_perms,
        name = selected_channeldata.name
    )


def enter_room(selected_room: ObjectIdStr, roles, channel_perms, id: ObjectIdStr) -> RoomData:
    '''
    1.  Fetch room data.
    2.  Socket operations.
    3.  Get channel overwrites.
    3.  Return fetched data.
    '''
    debug('enter_room')
    #1
    selected_roomdata = rooms.find_one(query_id(selected_room))
    if selected_roomdata['type'] == RoomTypesEnum.SERVER_ROOM:
        selected_roomdata = ServerRoom(**rooms.find_one(query_id(selected_room)))
    else:
        selected_roomdata = DmRoom(**rooms.find_one(query_id(selected_room)))
    #2
    try:
        emitter.enter_sio_room(id, selected_room)
    except KeyError:
        # offline case
        pass
    #3
    return  RoomData(
        selected_roomdata = selected_roomdata,
        # 'selected_room': str(selected_room),
        room_permissions = compute_room_permissions(selected_roomdata, roles, channel_perms, id)
    )

def compute_room_permissions(selected_roomdata, roles, channel_perms, id) -> int:
    room_perms = channel_perms
    def inverter(num):
        return (1<<36) - 1 - num
    try:
        room_perms &= inverter(selected_roomdata['permissions']['deny'])
    except:
        pass
    try:
        room_perms |= selected_roomdata['permissions']['allow']
    except:
        pass
    for role in roles:
        try:
            room_perms &= inverter(selected_roomdata['permissions_role'][role]['deny'])
        except:
            pass
        try:
            room_perms |= selected_roomdata['permissions_role'][role]['allow']
        except:
            pass
    try:
        room_perms &= inverter(selected_roomdata['permissions_member'][id]['deny'])
    except:
        pass
    try:
        room_perms |= selected_roomdata['permissions_member'][id]['allow']
    except:
        pass
    return room_perms
