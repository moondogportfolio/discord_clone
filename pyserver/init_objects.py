from emitter import Emitter
import socketio
from session import SessionManager


sio = socketio.AsyncServer(
    async_mode='asgi',
    cors_allowed_origins = []
)
socketapp = socketio.ASGIApp(sio)
session = SessionManager()
emitter = Emitter(sio, session)