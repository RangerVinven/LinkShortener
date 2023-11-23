from pydantic import BaseModel, EmailStr

class User(BaseModel):
    UserID: int
    FirstName: str
    LastName: str
    Email: EmailStr
    Password: str
    SessionToken: str

class CreateUser(BaseModel):
    FirstName: str
    LastName: str
    Email: EmailStr
    Password: str

class GetUser(BaseModel):
    SessionToken: str