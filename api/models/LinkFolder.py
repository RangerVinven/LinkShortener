from pydantic import BaseModel

class LinkFolder(BaseModel):
    FolderID: int
    FolderName: str
    UserID: int

# Used to create the link folder
class CreateLinkFolder(BaseModel):
    FolderName: str

# Used for updating link folder
class UpdateLinkFolder(BaseModel):
    FolderID: int
    FolderName: str