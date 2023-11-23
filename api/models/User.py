from pydantic import BaseModel, EmailStr

class User(BaseModel):
    UserID: int
    FirstName: str
    LastName: str
    Email: EmailStr
    SessionToken: str