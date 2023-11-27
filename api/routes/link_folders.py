
from fastapi import APIRouter, Request

from models.LinkFolder import CreateLinkFolder
from services.linkFolder_service import get_linkFolders, create_linkFolders

linkFoldersRouter = APIRouter()

@linkFoldersRouter.get("/")
async def getLinkFolders(request: Request):
    return await get_linkFolders(request)

@linkFoldersRouter.post("/")
async def createLinkFolder(linkFolder: CreateLinkFolder, request: Request):
    return await create_linkFolders(linkFolder, request)