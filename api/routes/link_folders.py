
from fastapi import APIRouter, Request

from models.LinkFolder import CreateLinkFolder, UpdateLinkFolder, DeleteLinkFolder
from services.linkFolder_service import get_linkFolders, create_linkFolders, update_linkFolder, delete_linkFolder

linkFoldersRouter = APIRouter()

@linkFoldersRouter.get("/")
async def getLinkFolders(request: Request):
    return await get_linkFolders(request)

@linkFoldersRouter.post("/")
async def createLinkFolder(linkFolder: CreateLinkFolder, request: Request):
    return await create_linkFolders(linkFolder, request)

@linkFoldersRouter.put("/")
async def updateLinkFolder(linkFolder: UpdateLinkFolder, request: Request):
    return await update_linkFolder(linkFolder, request)

@linkFoldersRouter.delete("/")
async def deleteLinkFolder(linkFolder: DeleteLinkFolder, request: Request):
    return await delete_linkFolder(linkFolder, request)