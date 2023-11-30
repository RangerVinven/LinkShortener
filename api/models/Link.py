from datetime import date

from pydantic import BaseModel

class Link(BaseModel):
    LinkCode: int
    LinkName: str
    RedirectsTo: str
    NumberOfVisits: int
    IsEnabled: bool
    IsExpired: bool
    StartDate: date | None = None
    ExpiryDate: date | None = None
    DateCreated: date
    FolderID: int

class CreateLink(BaseModel):
    LinkName: str
    RedirectsTo: str
    NumberOfVisits: int
    IsEnabled: bool
    IsExpired: bool
    StartDate: date | None = None
    ExpiryDate: date | None = None
    DateCreated: date