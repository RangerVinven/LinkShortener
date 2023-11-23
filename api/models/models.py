from datetime import date

from pydantic import BaseModel, EmailStr

class User(BaseModel):
    UserID: int
    FirstName: str
    LastName: str
    Email: EmailStr
    SessionToken: str

class LinkFolder(BaseModel):
    FolderID: int
    FolderName: str
    UserID: int

class Link(BaseModel):
    LinkCode: int
    LinkDescription: str
    RedirectsTo: str
    NumberOfVisits: int
    IsEnabled: bool
    IsExpired: bool
    StartDate: date | None = None
    ExpiryDate: date | None = None
    DateCreated: date
    FolderID: int

class QRCode(BaseModel):
    QRCodeID: str
    LinkCode: str