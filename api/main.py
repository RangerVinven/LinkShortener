from fastapi import FastAPI
from routes.users import usersRouter

api = FastAPI()

api.include_router(usersRouter, prefix="/users")

@api.get("/")
def root():
    return { "Hello":"World" }