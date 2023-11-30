from fastapi import FastAPI

from routes.users import usersRouter
from routes.link_folders import linkFoldersRouter
from routes.links import linksRouter

api = FastAPI()

api.include_router(usersRouter, prefix="/users")
api.include_router(linkFoldersRouter, prefix="/linkfolders")
api.include_router(linksRouter, prefix="/links")

@api.get("/")
def root():
    return { "Hello":"World" }