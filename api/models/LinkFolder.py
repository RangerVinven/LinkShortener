from pydantic import BaseModel

class LinkFolder(BaseModel):
    FolderID: int
    FolderName: str
    UserID: int

# Used to create the link folder
class CreateLinkFolder(BaseModel):
    FolderName: str

# Used for updating a link folder
class UpdateLinkFolder(BaseModel):
    FolderID: int
    NewFolderName: str

# Used for deleting a link folder
class DeleteLinkFolder(BaseModel):
    FolderID: int