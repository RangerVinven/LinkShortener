
from fastapi import APIRouter, Request

from services.linkFolder_service import get_linkFolders

linkFoldersRouter = APIRouter()

@linkFoldersRouter.get("/")
async def getLinkFolders(request: Request):
    return await get_linkFolders(request)