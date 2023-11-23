from fastapi import APIRouter, HTTPException

from models.User import CreateUser
from services.database import cursor

from mysql.connector.errors import IntegrityError

usersRouter = APIRouter()

# For Development only
@usersRouter.get("/")
async def getUsers():
    cursor.execute("SELECT * FROM Users;")
    return cursor.fetchall()

@usersRouter.post("/")
async def createUser(user: CreateUser):
    try:
        cursor.execute("INSERT INTO Users (FirstName, LastName, Email, Password) VALUES (%s, %s, %s, %s)", (user.FirstName, user.LastName, user.Email, user.Password))

    except IntegrityError:
        raise HTTPException(status_code=403, detail="Account with that email already exists")
    
    return {}
