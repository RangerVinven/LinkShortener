from fastapi import APIRouter
from models.User import CreateUser

usersRouter = APIRouter()

# For Development only
@usersRouter.get("/")
def getUsers():
    return {}

@usersRouter.post("/")
def createUser(user: CreateUser):
    return user