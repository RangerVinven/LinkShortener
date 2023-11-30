from fastapi import APIRouter, Request

from services.links_service import get_links

linksRouter = APIRouter()

# Gets all the links belonging to a user
@linksRouter.get("/")
async def getUsersLinks(request: Request):
    return await get_links(request)