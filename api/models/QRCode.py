from pydantic import BaseModel

class QRCode(BaseModel):
    QRCodeID: str
    LinkCode: str