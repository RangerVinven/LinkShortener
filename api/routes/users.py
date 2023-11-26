from fastapi import APIRouter, Request, Response

from services.users_service import *

usersRouter = APIRouter()

@usersRouter.post("/login")
async def login(credentials: LoginUser, response: Response):
    return await login_user(credentials, response)

@usersRouter.get("/signout")
async def login(request: Request, response: Response):
    return await signout_user(request, response)

# @usersRouter.get("/")
# async def getUser(request: Request):
#     return await get_user(request)

# For Development only!!!
@usersRouter.get("/")
async def getUsers():
    return await get_users()

@usersRouter.post("/")
async def createUser(user: CreateUser, response: Response):
    return await create_user(user, response)

@usersRouter.put("/")
async def updateUser(user: CreateUser, request: Request):
    return await update_user(user, request)

@usersRouter.delete("/")
async def deleteUser(request: Request):
    return await delete_user(request)