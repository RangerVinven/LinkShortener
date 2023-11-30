from fastapi import APIRouter, Request

from models.Link import CreateLink
from services.links_service import get_links, create_link

linksRouter = APIRouter()

# Gets all the links belonging to a user
@linksRouter.get("/")
async def getUsersLinks(request: Request):
    return await get_links(request)

@linksRouter.post("/")
async def createLink(link: CreateLink, request: Request):
    return await create_link(link, request)