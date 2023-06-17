# from io import BytesIO
# from typing import Any, List, Tuple, Dict

# from bson.objectid import ObjectId
# from devtools import debug
# from fastapi import HTTPException, status
# from pydantic.utils import Obj
# from pymongo.collection import ReturnDocument
# from pymongo.operations import DeleteOne, InsertOne, UpdateOne

# from datetime import timedelta

# from models import *
# from models_enum import *
# from mongo_cons import *
# from search import audit_log, rooms, servers, users, files
# from applications import generate_default_apps

# from PIL import Image
# from io import BytesIO
# import base64

# from emitter import Emitter

# from dotty_dict import dotty



# class Operation(BaseModel):
#     attr_val: Optional[Dict] = None
#     operation: Optional[str] = 'set'

# class UpdateObject(Operation):
#     filter: Dict
#     operation_list: Optional[List[Operation]] = None
#     collection: str
#     mongo_ops: str = 'update'
#     upsert: bool = False
#     array_filters: List = None



# class BulkUpdateObject(BaseModel):
#     collection: str
#     update_items: List[UpdateObject]


# emitter = Emitter

# async def data_update(update_object, sio_event = None, announce = True, subscribers = None):
#     def get_ops(operation, attr_val, operation_list: list[Operation] = None):
#         if operation_list:
#             return {f"${item.operation}": item.attr_val for item in operation_list}
#         return {f'${operation}': attr_val}

#     def get_data(collection, data, operation, event):
#         return_data = {'operation': operation, 'event': event, 'data': None}
#         dotty_data = dotty()
#         for k, v in data.items():
#             dotty_data[k] = v
#         data = dotty_data.to_dict()
#         if collection == 'users':
#             return_data['data'] = {'userdata': data}
#         if collection == 'servers':
#             return_data['data'] = {'serverdata': {'selected_serverdata': data}}
#         if collection == 'rooms':
#             return_data['data'] = {'roomdata': {'selected_roomdata': data}}
#         return return_data

#     collection_dict = {
#         'users': users,
#         'servers': servers,
#         'rooms': rooms
#     }

#     mongo_ops_dict = {
#         'insert': InsertOne,
#         'update': UpdateOne,
#         'delete': DeleteOne
#     }
        
#     if type(update_object) is BulkUpdateObject:
#         result = collection_dict[update_object.collection].bulk_write(
#             [
#                 UpdateOne(
#                 filter = item.filter,
#                 update = get_ops(
#                     item.operation,
#                     item.attr_val,
#                     item.operation_list
#                     )
#                 )
#                 for item in update_object.update_items
#             ]
#         ).bulk_api_result
#         debug(result)

#     elif update_object.mongo_ops == 'update_many':
#         collection_dict[update_object.collection].update_many(
#             filter = update_object.filter,
#             update = get_ops(
#                 update_object.operation,
#                 update_object.attr_val
#                 ),
#             upsert = update_object.upsert,
#             array_filters = update_object.array_filters
#         )
#     else:

        
#         collection_dict[update_object.collection].update_one(
#             update_object.filter,
#             get_ops(
#                 update_object.operation,
#                 update_object.attr_val
#                 ),
#             upsert = update_object.upsert,
#             array_filters = update_object.array_filters
#         )
#         if announce:
#             await emitter.emit(
#                 'DATA_UPDATE',
#                 get_data(
#                     update_object.collection,
#                     update_object.attr_val,
#                     update_object.operation,
#                     sio_event
#                     ),
#                 room = str(update_object.filter['_id']) if not subscribers else subscribers)




class Manager(object):
    def __init__ (self, emitter: Emitter):

        self.emitter = emitter


    
    '''
    -----------------------------------------------------------
    ACCOUNT METHODS transferok
    -----------------------------------------------------------
    '''



    # def register_account(self, reg_form: RegistrationForm):
    #     user_obj = User(
    #         discriminator = 5,
    #         username = reg_form.username,
    #         password = reg_form.password_hash,
    #         email = reg_form.email,
    #         state = UserState(),
    #         statistics = UserStatistics()
    #     )
    #     users.insert_one(user_obj.dict())


    # def validate_email(self, user_id: ObjectIdStr):
    #     if users.update_one(query_id(user_id), set_attr('state.verified', True)).modified_count > 0:
    #         return True


    # def attempt_login_account(self, account_details:dict):
    #     fetched_userdata = users.find_one({'username': account_details.username})
    #     if fetched_userdata['password'] == account_details.password:
    #         return True, self.on_login_success(fetched_userdata)
    #     else:
    #         return False, None
    #         # emit('login_fail', sid=sid)


    # def create_otp_secret(self, user_id, secret):
    #     if (users.update_one(query_id(user_id), set_attr('otp_hash', secret)).modified_count > 0):
    #         return True



    '''
    -----------------------------------------------------------
    USER METHODS transferok
    -----------------------------------------------------------
    '''

    


    # async def data_update(self, update_object, sio_event = None, announce = True, subscribers = None):


    #     def get_ops(operation, attr_val, operation_list: list[Operation] = None):
    #         if operation_list:
    #             return {f"${item.operation}": item.attr_val for item in operation_list}
    #         return {f'${operation}': attr_val}

    #     def get_data(collection, data, operation, event):
    #         return_data = {'operation': operation, 'event': event, 'data': None}
    #         dotty_data = dotty()
    #         for k, v in data.items():
    #             dotty_data[k] = v
    #         data = dotty_data.to_dict()
    #         if collection == 'users':
    #             return_data['data'] = {'userdata': data}
    #         if collection == 'servers':
    #             return_data['data'] = {'serverdata': {'selected_serverdata': data}}
    #         if collection == 'rooms':
    #             return_data['data'] = {'roomdata': {'selected_roomdata': data}}
    #         return return_data

    #     collection_dict = {
    #         'users': users,
    #         'servers': servers,
    #         'rooms': rooms
    #     }

    #     mongo_ops_dict = {
    #         'insert': InsertOne,
    #         'update': UpdateOne,
    #         'delete': DeleteOne
    #     }
            
    #     if type(update_object) is BulkUpdateObject:
    #         result = collection_dict[update_object.collection].bulk_write(
    #             [
    #                UpdateOne(
    #                 filter = item.filter,
    #                 update = get_ops(
    #                     item.operation,
    #                     item.attr_val,
    #                     item.operation_list
    #                     )
    #                 )
    #                 for item in update_object.update_items
    #             ]
    #         ).bulk_api_result
    #         debug(result)

    #     elif update_object.mongo_ops == 'update_many':
    #         collection_dict[update_object.collection].update_many(
    #             filter = update_object.filter,
    #             update = get_ops(
    #                 update_object.operation,
    #                 update_object.attr_val
    #                 ),
    #             upsert = update_object.upsert,
    #             array_filters = update_object.array_filters
    #         )
    #     else:

            
    #         collection_dict[update_object.collection].update_one(
    #             update_object.filter,
    #             get_ops(
    #                 update_object.operation,
    #                 update_object.attr_val
    #                 ),
    #             upsert = update_object.upsert,
    #             array_filters = update_object.array_filters
    #         )
    #         if announce:
    #             await self.emitter.emit(
    #                 'DATA_UPDATE',
    #                 get_data(
    #                     update_object.collection,
    #                     update_object.attr_val,
    #                     update_object.operation,
    #                     sio_event
    #                     ),
    #                 room = str(update_object.filter['_id']) if not subscribers else subscribers)

    
    # async def modify_user_connection(self, user_id: ObjectIdStr, connection,  user_obj: User = None):
    #     await self.data_update(
    #         UpdateObject(
    #             collection = 'users',
    #             filter = query_id(user_id),
    #             attr_val = {'state.connection': connection}),
    #         announce = False
    #         )

    #     # TODO, CACHE
    #     subscribers = users.find_one(
    #         query_id(user_id),
    #         {'servers': 1, '_id': 0}
    #     )
    #     subscribers = list(subscribers['servers'].keys())
    #     debug(subscribers)

    #     await self.data_update(
    #         UpdateObject(
    #             collection = 'servers',
    #             filter = query_ids(subscribers),
    #             attr_val = {f'members.{user_id}.connection': connection}),
    #         'MEMBER_PRESENCE_DELTA',
    #         subscribers = subscribers


    #     )


        


    # def get_user(self, user_id: ObjectIdStr):
    #     return users.find_one(query_id(user_id))


    # def modify_user(self, user_id: ObjectIdStr, username: str, avatar: BytesIO):
    #     avatar_id  = self.upload_file(avatar)
    #     print(type(avatar_id))
    #     attr_dict = {
    #         'username': username,
    #         'avatar': avatar_id
    #     }
    #     if users.update_one(query_id(user_id), set_attr(attr_dict = attr_dict)).modified_count > 0:
    #         return True


    # async def add_relationship(self, initiator_id, target_id):
    #     debug('enter')
    #     op1 = UpdateObject.construct(
    #         filter = query_id(initiator_id),
    #         attr_val = {'relationships.pending_outgoing': target_id},
    #         operation = 'push'
    #         )
    #     op2 = UpdateObject.construct(
    #         filter = query_id(target_id),
    #         attr_val = {'relationships.pending_incoming': initiator_id},
    #         operation = 'push'
    #         )
    #     results = await self.data_update(BulkUpdateObject.construct(
    #         collection = 'users',
    #         update_items = [op1, op2])
    #         )
    #     debug(results)


    # async def confirm_relationship(self, initiator_id, target_id):
    #     op1 = UpdateObject.construct(
    #         filter = query_id(initiator_id),
    #         operation_list = [
    #             Operation(
    #                 attr_val = {'relationships.friend': target_id},
    #                 operation = 'push'
    #             ),
    #             Operation(
    #                 attr_val = {'relationships.pending_incoming': target_id},
    #                 operation = 'pull'
    #             )
    #         ]
    #         )

    #     op2 = UpdateObject.construct(
    #         filter = query_id(target_id),
    #         operation_list = [
    #             Operation(
    #                 attr_val = {'relationships.friend': initiator_id},
    #                 operation = 'push'
    #             ),
    #             Operation(
    #                 attr_val = {'relationships.pending_outgoing': initiator_id},
    #                 operation = 'pull'
    #             )
    #         ]
    #         )
    #     await self.data_update(BulkUpdateObject.construct(
    #         collection = 'users',
    #         update_items = [op1, op2])
    #         )


    # def deny_relationship(self, initiator_id, target_id):
    #     op1 = UpdateObject.construct(
    #         filter = query_id(initiator_id),
    #         attr_val = {'relationships.pending_outgoing': target_id},
    #         operation = 'pull'
    #         )
    #     op2 = UpdateObject.construct(
    #         filter = query_id(target_id),
    #         attr_val = {'relationships.pending_incoming': initiator_id},
    #         operation = 'pull'
    #         )
    #     self.data_update(BulkUpdateObject.construct(
    #         collection = 'users',
    #         update_items = [op1, op2])
    #         )



    '''
    -----------------------------------------------------------
    FILE METHODS transferok
    -----------------------------------------------------------
    '''



    # def upload_file(self, byte_file, description: GraphicsDescriptionIn) -> ObjectIdStr:
    #     mongo_file = description.dict()
    #     mongo_file.update({'data': byte_file})
    #     return str(files.insert_one(mongo_file).inserted_id)


    # def convert_mongo_image_bytes(self, image_obj: GraphicsDescriptionIn, image_request: RequestImageFile) -> Tuple[bytes, str]:
    #     '''
    #     1.  Fetch image data and open.  
    #     2.  Process image (resize, convert)
    #     3.  Create byte-obj then return.
    #     '''
    #     #1
    #     image_request.native_extension = image_obj.extension
    #     pil_img = Image.open(BytesIO(image_obj.data))
    #     #2
    #     buffer = BytesIO()
    #     image_format = image_request.desired_extension if image_request.desired_extension else image_request.native_extension
    #     if (image_request.desired_extension
    #         and image_request.desired_extension != image_request.native_extension
    #         and pil_img.mode != 'RGB'):
    #         pil_img = pil_img.convert('RGB')
    #     pil_img.save(buffer, image_format)
    #     buffer.seek(0)
    #     return buffer, image_format

    # def get_file_emoji(self, server_id: ObjectIdStr,image_obj: RequestImageFile):
    #     image = servers.find_one(
    #         query_id(server_id),
    #         {'file': f'$emoji.{image_obj.filename}.file', '_id': False}
    #     )
    #     if not image:
    #         return None
    #     return self.convert_mongo_image_bytes(
    #         GraphicsDescriptionIn.construct(**image['file']),
    #         image_obj)

    # def get_server_icon(self, server_id: ObjectIdStr):
    #     image = servers.find_one(
    #         query_id(server_id),
    #         {'icon': 1, '_id': False}
    #     )
    #     if not image:
    #         return None
    #     return self.convert_mongo_image_bytes(
    #         GraphicsDescriptionIn.construct(**image['icon']),
    #         RequestImageFile.construct())

    # def get_user_icon(self, user_id: ObjectIdStr):
    #     image = users.find_one(
    #         query_id(user_id),
    #         {'icon': 1, '_id': False}
    #     )
    #     if not image:
    #         return None
    #     return self.convert_mongo_image_bytes(
    #         GraphicsDescriptionIn.construct(**image['icon']),
    #         RequestImageFile.construct())

    '''
    -----------------------------------------------------------
    LOGGER METHODS transferok
    -----------------------------------------------------------
    '''



    # def logger(self, changes: List[AuditLogChange], actuator_id: ObjectIdStr, victim_id: ObjectIdStr):
    #     changes = AuditLogChange(
    #         new_val = new_val,
    #         old_val= old_val,
    #         key = key
    #     )

    #     entry = AuditLogEntry(
    #         id = str(ObjectId()),
    #         actuator_id = actuator_id,
    #         target_id = victim_id,
    #         changes = changes,
    #         action_type = None,
    #         options = None,
    #         reasons = None             
    #     )
    #     audit_log.insert_one()

    '''
    -----------------------------------------------------------
    SERVER DISCOVERY METHODS transferok
    -----------------------------------------------------------
    '''

    # def discover_servers(self):
    #     return [ServerDiscoveryPartial(**x) for x in servers.find(
    #         projection={
    #         'id': 1,
    #         'name': 1,
    #         'description': 1,
    #         'icon': 1,
    #         'splash': 1
    #         }
    #     )]


    '''
    -----------------------------------------------------------
    SERVER METHODS transferok
    -----------------------------------------------------------
    '''

    # def create_server(self, server_obj: ServerBase, icon: ObjectIdStr, owner_id: ObjectIdStr):
    #     rooms = []
    #     server_id = ObjectId()
    #     def create_room(room: BaseServerRoom, channel_id, index):
    #         room_id = self.create_server_room(
    #             server_id = str(server_id),
    #             channel_id = channel_id,
    #             name = room.name
    #             )
    #         rooms.append(room_id)
    #         return room_id, RoomChannelPartial(position=index,name=room.name)            
    #     if icon:
    #         icon = base64.standard_b64decode(icon)
    #     channels = {
    #         channel.id: {
    #             'rooms': dict([create_room(room, channel.id, index) for index, room in enumerate(channel.rooms)]),
    #             'name': channel.name
    #             }
    #         for channel in server_obj.channels
    #         }
    #     server_obj = Server(
    #         name = server_obj.name,
    #         channels = channels,
    #         owner_id = owner_id,
    #         default_room = next(iter(channels[next(iter(channels))]['rooms'])),
    #         default_channel = next(iter(channels))
    #         )
    #     server_obj = server_obj.dict(exclude={'id'})
    #     server_obj.update({'_id': server_id})
    #     servers.insert_one(server_obj)
    #     self.add_server_member(server_id, owner_id)
    #     return server_obj

    

    # def delete_server(self, server_id: ObjectIdStr) -> int:
    #     return servers.delete_one(query_id(server_id)).deleted_count


    # def get_server(self, server_id):
    #     return servers.find_one(query_id(server_id))



    # def base64_encoder(self, image):
    #     return base64.standard_b64encode(image)

        
    # def server_modify_member(self, server_id, member_id, member_obj: ServerMemberIn):
    #     mongo_ops = {'$set': {}, '$push': {}, '$pull': {}}
    #     for k, v in member_obj.dict(exclude_none=True).items():
    #         if type(v) is list:
    #             for v1 in v:
    #                 try:
    #                     mongo_ops['$push'].update({f'members.{member_id}.{k}': {'$each': v1['add']}})
    #                 except:
    #                     pass
    #                 try:
    #                     mongo_ops['$pull'].update({k: {'$each': v1['remove']}})
    #                 except:
    #                     pass
    #         else:
    #             mongo_ops['$set'].update({f'members.{member_id}.{k}':v })
    #     debug(mongo_ops)
    #     return servers.update_one(query_id(server_id),mongo_ops).modified_count


    # def add_server_emoji(self, server_id: ObjectIdStr, name: str, emoji_file: GraphicsDescriptionIn):
    #     result = servers.update_one(
    #         query_id(server_id),
    #         set_attr(
    #             f'emoji.{str(ObjectId())}',
    #             Emoji.construct(name=name, file = emoji_file).dict()
    #             )
    #         )
    #     debug(result.raw_result)
    
    # def edit_server_icon(self, server_id: ObjectIdStr, icon_file: GraphicsDescriptionIn):
    #     debug(server_id)
    #     result = servers.update_one(
    #         query_id(server_id),
    #         set_attr('icon', icon_file.dict())
    #         )
    #     debug(result.raw_result)
        
    # def edit_user_icon(self, user_id, icon_file: GraphicsDescriptionIn):
    #     result = users.update_one(
    #         query_id(user_id),
    #         set_attr('icon', icon_file.dict())
    #         )
    #     debug(result.raw_result)

    # '''
    # -----------------------------------------------------------
    # SERVER USER METHODS
    # -----------------------------------------------------------
    # '''

    # def add_server_member(self, server_id, user_id, invite_id=None):
    #     '''
    #     1.  Find user.
    #     2.  Update server.members.{user_id}
    #     3.  Update user.servers.{server_id}
    #     '''
    #     #1
    #     user = users.find_one(query_id(user_id),
    #         {'connection': '$state.connection',
    #         'activity': '$state.activity'}
    #         )
    #     #2
    #     query = query_id(server_id)
    #     query.update({f'members.{user_id}':{'$exists': False}})
    #     update = set_attr(f'members.{user_id}', UserServerPartial.construct(**user).dict())
    #     if invite_id: update.update(inc_attr(f'invites.{invite_id}.uses', 1))
    #     debug(update)
    #     server_obj = servers.find_one_and_update(
    #         query,
    #         update,
    #         return_document = ReturnDocument.AFTER,
    #         projection={'default_room': 1, 'default_channel': 1,'_id':0}
    #     )
    #     #3
    #     query = set_attr(f'servers.{server_id}',
    #         UserSelectedState.construct(
    #             selected_room= server_obj['default_room'],
    #             selected_channel = server_obj['default_channel']
    #         ).dict()
    #         )
    #     query.update(inc_attr('statistics.joined_servers', 1))
    #     if server_obj:
    #         users.update_one(
    #             query_id(user_id),
    #             query
    #         )

    # def delete_server_member(self, server_id, user_id):
    #     result1 = servers.update_one(
    #         query_id(server_id),
    #         remove_attr(f'members.{user_id}', '')
    #     ).modified_count
    #     if result1 > 0:
    #         users.update_one(
    #             query_id(user_id),
    #             remove_attr(f'servers.{server_id}', '')
    #         )

    '''
    -----------------------------------------------------------
    SERVER ROLE METHODS
    -----------------------------------------------------------
    '''

    # def create_server_role(self, server_id):
    #     role = Role()
    #     self.data_update(
    #         'servers',
    #         query_id(server_id),
    #         f'roles.{str(ObjectId())}',
    #         role.dict(),
    #         operation='set'
    #     )
    #     return role



    '''
    -----------------------------------------------------------
    SERVER ROOM METHODS
    -----------------------------------------------------------
    '''



    # def get_server_room(self, room_id: ObjectIdStr):
    #     return rooms.find_one(query_id(room_id))



    # def get_list_of_server_rooms(self, server_id):
    #     '''
    #     TODO
    #     '''
    #     result = rooms.find({'server': server_id})
    #     if result:
    #         return list(result)
    #     return result



    # def delete_server_room(self, room_id: ObjectIdStr):
    #     result = self.delete_room(room_id)
    #     return result

    # async def create_server_channel(self, server_id: ObjectIdStr, name: str):
    #     await self.data_update(UpdateObject.construct(
    #         filter = query_id(server_id),
    #         collection = 'servers',
    #         attr_val = {
    #             f'channels.{str(ObjectId())}': Channel(name = name).dict()
    #         },
    #         operation = 'set'),
    #         'SERVER_CHANNEL_CREATED'
    #     )

    # def create_server_room(self, server_id: ObjectIdStr, channel_id: ObjectIdStr, name: str):
    #     new_server_room_obj = ServerRoom(
    #         name = name,
    #         server = server_id,
    #         channel = channel_id
    #         )
    #     new_room_id = rooms.insert_one(
    #         new_server_room_obj.dict(),
    #         ).inserted_id
    #     new_room_id = str(new_room_id)
    #     if new_room_id:
    #         servers.update_one(
    #             query_id(server_id),
    #             set_attr(
    #                 f'channels.{channel_id}.rooms.{new_room_id}',
    #                 RoomChannelPartial.construct(
    #                     position= 'TODO',
    #                     name= name
    #                 ).dict()
    #             ))
    #     return new_room_id
    #     # self.data_update(UpdateObject.construct(
    #     #     filter = query_id(server_id),
    #     #     collection = 'servers',
    #     #     attr_val = {
    #     #         f'channels.{channel_id}.rooms.{new_room_id}':
    #     #         RoomChannelPartial.construct(position= 69, name= name).dict()
    #     #     },
    #     #     operation = 'set'),
    #     #     'SERVER_ROOM_CREATED',
    #     #     announce= False
    #     # )
    #     # return new_room_id


    '''
    -----------------------------------------------------------
    INVITE METHODS
    -----------------------------------------------------------
    '''
    # def add_server_invite(self, invite_obj: InviteIn):
    #     debug(invite_obj)
    #     invite_obj = Invite.construct(
    #         **invite_obj.dict(),
    #         expires_at = datetime.utcnow() + timedelta(
    #             days = invite_obj.max_age.days,
    #             seconds = invite_obj.max_age.seconds,
    #             hours = invite_obj.max_age.hours,
    #             weeks = invite_obj.max_age.weeks
    #             ) if invite_obj.max_age else None
    #         )
    #     servers.update_one(
    #         query_id(invite_obj.server),
    #         set_attr(f'invites.{str(ObjectId())}', invite_obj.dict())
    #     )

    # def use_server_invite(self, invite_id, current_user: User):
    #     invite = Invite(**servers.find_one(
    #         query_field_exists(f'invites.{invite_id}'),
    #         {'invite': f'$invites.{invite_id}'})['invite']
    #         )
    #     if invite.expires_at < datetime.now(): return 'Expired'
    #     if invite.uses >= invite.max_uses: return 'Already used up'
    #     if invite.server in current_user.servers.keys(): return 'Already a member'
    #     self.add_server_member(invite.server,current_user.id, invite_id)        
    #     return 'OK'
    '''
    -----------------------------------------------------------
    DM ROOM METHODS
    -----------------------------------------------------------
    '''



    # async def create_dm_room(self, dmroom_in: DmRoomIn, owner_id: ObjectIdStr):
    #     '''
    #     1.  Create room object and update database.
    #     2.  Update each participant.
    #     3.  Return updated data.
    #     '''
    #     #1
    #     participants = users.find(
    #         query_ids(dmroom_in.participants),
    #         {
    #             'username': 1,
    #             'connection': '$state.connection',
    #             'activity': '$state.activity',
    #             'icon': 1,
    #         }
    #         )
    #     participants = [
    #         UserPartialDmRoom.construct(
    #             participant,
    #             id = str(participant['_id']),
    #             nick = participant['username']
    #         )
    #         for participant in participants
    #     ]
    #     create_result = rooms.insert_one(
    #         DmRoom(
    #             name = dmroom_in.name,
    #             participants = participants,
    #             owner_id = owner_id
    #             ).dict()
    #         )
    #     await self.data_update(
    #         UpdateObject.construct(
    #         filter = query_ids(dmroom_in.participants),
    #         collection = 'users',
    #         mongo_ops = 'update_many',
    #         operation = 'push',
    #         attr_val = {'dm_rooms': str(create_result.inserted_id)}
    #     )
    #     )
    #     return str(create_result.inserted_id)


    # def get_dm_room(self, dm_room_id: ObjectIdStr):
    #     '''
    #     1.  Fetch db data and return.
    #     '''
    #     #1
    #     return rooms.find_one(query_id(dm_room_id))


    # async def delete_dm_room(self, requesting_id: ObjectIdStr, dm_room_id: ObjectIdStr, method: str, reasons: str = None):
    #     '''
    #     1.  Attempt deleting room.
    #     2.  Attempt unlinking room from User 'dm_rooms' attr.
    #     3.  Log.
    #     4.  Return result.
    #     Behavior:
    #     Room database entry is not deleted. 
    #     '''
    #     #1
    #     if method == 'obliterate':
    #         result = rooms.find_one_and_delete(query_id(dm_room_id))
    #         debug(result)
    #         deleted_room = DmRoom.construct(**result)
    #         if not result:
    #             return
    #         await self.data_update(
    #             UpdateObject.construct(
    #                 filter = query_ids(map(lambda x: x['id'], deleted_room.participants)),
    #                 attr_val = {'dm_rooms': dm_room_id},
    #                 operation = 'pull',
    #                 collection = 'users',
    #                 mongo_ops = 'update_many'
    #             ),
    #             announce=False
    #             )
    #         # if result < 1:
    #         #     changes = AuditLogChange(
    #         #         new_val = None,
    #         #         old_val= dm_room_id,
    #         #         key = 'rooms')
    #         #     entry = AuditLogEntry(
    #         #         id = str(ObjectId()),
    #         #         actuator_id = user_id,
    #         #         target_id = None,
    #         #         changes = changes,
    #         #         action_type = AuditEnumEvents.ROOM_DELETE.value,
    #         #         options = {
    #         #             'members_removed': user_id
    #         #         },
    #         #         reasons = reasons
    #         #     )
    #         #     #3
    #         #     audit_log.insert_one(entry.dict())
    #         #     #4
    #         #     return 'No such room.'
    #         # else:
    #         #     return True
    #     #2
    #     if method == 'unlink':
    #        await self.data_update(
    #             UpdateObject.construct(
    #                 filter = query_id(requesting_id),
    #                 attr_val = {'dm_rooms': dm_room_id},
    #                 operation = 'pull',
    #                 collection = 'users'
    #             ),
    #             announce=False
    #             )
            


            

    '''
    -----------------------------------------------------------
    ROOM METHODS
    -----------------------------------------------------------
    '''

    # def delete_room(self, room_id):
    #     '''
    #     Returns deleted count.
    #     '''
    #     result = rooms.delete_one(query_id(room_id)).deleted_count
    #     return result


    # async def post_to_room(self, room_id: ObjectIdStr, post: PostIn):
    #     post = Post(
    #         **post.dict(),
    #         type = MessageTypes.REPLY.value if post.message_reference else MessageTypes.DEFAULT.value
    #     )
    #     ops1 = UpdateObject(
    #         collection = 'rooms',
    #         filter = query_id(room_id),
    #         attr_val = {f'posts.{str(ObjectId())}': post.dict()},
    #         operation = 'set'
    #     )
    #     await self.data_update(ops1, 'NEW_POST_INSERTED')


    # async def edit_room_message(self, room_id: ObjectIdStr, post_id: ObjectIdStr, post: PostEdit):
    #     ops1 = UpdateObject(
    #         collection = 'rooms',
    #         filter = query_id(room_id),
    #         attr_val = {f'posts.{post_id}.{k}':v for k,v in post.dict(exclude_none=True).items()},
    #         operation = 'set'
    #     )
    #     await self.data_update(ops1, 'OLD_POST_EDITED')


    # def get_room_messages(self, room_id:ObjectIdStr, limit: int = None):
    #     if limit:
    #         result = list(rooms.aggregate([
    #         {
    #             '$match': query_id(room_id)
    #         },
    #         {
    #         '$project': {
    #             'posts': {
    #                 '$slice': [
    #                     '$posts', limit
    #                 ]
    #             }
    #         }
    #         }
    #     ]))[0]    
    #     else:
    #         result = rooms.find_one(query_id(room_id), {'posts': 1})
    #     debug(result)
    #     if result:
    #         return result['posts']
    #     return None



    # def get_one_room_message(self, room_id: ObjectIdStr, msg_id: ObjectIdStr):
    #     result = rooms.aggregate([
    #         {
    #             '$match': query_id(room_id)
    #         }, {
    #             '$unwind': {
    #                 'path': '$posts', 
    #                 'preserveNullAndEmptyArrays': False
    #             }
    #         }, {
    #             '$project': {
    #                 'post': '$posts', 
    #                 '_id': 0
    #             }
    #         }, {
    #             '$match': {
    #                 'post.id': msg_id
    #             }
    #         }
    #     ])
    #     result = list(result)
    #     if len(result) > 0:
    #         return result[0]['post']
    #     else:
    #         return None
        


    # def modify_dm_room(dm_room_id, icon, name):
    #     if icon:
    #         rooms.update_one(query_id(dm_room_id), set_attr('icon', icon))
    #     if name:
    #         rooms.update_one(query_id(dm_room_id), set_attr('name', name))


    '''
    -----------------------------------------------------------
    REACTION METHODS transferok
    -----------------------------------------------------------
    '''

    # async def add_reaction(self, room_id, message_id, emoji_id):
    #     user_id = "60e94ad49a39c29595d1589e"
    #     await self.data_update(
    #         UpdateObject(
    #             collection = 'rooms',
    #             filter = query_id(room_id),
    #             attr_val = {f'posts.$[post].reactions.{emoji_id}': user_id},
    #             operation = 'addToSet',
    #             upsert = False,
    #             array_filters = [{"post.id": {"$eq": message_id}}],
    #         ),
    #         sio_event= 'REACTION_POST'
    #     )
    #     # rooms.update_one(
    #     #     query_id(room_id),
    #     #     {
    #     #         '$addToSet': {
    #     #             f'posts.$[post].reactions.{emoji_id}': user_id
    #     #         }
    #     #     },
    #     #     upsert = False,
    #     #     array_filters = [{"post.id": {"$eq": message_id}}]
    #     # ).modified_count



    # def delete_reaction(self, room_id, message_id, emoji_id):
    #     user_id = "60e94ad49a39c29595d1589e"
    #     return rooms.update_one(
    #         query_id(room_id),
    #         pull_arr_ele('posts.$[post].reactions', {user_id: emoji_id}),
    #         upsert = False,
    #         array_filters = [{"post.id": {"$eq": message_id}}]
    #     ).modified_count
    

    '''
    -----------------------------------------------------------
    INIT DATA
    -----------------------------------------------------------
    '''

    # def fetch_init_data(self, userdata: User):
    #     serverlist = []
    #     if userdata.statistics.joined_servers > 0:
    #         # return InitData(userdata = userdata)
    #         serverlist = list(servers.aggregate(
    #             [
    #                 {'$match':{'_id': {"$in": list(map(lambda item: ObjectId(item), userdata.servers.keys()))}}},
    #                 {'$project':{'name': True, 'icon': True, 'emoji': True}}
    #             ]
    #         ))
    #     if userdata.state.selected_view in ['friends', 'dm']:
    #         '''
    #         1. Get friendlist (to show in second_panel)
    #         2. Get active friends (to show in third_panel) > pass
    #         3. If selected_dm is not 'friends_button', enter dm room.
    #         '''
    #         #1
    #         friendlist = list(users.find(
    #             query_ids([ObjectId(item) for k, v in userdata.relationships.dict().items() for item in v]),
    #             {'username': 1, 'avatar': 1, 'connection': '$state.connection'}
    #             ))
    #         #2
    #         #3
    #         debug(userdata)
    #         self.emitter.enter_sio_room(userdata.id, userdata.dm_rooms)
    #         dmlist = list(rooms.find(
    #             query_ids([ObjectId(item) for item in userdata.dm_rooms]),
    #             {'name': 1, 'icon': 1}
    #             ))
    #         #4
    #         if userdata.state.selected_view == 'dm':
    #             return InitData(
    #                 userdata = userdata,
    #                 roomdata = servers.find_one(query_id(userdata.state.selected_dm)),
    #                 serverlist = serverlist,
    #                 friendlist = friendlist,
    #                 dmlist = dmlist,
    #                 applist = generate_default_apps()
    #             )
    #         return InitData(
    #             userdata = userdata,
    #             serverlist = serverlist,
    #             friendlist = friendlist,
    #             dmlist = dmlist,
    #             applist = generate_default_apps()
    #         )
    #     return InitData(
    #         self.enter_server_main(userdata),
    #         userdata = userdata,
    #         serverlist = serverlist,
    #         applist = generate_default_apps()
    #     )
        

    # def enter_server_main(self, server_id: ObjectIdStr, userdata: User):
    #     users.update(query_id(userdata.id), set_attr(attr_dict=
    #         {
    #             'state.selected_server': server_id,
    #             'state.selected_channel': userdata.servers[server_id].selected_channel,
    #             'state.selected_room': userdata.servers[server_id].selected_room
    #         }))
    #     serverdata = self.enter_server(
    #         server_id,
    #         userdata.id
    #     )
    #     channeldata = self.enter_channel(
    #         serverdata.selected_serverdata.channels[userdata.servers[server_id].selected_channel],
    #         serverdata.user_roles,
    #         serverdata.base_permissions,
    #         userdata.id
    #     )
    #     roomdata = self.enter_room(
    #         userdata.servers[server_id].selected_room,
    #         serverdata.user_roles,
    #         channeldata.channel_permissions,
    #         userdata.id
    #     )

        
    #     return EnterServerInitData(
    #         serverdata = serverdata,
    #         channeldata = channeldata,
    #         roomdata = roomdata
    #     )

    # def enter_server(self, selected_server: ObjectIdStr, user_id: ObjectIdStr) -> ServerData:
    #     '''
    #     0.  Create server entry of user (ServerMember)
    #     1.  Fetch server data.
    #     2.  Generate roomlist.
    #     3.  Compute base permissions.
    #     4.  Socket operations.
    #     5.  Return fetched data.
    #     '''
    #     #1
    #     selected_serverdata = Server(**servers.find_one(query_id(selected_server)))
    #     #3
    #     base_perms = selected_serverdata.settings.permissions
    #     try:
    #         user_roles = selected_serverdata.members[user_id].roles
    #         for role in user_roles:
    #             base_perms = base_perms | selected_serverdata.roles[role].permissions
    #     except KeyError:
    #         user_roles = None
    #     #4
    #     #new user in server
    #     #5
    #     return ServerData(
    #         selected_serverdata = selected_serverdata,
    #         base_permissions = base_perms,
    #         user_roles = user_roles,
    #     )

    # def enter_channel(self, selected_channeldata, user_roles, base_perms, id) -> ChannelData:
    #     '''
    #     1. Compute and return channel_permission.
    #     '''
    #     channel_perms = base_perms
    #     def inverter(num):
    #         return (1<<36) - 1 - num
    #     try:
    #         channel_perms &= inverter(selected_channeldata.permissions.deny)
    #     except:
    #         pass
    #     try:
    #         channel_perms |= selected_channeldata.permissions.allow
    #     except:
    #         pass
    #     for role in user_roles:
    #         try:
    #             channel_perms &= inverter(selected_channeldata.permissions_member.role.deny)
    #         except:
    #             pass
    #         try:
    #             channel_perms |= selected_channeldata.permissions_member.role.allow
    #         except:
    #             pass
    #     try:
    #         channel_perms &= inverter(selected_channeldata.permissions_member.id.deny)
    #     except:
    #         pass
    #     try:
    #         channel_perms |= selected_channeldata.permissions_member.id.allow
    #     except:
    #         pass
    #     return ChannelData(
    #         channel_permissions = channel_perms,
    #         name = selected_channeldata.name
    #     )


    # def enter_room(self, selected_room: ObjectIdStr, roles, channel_perms, id: ObjectIdStr) -> RoomData:
    #     '''
    #     1.  Fetch room data.
    #     2.  Socket operations.
    #     3.  Get channel overwrites.
    #     3.  Return fetched data.
    #     '''
    #     debug('enter_room')
    #     #1
    #     selected_roomdata = rooms.find_one(query_id(selected_room))
    #     if selected_roomdata['type'] == RoomTypes.SERVER_ROOM:
    #         selected_roomdata = ServerRoom(**rooms.find_one(query_id(selected_room)))
    #     else:
    #         selected_roomdata = DmRoom(**rooms.find_one(query_id(selected_room)))
    #     #2
    #     try:
    #         self.emitter.enter_sio_room(id, selected_room)
    #     except KeyError:
    #         # offline case
    #         pass
    #     #3
    #     return  RoomData(
    #         selected_roomdata = selected_roomdata,
    #         # 'selected_room': str(selected_room),
    #         room_permissions = self.compute_room_permissions(selected_roomdata, roles, channel_perms, id)
    #     )

    # def compute_room_permissions(self, selected_roomdata, roles, channel_perms, id) -> int:
    #     room_perms = channel_perms
    #     def inverter(num):
    #         return (1<<36) - 1 - num
    #     try:
    #         room_perms &= inverter(selected_roomdata['permissions']['deny'])
    #     except:
    #         pass
    #     try:
    #         room_perms |= selected_roomdata['permissions']['allow']
    #     except:
    #         pass
    #     for role in roles:
    #         try:
    #             room_perms &= inverter(selected_roomdata['permissions_role'][role]['deny'])
    #         except:
    #             pass
    #         try:
    #             room_perms |= selected_roomdata['permissions_role'][role]['allow']
    #         except:
    #             pass
    #     try:
    #         room_perms &= inverter(selected_roomdata['permissions_member'][id]['deny'])
    #     except:
    #         pass
    #     try:
    #         room_perms |= selected_roomdata['permissions_member'][id]['allow']
    #     except:
    #         pass
    #     return room_perms

    # def enter_thread(self, selected_thread: ObjectIdStr) -> ThreadData:
    #     '''
    #     1.  Fetch room data.
    #     2.  Socket operations.
    #     3.  Get channel overwrites.
    #     3.  Return fetched data.
    #     '''
    #     #1
    #     selected_roomdata = ThreadRoom(**rooms.find_one(query_id(selected_thread)))
    #     #2
    #     try:
    #         self.emitter.enter_sio_room(id, selected_thread)
    #     except KeyError:
    #         # offline case
    #         pass
    #     #3
    #     return  ThreadData(
    #         selected_roomdata = selected_roomdata
    #     )