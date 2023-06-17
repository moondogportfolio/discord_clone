from socketio import AsyncServer
from session import SessionManager
from devtools import debug, sprint
from pydantic.json import pydantic_encoder
from json import dumps

class Emitter:

    def __init__(self, sio: AsyncServer, session: SessionManager) -> None:
        self.sio = sio
        self.session = session

    async def emit(self, event:str, data, room):
        sprint('--------GET LISTENERS----------', sprint.cyan)
        sprint(f'emit event {event} \n>\nwith data {data} \n>\nto room {room}', sprint.cyan)
        try:
            debug(list(self.sio.manager.get_participants('/', room)))
        except:
            return

        if type(room) is list:
            for single_room in room:
                await self.emit(event, data, single_room)   
        else:         
            await self.sio.emit(
                event = event,
                data = dumps(data, indent=4, default=pydantic_encoder),
                to = room
                )

    def oid_to_sid(self, oid):
        return self.session.get_sid(oid)

    def enter_sio_room(self, uid, room): 
        debug(uid, room)
        if type(room) is list:
            for single_room in room:
                self.enter_sio_room(uid, single_room)  
        else:
            self.sio.enter_room(self.oid_to_sid(uid), room)
        