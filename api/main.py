from fastapi import FastAPI

from routes.users import usersRouter
from routes.link_folders import linkFoldersRouter

api = FastAPI()

api.include_router(usersRouter, prefix="/users")
api.include_router(linkFoldersRouter, prefix="/linkfolders")

@api.get("/")
def root():
    return { "Hello":"World" }