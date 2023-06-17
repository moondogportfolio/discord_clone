# from models import ServerMemberQuery
from bson.objectid import ObjectId

def query_id(obj_id):
    return {'_id': ObjectId(obj_id)}

def query_field_exists(field):
    return {field: {'$exists': True}}

def query_ids(arr_obj_id):
    return {'_id': {'$in': [ObjectId(item) for item in arr_obj_id]}}

def pull_arr_ele(arr_name: str, ele):
    return {'$pull': {arr_name: ele}}

def push_arr_ele(arr_name: str = None, ele = None, attr_dict: dict = None):
    if attr_dict:
        return {'$push': {k:v for k,v in attr_dict.items() if v is not None}}
    return {'$push': {arr_name: ele}}

def push_arr_uniq_ele(arr_name: str = None, ele = None, attr_dict: dict = None):
    if attr_dict:
        return {'$addToSet': {k:v for k,v in attr_dict.items() if v is not None}}
    return {'$addToSet': {arr_name: ele}}

def set_attr(attr_name: str = None, attr_value: str = None, attr_dict: dict = None):
    if attr_dict:
        return {'$set': attr_dict}
    return {'$set': {attr_name: attr_value}}

def inc_attr(attr_name: str = None, attr_value: str = None):
    return {'$inc': {attr_name: attr_value}}


def remove_attr(attr_name: str = None, attr_value: str = None, attr_dict: dict = None):
    if attr_dict:
        return {'$unset': attr_dict}
    return {'$unset': {attr_name: attr_value}}

