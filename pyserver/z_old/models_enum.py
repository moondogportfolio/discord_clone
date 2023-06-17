from enum import IntEnum, auto, Enum

class AuditEnumEvents(Enum):
    GUILD_UPDATE = 1
    ROOM_CREATE = 10
    ROOM_UPDATE = 11
    ROOM_DELETE = 12
    ROOM_UNLINK = 13
    ROOM_OVERWRITE_UPDATE = 14
    ROOM_OVERWRITE_DELETE = 15
    ROOM_OVERWRITE_CREATE = 16
    MEMBER_KICK = 20
    MEMBER_PRUNE = 21
    MEMBER_BAN_ADD = 22
    MEMBER_BAN_REMOVE = 23
    MEMBER_UPDATE = 24
    MEMBER_ROLE_UPDATE = 25
    MEMBER_MOVE = 26
    MEMBER_DISCONNECT =27
    BOT_ADD = 28
    ROLE_CREATE = 30
    ROLE_UPDATE = 31
    ROLE_DELETE = 32
    INVITE_CREATE = 40
    INVITE_UPDATE = 41
    INVITE_DELETE = 42
    WEBHOOK_CREATE = 50
    WEBHOOK_UPDATE = 51
    WEBHOOK_DELETE = 52
    EMOJI_CREATE = 60
    EMOJI_UPDATE = 61
    EMOJI_DELETE = 62
    MESSAGE_DELETE = 72
    MESSAGE_BULK_DELETE = 73
    MESSAGE_PIN = 74
    MESSAGE_UNPIN = 75

# import yagmail

# yagmail.register('mccndcg@gmail.com', 'naho20qeno')


class RoomTypes(IntEnum):
    SERVER_ROOM = auto()
    DM_ROOM = auto()
    GROUP_DM_ROOM = auto()
    THREAD_ROOM = auto()
    

class MessageTypes(Enum):
    DEFAULT = auto()
    REPLY = auto()
    CHANNEL_PINNED_MESSAGE = auto()
    APPLICATION_COMMAND = auto()
    SYSTEM_MESSAGE = auto()
