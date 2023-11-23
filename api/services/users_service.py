from services.database_service import cursor
from services.security_service import generateSessionToken

from models.User import CreateUser
from fastapi import Request, HTTPException

from mysql.connector.errors import IntegrityError



async def get_users():
    cursor.execute("SELECT * FROM Users;")
    return cursor.fetchall()



async def create_user(user: CreateUser):
    try:
        cursor.execute("INSERT INTO Users (FirstName, LastName, Email, Password, SessionToken) VALUES (%s, %s, %s, %s, %s)", (user.FirstName, user.LastName, user.Email, user.Password, generateSessionToken()))

    except IntegrityError:
        raise HTTPException(status_code=403, detail="Account with that email already exists")
    
    return {}



async def update_user(user: CreateUser, request: Request):
    try:
        sessionToken = request.cookies.get("SessionToken")
        cursor.execute("UPDATE Users SET FirstName=%s, LastName=%s, Email=%s, Password=%s WHERE SessionToken=%s", (user.FirstName, user.LastName, user.Email, user.Password, sessionToken))

    except IntegrityError:
        raise HTTPException(status_code=403, detail="Account with that email already exists")

    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Something went wrong")
    
    return {}



async def delete_user(request: Request):
    try:
        cursor.execute("DELETE FROM Users WHERE SessionToken=%s", (request.cookies.get("SessionToken"),))
        return True

    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Something went wrong")    