from mongo_cons import query_id, pull_arr_ele
from pydantic_models.update import UpdateObject

from processors.mongo_update import rooms, data_update

async def add_reaction(room_id, message_id, emoji_id):
    user_id = "60e94ad49a39c29595d1589e"
    await data_update(
        UpdateObject(
            collection = 'rooms',
            filter = query_id(room_id),
            attr_val = {f'posts.$[post].reactions.{emoji_id}': user_id},
            operation = 'addToSet',
            upsert = False,
            array_filters = [{"post.id": {"$eq": message_id}}],
        ),
        sio_event= 'REACTION_POST'
    )
    # rooms.update_one(
    #     query_id(room_id),
    #     {
    #         '$addToSet': {
    #             f'posts.$[post].reactions.{emoji_id}': user_id
    #         }
    #     },
    #     upsert = False,
    #     array_filters = [{"post.id": {"$eq": message_id}}]
    # ).modified_count



async def delete_reaction(room_id, message_id, emoji_id):
    user_id = "60e94ad49a39c29595d1589e"
    return rooms.update_one(
        query_id(room_id),
        pull_arr_ele('posts.$[post].reactions', {user_id: emoji_id}),
        upsert = False,
        array_filters = [{"post.id": {"$eq": message_id}}]
    ).modified_count
