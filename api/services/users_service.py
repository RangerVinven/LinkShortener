from services.database_service import cursor
from services.security_service import generateSessionToken, hashPassword

from models.User import CreateUser, LoginUser
from fastapi import Request, Response, HTTPException
from fastapi.responses import JSONResponse

from mysql.connector.errors import IntegrityError


async def get_users():
    try:
        cursor.execute("SELECT * FROM Users;")
        return cursor.fetchall()
    except:
        raise HTTPException(status_code=500, detail="Something went wrong")

async def get_user(request: Request):

    try:
        sessionToken = request.cookies.get("SessionToken")

        cursor.execute("SELECT FirstName, LastName, Email FROM Users WHERE SessionToken=%s", (sessionToken,))
        return cursor.fetchone()
    except:
        raise HTTPException(status_code=500, detail="Something went wrong")

async def create_user(user: CreateUser, response: Response):

    try:
        password = hashPassword(user.Password)
        sessionToken = generateSessionToken()

        cursor.execute("INSERT INTO Users (FirstName, LastName, Email, Password, SessionToken) VALUES (%s, %s, %s, %s, %s)", (user.FirstName, user.LastName, user.Email, password, sessionToken))
        response.set_cookie(key="SessionToken", value=sessionToken)

        return Response(status_code=200)

    except IntegrityError:
        raise HTTPException(status_code=403, detail="Account with that email already exists")

async def update_user(user: CreateUser, request: Request):
    try:
        sessionToken = request.cookies.get("SessionToken")

        
        # Makes sure the email doesn't exist in the table
        cursor.execute("SELECT Email FROM Users WHERE Email=%s", (user.Email,))
        emails = cursor.fetchall()
        
        # If the email exists in the table
        if len(emails) != 0:
            return JSONResponse(status_code=409, content={"Detail": "Account with that email already exists"})
        
        else:
            cursor.execute("UPDATE Users SET FirstName=%s, LastName=%s, Email=%s, Password=%s WHERE SessionToken=%s", (user.FirstName, user.LastName, user.Email, user.Password, sessionToken))
            return Response(status_code=200)


    # Catches if the email already exists in the table
    except IntegrityError:
        raise HTTPException(status_code=403, detail="Account with that email already exists")

    except:
        raise HTTPException(status_code=500, detail="Something went wrong")
    
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