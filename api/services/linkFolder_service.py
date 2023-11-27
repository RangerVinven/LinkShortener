from models.LinkFolder import CreateLinkFolder
from services.database_service import cursor

from fastapi import Response, Request, HTTPException

async def get_linkFolders(request: Request):
    try:
        sessionToken = request.cookies.get("SessionToken")
        
        # Gets all the LinkFolders belonging to the user with above session token
        cursor.execute("SELECT LF.FolderName FROM LinkFolders as LF JOIN Users as U ON U.UserID=LF.UserID WHERE U.SessionToken=%s", (sessionToken,))
        return cursor.fetchall()

    except:
        raise HTTPException(status_code=500, detail="Something went wrong")

async def create_linkFolders(linkFolder: CreateLinkFolder, request: Request):
    try:
        sessionToken = request.cookies.get("SessionToken")

        # Get's the user's ID
        cursor.execute("SELECT UserID FROM Users WHERE SessionToken=%s", (sessionToken,))
        userID = cursor.fetchone()["UserID"]

        # Creates the link folder
        cursor.execute("INSERT INTO LinkFolders (FolderName, UserID) VALUES (%s, %s)", (linkFolder.FolderName, userID))

        return Response(status_code=200)

    except:
        raise HTTPException(status_code=500, detail="Something went wrong")