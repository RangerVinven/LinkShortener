from services.database_service import cursor
from fastapi import Request

# Gets the user's ID from their request
async def getUserIDFromRequest(request: Request):
    sessionToken = request.cookies.get("SessionToken")

    cursor.execute("SELECT UserID FROM Users WHERE SessionToken=%s;", (sessionToken,))
    userID = cursor.fetchone()["UserID"]

    return userID

# Checks whether the user can access the LinkFolder they want to modify
async def doesUserOwnLinkFolder(linkFolderID: int, userID: int):
    # Makes sure the LinkFolder is owned by the user
    # Below query should return a list with the FolderID if the LinkFolder is owned by the user
    cursor.execute("SELECT FolderID FROM LinkFolders WHERE FolderID=%s AND UserID=%s", (linkFolderID, userID))
    queryResponse = cursor.fetchall() # Should be a list with 1 element if it's owned by the user

    if len(queryResponse) != 1:
        return False

    return True