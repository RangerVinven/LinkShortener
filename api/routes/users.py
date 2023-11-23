from fastapi import APIRouter

from models.User import CreateUser
from database.database import cursor

usersRouter = APIRouter()

# For Development only
@usersRouter.get("/")
def getUsers():
    cursor.execute("SELECT * FROM Users;")
    return cursor.fetchall()

@usersRouter.post("/")
def createUser(user: CreateUser):
    return user