from devtools import debug
from bson.objectid import ObjectId

from pydantic_models.universal import ObjectIdStr
from pydantic_models.rooms import PostIn, Post, PostEdit
from pydantic_models.update import UpdateObject
from enum import Enum, auto
from mongo_cons import query_id, set_attr

from processors.mongo_update import data_update, rooms


class MessageTypesEnum(Enum):
    DEFAULT = auto()
    REPLY = auto()
    CHANNEL_PINNED_MESSAGE = auto()
    APPLICATION_COMMAND = auto()
    SYSTEM_MESSAGE = auto()


def delete_room(room_id):
    '''
    Returns deleted count.
    '''
    result = rooms.delete_one(query_id(room_id)).deleted_count
    return result


async def post_to_room(room_id: ObjectIdStr, post: PostIn):
    post = Post(
        **post.dict(),
        type = MessageTypesEnum.REPLY.value if post.message_reference else MessageTypesEnum.DEFAULT.value
    )
    ops1 = UpdateObject(
        collection = 'rooms',
        filter = query_id(room_id),
        attr_val = {f'posts.{str(ObjectId())}': post.dict()},
        operation = 'set'
    )
    await data_update(ops1, 'NEW_POST_INSERTED')


async def edit_room_message(room_id: ObjectIdStr, post_id: ObjectIdStr, post: PostEdit):
    ops1 = UpdateObject(
        collection = 'rooms',
        filter = query_id(room_id),
        attr_val = {f'posts.{post_id}.{k}':v for k,v in post.dict(exclude_none=True).items()},
        operation = 'set'
    )
    await data_update(ops1, 'OLD_POST_EDITED')


def get_room_messages(room_id:ObjectIdStr, limit: int = None):
    if limit:
        aggregate = [
            {
                '$match': query_id(room_id)
            },
            {
            '$project': {
                'posts': {
                    '$slice': [
                        '$posts', limit
                    ]
                }
            }
            }
        ]
        result = list(rooms.aggregate(aggregate))[0]    
    else:
        rooms.find_one(query_id(room_id), {'posts': 1})
    debug(result)
    if result:
        return result['posts']
    return None



def get_one_room_message(room_id: ObjectIdStr, msg_id: ObjectIdStr):
    aggregate = ([
        {
            '$match': query_id(room_id)
        }, {
            '$unwind': {
                'path': '$posts', 
                'preserveNullAndEmptyArrays': False
            }
        }, {
            '$project': {
                'post': '$posts', 
                '_id': 0
            }
        }, {
            '$match': {
                'post.id': msg_id
            }
        }
    ])
    result = rooms.aggregate(aggregate)
    result = list(result)
    if len(result) > 0:
        return result[0]['post']
    else:
        return None
    

