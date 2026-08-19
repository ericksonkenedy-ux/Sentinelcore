from pydantic import BaseModel

class AssetBase(BaseModel):
    hostname: str
    ip: str

class AssetCreate(AssetBase):
    pass

class Asset(AssetBase):
    id: int
    class Config:
        orm_mode = True
