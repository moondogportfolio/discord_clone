from pymongo import MongoClient, InsertOne, DeleteOne, UpdateOne
from devtools import debug
from dotty_dict import dotty

from pydantic_models.update import BulkUpdateObject, Operation
from init_objects import emitter

# from datetime import datetime

source = 'mongodb+srv://mccndcg:ePRZiwIV5x3uU66Q@cluster0.spy9n.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
client = MongoClient(source)
discolord = client.discolord
servers = discolord.servers_test
users = discolord.users_test
rooms = discolord.rooms
audit_log = discolord.audit_log
files = discolord.files
workspaces = discolord.workspaces

collection_dict = {
            'users': users,
            'servers': servers,
            'rooms': rooms,
            'workspaces': workspaces
        }

async def data_update(update_object, sio_event = None, announce = True, subscribers = None):
    def get_ops(operation, attr_val, operation_list: list[Operation] = None):
        if operation_list:
            return {f"${item.operation}": item.attr_val for item in operation_list}
        return {f'${operation}': attr_val}

    def get_data(filter, collection, data, operation, event):
        return_data = {'operation': operation, 'event': event, 'data': None}
        dotty_data = dotty()
        for k, v in data.items():
            dotty_data[k] = v
        data = dotty_data.to_dict()
        if collection == 'users':
            return_data['data'] = {'userdata': data}
        if collection == 'servers':
            return_data['data'] = {'serverdata': {'selected_serverdata': data}}
        if collection == 'rooms':
            return_data['data'] = {'roomdata': {filter: data}}
        if collection == 'workspaces':
            return_data['data'] = {'workspacedata': {filter: data}}
        return return_data


    mongo_ops_dict = {
        'insert': InsertOne,
        'update': UpdateOne,
        'delete': DeleteOne
    }
        
    if type(update_object) is BulkUpdateObject:
        result = collection_dict[update_object.collection].bulk_write(
            [
                UpdateOne(
                filter = item.filter,
                update = get_ops(
                    item.operation,
                    item.attr_val,
                    item.operation_list
                    )
                )
                for item in update_object.update_items
            ]
        ).bulk_api_result

    elif update_object.mongo_ops == 'update_many':
        collection_dict[update_object.collection].update_many(
            filter = update_object.filter,
            update = get_ops(
                update_object.operation,
                update_object.attr_val
                ),
            upsert = update_object.upsert,
            array_filters = update_object.array_filters
        )
    else:
        collection_dict[update_object.collection].update_one(
            update_object.filter,
            get_ops(
                update_object.operation,
                update_object.attr_val,
                update_object.operation_list
                ),
            upsert = update_object.upsert,
            array_filters = update_object.array_filters
        )
        if update_object.operation_list:
            data = [get_data(
                str(update_object.filter['_id']),
                update_object.collection,
                item.attr_val,
                item.operation,
                sio_event
                )
                for item in update_object.operation_list]
        else:
            data = get_data(
                str(update_object.filter['_id']),
                update_object.collection,
                update_object.attr_val,
                update_object.operation,
                sio_event
                )
        if announce:
            await emitter.emit('DATA_UPDATE', data, room = str(update_object.filter['_id']) if not subscribers else subscribers)
