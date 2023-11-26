from services.database_service import cursor
from services.security_service import generateSessionToken, hashPassword

from models.User import CreateUser, GetUser, LoginUser
from fastapi import Request, Response, HTTPException

from mysql.connector.errors import IntegrityError



async def get_users():
    cursor.execute("SELECT * FROM Users;")
    return cursor.fetchall()


async def get_user(user: GetUser):
    cursor.execute("SELECT FirstName, LastName, Email FROM Users WHERE SessionToken=%s", (user.SessionToken,))
    return cursor.fetchone()


async def create_user(user: CreateUser, response: Response):

    password = hashPassword(user.Password)
    sessionToken = generateSessionToken()

    try:
        cursor.execute("INSERT INTO Users (FirstName, LastName, Email, Password, SessionToken) VALUES (%s, %s, %s, %s, %s)", (user.FirstName, user.LastName, user.Email, password, sessionToken))
        response.set_cookie(key="SessionToken", value=sessionToken)

        return Response(status_code=200)

    except IntegrityError:
        raise HTTPException(status_code=403, detail="Account with that email already exists")
    


async def update_user(user: CreateUser, request: Request):
    try:
        sessionToken = request.cookies.get("SessionToken")
        cursor.execute("UPDATE Users SET FirstName=%s, LastName=%s, Email=%s, Password=%s WHERE SessionToken=%s", (user.FirstName, user.LastName, user.Email, user.Password, sessionToken))

    except IntegrityError:
        raise HTTPException(status_code=403, detail="Account with that email already exists")

    except:
        raise HTTPException(status_code=500, detail="Something went wrong")
    
    return Response(status_code=200)


async def delete_user(request: Request):


    try:
        cursor.execute("DELETE FROM Users WHERE SessionToken=%s", (request.cookies.get("SessionToken"),))
        return Response(status_code=200)

    except:
        raise HTTPException(status_code=500, detail="Something went wrong")    
    

async def login_user(credentials: LoginUser, response: Response):
    
    password = hashPassword(credentials.Password)

    # Checks if the credentials are correct
    cursor.execute("SELECT UserID FROM Users WHERE Email=%s AND Password=%s", (credentials.Email, password))
    queryResponse = cursor.fetchone()

    # If credentials are correct
    if queryResponse != None:
        userID = queryResponse["UserID"]

        # Sets session token
        sessionToken = generateSessionToken()
        cursor.execute("UPDATE Users SET SessionToken=%s WHERE UserID=%s", (sessionToken, userID))

        response.set_cookie(key="SessionToken", value=sessionToken)

        return response(status_code=200)

    else:
        raise HTTPException(status_code=401, detail="Email or password incorrect")


async def signout_user(request: Request, response: Response):
    try:
        sessionToken = request.cookies.get("SessionToken")
        cursor.execute("UPDATE Users SET SessionToken=null WHERE SessionToken=%s", (sessionToken,))

        response.delete_cookie("SessionToken")
        return response(status_code=200)
    
    except:
        raise HTTPException(status_code=500, detail="Something went wrong")