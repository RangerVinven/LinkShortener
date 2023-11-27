from services.database_service import cursor
from fastapi import Request

# Gets the user's ID from their request
async def getUserIDFromRequest(request: Request):
    sessionToken = request.cookies.get("SessionToken")

    cursor.execute("SELECT UserID FROM Users WHERE SessionToken=%s;", (sessionToken,))
    userID = cursor.fetchone()["UserID"]

    return userID