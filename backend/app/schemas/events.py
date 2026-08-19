from pydantic import BaseModel

class EventBase(BaseModel):
    type: str
    payload: dict

class EventCreate(EventBase):
    pass

class Event(EventBase):
    id: int
    class Config:
        orm_mode = True
