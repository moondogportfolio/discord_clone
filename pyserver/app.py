# from constants import CHANNEL_EX, EMOJI_EX, ROOM_EX, ROOM_SERVER_POST_MSG_EX, SERVER_EX, SERVER_MODIFY_EX, SERVER_USER_EX, SPECIFIC_MSG_EX
# from devtools import debug, sprint
# from fastapi import Depends, FastAPI, status, HTTPException, UploadFile, File, Request, Response, Form
# from fastapi.param_functions import Body, Path, Query
# from fastapi.responses import JSONResponse


# from typing import List, Optional
# from pydantic_models.exceptions import DatabaseException

# import socketio
# from socketio.exceptions import ConnectionRefusedError
# import yagmail

# import asyncio
# from hypercorn.asyncio import serve
# from hypercorn.config import Config
# config = Config()
# config.use_reloader = True
# config.loglevel = 'INFO'



from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Request
from init_objects import socketapp

app = FastAPI()

from routers.room.dm_rooms import router as dm_rooms_router
from routers.room.reactions import router as reactions_router
from routers.room.rooms import router as rooms_router
from routers.room.server_rooms import router as server_rooms_router
from routers.room.threads import router as threads_router

from routers.data.files import router as files_router
from routers.data.init import router as init_router

from routers.server.invite import router as invite_router
from routers.server.server_roles import router as server_roles_router
from routers.server.server import router as server_router

from routers.server.server_user import router as server_user_router

from routers.user.user import router as user_router
from routers.user.user_relationships import router as user_relationships_router

from routers.account import router as account_router
from routers.security_router import router as security_router
from routers.utils import router as utils_router

from routers.tasks.workspace import router as workspace
from routers.tasks.resource import router as resource
from routers.tasks.entity import router as workspace_entity
from routers.tasks.automations import router as automations
from routers.tasks.task import router as workspace_task


from devtools import debug



app.include_router(server_rooms_router)
app.include_router(rooms_router)
app.include_router(threads_router)
app.include_router(reactions_router)
app.include_router(dm_rooms_router)

app.include_router(files_router)
app.include_router(init_router)

app.include_router(invite_router)
app.include_router(server_roles_router)
app.include_router(server_router)
app.include_router(server_user_router)

app.include_router(user_router)
app.include_router(user_relationships_router)

app.include_router(account_router)
app.include_router(security_router)
app.include_router(utils_router)

app.include_router(workspace)
app.include_router(resource)
app.include_router(workspace_entity)
app.include_router(automations)
app.include_router(workspace_task)


# sio = socketio.AsyncServer(
#     async_mode='asgi',
#     cors_allowed_origins = []
# )
# socketapp = socketio.ASGIApp(sio)
# session = SessionManager()
# coordinator = Manager(Emitter(sio, session))

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8082"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


app.mount('/', socketapp)




# '''
# -----------------------------------------------------------
# ERROR HANDLER
# -----------------------------------------------------------
# '''


# from pydantic_models.exceptions import DatabaseException
# @app.exception_handler(DatabaseException)
# async def unicorn_exception_handler(request: Request, exc: DatabaseException):
#     return JSONResponse(
#         status_code=418,
#         content={"message": f"Something wrong with {exc.name} database."},
#     )



# '''
# -----------------------------------------------------------
# MIDDLEWARE
# -----------------------------------------------------------
# '''



# @app.middleware("http")
# async def add_process_time_header(request: Request, call_next):
#     response = await call_next(request)
#     print(request.client)
#     return response



# '''
# -----------------------------------------------------------
# SERVER ENDPOINTS
# -----------------------------------------------------------
# '''


# @app.get("/server/discover", 
#         response_model=List[ServerDiscoveryPartial],
#         tags=["discovery"])
# async def _discover_servers():
#     return coordinator.discover_servers()


# @app.post("/base64encoder", response_model=str, tags=["utils"])
# async def _base64_encoder(image: Optional[UploadFile] = File(...)):
#     img_bytes = await img_filelike_to_bytes(image.file)
#     result = coordinator.base64_encoder(img_bytes)
#     return result
    

# @app.post("/server/{server_id}/emojis", tags=["server"])
# async def _create_emoji(
#     server_id: ObjectIdStr, 
#     name: str = Query(..., min_length=2, max_length=100),
#     file: UploadFile = File(...) ):
#     data, extension, animated = await img_filelike_to_bytes(file.file)
#     mongo_file = GraphicsDescriptionIn.construct(
#             category = 'emoji',
#             extension = extension,
#             data = data,
#             animated = animated
#         )
#     coordinator.add_server_emoji(server_id, name, mongo_file)


# @app.post("/server/{server_id}/icon", tags=["server"])
# async def _edit_server_icon(
#     server_id: ObjectIdStr, 
#     file: UploadFile = File(...) ):
#     data, extension, animated = await img_filelike_to_bytes(file.file)
#     mongo_file = GraphicsDescriptionIn.construct(
#             category = 'server_icon',
#             extension = extension,
#             data = data,
#             animated = animated
#         )
#     coordinator.edit_server_icon(server_id, mongo_file)


# # @app.post("/server/{server_id}/rooms", tags=["server"])


# @app.post("/server",
#         tags=["server"])
# async def _create_server(
#     server_obj: ServerBase,
#     icon: Optional[str] = None,
#     current_user: User = Depends(get_current_user)
#     ):
#     '''
#     ✔ - Create new server.
#     '''
#     result = coordinator.create_server(server_obj, icon, current_user.id)
#     # return server_obj
#     # if result:
#     #     return server_obj
#     # return Response(status_code=404)
    

# @app.delete("/server/{server_id}",
#         status_code=204,
#         response_description="No content. Server has been deleted.",
#         responses={404: {'description': 'Server not found.'}},
#         tags = ["server"]
#         )
# async def _delete_server(
#     server_id: ObjectIdStr = Path(..., example = "60fbabedc30a2589720f09a4"),
#     ):
#     '''
#     Delete server.
#     '''
#     result = coordinator.delete_server(server_id)
#     if result == 0:
#         return Response(status_code=404) 




# @app.patch("/server/{server_id}",
#         tags = ["server"]
#         )
# async def _modify_server(
#     server_obj: BaseServer,
#     server_id: ObjectIdStr = Path(..., example = "60fbabedc30a2589720f09a4"),
#     ):
#     '''
#     Modify server.
#     '''
#     return coordinator.modify_server(server_id, server_obj)


# @app.get("/server/{serverid}",
#         response_model=Server,
#         responses={404: {'description': 'Server not found.'}},
#         tags=["server"])
# async def _get_server(
#     server_id: ObjectIdStr
#     ):
#     '''
#     ✔ - Get server.
#     '''
#     result = coordinator.get_server(server_id)
#     if result:
#         return result
#     return Response(status_code=404) 



# @app.post("/server/{server_id}/channel",
#         tags=["server_channel"])
# async def _create_server_channel(
#     server_id: ObjectIdStr,
#     name: str
#     ):
#     '''
#     ✔ - Create server channel.
#     '''
#     await coordinator.create_server_channel(server_id, name)




'''
-----------------------
SERVER MEMBER ENDPOINTS
-----------------------
'''




# @app.put("/server/{server_id}/enter",
#         response_model=EnterServerInitData,
#         tags = ["server_user"])
# async def _enter_server(
#     server_id: ObjectIdStr = Path(..., example=SERVER_EX),
#     current_user: User = Depends(get_current_user)
#     ):
#     '''
#     ✔ - Enter server.
#     '''
#     result =  coordinator.enter_server_main(server_id, current_user)
#     return result


# @app.put("/server/{server_id}/member/{user_id}",
#         tags = ["server_user"])
# async def _add_server_member(
#     server_id: ObjectIdStr = Path(..., example=SERVER_EX),
#     user_id: ObjectIdStr = Path(..., example=SERVER_USER_EX)
#     ):
#     '''
#     ✔ - Add server member.
#     '''
#     return coordinator.add_server_member(server_id, user_id)



# @app.patch("/server/{server_id}/member/{user_id}", tags=["server_user"])
# async def _server_modify_member(
#     modifiers: ServerMemberIn,
#     server_id: ObjectIdStr = Path(..., example=SERVER_EX),
#     user_id: ObjectIdStr = Path(..., example=SERVER_USER_EX)
#     ):
#     '''
#     ✔ - Modify server member.
#     '''
#     if coordinator.server_modify_member(server_id, user_id, modifiers) == 0:
#         return Response(status_code=404)  


# @app.delete("/server/{server_id}/member/{user_id}",
#         status_code=204,
#         response_description="No content. Room has been deleted.",
#         responses={404: {'description': 'Server room not found.'}},
#         tags = ["server_user"]
#         )
# async def _delete_server_member(
#     server_id: ObjectIdStr = Path(..., example=SERVER_EX),
#     user_id: ObjectIdStr = Path(..., example=SERVER_USER_EX)
#     ):
#     '''
#     ✔ - Kick server member.
#     '''
#     result = coordinator.delete_server_member(server_id, user_id)
#     if result == 0:
#         return Response(status_code=404) 



'''
-----------------------
SERVER ROLE ENDPOINTS
-----------------------
'''


# @app.post("/server/{server_id}/role",
#         response_model=Role,
#         tags = ["server_role"])
# async def _create_server_role(
#     server_id: ObjectIdStr
#     ):
#     return coordinator.create_server_role(server_id)


# @app.get("/server/{server_id}/role/{role_id}",
#         tags = ["server_role"])
# async def _get_server_role(
#     server_id: ObjectIdStr = Path(..., example=SERVER_EX),
#     role_id: ObjectIdStr = Path(..., example=SERVER_USER_EX)
#     ):
#     return coordinator.get_server_role(server_id, role_id)


# @app.patch("/server/{server_id}/role/{role_id}", tags=["server_role"])
# async def _modify_server_role(
#     modifiers: ServerMemberIn,
#     server_id: ObjectIdStr = Path(..., example=SERVER_EX),
#     role_id: ObjectIdStr = Path(..., example=SERVER_USER_EX)
#     ):
#     '''
#     ✔ - Modify server member.
#     '''
#     if coordinator.modify_server_role(server_id, role_id, modifiers) == 0:
#         return Response(status_code=404)  


# @app.delete("/server/{server_id}/role/{role_id}",
#         status_code=204,
#         response_description="No content. Room has been deleted.",
#         responses={404: {'description': 'Server room not found.'}},
#         tags = ["server_role"]
#         )
# async def _delete_server_role(
#     server_id: ObjectIdStr = Path(..., example=SERVER_EX),
#     role_id: ObjectIdStr = Path(..., example=SERVER_USER_EX)
#     ):
#     result = coordinator.delete_server_role(server_id, role_id)
#     if result == 0:
#         return Response(status_code=404) 



'''
-----------------------------------------------------------
SERVER ROOM ENDPOINTS
-----------------------------------------------------------
'''


# @app.post("/server/{server_id}/rooms",
#         tags=["server_room"]
#         )
# async def _create_server_room(
#     name: str = Query(..., example='Test Room'),
#     server_id: ObjectIdStr = Path(..., example=SERVER_EX),
#     channel_id: ObjectIdStr = Query(..., example=CHANNEL_EX)
#     ):
#     '''
#     ✔ - Create new server room.
#     '''
#     coordinator.create_server_room(server_id, channel_id, name)
    


# @app.get("/server/{server_id}/rooms",
#         response_model=List[ServerRoom],
#         responses={404: {'description': 'Server not found.'}},
#         tags=["server_room"])
# async def _get_server_rooms(
#     server_id: ObjectIdStr = Path(..., example=SERVER_EX),
#     ):
#     '''
#     ✔ - Get server rooms. 
#     '''
#     result = coordinator.get_list_of_server_rooms(server_id)
#     if result:
#         return result
#     return Response(status_code=404) 



# @app.get("/server_room/{room_id}", 
#         response_model=ServerRoom,
#         responses={404: {'description': 'Room not found.'}},
#         tags=["server_room"],
#         )
# async def _get_server_room(room_id: ObjectIdStr = Path(..., example=ROOM_EX)):
#     '''
#     ✔ - Get server room. 
#     '''
#     result = coordinator.get_server_room(room_id)
#     if result:
#         return result
#     return Response(status_code=404) 



# @app.patch("/server_room/{room_id}",
#         response_model=ServerRoom,
#         tags=["server_room"])
# async def modify_server_room(server_room_id: ObjectIdStr):
#     '''
#     Modify server room.  TODO
#     '''
#     return coordinator.modify_server_room(server_room_id)



# @app.delete("/server_room/{room_id}",
#         status_code=204,
#         response_description="No content. Room has been deleted.",
#         responses={404: {'description': 'Server room not found.'}},
#         tags = ["server_room"]
#         )
# async def _delete_server_room(server_room_id: ObjectIdStr):
#     '''
#     ✔ - Delete server room. 
#     '''
#     result = coordinator.delete_server_room(server_room_id)
#     if result == 0:
#         return Response(status_code=404) 



'''
-----------------------------------------------------------
FILE DL/UL ENDPOINTS
-----------------------------------------------------------
'''


# @app.post("/uploadfile/",
#         response_model=ObjectIdStr,
#          tags=["file upload/download"]
#          )
# async def _create_upload_file(category: str, file: UploadFile = File(...)):
#     if category not in ['emoji']:
#         return Response(status_code=404) 
#     img_bytes, extension = await img_filelike_to_bytes(file.file)
#     try:
#         description = GraphicsDescriptionIn(
#             category=category,
#             extension=extension
#         )
#     except Exception as e:
#         debug(e, category, extension)
#         return Response(status_code=404)
#     return coordinator.upload_file(img_bytes, description)
    


# @app.get("/emojis/{server_id}/{request_image}", response_class=Response,
#         responses={
#             200: {"content": {"image/png": {}}},
#             404: {"description": "Item not found"},
#         },
#         tags=["file upload/download"])
# async def _get_emoji_image(
#     server_id: ObjectIdStr,
#     request_image: str = RequestImageFile):
#     '''
#     Example: 60f8e8ed6cdb71569db2fa06
#     '''
#     try:
#         request_image = RequestImageFile(filename = request_image)       
#     except Exception as e:
#         print(e)
#         errors = ValidationErrorMessage(errors = e.errors()).dict()
#         return JSONResponse(status_code=422, content=errors)
#     buffer, extension = coordinator.get_file_emoji(server_id, request_image)
#     if not buffer:
#         raise HTTPException(status_code=404, detail="No such image.")
#     return Response(content=buffer.read(), media_type=f"image/{extension}")


# @app.get("/server-icon/{server_id}", response_class=Response,
#         responses={
#             200: {"content": {"image/png": {}}},
#             404: {"description": "Item not found"},
#         },
#         tags=["file upload/download"])
# async def _get_server_icon(server_id: ObjectIdStr):
#     try:
#         buffer, extension = coordinator.get_server_icon(server_id)
#     except TypeError: # cannot unpack non-iterable NoneType object
#         raise HTTPException(status_code=404, detail="Server has no icon/avatar.")
#     return Response(content=buffer.read(), media_type=f"image/{extension}")


# @app.get("/user-icon/{user_id}", response_class=Response,
#         responses={
#             200: {"content": {"image/png": {}}},
#             404: {"description": "Item not found"},
#         },
#         tags=["file upload/download"])
# async def _get_user_icon(user_id: ObjectIdStr):
#     try:
#         buffer, extension = coordinator.get_user_icon(user_id)
#     except TypeError: # cannot unpack non-iterable NoneType object
#         raise HTTPException(status_code=404, detail="User has no icon/avatar.")
#     return Response(content=buffer.read(), media_type=f"image/{extension}")


    


'''
-----------------------------------------------------------
ACCOUNT ENDPOINTS
-----------------------------------------------------------
'''



# @app.post("/register", tags=["account management"])
# async def _register_account(reg_form: RegistrationForm):
#     # email = False
#     # if email:
#     #     # to = RegistrationForm.email
#     #     to = 'mccndcg@gmail.com'
#     #     subject = 'Account registration.'
#     #     body = 'Click me.'
#     #     html = '127.0.0.1/8000/OK'
#     #     yag.send(to = to, subject = subject, contents = [body, html])
#     reg_form.password_hash = get_password_hash(reg_form.password)
#     coordinator.register_account(reg_form)


# @app.get("/register/{email_code}", tags=["account management"])
# async def _validate_email(email_code, current_user: User = Depends(get_current_user)):
#     if (email_code == 'OK'
#         and not current_user.state.verified
#         and coordinator.validate_email(current_user.id)
#         ):
#         return {'response': 'EMAIL VALIDATED'}
#     else:
#         return JSONResponse(status_code=status.HTTP_406_NOT_ACCEPTABLE, content='EMAIL VALIDATION UNSUCCESSFUL.')
    


'''
-----------------------------------------------------------
✔ USER ENDPOINTS
-----------------------------------------------------------
'''


# @app.post("/users/{user_id}/icon", tags=["user"])
# async def _edit_user_icon(
#     user_id: ObjectIdStr, 
#     file: UploadFile = File(...) ):
#     data, extension, animated = await img_filelike_to_bytes(file.file)
#     mongo_file = GraphicsDescriptionIn.construct(
#             category = 'server_icon',
#             extension = extension,
#             data = data,
#             animated = animated
#         )
#     coordinator.edit_user_icon(user_id, mongo_file)


# @app.get("/users/@me", response_model=User, tags=["user"])
# async def _get_current_user(current_user: User = Depends(get_current_user)):
#     return current_user


# @app.get("/users/{user_id}",
#         response_model=User, 
#         responses={404: {"description": "Item not found"}},
#         tags=["user"])
# async def _get_user(user_id: ObjectIdStr):
#     result = coordinator.get_user(user_id)
#     if not result:
#         raise HTTPException(status_code=404, detail="No such user.")
#     return result


# @app.patch("/users/@me", response_model=User, tags=["user"])
# async def _modify_current_user(
#         username: Optional[str] = None,
#         avatar: Optional[UploadFile] = File(None),
#         current_user: User = Depends(get_current_user)):

#     if not avatar and not username:
#         raise HTTPException(status_code=400)
#     img_bytes = await img_filelike_to_bytes(avatar.file) if avatar else None
#     if not coordinator.modify_user(current_user.id, username, img_bytes):
#         raise HTTPException(status_code=401)
#     # return FileResponse("image.png", media_type="image/png")



'''
-----------------------------------------------------------
✔ INIT ENDPOINTS
-----------------------------------------------------------
'''


# @app.get("/init_data", response_model=InitData, tags=["user"])
# async def read_users_me(current_user: User = Depends(get_current_user)):
#     await update_connectivity(current_user.id, 'online')
#     init_data = coordinator.fetch_init_data(current_user)
#     return init_data


# async def update_connectivity(user_id, connection):
#     debug(connection, user_id)
#     await coordinator.modify_user_connection(user_id, connection)





@app.get("/test2")
@app.get("/")
async def main():
    return {'Hi': 'Hello world.'}



'''
-----------------------------------------------------------
SECURITY ENDPOINTS 💕
-----------------------------------------------------------
'''



# @app.post("/token", response_model=Token, tags=["security"])
# async def token(form_data: OAuth2PasswordRequestForm = Depends()):
#     return login_access_token_fetch(form_data)


# #https://github.com/pyauth/pyotp
# @app.get("/otp_protected", responses={404: {"model": Message}}, tags=["security"])
# async def _otp_protected(current_user: User = Depends(get_current_user), otp: Optional[int] = Query(None, ge=100000, le=999999)):
#     secret = current_user.otp_hash
#     print(current_user)
#     if not verify_otp(secret, otp):
#         return JSONResponse(status_code=401, content={"message": "Wrong OTP."})
#     #PROCEED


# @app.get("/otp", tags=["security"])
# async def _get_otp_secret(current_user: User = Depends(get_current_user)):
#     otp_secret = create_otp_secretkey()
#     if not coordinator.create_otp_secret(current_user.id, otp_secret):
#         raise DatabaseException(name='MongoDB')
#     return {'otp_secret': otp_secret}



'''
-----------------------------------------------------------
DM ENDPOINTS
-----------------------------------------------------------
'''



# @app.post("/dm_room",
#     status_code=201,
#     tags=["dm room"])
# async def _create_dm_room(
#     dmroom: DmRoomIn,
#     current_user: User = Depends(get_current_user)
#     ):
#     return await coordinator.create_dm_room(dmroom, current_user.id)



# @app.get("/dm_room/{dm_room_id}",
#     response_model=RoomData,
#     responses={404: {"model": Message}},
#     tags=["dm room"]
#     )
# async def _get_dm_room(dm_room_id: ObjectIdStr):
#     result = coordinator.get_dm_room(dm_room_id)
#     if result:
#         return RoomData(selected_roomdata=result)
#     else:
#         return JSONResponse(status_code=404, content={"message": "DM room not found."})



# @app.delete("/dm_room/{dm_room_id}",
#     response_model=BaseRoom,
#     responses={404: {"model": Message}},
#     tags=["dm room"]
#     )
# async def _delete_dm_room(dm_room_id: ObjectIdStr, method: Optional[str] = 'obliterate', user_id: ObjectIdStr = TESTING):
#     '''
#     DELETE ROOM.
#     '''
#     await coordinator.delete_dm_room(user_id, dm_room_id, method)



'''
-----------------------------------------------------------
ROOM ENDPOINTS
-----------------------------------------------------------
'''



# '''
# -----------------------
# icon: ObjectIdStr
# name: str
# -----------------------
# '''
# @app.patch("/dm_room/{object_id}", tags=["dm room"])
# async def _modify_dm_room(dm_room_id: ObjectIdStr, icon: Optional[str] = None, name: Optional[str] = None):
#     return coordinator.modify_dm_room(dm_room_id, icon, name)



# '''
# -----------------------
# posts: Optional[List[Post]]
# -----------------------
# '''
# @app.get("/room/{room_id}/message",
#         response_model=List[Post],
#         responses={404: {'description': 'Room not found.'}},
#         tags=["room"]
#         )
# async def _get_room_messages(
#     room_id: ObjectIdStr = Path(..., example=ROOM_EX),
#     limit: Optional[int] = Query(None, le=100, ge=-100, description='Positive limit gets the FIRST n posts, negative limit gets the LAST n posts.')):
#     '''
#     GET MESSAGES FROM ROOM.
#     '''
#     result = coordinator.get_room_messages(room_id, limit)
#     print(result)
#     if result:
#         return result
#     return Response(status_code=404)




# #save timestamp of last post to user
# @app.post("/room/{room_id}/message",
#         tags=["room"],
#         responses={404: {'description': 'Room not found.'}}
#         )
# async def _post_to_room(
#     room_id: ObjectIdStr = Path(..., example=ROOM_EX),
#     post: PostIn = Body(..., examples=ROOM_SERVER_POST_MSG_EX)
#     ):
#     '''
#     POST MESSAGE TO ROOM.
#     '''
#     await coordinator.post_to_room(room_id, post)
#     return Response(status_code=204)




# @app.get("/room/{room_id}/message/{message_id}",
#         response_model=Post,
#         responses={404: {'description': 'Room or message not found.'}},
#         tags=["room"]
#         )
# async def _get_room_message(
#     room_id: ObjectIdStr = Path(..., example=ROOM_EX),
#     message_id: ObjectIdStr = Path(..., example=SPECIFIC_MSG_EX)
#     ):
#     '''
#     GET MESSAGE FROM ROOM.
#     '''
#     result = coordinator.get_one_room_message(room_id, message_id)
#     if result:
#         return result
#     return Response(status_code=404)



# @app.patch("/room/{room_id}/message/{post_id}",
#         tags=["room"],
#         responses={404: {'description': 'Room not found.'}}
#         )
# async def _edit_room_message(
#     post_id: ObjectIdStr,
#     room_id: ObjectIdStr = Path(..., example=ROOM_EX),
#     post: PostIn = Body(..., examples=ROOM_SERVER_POST_MSG_EX)
#     ):
#     '''
#     EDIT MESSAGE.
#     '''
#     await coordinator.edit_room_message(room_id, post_id, post)



# @app.delete("/room/{room_id}/message",
#         tags=["room"],
#         responses={404: {'description': 'Room not found.'}}
#         )
# async def _delete_room_message(
#     room_id: ObjectIdStr = Path(..., example=ROOM_EX),
#     post: PostIn = Body(..., examples=ROOM_SERVER_POST_MSG_EX)
#     ):
#     '''
#     EDIT MESSAGE.
#     '''
#     if coordinator.delete_room_message(room_id, post) == 0:
#         return Response(status_code=404)


'''
-----------------------
RELATIONSHIP ENDPOINTS
-----------------------
'''
# @app.put("/users/@me/relationships/{user_id}",
#     tags=["user"],
#     responses={412: {'description': 'Already a friend.'}}
#     )
# async def _add_relationship(
#     user_id: ObjectIdStr,
#     current_user: User = Depends(get_current_user)
#     ):
#     if user_id in current_user.relationships:
#         return Response(status_code=412)
#     await coordinator.add_relationship(current_user.id, user_id)


# @app.patch("/users/@me/relationships/{user_id}",
#     tags=["user"],
#     responses={412: {'description': 'Already a friend.'}}
#     )
# async def _confirm_relationship(
#     user_id: ObjectIdStr,
#     current_user: User = Depends(get_current_user)
#     ):
#     if user_id in current_user.relationships:
#         return Response(status_code=412)
#     await coordinator.confirm_relationship(current_user.id, user_id)


# @app.delete("/users/@me/relationships/{user_id}",
#     tags=["user"],
#     responses={412: {'description': 'Already a friend.'}}
#     )
# async def _deny_relationship(
#     user_id: ObjectIdStr,
#     current_user: User = Depends(get_current_user)
#     ):
#     try:
#         if current_user.relationships[user_id] == 'friends':
#             return Response(status_code=412)
#         coordinator.deny_relationship(current_user.id, user_id)
#     except:
#         coordinator.deny_relationship(current_user.id, user_id)

'''
-----------------------
INVITE ENDPOINTS
-----------------------
'''

# @app.post("/invite",
#         tags=["invites"]
#         )
# async def _add_server_invite(
#     invite_obj: InviteIn
#     ):
#     coordinator.add_server_invite(invite_obj)

# @app.put("/invite/{invite_id}",
#         tags=["invites"]
#         )
# async def _use_server_invite(
#     invite_id: str,
#     current_user: User = Depends(get_current_user)
#     ):
#     result = coordinator.use_server_invite(invite_id, current_user)
#     return result


'''
-----------------------
REACTION ENDPOINTS
-----------------------
'''

# #save timestamp of last post to user
# @app.put("/room/{room_id}/message/{message_id}/reaction/{emoji_id}/@me",
#         tags=["reaction"]
#         )
# async def _add_reaction(
#     room_id: ObjectIdStr = Path(..., example=ROOM_EX),
#     message_id: ObjectIdStr = Path(..., example=SPECIFIC_MSG_EX),
#     emoji_id: str = Path(..., example=EMOJI_EX)
#     ):
#     '''
#     ✔ - ADD REACTION.
#     '''
#     await coordinator.add_reaction(room_id, message_id, emoji_id)


# @app.delete("/room/{room_id}/message/{message_id}/reaction/{emoji_id}/@me",
#         tags=["reaction"],
#         responses={404: {'description': 'Room not found.'}}
#         )
# async def _delete_reaction(
#     room_id: ObjectIdStr = Path(..., example=ROOM_EX),
#     message_id: ObjectIdStr = Path(..., example=SPECIFIC_MSG_EX),
#     emoji_id: str = Path(..., example=EMOJI_EX)
#     ):
#     '''
#     ✔ - REMOVE REACTION.
#     '''
#     if coordinator.delete_reaction(room_id, message_id, emoji_id) == 0:
#         return Response(status_code=404)




# @sio.event
# async def connect(sid, environ, auth=None):
#     debug('SOCKET ATTEMPT CONNECTION.')
#     if auth['token']:
#         try:
#             user = await get_current_user(auth['token'].replace('Bearer ', ''))
#             session.add_user(sid, user.id)
#             [sio.enter_room(sid, server) for server in user.servers.keys()]
#             debug(sio.manager.get_rooms(sid, namespace='/'))
#             await sio.emit('socket_init', sid)
#             debug(session.get_state())
#         except Exception as e:
#             debug(e)
#             raise ConnectionRefusedError('Authentication failed.')
#     else:
#         raise ConnectionRefusedError('Authentication failed.') 
        

#     # debug('connect ', sid, auth, environ)
#     # heartbeat_interval = {
#     #     'heartbeat_interval': 1000
#     # }
#     # await sio.emit('SERVER_HELLO', heartbeat_interval, to=sid)
#     # print('DONE')

# @sio.event
# async def disconnect(sid):
#     debug(f'SOCKET DISCONNECT {sid}, {session.get_user_id(sid)}')
#     await update_connectivity(session.get_user_id(sid), 'offline')
#     session.remove_user(sid)
#     debug(session.get_state())


# @sio.event
# async def HEARTBEAT(sid, payload):
#     await sio.emit('SERVER_HEARTBEAT_ACK', to=sid)
#     debug(sid, payload)

# app.mount('/', app)
#
# asyncio.run(serve(app, config))
