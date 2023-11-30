from fastapi import Request

from models.Link import CreateLink

from services.database_service import cursor

async def get_links(request: Request):
    # Gets the user's sesison token
    sessionToken = request.cookies.get("SessionToken")

    cursor.execute("SELECT l.LinkCode, l.LinkName, l.RedirectsTo, l.NumberOfVisits, l.IsEnabled, l.IsExpired, l.StartDate, l.ExpiryDate, l.DateCreated, l.FolderID FROM Links AS l INNER JOIN LinkFolders as lk ON l.FolderID=lk.FolderID INNER JOIN Users as u ON lk.UserID=u.UserID WHERE u.SessionToken=%s", (sessionToken,))
    links = cursor.fetchall()

    return links

async def create_link(link: CreateLink, request: Request):
    return link