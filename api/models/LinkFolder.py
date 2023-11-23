from pydantic import BaseModel

class LinkFolder(BaseModel):
    FolderID: int
    FolderName: str
    UserID: int