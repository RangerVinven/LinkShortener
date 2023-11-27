from models.LinkFolder import CreateLinkFolder

from services.database_service import cursor
from helpers.database_helpers import getUserIDFromRequest

from fastapi import Response, Request, HTTPException

async def get_linkFolders(request: Request):
    try:
        sessionToken = request.cookies.get("SessionToken")

        # Gets all the LinkFolders belonging to the user with above session token
        cursor.execute("SELECT LF.FolderID, LF.FolderName FROM LinkFolders as LF JOIN Users as U ON U.UserID=LF.UserID WHERE U.SessionToken=%s", (sessionToken,))
        return cursor.fetchall()

    except:
        raise HTTPException(status_code=500, detail="Something went wrong")

async def create_linkFolders(linkFolder: CreateLinkFolder, request: Request):
    try:
        userID = await getUserIDFromRequest(request)

        # Creates the link folder
        cursor.execute("INSERT INTO LinkFolders (FolderName, UserID) VALUES (%s, %s)", (linkFolder.FolderName, userID))

        return Response(status_code=200)

    except:
        raise HTTPException(status_code=500, detail="Something went wrong")

async def update_linkFolder(request: Request):
    try:
        userID = await getUserIDFromRequest(request)


    except:
        raise HTTPException(status_code=500, detail="Something went wrong")