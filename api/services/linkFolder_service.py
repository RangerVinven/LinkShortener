from models.LinkFolder import CreateLinkFolder, UpdateLinkFolder, DeleteLinkFolder

from services.database_service import cursor
from helpers.linkFolder_helpers import getUserIDFromRequest, doesUserOwnLinkFolder

from fastapi import Response, Request, HTTPException
from fastapi.responses import JSONResponse

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

async def update_linkFolder(linkFolder: UpdateLinkFolder, request: Request):

    try:
        # Gets the userID
        userID = await getUserIDFromRequest(request)

        # Checks if the user can modify the LinkFolder - returns true if they can
        userOwnsLinkFolder = await doesUserOwnLinkFolder(linkFolder.FolderID, userID)

        if not userOwnsLinkFolder:
            # Tells the user they can't modify that LinkFolder
            return JSONResponse(status_code=401, content={"Detail": "You can't access that LinkFolder"})

        else:
            cursor.execute("UPDATE LinkFolders SET FolderName=%s WHERE FolderID=%s AND UserID=%s", (linkFolder.NewFolderName, linkFolder.FolderID, userID))
            return Response(status_code=200)

    except:
        raise HTTPException(status_code=500, detail="Something went wrong")

async def delete_linkFolder(linkFolder: DeleteLinkFolder, request: Request):
    try:
        # Gets the userID
        userID = await getUserIDFromRequest(request)

        # Checks if the user can modify the LinkFolder - returns true if they can
        userOwnsLinkFolder = await doesUserOwnLinkFolder(linkFolder.FolderID, userID)

        if not userOwnsLinkFolder:
            # Tells the user they can't modify the LinkFolder
            return JSONResponse(status_code=401, content={"Detail": "You can't access that LinkFolder"})

        else:
            cursor.execute("DELETE FROM LinkFolders WHERE FolderID=%s AND UserID=%s", (linkFolder.FolderID, userID))
            return Response(status_code=200)

    except:
        raise HTTPException(status_code=500, detail="Something went wrong")