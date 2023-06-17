# from pymongo import MongoClient, InsertOne
# from pymongo import UpdateOne
# from bson.objectid import ObjectId
# from models import User, UserState, UserStatistics, Server, BaseRoom
# import pprint
# from helpers import parse
# pp = pprint.PrettyPrinter(indent=4).pprint
# from devtools import debug

# # from datetime import datetime

# source = 'mongodb+srv://mccndcg:ePRZiwIV5x3uU66Q@cluster0.spy9n.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
# client = MongoClient(source)
# discolord = client.discolord
# # servers = discolord.servers
# servers = discolord.servers_test
# # users = discolord.users
# users = discolord.users_test
# rooms = discolord.rooms
# audit_log = discolord.audit_log
# files = discolord.files

# def agg_names(id_array):
#     return [
#     {'$match':{'_id': {"$in": id_array}}},
#     {'$project':{'name': True}}
#     ]

# def agg_room_participants(id_array):
#     return [
#     {'$match':{'_id': {"$in": id_array}}},
#     {'$project':{'participants': True}},
#     ]

# def agg_usernames(id_array):
#     return [
#     {'$match':{'_id': {"$in": id_array}}},
#     {'$project':{'userclass': True, 'username': True}}
#     ]

# def agg_comembers(arr):
#     return [
#     {'$match':{'_id': {"$in": arr}}}
#     ]


# class Search(object):

#     def __init__(self) -> None:
#         self.coll = {
#             'room': rooms,
#             'user': users,
#             'server': servers
#         }

#     def delete_obj_instance(self, obj_id, obj):
#         self[obj].delete_one({'_id': ObjectId(obj_id)})

#     def delete_arr_element(self, user_id, arr_name, ele, obj):
#         self[obj].update({'_id': ObjectId(user_id)}, )

#     def toggle_is_online(self, user_id: ObjectId, bool):
#         users.update_one(
#             {"_id": user_id},
#             {'$set':
#                 {
#                 'state.is_online': bool
#                 }
#             })
#     def create_server(self, serverdata):
#         return servers.insert_one(serverdata)

#     def create_room(self, roomdata):
#         return rooms.insert_one(roomdata)

#     def create_user(self, userdata):
#         return users.insert_one(userdata)

#     def update_server(self, query, data):
#         print(servers.update_one(query, data).raw_result)

#     def update_user(self, query, data):
#         print(users.update_one(query, data).raw_result)

#     def update_room(self, query, data):
#         return users.update_one(query, data)

#     def mass_update_users(self, update_array):
#         debug(update_array)
#         result = users.bulk_write([UpdateOne(*x) for x in update_array])
#         debug(result.bulk_api_result)

#     def find_user(self, username) -> User:
#         result = users.find_one({"username": username})
#         return User(**result)

#     def find_server(self, id) -> Server:
#         result = servers.find_one({"_id": ObjectId(id)})
#         return Server(**result)

#     def find_room(self, id) -> BaseRoom:
#         result = rooms.find_one({"_id": ObjectId(id)} )
#         return BaseRoom(**result)

#     def find_channel(self, channel_id, server_id):
#         if type(server_id) is not ObjectId:
#             id = ObjectId(server_id)
#         return rooms.find_one({"_id": server_id, "channels": {"id": {"$in": channel_id}} } )

#     def find_server_comembers(self, id_array):
#         result = list(users.aggregate(agg_comembers(id_array)))
#         for v in result:
#             v.update({'id': str(v['_id'])})
#             v.pop('_id')
#         return result

#     def server_names(self, id_array):
#         result = list(servers.aggregate(agg_names(id_array)))
#         for v in result:
#             v.update({'id': str(v['_id'])})
#             v.pop('_id')
#         return result

#     def roomlist(self, id_array):
#         result = list(rooms.aggregate(agg_names(id_array)))
#         for v in result:
#             v.update({'id': str(v['_id'])})
#             v.pop('_id')
#         return result

#     def dm_participants(self, id_array):
#         result = list(rooms.aggregate(agg_room_participants(id_array)))
#         print(result)
#         return {str(v['_id']) : list(map(lambda item: item['name'], v['participants'])) for v in result}

#     def friend_names(self, id_array):
#         result = list(users.aggregate(agg_usernames(id_array)))
#         for v in result:
#             v.update({'id': str(v['_id'])})
#             v.pop('_id')
#         return result
