from fastapi import APIRouter
from models.User import CreateUser

usersRouter = APIRouter()

@usersRouter.post("/")
def createUser(user: CreateUser):
    return user