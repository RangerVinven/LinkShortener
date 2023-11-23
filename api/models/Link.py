from datetime import date

from pydantic import BaseModel

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
