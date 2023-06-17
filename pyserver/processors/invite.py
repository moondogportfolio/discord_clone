from datetime import datetime, timedelta

from pydantic_models.servers import Invite, InviteIn
from pydantic_models.users import User
from pydantic_models.universal import ObjectId

from processors.mongo_update import servers
from processors.server_user import add_server_member

from mongo_cons import query_field_exists, query_id, set_attr

def add_server_invite(invite_obj: InviteIn):
    invite_obj = Invite.construct(
        **invite_obj.dict(),
        expires_at = datetime.utcnow() + timedelta(
            days = invite_obj.max_age.days,
            seconds = invite_obj.max_age.seconds,
            hours = invite_obj.max_age.hours,
            weeks = invite_obj.max_age.weeks
            ) if invite_obj.max_age else None
        )
    servers.update_one(
        query_id(invite_obj.server),
        set_attr(f'invites.{str(ObjectId())}', invite_obj.dict())
    )

def use_server_invite(invite_id, current_user: User):
    invite = Invite(**servers.find_one(
        query_field_exists(f'invites.{invite_id}'),
        {'invite': f'$invites.{invite_id}'})['invite']
        )
    if invite.expires_at < datetime.now(): return 'Expired'
    if invite.uses >= invite.max_uses: return 'Already used up'
    if invite.server in current_user.servers.keys(): return 'Already a member'
    add_server_member(invite.server,current_user.id, invite_id)        
    return 'OK'