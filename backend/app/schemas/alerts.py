from pydantic import BaseModel

class AlertBase(BaseModel):
    severity: str
    description: str

class AlertCreate(AlertBase):
    pass

class Alert(AlertBase):
    id: int
    class Config:
        orm_mode = True
