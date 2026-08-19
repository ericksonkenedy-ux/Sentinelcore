from fastapi import APIRouter
from backend.app.schemas.events import EventCreate

router = APIRouter()

@router.post("/")
def create_event(event: EventCreate):
    return {"id": 1, **event.dict()}
