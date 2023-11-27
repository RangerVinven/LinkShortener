from services.database_service import cursor

from fastapi import Request, HTTPException

async def get_linkFolders(request: Request):
    try:
        sessionToken = request.cookies.get("SessionToken")
        
        # Gets all the LinkFolders belonging to the user with above session token
        cursor.execute("SELECT LF.FolderName FROM LinkFolders as LF JOIN Users as U ON U.UserID=LF.UserID WHERE U.SessionToken=%s", (sessionToken,))
        return cursor.fetchall()

    except:
        raise HTTPException(status_code=500, detail="Something went wrong")

