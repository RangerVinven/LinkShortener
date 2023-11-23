from fastapi import APIRouter, HTTPException, Request

from models.User import CreateUser
from services.database import cursor
from services.security_service import generateSessionToken

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
        cursor.execute("INSERT INTO Users (FirstName, LastName, Email, Password, SessionToken) VALUES (%s, %s, %s, %s, %s)", (user.FirstName, user.LastName, user.Email, user.Password, generateSessionToken()))

    except IntegrityError:
        raise HTTPException(status_code=403, detail="Account with that email already exists")
    
    return {}


@usersRouter.put("/")
async def updateUser(user: CreateUser, request: Request):
    try:
        sessionToken = request.cookies.get("SessionToken")
        cursor.execute("UPDATE Users SET FirstName=%s, LastName=%s, Email=%s, Password=%s WHERE SessionToken=%s", (user.FirstName, user.LastName, user.Email, user.Password, sessionToken))

    except IntegrityError:
        raise HTTPException(status_code=403, detail="Account with that email already exists")

    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Something went wrong")
    
    return {}

@usersRouter.delete("/")
async def deleteUser(request: Request):
    try:
        cursor.execute("DELETE FROM Users WHERE SessionToken=%s", (request.cookies.get("SessionToken"),))
        return True

    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Something went wrong")    